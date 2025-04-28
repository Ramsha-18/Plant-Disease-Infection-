import torch
import os
from pathlib import Path
import shutil

# ====== CONFIG ======
MODEL_PATH = 'runs/train/exp/weights/best.pt'  # Path to your custom trained model
SOURCE_DIR = 'inference/images/'               # Folder containing images to detect
OUTPUT_DIR = 'inference/output/'                # Folder where results will be saved
IMG_SIZE = 640                                 # Inference image size
CONF_THRESHOLD = 0.4                           # Confidence threshold

# ====== SETUP ======
# Load model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH, force_reload=True)

# Set model parameters
model.conf = CONF_THRESHOLD  # Confidence threshold
model.iou = 0.45             # IoU threshold for NMS
model.max_det = 1000         # Maximum number of detections per image

# Prepare output folder
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ====== RUN DETECTION ======
# Get all image files
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
image_files = [os.path.join(SOURCE_DIR, f) for f in os.listdir(SOURCE_DIR) if Path(f).suffix.lower() in image_extensions]

print(f"Found {len(image_files)} images for detection.")

# Run detection
for img_path in image_files:
    results = model(img_path)
    # Save results
    results.save(save_dir=OUTPUT_DIR)

print(f"Detection completed. Results saved in '{OUTPUT_DIR}' folder.")
