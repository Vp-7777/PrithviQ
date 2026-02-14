from ultralytics import YOLO
import cv2
import numpy as np
from collections import defaultdict

# -----------------------------
# SETTINGS
# -----------------------------
MODEL_PATH = "runs/detect/train10/weights/best.pt"
IMAGE_PATH = "garbage.jpg"

TILE_SIZE = 800
OVERLAP = 0.2  # 20% overlap
CONF_THRESHOLD = 0.15

# -----------------------------
# LOAD MODEL
# -----------------------------
model = YOLO(MODEL_PATH)

# -----------------------------
# LOAD IMAGE
# -----------------------------
image = cv2.imread(IMAGE_PATH)
img_h, img_w = image.shape[:2]
image_area = img_h * img_w

stride = int(TILE_SIZE * (1 - OVERLAP))

detections = []

# -----------------------------
# TILE LOOP
# -----------------------------
for y in range(0, img_h, stride):
    for x in range(0, img_w, stride):

        y_end = min(y + TILE_SIZE, img_h)
        x_end = min(x + TILE_SIZE, img_w)

        tile = image[y:y_end, x:x_end]

        if tile.shape[0] < 100 or tile.shape[1] < 100:
            continue

        results = model(tile, conf=CONF_THRESHOLD, imgsz=1024)

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                # Adjust coordinates to original image
                x1 = x1 + x
                x2 = x2 + x
                y1 = y1 + y
                y2 = y2 + y

                detections.append((cls_id, conf, x1, y1, x2, y2))

# -----------------------------
# AGGREGATE RESULTS
# -----------------------------
class_counts = defaultdict(int)
class_area = defaultdict(float)

for det in detections:
    cls_id, conf, x1, y1, x2, y2 = det
    cls_name = model.names[cls_id]

    class_counts[cls_name] += 1
    box_area = (x2 - x1) * (y2 - y1)
    class_area[cls_name] += box_area

# -----------------------------
# REPORT
# -----------------------------
print("\nTILED Waste Analysis Report")
print("============================")

for cls in class_counts:
    coverage = (class_area[cls] / image_area) * 100
    print(f"{cls}:")
    print(f"  Count: {class_counts[cls]}")
    print(f"  Coverage: {round(coverage,2)} %")
    print()

total_detected_area = sum(class_area.values())
total_coverage = (total_detected_area / image_area) * 100

print("Total Waste Coverage:", round(total_coverage,2), "%")
