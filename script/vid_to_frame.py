"""Convert video to frame"""

import cv2

def convert(vid_path, frame_path):
    """Convert video to frame"""
    vid = cv2.VideoCapture(vid_path)
    frame_count = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Frame count: {}".format(frame_count))
    for i in range(frame_count):
        vid.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = vid.read()
        cv2.imwrite(frame_path + "/frame{}.jpg".format(i), frame)
    vid.release()
    print("Done!")