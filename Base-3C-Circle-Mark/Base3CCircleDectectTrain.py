from  ultralytics import YOLO
import os
os.environ['WANDB_MODE'] = 'dryrun' # 去除wandb同步选择

# model = YOLO('yolov8n.yaml')  # build a new model from YAML
# model = YOLO('yolov8n.pt') # 切记加载预训练模型

# model = YOLO('circle_pre.pt')
# results = model.train(data='Base-3C-Circle-Mark/Base-3C-Circle-Mark.yaml', epochs=1000, device='mps', imgsz=960)

# 恢复
model = YOLO('runs/detect/train/weights/last.pt')
results = model.train(resume=True)
# 验证
# model.val()w
# 导出模型
# success = model.export(format="coreml", int8=True, nms=True, imgsz=[640, 384])