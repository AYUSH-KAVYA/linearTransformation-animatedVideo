"""
Build & Render Script for Linear Transformations M3 Animation Video.
Usage:
    python _Code/build_video.py --quality preview   # Fast 480p check + timing report
    python _Code/build_video.py --quality 1080p     # Production 1920x1080 30fps MP4
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
CODE_DIR = Path(__file__).resolve().parent
MEDIA_DIR = ROOT_DIR / "media"
OUTPUT_VIDEO = ROOT_DIR / "LinearTransformations_Video.mp4"

SCENES = [
    ("scene1_hook.py", "HookScene"),
    ("scene2_concept.py", "ConceptIntroScene"),
    ("scene3_intuition.py", "VisualIntuitionScene"),
    ("scene4_worked_example.py", "WorkedExampleScene"),
    ("scene5_interpretation.py", "InterpretationScene"),
    ("scene6_summary.py", "SummaryScene"),
]


def setup_env() -> dict:
    env = os.environ.copy()
    tinytex_bin = Path.home() / "Library" / "TinyTeX" / "bin" / "universal-darwin"
    if tinytex_bin.exists():
        env["PATH"] = f"{tinytex_bin}:{env.get('PATH', '')}"
    env["PYTHONPATH"] = f"{CODE_DIR}:{env.get('PYTHONPATH', '')}"
    return env


def get_duration(mp4_path: Path) -> float:
    res = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(mp4_path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return float(res.stdout.strip())


def format_ts(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = seconds % 60
    return f"{mins:02d}:{secs:04.1f}"


def main():
    parser = argparse.ArgumentParser(description="Render and assemble Linear Transformations video.")
    parser.add_argument(
        "--quality",
        choices=["preview", "1080p"],
        default="1080p",
        help="Render quality preset (preview=480p15, 1080p=1080p30)",
    )
    parser.add_argument(
        "--scenes",
        nargs="*",
        type=int,
        help="Optional 1-based scene indices to re-render (e.g. --scenes 1 6)",
    )
    args = parser.parse_args()

    env = setup_env()
    quality_flags = (
        ["-ql", "--fps", "15"]
        if args.quality == "preview"
        else ["-qh", "--fps", "30", "-r", "1920,1080"]
    )
    quality_folder = "480p15" if args.quality == "preview" else "1080p30"

    scene_videos = []
    for idx, (filename, scene_cls) in enumerate(SCENES, start=1):
        script_path = CODE_DIR / filename
        stem = script_path.stem
        out_mp4 = MEDIA_DIR / "videos" / stem / quality_folder / f"{scene_cls}.mp4"

        if args.scenes is None or idx in args.scenes:
            print(f"\n=== Rendering Scene {idx}: {scene_cls} ({args.quality}) ===")
            cmd = [
                sys.executable,
                "-m",
                "manim",
                *quality_flags,
                "--media_dir",
                str(MEDIA_DIR),
                str(script_path),
                scene_cls,
            ]
            subprocess.run(cmd, env=env, cwd=str(ROOT_DIR), check=True)

        if not out_mp4.exists():
            raise FileNotFoundError(f"Expected rendered scene not found: {out_mp4}")
        scene_videos.append((scene_cls, out_mp4))

    # Concatenate into final MP4
    concat_file = MEDIA_DIR / f"concat_{args.quality}.txt"
    concat_file.parent.mkdir(parents=True, exist_ok=True)
    with open(concat_file, "w") as f:
        for _, vp in scene_videos:
            f.write(f"file '{vp.resolve()}'\n")

    target_mp4 = (
        ROOT_DIR / "LinearTransformations_Preview.mp4"
        if args.quality == "preview"
        else OUTPUT_VIDEO
    )

    print(f"\n=== Concatenating into {target_mp4.name} ===")
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", str(concat_file),
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-crf", "20",
            "-preset", "medium",
            "-movflags", "+faststart",
            str(target_mp4),
        ],
        check=True,
    )

    print("\n=== Scene Timing Summary ===")
    cursor = 0.0
    for scene_cls, vp in scene_videos:
        dur = get_duration(vp)
        print(f"  {scene_cls:22s}: {format_ts(cursor)} -> {format_ts(cursor + dur)}  ({dur:.2f}s)")
        cursor += dur
    total_dur = get_duration(target_mp4)
    size_mb = target_mp4.stat().st_size / (1024 * 1024)
    print(f"\nFinal video: {target_mp4}")
    print(f"Total duration: {format_ts(total_dur)} ({total_dur:.2f}s) | Size: {size_mb:.2f} MB")


if __name__ == "__main__":
    main()
