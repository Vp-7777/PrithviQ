from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
