import streamlit as st 
import joblib as jb
import numpy as np
st.title("Student's Score Calculator")
Hours=st.number_input("Enter hours studied:",0,12)

if st.button("Predict"):
    model=jb.load("Student_model.pkl")
    prediction=model.predict([[Hours]])
    st.write("Score: ",prediction[0])