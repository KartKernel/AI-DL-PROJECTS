# Brain Tumor Detection App

This is a web application built using Streamlit for detecting brain tumors in medical images.

## Overview

The Brain Tumor Detection Web App allows users to upload MRI images of the brain and get predictions on whether a tumor is present or not using a pre-trained CNN model.

## Features

- Upload MRI images in JPG, JPEG, or PNG format.
- Display the uploaded image and preprocess it for model input.
- Make predictions using a pre-trained CNN model for brain tumor detection.
- Display the prediction result (tumor present or not) with confidence score.

## Prerequisites

Before running the app, ensure you have the following installed:

- Python (recommended version 3.6+)
- Streamlit (install using `pip install streamlit`)
- TensorFlow (install using `pip install tensorflow`)
- Other required libraries specified in `requirements.txt`

## Usage

- Clone or download the repository to your local machine.
- Navigate to the project directory in the terminal or command prompt.
- Install the required dependencies using: `pip install -r requirements.txt`
- Run the Streamlit app using: `streamlit run app.py`
- Upload an MRI image using the file uploader on the app's interface.
- Click the "Predict" button to get the prediction result.

## Folder Structure

- appl.py: Main Streamlit app script.
- BrainTumor10Epochs.h5: Pre-trained TensorFlow model for brain tumor detection.
- requirements.txt: List of required Python packages and versions.
- README.md: Documentation and instructions.

## Credits

- The medical images used for training and testing the model are from public dataset Br35H found in kaggle (https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection).
