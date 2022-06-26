<div align="center">

# Toll Gate Vehicle Counting

<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-Python 3.8+-blue?style=flat&logo=python&logoColor=white"></a>
<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/-PyTorch 1.8+-ee4c2c?style=flat&logo=pytorch&logoColor=white"></a>
<a href="https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet"><img alt="Template" src="https://img.shields.io/badge/-Yolov5__StrongSORT__OSNet-017F2F?style=flat&logo=github&labelColor=gray"></a><br>

</div>

## ⚠️&nbsp;&nbsp;Cautions
> This repository currently under development

## 📼&nbsp;&nbsp;Demo
<div align="center">

![demo](./docs/demo.gif)

</div>

## 📌&nbsp;&nbsp;Introduction

Lorem ipsum

## 🚀&nbsp;&nbsp;Quickstart
> Lorem ipsum

### 🍿&nbsp;&nbsp;Inference
```bash
python track.py \
    --source ./data/toll_gate.mp4 \
    --yolo-weights ./weights/yolov5s.pt \
    --strong-sort-weights ./weights/osnet_x0_25_msmt17.pt \
    --classes 2 5 7 \
    --save-vid
```

## ❤️&nbsp;&nbsp;Acknowledgement

- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)
- [mikel-brostrom/Yolov5_StrongSORT_OSNet](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet)