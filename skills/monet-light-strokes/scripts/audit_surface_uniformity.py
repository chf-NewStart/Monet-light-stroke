#!/usr/bin/env python3
"""Report corpus-calibrated surface metrics for an image and optional material crop.

This is a diagnostic aid, not an authenticity classifier. Use a crop that contains
mostly one dominant material (water, sky, meadow, snow, foliage, or ground) so
contrast with other materials cannot hide a locally uniform texture.

The central corpus band is reported as PASS, an ambiguous margin as REVIEW, and
only a strong dot-grid-like outlier as REJECT. All-over handling makes density
advisory because legitimate late ponds, dense gardens, and fog can be even in
density while remaining nonperiodic, multiscale, and materially directed.
Passing every metric does not certify the image; repeated relief and stamp shape
still require direct visual inspection of each dominant material.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image


SIZE = 256


@dataclass
class Metrics:
    coherence: float
    peakiness: float
    density_cv: float
    spectrum_slope: float
    luminance_floor: float
    luminance_ceiling: float
    dark_saturation: float


def load_image(
    path: Path, crop: tuple[int, int, int, int] | None
) -> tuple[np.ndarray, np.ndarray]:
    with Image.open(path) as image:
        image = image.convert("RGB")
        if crop is not None:
            x0, y0, x1, y1 = crop
            if not (0 <= x0 < x1 <= image.width and 0 <= y0 < y1 <= image.height):
                raise ValueError(
                    f"crop {crop} is outside image bounds {image.width}x{image.height}"
                )
            image = image.crop(crop)
        image = image.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
        rgb = np.asarray(image, dtype=np.float64) / 255.0
        hsv = np.asarray(image.convert("HSV"), dtype=np.float64) / 255.0
    gray = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]
    return gray, hsv


def box_mean(array: np.ndarray, size: int = 8) -> np.ndarray:
    cumulative = np.cumsum(np.cumsum(array, axis=0), axis=1)
    cumulative = np.pad(cumulative, ((1, 0), (1, 0)))
    return (
        cumulative[size:, size:]
        - cumulative[:-size, size:]
        - cumulative[size:, :-size]
        + cumulative[:-size, :-size]
    ) / size**2


def structure_coherence(gray: np.ndarray) -> float:
    gy, gx = np.gradient(gray)
    xx = box_mean(gx * gx)
    yy = box_mean(gy * gy)
    xy = box_mean(gx * gy)
    trace = xx + yy
    anisotropy = np.sqrt((xx - yy) ** 2 + 4 * xy**2)
    coherence = np.where(trace > 1e-6, anisotropy / (trace + 1e-9), 0)
    textured = trace > np.percentile(trace, 75)
    return float(coherence[textured].mean())


def radial_spectrum(gray: np.ndarray) -> np.ndarray:
    window = np.hanning(SIZE)
    energy = np.abs(
        np.fft.fftshift(np.fft.fft2(gray * window[:, None] * window[None, :]))
    ) ** 2
    y, x = np.indices(energy.shape)
    radius = np.hypot(x - SIZE / 2, y - SIZE / 2).astype(int)
    counts = np.bincount(radius.ravel())[: SIZE // 2]
    return np.bincount(radius.ravel(), energy.ravel())[: SIZE // 2] / np.maximum(counts, 1)


def spectral_peakiness(profile: np.ndarray) -> float:
    band = np.arange(8, 90)
    log_profile = np.log(profile[band] + 1e-12)
    trend = np.polyval(np.polyfit(np.log(band), log_profile, 2), np.log(band))
    return float((log_profile - trend).max())


def density_modulation(gray: np.ndarray) -> float:
    y, x = np.indices((SIZE, SIZE))
    radius = np.hypot(x - SIZE / 2, y - SIZE / 2)
    bandpass = ((radius > 16) & (radius < 64)).astype(float)
    filtered = np.real(
        np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(gray)) * bandpass))
    )
    energy = filtered**2
    blocks = energy.reshape(8, 32, 8, 32).mean(axis=(1, 3))
    return float(blocks.std() / (blocks.mean() + 1e-9))


def measure(gray: np.ndarray, hsv: np.ndarray) -> Metrics:
    profile = radial_spectrum(gray)
    band = np.arange(6, 100)
    slope = np.polyfit(np.log(band), np.log(profile[band] + 1e-12), 1)[0]
    dark = hsv[..., 2] < np.percentile(hsv[..., 2], 25)
    return Metrics(
        coherence=structure_coherence(gray),
        peakiness=spectral_peakiness(profile),
        density_cv=density_modulation(gray),
        spectrum_slope=float(slope),
        luminance_floor=float(np.percentile(gray, 0.5)),
        luminance_ceiling=float(np.percentile(gray, 99.5)),
        dark_saturation=float(hsv[..., 1][dark].mean()),
    )


def band_status(passes: bool, rejects: bool) -> str:
    if passes:
        return "PASS"
    if rejects:
        return "REJECT"
    return "REVIEW"


def print_report(label: str, metrics: Metrics, handling: str) -> bool:
    checks = [
        (
            band_status(metrics.coherence >= 0.25, metrics.coherence < 0.15),
            "coherence: pass >= 0.25; reject < 0.15",
        ),
        (
            band_status(metrics.peakiness < 0.70, metrics.peakiness > 1.00),
            "peakiness: pass < 0.70; reject > 1.00",
        ),
        (
            "PASS"
            if metrics.density_cv > 0.40
            else "REVIEW"
            if handling == "allover" or metrics.density_cv >= 0.30
            else "REJECT",
            "density_cv: pass > 0.40; reject < 0.30 unless all-over",
        ),
        (
            band_status(
                -2.60 <= metrics.spectrum_slope <= -1.60,
                metrics.spectrum_slope > -1.20,
            ),
            "slope: pass -2.60..-1.60; reject > -1.20",
        ),
    ]
    print(label)
    print(f"  handling      {handling}")
    print(f"  coherence     {metrics.coherence:7.3f}")
    print(f"  peakiness     {metrics.peakiness:7.3f}")
    print(f"  density_cv    {metrics.density_cv:7.3f}")
    print(f"  spectrum_slope{metrics.spectrum_slope:7.3f}")
    print(f"  luminance_p005{metrics.luminance_floor:7.3f}  context only")
    print(f"  luminance_p995{metrics.luminance_ceiling:7.3f}  context only")
    print(f"  dark_saturation{metrics.dark_saturation:6.3f}  context only")
    for status, name in checks:
        print(f"  {status:6s} {name}")
    return all(status != "REJECT" for status, _ in checks)


def parse_crop(value: str) -> tuple[int, int, int, int]:
    try:
        crop = tuple(int(part.strip()) for part in value.split(","))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("crop must contain four integers") from exc
    if len(crop) != 4:
        raise argparse.ArgumentTypeError("crop must be x0,y0,x1,y1")
    return crop


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument(
        "--crop",
        type=parse_crop,
        help="dominant-material crop in source pixels: x0,y0,x1,y1",
    )
    parser.add_argument(
        "--handling",
        choices=("conventional", "allover"),
        default="conventional",
        help="allover makes density advisory; spacing, scale, and flow still apply",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return nonzero only for a strong REJECT diagnostic, not REVIEW",
    )
    args = parser.parse_args()

    gray, hsv = load_image(args.image, None)
    passes = [print_report("whole image", measure(gray, hsv), args.handling)]
    if args.crop is not None:
        gray, hsv = load_image(args.image, args.crop)
        passes.append(
            print_report(
                f"material crop {args.crop}",
                measure(gray, hsv),
                args.handling,
            )
        )
    print(
        "Visual gates still required: nonperiodic spacing, mixed scale, material flow, "
        "desaturation, stamp-family, and object-material contact. Conventional scenes "
        "also require quiet/transition/active organization."
    )
    return 1 if args.strict and not all(passes) else 0


if __name__ == "__main__":
    raise SystemExit(main())
