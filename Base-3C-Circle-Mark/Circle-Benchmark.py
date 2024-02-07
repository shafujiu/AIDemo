from ultralytics.utils.benchmarks import benchmark

benchmark(model='runs/detect/train8/weights/best.pt', data='Base-3C-Circle-Mark/Base-3C-Circle-Mark.yaml', imgsz=640, half=False, device='mps')