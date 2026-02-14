import os

# Old class names from your dataset
old_classes = ['1', '2', '4', 'Beverage Cans', 'Bolsa', 'Botella', 'Bottle', 'Bottle cap', 'Branch',
'Bungkus Makanan', 'Can', 'Fishing wastes', 'Glass Bottles', 'Glass wastes',
'Juice Box', 'Juice box', 'Kantong Plastik', 'Metal wastes', 'Natural wastes',
'Paper', 'Plastic', 'Plastic Bags', 'Plastic Bottle', 'Plastic Bottles',
'Plastic bag', 'Plastic bottle', 'Plastic cup', 'Plastic packaging',
'Plastic wastes', 'Plastic-Bottle', 'Plastic-Bottles', 'Plastics Container',
'Plastics Trash', 'Plato', 'Red de pesca', 'Trash', 'Undefined trash',
'Vaso', 'Waste', 'Wood', 'Wood wastes', 'botellas-de-plastico',
'bottle', 'bouteille', 'can', 'cardboard', 'dechet', 'drink can',
'drink carton', 'fishing_net', 'foam', 'glass', 'glass-bottle',
'metal', 'misc', 'other', 'paper', 'pbag', 'pbottle',
'pet bottle', 'petbottle', 'plastic', 'plastic bottle',
'plastic_ silverware', 'plastic_bag', 'plastic_bags',
'plastic_bottle', 'plastic_cup', 'plastic_mug',
'plastic_plates', 'pmb', 'polythene bag', 'sac',
'sld', 'slh', 'slp', 'soda_cans', 'sprite',
'tire', 'unknow']

# Mapping old → new class index
mapping = {}

def assign(idx, new_class):
    mapping[idx] = new_class

for i, name in enumerate(old_classes):
    n = name.lower()

    if "bottle" in n:
        assign(i, 0)

    elif "bag" in n or "bolsa" in n or "sac" in n or "pbag" in n or "polythene" in n:
        assign(i, 1)

    elif "container" in n or "cup" in n or "mug" in n or "plates" in n:
        assign(i, 2)

    elif "can" in n or "soda" in n or "sprite" in n:
        assign(i, 3)

    elif "metal" in n:
        assign(i, 4)

    elif "glass" in n or "vaso" in n or "bouteille" in n:
        assign(i, 5)

    elif "paper" in n or "cardboard" in n or "carton" in n:
        assign(i, 6)

    elif "wood" in n or "branch" in n or "natural" in n:
        assign(i, 7)

    elif "fishing" in n or "red de pesca" in n:
        assign(i, 8)

    elif "tire" in n:
        assign(i, 9)

    elif "electronic" in n:
        assign(i, 10)

    elif "hazard" in n:
        assign(i, 12)

    elif "trash" in n or "waste" in n or "misc" in n or "other" in n or "undefined" in n:
        assign(i, 11)

    else:
        assign(i, 13)


def process_labels(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    lines = f.readlines()

                new_lines = []
                for line in lines:
                    parts = line.strip().split()
                    old_id = int(parts[0])
                    new_id = mapping.get(old_id, 13)
                    parts[0] = str(new_id)
                    new_lines.append(" ".join(parts) + "\n")

                with open(path, "w") as f:
                    f.writelines(new_lines)


print("Remapping train labels...")
process_labels("train/labels")

print("Remapping valid labels...")
process_labels("valid/labels")

print("Remapping test labels...")
process_labels("test/labels")

print("Done.")
