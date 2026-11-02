#!/usr/bin/env python
import argparse
from pathlib import Path

from PIL import Image, ImageSequence


def load_frames(frames_dir: Path):
    paths = sorted(
        p for p in frames_dir.iterdir()
        if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
    )
    if not paths:
        raise SystemExit(f"No image frames found in {frames_dir}")

    frames = []
    size = None
    for path in paths:
        img = Image.open(path).convert("RGB")
        if size is None:
            size = img.size
        elif img.size != size:
            img = img.resize(size, Image.Resampling.LANCZOS)
        frames.append(img)
    return frames


def save_gif(frames, output: Path, fps: float):
    duration_ms = int(1000 / fps)
    gif_path = output.with_suffix(".gif")
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration_ms,
        loop=0,
        optimize=True,
    )
    return gif_path


def save_mp4_with_imageio(frames, output: Path, fps: float):
    import imageio.v3 as iio
    import numpy as np

    output.parent.mkdir(parents=True, exist_ok=True)
    arr = [np.asarray(frame) for frame in frames]
    iio.imwrite(output, arr, fps=fps, codec="libx264", quality=8)


def main():
    parser = argparse.ArgumentParser(description="Assemble ordered image frames into a looping MP4 and optional GIF.")
    parser.add_argument("--frames", required=True, help="Folder containing ordered frame images.")
    parser.add_argument("--output", required=True, help="Output MP4 path.")
    parser.add_argument("--fps", type=float, default=2.0, help="Frames per second.")
    parser.add_argument("--gif", action="store_true", help="Also export a GIF preview.")
    args = parser.parse_args()

    frames_dir = Path(args.frames)
    output = Path(args.output)
    frames = load_frames(frames_dir)

    try:
        save_mp4_with_imageio(frames, output, args.fps)
        print(f"Saved MP4: {output}")
    except Exception as exc:
        print(f"MP4 export failed: {exc}")
        print("GIF export may still work. Install imageio[ffmpeg] or use a runtime with ffmpeg support for MP4.")

    if args.gif:
        gif_path = save_gif(frames, output, args.fps)
        print(f"Saved GIF: {gif_path}")


if __name__ == "__main__":
    main()

