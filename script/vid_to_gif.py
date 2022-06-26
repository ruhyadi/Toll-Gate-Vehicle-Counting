"""Convert video to gif with moviepy"""

import moviepy.editor as mp
import argparse

def convert(vid_path, gif_path, fps=10):
    """Convert video to gif"""
    clip = mp.VideoFileClip(vid_path).resize(width=480)
    clip.write_gif(gif_path, fps=fps)
    clip.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert video to gif")
    parser.add_argument("--vid_path", default="/raid/didir/Repository/Toll-Gate-Vehicle-Counting/runs/track/exp/toll_gate.mp4", help="Path to video")
    parser.add_argument("--gif_path", default="/raid/didir/Repository/Toll-Gate-Vehicle-Counting/runs/track/exp/toll_gate.gif", help="Path to gif")
    parser.add_argument("--fps", type=int, default=5, help="FPS of gif")
    args = parser.parse_args()

    convert(args.vid_path, args.gif_path, args.fps)