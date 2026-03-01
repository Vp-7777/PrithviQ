# PrithviQ – Development Roadmap

## 🎯 Vision
To build a world-class AI-powered environmental intelligence system capable of analyzing lake and marine waste using computer vision and generating actionable cleanup insights.

---

## ✅ Phase 1 – Baseline Detection (Completed)

- 14-class YOLOv8m baseline
- Identified class imbalance issues
- Macro class remapping (14 → 5 classes)
- Achieved mAP50 ≈ 0.326
- Stable detection pipeline
- Tile-based inference for dense scenes
- Waste coverage estimation system

---

## 🚀 Phase 2 – Performance Enhancement (In Progress)

- Increase resolution (640 → 768)
- Improve small-object detection
- Optimize augmentations
- Address rare class imbalance
- Improve recall without sacrificing precision

---

## 🔬 Phase 3 – Segmentation Upgrade

- Train YOLOv8-seg model
- Pixel-level waste masking
- Improve coverage accuracy
- Better dense clutter handling
- Improve real-world reliability

---

## 📊 Phase 4 – Waste Intelligence Engine

- Waste severity scoring
- Density heatmap generation
- Waste composition percentage report
- Recyclable material estimation
- Environmental impact estimation

---

## 🌍 Phase 5 – Deployment & Integration

- Web dashboard interface
- NGO/Government report export (PDF/JSON)
- Drone image support
- Real-time inference capability
- API endpoint for integrations

---

## 💡 Long-Term Goal

PrithviQ aims to become a scalable environmental AI system capable of assisting municipalities, NGOs, and environmental agencies in sustainable waste management and cleanup planning.