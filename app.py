import streamlit as st
import pickle
import numpy as np

# load model
model = pickle.load(open('model.pkl', 'rb'))

# app title
st.title('Purchase Prediction App')
st.write('Enter the details to predict if a purchase will be made.')

# Inputs
age = st.number_input('Age', min_value=18, max_value=100, value=30)
annual_icome = st.number_input('Annual Icome', min_value=0, value=20000)
number_of_items = st.number_input('Number of Items', min_value=1, value=1)
time_on_site = st.number_input('Time on Site (minutes)', min_value=0, value=5)
loyalty_score = st.number_input('Loyalty Program', min_value=0, max_value=100, value=50)
discount_offered = st.number_input('Discount Offered (%)', min_value=0, max_value=100, value=10)

# prediction
if st.button('Predict'):
    input_data = np.array([[age, annual_icome, number_of_items, time_on_site, loyalty_score, discount_offered]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success('The customer is likely to make a purchase.')
    else:
        st.warning('The customer is unlikely to make a purchase.')
