import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os


SEED = 42
# Set the global random seed
tf.random.set_seed(SEED)

# Paths and hyperparams
DATA_DIR = 'data'
IMG_SIZE = 224
BATCH = 32
AUTOTUNE = tf.data.AUTOTUNE #自动调优

# load datasets from folders(train/val/test)
# Keras预处理效用函数
train_ds =  tf.keras.utils.image_dataset_from_directory(
    os.path.join(DATA_DIR, 'training'),
    labels = 'inferred',
    label_mode = 'binary', # 0/1. cats or dogs
    image_size = (IMG_SIZE, IMG_SIZE),
    batch_size = BATCH,
    shuffle = True,
    seed = SEED
)

# val_ds =  tf.keras.utils.image_dataset_from_directory(
#     os.path.join(DATA_DIR, 'validation'),
#     labels = 'inferred',
#     label_mode = 'binary', 
#     image_size = (IMG_SIZE, IMG_SIZE),
#     batch_size = BATCH,
#     shuffle = False
# )

# test_ds =  tf.keras.utils.image_dataset_from_directory(
#     os.path.join(DATA_DIR, 'test'),
#     labels = 'inferred',
#     label_mode = 'binary', 
#     image_size = (IMG_SIZE, IMG_SIZE),
#     batch_size = BATCH,
#     shuffle = False
# )

class_names = train_ds.class_names
print('Classes:', class_names)

# MobileNet2 expects inputs in a specific range, use the built-in preprocess layer
preprocess = tf.keras.applications.mobilenet_v2.preprocess_input

# Performance: cache & prefetch 
train_ds = train_ds.map(lambda x,y: (preprocess(x), y),num_parallel_cell = AUTOTUNE).prefetch(AUTOTUNE)

# Base(pretrained on imageNet)
base = tf.keras.applications.MobileNetV2(
    input_shape = (IMG_SIZE, IMG_SIZE, 3),
    include_top = False,
    weights = 'imagenet'
)
base.trainable = False

# Build the model
# inputs = tf.keras.Input(shape = (IMG_SIZE, IMG_SIZE, 3))
# x = inputs
# x = base(x, training = False)
# x = tf.keras.layers.GlobalAveragePooling2D()(x)
# x = tf.keras.layers.Dropout(0.2)(x)
# outputs = tf.keras.layers.Dense(1, activation = 'sigmoid')(x)

inputs = tf.keras.Input(shape = (IMG_SIZE, IMG_SIZE, 3))
base_output = base(inputs, training = False)
pooling_output = tf.keras.layers.GlobalAveragePooling2D()(base_output)
drop_out = tf.keras.layers.Dropout(0.2)(pooling_output)
outputs = tf.keras.layers.Dense(1, activation = 'sigmoid')(drop_out)

model = tf.keras.Model(inputs, outputs, name = 'cats_dogs_mobilenetv2')
model.summary()


# Train the model
# model.compile(
#     optimizer = tf.keras.optimizer.Adam(1e-3),
#     loss = 'binary_crossentropy',
#     metrics = ['accuracy']
# )

