from ultralytics import YOLO
# 创建全新模型
# Load a model
# model = YOLO('yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

model = YOLO('runs/detect/train13/weights/best.pt')

# results = model.train(data='3C-Circle-2024-01-31.yaml', epochs=100)
# metrics = model.val()  
# model.predict('1.jpg', save=True, show=True, line_width=1)

success = model.export(format='onnx')

