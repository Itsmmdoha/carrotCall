from ultralytics import YOLO

model = YOLO("yolov8m.pt")

results = model("your_image.png", conf=.6)

results[0].show()
