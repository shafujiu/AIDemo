from  ultralytics import YOLO
model = YOLO('runs/detect/train14/weights/best.pt')
model.predict('../datasets/Base-3C-Circle-Mark/images', save=True, line_width=1)