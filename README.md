# Plant Disease Detection using YOLOv5

Welcome to the **Plant Disease Infection Detection** project!  
This project uses a **YOLOv5** object detection model, trained on a custom dataset, to automatically identify infections and diseases in plant leaves.

---

## 📂 Project Overview

- **Model**: YOLOv5 (custom trained)
- **Task**: Object Detection – Detect plant infections
- **Dataset**: Custom annotated dataset
- **Framework**: PyTorch (via YOLOv5)
- **Goal**: Early identification of plant diseases to assist in timely intervention.

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/Ramsha-18/Plant-Disease-Infection-.git
cd Plant-Disease-Infection-
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Make sure you have:
- Python 3.8+
- PyTorch installed
- Other YOLOv5 dependencies

You can install PyTorch from [official site](https://pytorch.org/get-started/locally/).

### 3. Inference on Custom Images
Put your test images inside a folder, e.g., `inference/images/`, then run:
```bash
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.4 --source inference/images
```

### 4. Training on Custom Dataset
If you want to retrain:
```bash
python train.py --img 640 --batch 16 --epochs 100 --data dataset.yaml --weights yolov5s.pt
```
- Modify `dataset.yaml` according to your dataset classes and paths.

---

## 🔧 Project Structure
```
Plant-Disease-Infection-
├── dataset/          # Custom annotated dataset
├── runs/             # Training results and weights
├── models/           # YOLOv5 models
├── detect.py         # Inference script
├── train.py          # Training script
├── dataset.yaml      # Dataset configuration
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 📊 Results
- **Precision**: *Coming soon*
- **Recall**: *Coming soon*
- **mAP**: *Coming soon*

(You can update this after your evaluation)

---

## 🎓 Acknowledgements
- [Ultralytics YOLOv5 Repository](https://github.com/ultralytics/yolov5)
- [LabelImg](https://github.com/tzutalin/labelImg) for dataset annotation

---

## 🚀 Future Work
- Improve model performance with more diverse datasets
- Deploy model on mobile devices
- Create an API for easy access

---

## 👤 Author
**Ramsha**

[GitHub](https://github.com/Ramsha-18)

---

## ✨ Feel free to Fork and Star the repository if you find it helpful!


> Made with ❤️ for improving plant health!
