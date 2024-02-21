from ultralytics.utils.benchmarks import benchmark
# 模型在各个平台的效果
benchmark(model='runs/detect/train8/weights/best.pt', data='Base-3C-Circle-Mark/Base-3C-Circle-Mark.yaml', imgsz=640, half=False, device='mps')