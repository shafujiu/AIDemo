from ultralytics import YOLO

# Loop through all YOLOv8 model sizes
for size in ("n", "s", "m", "l", "x"):

    # Load a YOLOv8 PyTorch model
    model = YOLO(f"yolov8{size}.pt")

    # Export the PyTorch model to CoreML INT8 format with NMS layers
    model.export(format="coreml", int8=True, nms=True, imgsz=[640, 384])


# 导出训练的某个模型
model = YOLO('runs/detect/train/weights/last.pt')
# results = model.train(resume=True)
# 验证
# model.val()w
success = model.export(format="coreml", int8=True, nms=True, imgsz=[640, 384])