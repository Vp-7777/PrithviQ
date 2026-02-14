import os
from collections import defaultdict

TRAIN_LABELS = "train/labels"
VAL_LABELS = "valid/labels"

def count_labels(label_folder):
    class_counts = defaultdict(int)
    total_instances = 0
    total_images = 0

    for file in os.listdir(label_folder):
        if file.endswith(".txt"):
            total_images += 1
            with open(os.path.join(label_folder, file), "r") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 0:
                        continue

                    cls_id = parts[0]
                    class_counts[cls_id] += 1
                    total_instances += 1

    return total_images, total_instances, class_counts


train_imgs, train_instances, train_class_counts = count_labels(TRAIN_LABELS)
val_imgs, val_instances, val_class_counts = count_labels(VAL_LABELS)

print("\n===== DATASET STATISTICS =====\n")

print("TRAIN SET")
print("Images:", train_imgs)
print("Instances:", train_instances)
print("Instances per class:")
for cls in sorted(train_class_counts):
    print(f"Class {cls}: {train_class_counts[cls]}")

print("\nVALIDATION SET")
print("Images:", val_imgs)
print("Instances:", val_instances)
print("Instances per class:")
for cls in sorted(val_class_counts):
    print(f"Class {cls}: {val_class_counts[cls]}")

print("\nTOTAL DATASET")
print("Total Images:", train_imgs + val_imgs)
print("Total Instances:", train_instances + val_instances)
