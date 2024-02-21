from  ultralytics import YOLO
import os
os.environ['WANDB_MODE'] = 'dryrun' # 去除wandb同步选择

# model = YOLO('yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.pt') # 切记加载预训练模型

model = YOLO('circle_pre.pt')
results = model.train(data='Base-3C-Circle-Mark/3C-Circle-Mark-Sub.yaml', epochs=1000, device='mps', imgsz=960)


# 恢复
# model = YOLO('runs/detect/train4/weights/best.pt')
# model.val()
# results = model.train(resume=True)
# success = model.export(format='coreml')