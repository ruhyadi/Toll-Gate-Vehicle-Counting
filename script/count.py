"""Count vehicle entrace gate"""

import pandas as pd

class Counting:
    """Counting vehicle entrace gate"""
    def __init__(self, line, classes=None):
        self.line = line
        self.classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
            'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
            'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
            'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
            'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
            'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
            'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
            'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
            'hair drier', 'toothbrush'] if classes is None else classes

        self.df = pd.DataFrame(columns=['ids', 'cls'])

    def count(self, cxcy, id, cls):
        """Count vehicle entrace gate"""
        cx, cy = cxcy[0], cxcy[1]

        if cy < self.line and id not in self.df['ids'].unique():
            # append id to dataframe
            self.df = pd.concat(
                [self.df, pd.DataFrame([[id, self.classes[cls]]], columns=['ids', 'cls'])], 
                ignore_index=True)

    def result(self):
        """Get result"""
        total = len(self.df.index)
        total_class = self.df['cls'].value_counts().to_dict()

        return [total, total_class]

if __name__ == "__main__":

    counting = Counting(line=30)
    points = [(20, 10), (20, 15), (20, 17)]
    for i, point in enumerate(points):
        counting.count(point, i, 0)

    print(counting.result())