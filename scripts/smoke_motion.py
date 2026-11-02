#!/usr/bin/env python3
"""Exercise the uploaded motion CLIs with synthetic, temporary fixtures."""
import subprocess
import sys
import tempfile
from pathlib import Path

import imageio.v3 as iio
import numpy as np
from PIL import Image


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def check_gif(path, size, minimum_frames):
    require(path.is_file(), f"Missing GIF: {path}")
    with Image.open(path) as image:
        require(image.size == size, f"Wrong GIF dimensions: {path}")
        require(image.n_frames >= minimum_frames, f"Missing GIF frames: {path}")
        require(image.info.get("loop") == 0, f"GIF is not looping: {path}")
        for index in range(image.n_frames):
            image.seek(index)
            image.load()
            require(image.info.get("duration", 0) > 0, f"Missing GIF timing: {path}")


def main():
    root = Path(__file__).resolve().parents[1]
    scripts = root / "skills/motion-creative-producer-codex/scripts"
    with tempfile.TemporaryDirectory(prefix="codex-social-smoke-") as directory:
        temporary = Path(directory)
        frames = temporary / "frames"
        frames.mkdir()
        yy, xx = np.indices((96, 96))
        for index in range(12):
            array = np.stack(
                ((xx * 2 + index * 12) % 256, yy * 2, (xx + yy + index * 8) % 256),
                axis=-1,
            ).astype("uint8")
            image = Image.fromarray(array)
            if index == 6:
                image = image.resize((128, 96))  # Exercise mixed-size frame handling.
            image.save(frames / f"frame-{index:03d}.png")

        output = temporary / "exports" / "loop.mp4"
        subprocess.run(
            [sys.executable, str(scripts / "make_loop.py"), "--frames", str(frames),
             "--output", str(output), "--fps", "8", "--gif"],
            check=True,
        )
        # The upstream CLI catches encoding errors, so verify actual artifacts.
        require(output.is_file() and output.stat().st_size > 0, "MP4 export failed")
        decoded = list(iio.imiter(output, plugin="FFMPEG"))
        require(len(decoded) == 12, "MP4 does not contain all 12 frames")
        require(all(frame.shape[:2] == (96, 96) for frame in decoded), "Wrong MP4 size")
        metadata = iio.immeta(output, plugin="FFMPEG")
        require(abs(metadata["fps"] - 8) < 0.01, "Wrong MP4 frame rate")
        require(not np.array_equal(decoded[0], decoded[-1]), "MP4 is static")
        check_gif(output.with_suffix(".gif"), (96, 96), 12)

        for effect in ("breathe", "push", "drift"):
            gif = temporary / f"{effect}.gif"
            subprocess.run(
                [sys.executable, str(scripts / "make_subtle_loop.py"),
                 "--input", str(frames / "frame-000.png"), "--output", str(gif),
                 "--frames", "24", "--fps", "8", "--effect", effect],
                check=True,
            )
            check_gif(gif, (96, 96), 2)
    print("PASS: decoded 12-frame MP4, looping GIF, and all 3 subtle-loop effects")


if __name__ == "__main__":
    main()
