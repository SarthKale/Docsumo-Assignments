# Task1-Image-Alignment
Implementation of image alignment using opencv and python which aligns all the misaligned images.

## Problem Statement

The file misaligned_images.zip which contains scanned images that are not perfectly aligned with the horizontal and vertical axes. Your task is to identify if the images are misaligned and correct the alignment if necessary.

## Requirements

* Python3

## Getting Started

To clone this repository, run the following in a terminal
```bash
git clone https://github.com/SarthKale/Docsumo-Assignments.git
cd Docsumo-Assignments
pip install -r requirements.txt
```

## Run Application
This application utilize opencv to read images from a folder named misaligned_images and process them. The aligned images are then saved into another folder named aligned_images. This application uses matrix rotation to realign the images.

Note: Unzip the misaligned_images.zip and aligned_images.zip files before executing the application.

```bash
python3 task1-image-alignment/src/image_alignment.py
```

## Expected Output
The aligned images are stored in a file named  `aligned_images.zip`.


# Task2-Text-Classification
Implementation of text-classification using python, sklearn and nltk which classifies the text into 12 different label values.

## Problem Statement

the training (train_set.csv) and testing (test_set.csv) data for the text classification task.  
Columns: 1. label:12 classes; 2. text: description of the code
Build the algorithm to classify text into these 12 categories.

## Requirements

* Python3

## Getting Started

To clone this repository, run the following in a terminal
```bash
git clone https://github.com/SarthKale/Docsumo-Assignments.git
cd Docsumo-Assignments
pip install -r requirements.txt
```

## Run Application
This application utilize different machine learning algorithms to create a model which trains on the provided training dataset and provides label predictions for the testing dataset. We are testing the accuracy of different models and obtain the one model with highest mean accuracy over training data. This model is then used to predict the different labels for the testing data.

Note: This text classification is performed in a Jupyter notebook. Check `text_classification.ipynb` Jupyter notebook file.

## Expected Output
The labeled test dataset is stored in `output_set.csv` file.

## Tech Stack

* Programming Language : Python3
* Python Code Formatter : autopep8

## Author

Sarthak Kale
