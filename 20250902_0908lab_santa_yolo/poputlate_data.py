# Loop through the files from labels folder, each file should pair to an image file from images folder with the same file name
# Randomly divide all the files into three groups: train, val, test
# Copy the label and image files from labels and images folder to target folder called 'data'
# 80% of the files should be saved to train folder
# 10% of the files should be saved to val folder
# 10% of the files should be saved to test folder
# the data folder content should be like this:
# data/
# ├── train/
# │   ├── images/
# │   │   └── ...
# │   └── labels/
# │       └── ...
# ├── val/
# │   ├── images/
# │   │   └── ...
# │   └── labels/
# │       └── ...
# └── test/
#     ├── images/
#     │   └── ...
#     └── labels/
#         └── ...

import os
import shutil
import random
from pathlib import Path

def populate_data():
    # Create directory structure
    splits = ['train', 'val', 'test']
    data_types = ['images', 'labels']
    
    for split in splits:
        for data_type in data_types:
            Path(f"data/{split}/{data_type}").mkdir(parents=True, exist_ok=True)
    
    # Source directories
    src_images = "images"
    src_labels = "labels"
    
    # Check if source directories exist
    if not os.path.exists(src_images) or not os.path.exists(src_labels):
        print("Source images or labels directory does not exist")
        return
    
    # Get all label files
    label_files = [f for f in os.listdir(src_labels) if f.endswith('.txt')]
    
    # Shuffle the files randomly
    random.shuffle(label_files)
    
    # Calculate split sizes
    total_files = len(label_files)
    train_count = int(0.8 * total_files)
    val_count = int(0.1 * total_files)
    test_count = total_files - train_count - val_count
    
    # Split files
    train_files = label_files[:train_count]
    val_files = label_files[train_count:train_count + val_count]
    test_files = label_files[train_count + val_count:]
    
    # Copy files to respective directories
    splits_data = [
        ('train', train_files),
        ('val', val_files),
        ('test', test_files)
    ]
    
    for split_name, files in splits_data:
        print(f"Copying {len(files)} files to {split_name}...")
        for label_file in files:
            # Copy label file
            src_label_path = os.path.join(src_labels, label_file)
            dst_label_path = os.path.join(f"data/{split_name}/labels", label_file)
            shutil.copy2(src_label_path, dst_label_path)
            
            # Copy corresponding image file
            # Try different image extensions
            base_name = os.path.splitext(label_file)[0]
            image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
            image_copied = False
            
            for ext in image_extensions:
                src_image_path = os.path.join(src_images, base_name + ext)
                if os.path.exists(src_image_path):
                    dst_image_path = os.path.join(f"data/{split_name}/images", base_name + ext)
                    shutil.copy2(src_image_path, dst_image_path)
                    image_copied = True
                    break
            
            if not image_copied:
                print(f"Warning: No image found for label {label_file}")
    
    print("Data population completed!")
    print(f"Train: {len(train_files)} files")
    print(f"Validation: {len(val_files)} files")
    print(f"Test: {len(test_files)} files")

if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(42)
    populate_data()