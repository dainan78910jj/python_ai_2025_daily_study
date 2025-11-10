import os
import shutil
import random

# Part 1: Data Preparation
# Organize the dataset into separate folders for training 80%, validation 10%, and test 10%.
def list_files(input_folder):
    
    arr = os.listdir(input_folder)
    
    return arr

def copy_file(from_path, to_path):
    # os.rename(from_path, to_path)
    shutil.copyfile(from_path, to_path)


def split(input_folder, training_folder, validation_folder, test_folder):

    file_list = list_files(input_folder)
    random.shuffle(file_list)

    total = len(file_list)
    training = int(total * 0.8)
    validation = int(total * 0.1)
    test = total - training - validation

    for i in range(total):
        resized_image_name = file_list[i]
        input_file_path = input_folder + '/' + resized_image_name
        if i < training:
            to_file_path = training_folder + '/' + resized_image_name
            copy_file(input_file_path, to_file_path)
        elif i < training + validation:
            to_file_path = validation_folder + '/' + resized_image_name
            copy_file(input_file_path, to_file_path)
        else:
            to_file_path = test_folder + '/' + resized_image_name
            copy_file(input_file_path, to_file_path)

split('source_cat', './data/training/cat', './data/validation/cat', './data/test/cat')
split('source_dog', './data/training/dog', './data/validation/dog', './data/test/dog')