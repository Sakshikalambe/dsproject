import streamlit as st
import pandas as pd
import pickle
import requests
import time
import sys
import select

arduino_ip = "192.168.4.1"  # Change this to the IP address of your Arduino

def get_sensor_data(endpoint):
    url = f"http://{arduino_ip}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None





oxygen = get_sensor_data("spo2")
pulse_rate = get_sensor_data("heartrate")
temperature = get_sensor_data("temperature")
       
# Load the best model from the pickle file
model_filename = 'best_model_Decision_Tree.pkl'
with open(model_filename, 'rb') as model_file:
    best_model = pickle.load(model_file)

# Streamlit app
st.title('Predict Result Interface')

# User input section
st.sidebar.header('User Input Features')


# Create a DataFrame with user input
user_input = pd.DataFrame({'Oxygen': [oxygen], 'PulseRate': [pulse_rate], 'Temperature': [temperature]})

# Prediction button
if st.button('Predict'):
    # Make predictions
    prediction = best_model.predict(user_input)

    # Optionally, display the probability score for the predicted class
    if hasattr(best_model, 'predict_proba'):
        st.subheader('Predicted Result')
        probabilities = best_model.predict_proba(user_input)

        # Find the class with the highest probability
        predicted_class = best_model.classes_[probabilities.argmax()]
        st.write(f'The predicted result is: {predicted_class}')

        
