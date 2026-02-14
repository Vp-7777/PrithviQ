from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train4/weights/best.pt")

# Run prediction on a test image
results = model.predict(source="dataset/images/train", save=True)
