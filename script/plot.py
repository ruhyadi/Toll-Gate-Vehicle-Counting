"""Plot utils"""

import numpy as np
import cv2

def get_trans_mtx(frame, src=None, dst=None):
    """Get transformation matrix"""
    H, W = frame.shape[0], frame.shape[1]
    if src is None and dst is None: # default to toll_gate.mp4 frame
        src = [(0, 195), (390, 292), (485, 262), (75, 175)] # counter-clock (bottom-left)
        dst = [[0, 125], [W, 125], [W, 25], [0, 25]] # counter-clock (bottom-left)
    src = np.float32(np.array(src))
    dst = np.float32(dst)
    matrix = cv2.getPerspectiveTransform(src, dst)

    return matrix

def wrap_perspective(frame, matrix, W=None, H=None):
    """Wrap frame with perspective"""
    if W is None and H is None:
        H, W = frame.shape[0], frame.shape[1]
    out = cv2.warpPerspective(frame, matrix, (W, H), flags=cv2.INTER_LINEAR)

    return out

def get_trans_point(xyxy, matrix):
    """Get transformed point with trans mtx"""
    cx = (xyxy[2] - xyxy[0])/2 + xyxy[0]
    cy = (xyxy[3] - xyxy[1])/2 + xyxy[1]
    centroid = np.array([[[cx, cy]]])
    trans_cent = cv2.perspectiveTransform(centroid, matrix)[0][0]

    return (int(trans_cent[0]), int(trans_cent[1]))

def draw_point(frame, cxcy, id):
    """Draw point to frame"""
    frame = cv2.circle(frame, cxcy, radius=7, color=(0, 255, 0), thickness=-1)
    frame = cv2.putText(frame, str(id), (cxcy[0] + 5, cxcy[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    return frame

if __name__ == "__main__":

    # Read image
    img = cv2.imread("/raid/didir/Repository/Toll-Gate-Vehicle-Counting/data/frame.png")
    src = [(0, 195), (390, 292), (485, 262), (75, 175)]
    dst = [[0, 125], [img.shape[1], 125], [img.shape[1], 25], [0, 25]]
    # Get transformation matrix
    matrix = get_trans_mtx(img, src, dst)
    out = wrap_perspective(img, matrix)

    # transform point
    xyxy = [150, 300, 160, 310]
    cxcy = get_trans_point(xyxy, matrix)

    out = draw_point(out, cxcy, '1')

    cv2.imwrite('/raid/didir/Repository/Toll-Gate-Vehicle-Counting/data/out.png', out)