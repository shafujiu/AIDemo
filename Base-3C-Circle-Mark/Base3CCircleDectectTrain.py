from  ultralytics import YOLO
# model = YOLO('yolov8n.yaml')  # build a new model from YAML 首次
# 接着之前已经训练好的模型训练
# model = YOLO('runs/detect/train8/weights/best.pt')
# 恢复
model = YOLO('runs/detect/train8/weights/last.pt')
results = model.train(resume=True)
# results = model.train(data='Base-3C-Circle-Mark/Base-3C-Circle-Mark.yaml', epochs=1000, device='mps')
success = model.export(format='onnx')