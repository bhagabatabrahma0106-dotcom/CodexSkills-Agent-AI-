#!/usr/bin/env python
import argparse
import math
from pathlib import Path

from PIL import Image, ImageEnhance


def ease_sine(t: float) -> float:
    return 0.5 - 0.5 * math.cos(2 * math.pi * t)


def cover_crop(img: Image.Image, width: int, height: int) -> Image.Image:
    src_w, src_h = img.size
    scale = max(width / src_w, height / src_h)
    new_size = (int(src_w * scale + 0.5), int(src_h * scale + 0.5))
    resized = img.resize(new_size, Image.Resampling.LANCZOS)
    left = (resized.width - width) // 2
    top = (resized.height - height) // 2
    return resized.crop((left, top, left + width, top + height))


def make_frame(base: Image.Image, i: int, total: int, effect: str) -> Image.Image:
    t = i / total
    e = ease_sine(t)
    w, h = base.size

    if effect == "push":
        zoom = 1.0 + 0.035 * e
        dx = int((e - 0.5) * w * 0.012)
        dy = int((0.5 - e) * h * 0.008)
    elif effect == "drift":
        zoom = 1.025
        dx = int(math.sin(2 * math.pi * t) * w * 0.018)
        dy = int(math.cos(2 * math.pi * t) * h * 0.012)
    else:
        zoom = 1.0 + 0.018 * e
        dx = 0
        dy = int(math.sin(2 * math.pi * t) * h * 0.006)

    enlarged = base.resize((int(w * zoom + 0.5), int(h * zoom + 0.5)), Image.Resampling.LANCZOS)
    left = (enlarged.width - w) // 2 + dx
    top = (enlarged.height - h) // 2 + dy
    left = max(0, min(left, enlarged.width - w))
    top = max(0, min(top, enlarged.height - h))
    frame = enlarged.crop((left, top, left + w, top + h))

    if effect in {"breathe", "drift"}:
        brightness = 1.0 + 0.025 * math.sin(2 * math.pi * t)
        frame = ImageEnhance.Brightness(frame).enhance(brightness)

    return frame


def main():
    parser = argparse.ArgumentParser(description="Create a seamless subtle GIF loop from a single image.")
    parser.add_argument("--input", required=True, help="Input image path.")
    parser.add_argument("--output", required=True, help="Output GIF path.")
    parser.add_argument("--frames", type=int, default=24, help="Number of frames.")
    parser.add_argument("--fps", type=float, default=8.0, help="Frames per second.")
    parser.add_argument("--effect", choices=["breathe", "push", "drift"], default="breathe")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    base = Image.open(input_path).convert("RGB")
    frames = [make_frame(base, i, args.frames, args.effect) for i in range(args.frames)]
    duration_ms = int(1000 / args.fps)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
    )
    print(f"Saved subtle loop: {output_path}")


if __name__ == "__main__":
    main()
