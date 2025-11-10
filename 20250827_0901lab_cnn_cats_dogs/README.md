# 20250827 - 20250901 Lab Instructions

## Setup

- Create a free Kaggle account if you haven't already
- Download the dataset from [Microsoft Cat Dataset](https://www.microsoft.com/en-us/download/details.aspx?id=54765)
- Place the images in folders: one for training cats, one for training dogs, and a smaller set for validation/testing

## Part 1: Data Preparation

- Organize the dataset into separate folders:
  - Training: 80% (data/train/cats, data/train/dogs)
  - Validation: 10% (data/val/cats, data/val/dogs)
  - Test: 10% (data/test/cats, data/test/dogs)
- Resize all images to the same size (e.g., 150x150 or 224x224 pixels)
- Apply data augmentation (like random flips or rotations) to make your model more robust (try this later)

## Part 2: Building the CNN

- Start by creating a simple CNN with a few convolution + pooling layers (or try MobileNetV2)
- Add fully connected layers at the end for classification
- Use activation functions:
  - ReLU in hidden layers
  - Sigmoid/Softmax in the output layer

## Part 3: Training the Model

- Compile the model with binary cross-entropy loss and an optimizer (like Adam)
- Train the model for several epochs (start small, maybe 5-10)
- Record the training and validation accuracy and loss after each epoch

## Part 4: Evaluation

- Test the model on your unseen test set
- Report metrics: accuracy, precision, recall
- Create a confusion matrix to see where the model makes mistakes (Optional)

## Part 5: Visualization

- Pick a few test images and show the model's predictions alongside the true labels
- Highlight at least 5 examples where the model was wrong and analyze why

## Stretch Goals

- Use transfer learning with a pre-trained network (like MobileNet or ResNet)
- Compare the accuracy of your CNN vs. transfer learning
- Experiment with changing batch size, learning rate, or number of layers

> Take the time you need and don't hesitate to ask any questions you might have.