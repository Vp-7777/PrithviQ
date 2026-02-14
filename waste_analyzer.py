from ultralytics import YOLO
import cv2
import numpy as np
from collections import defaultdict

# Load trained model
model = YOLO("runs/detect/train10/weights/best.pt")

# Load image
image_path = "garbage.jpg"
results = model(image_path, conf=0.15, imgsz=1024)


# Get image dimensions
img = cv2.imread(image_path)
img_h, img_w = img.shape[:2]
image_area = img_h * img_w

class_counts = defaultdict(int)
class_area = defaultdict(int)

for r in results:
    boxes = r.boxes
    for box in boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        conf = float(box.conf[0])

        # Count
        class_counts[cls_name] += 1

        # Area calculation
        x1, y1, x2, y2 = box.xyxy[0]
        box_area = (x2 - x1) * (y2 - y1)
        class_area[cls_name] += float(box_area)

# Calculate coverage %
class_coverage = {}
for cls in class_area:
    coverage = (class_area[cls] / image_area) * 100
    class_coverage[cls] = round(coverage, 2)

print("\nWaste Analysis Report")
print("======================")

for cls in class_counts:
    print(f"{cls}:")
    print(f"  Count: {class_counts[cls]}")
    print(f"  Coverage: {class_coverage.get(cls, 0)} %")
    print()

    
total_detected_area = sum(class_area.values())
total_coverage = (total_detected_area / image_area) * 100

print("Total Waste Coverage:", round(total_coverage, 2), "%")
