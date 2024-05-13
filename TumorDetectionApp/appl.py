import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the pretrained model
model = tf.keras.models.load_model('BrainTumor10Epochs.h5')

# Define a function to make predictions
def predict(image):
    # Preprocess the image (resize, normalize, etc.)
    # Make predictions using the loaded model
    # Return the prediction result

    img = Image.fromarray(image)
    img = img.resize((64, 64))
    img = np.array(img)
    input_img = np.expand_dims(img, axis = 0)
    res = model.predict(input_img)
    return res



# Streamlit app
st.title('Brain Tumor Detector')

st.write("-------------------------------")

# File uploader for user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display the uploaded image
    #image = np.array(Image.open(uploaded_file))
    st.image(uploaded_file, caption='Uploaded MRI Scan', width=200)
    image = np.array(Image.open(uploaded_file))
    # Make predictions when the user clicks a button
    if st.button('Predict'):
        prediction = predict(image)
        if prediction > 0.5:
            st.write('### Tumor detected!')
        else:
            st.write('### No Tumor detected!')
        
