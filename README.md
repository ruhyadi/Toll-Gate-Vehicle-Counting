# Toll-Gate-Vehicle-Counting
Counting Entrance Vehicle on Toll Gate


## Inference

```bash
python track.py \
    --source ./data/toll_gate.mp4 \
    --yolo-weights ./weights/yolov5s.pt \
    --strong-sort-weights ./weights/osnet_x0_25_msmt17.pt \
    --classes 2 5 7 \
    --save-vid \
    --save-result

```