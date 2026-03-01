# PrithviQ – Model Version Log

This file tracks major model experiments and performance evolution.

---

## 🔹 Model v1 – 14-Class Baseline

**Architecture:** YOLOv8m (Detection)  
**Classes:** 14  
**Image Size:** 640  
**Result:**
- mAP50 ≈ 0.17 – 0.20
- Unstable training
- Severe class imbalance
- Rare classes underperforming

**Issues Identified:**
- Dataset highly imbalanced
- Dense clutter scenes
- Bounding box confusion
- Poor recall

**Conclusion:** Not suitable for production-level use.

---

## 🔹 Model v2 – Macro 5-Class Model

**Architecture:** YOLOv8m (Detection)  
**Classes:** 5 (Plastic, Metal, Glass, Organic, Hazardous)  
**Image Size:** 640  
**Dataset Size:** 8,522 images  
**Total Instances:** 48,581  

**Validation Results:**
- Precision: 0.51
- Recall: 0.33
- mAP50: 0.326
- mAP50-95: 0.195

**Improvements Over v1:**
- Reduced class confusion
- More stable training
- Higher peak performance
- Improved detection of dominant waste categories

**Current Limitation:**
- Glass severely underrepresented
- Small-object detection still challenging
- Dense clutter limits bounding box accuracy

---

## 🔹 Next Planned Experiments

- Increase resolution to 768
- Train YOLOv8-seg for pixel-level coverage
- Improve recall using augmentation tuning
- Add density-based waste severity scoring

---

## 📌 Status

Macro detection model (v2) is considered the current stable baseline.
Future improvements will build on this checkpoint.