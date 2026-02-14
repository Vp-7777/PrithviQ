from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Run detection on your garbage image
results = model.predict(source="garbage.jpg", save=True, imgsz=640)

print("Detection completed.")
print("Check the folder: runs/detect/predict/")
