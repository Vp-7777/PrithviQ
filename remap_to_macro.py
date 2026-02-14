import os

# ORIGINAL DATASET
OLD_TRAIN_LABELS = "train/labels"
OLD_VAL_LABELS = "valid/labels"

# NEW MACRO DATASET
NEW_TRAIN_LABELS = "dataset_macro/train/labels"
NEW_VAL_LABELS = "dataset_macro/valid/labels"

os.makedirs(NEW_TRAIN_LABELS, exist_ok=True)
os.makedirs(NEW_VAL_LABELS, exist_ok=True)

# 14-class → 5-class mapping
mapping = {
    # Plastic group
    0: 0,
    1: 0,
    2: 0,
    8: 0,
    9: 0,
    11: 0,
    13: 0,

    # Metal
    3: 1,
    4: 1,

    # Glass
    5: 2,

    # Organic
    6: 3,
    7: 3,

    # Hazardous
    10: 4,
    12: 4
}

def remap_folder(old_folder, new_folder):
    for file in os.listdir(old_folder):
        if file.endswith(".txt"):
            old_path = os.path.join(old_folder, file)
            new_path = os.path.join(new_folder, file)

            with open(old_path, "r") as f:
                lines = f.readlines()

            new_lines = []

            for line in lines:
                parts = line.strip().split()
                if len(parts) == 0:
                    continue

                old_class = int(parts[0])

                if old_class in mapping:
                    new_class = mapping[old_class]
                    parts[0] = str(new_class)
                    new_lines.append(" ".join(parts))

            with open(new_path, "w") as f:
                f.write("\n".join(new_lines))


print("Remapping train labels...")
remap_folder(OLD_TRAIN_LABELS, NEW_TRAIN_LABELS)

print("Remapping validation labels...")
remap_folder(OLD_VAL_LABELS, NEW_VAL_LABELS)

print("Done. Macro dataset ready.")
