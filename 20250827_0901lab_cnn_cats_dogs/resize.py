import os
from PIL import Image

# Part 1: Data Preparation
# Resize all images to the same size (for example, 150x150 or 224x224 pixels)
def resize_image(input_path, output_path):
    try:
        print(input_path, output_path)
        image = Image.open(input_path)
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        resized_img = image.resize((150, 150))
        resized_img.save(output_path)
    except Exception as e:
        print(f"Error processing image {input_path}: {e}")
    

def list_files(input_folder):
    arr = os.listdir(input_folder)
    return arr
    

# input_folder_name = 'source_cat'
# output_folder_name = 'resized_cat'

def convert(input_folder_name, output_folder_name):
    images = list_files(input_folder_name)

    for image in images:
        
        input_image = input_folder_name + '/' + image
        output_image = output_folder_name + '/' + image
        
        if (input_image.endswith(".jpg")):
            resize_image(input_image, output_image)
            
            
convert('source_cat', 'resized_cat')
convert('source_dog', 'resized_dog')