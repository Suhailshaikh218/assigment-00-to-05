import streamlit as st
import numpy as np
import pandas as pd

# Title of the web app
st.title('My First Streamlit App')

# Adding a header
st.header('Welcome to my Python Website!')

# Adding a simple description
st.write("This is a simple Streamlit web app built in 15 minutes.")

# Adding an input widget
user_name = st.text_input("Enter your name:")
if user_name:
    st.write(f"Hello, {user_name}!")

# Adding a button
if st.button('Click Me'):
    st.write("Button Clicked!")

# Displaying a chart (for fun)
data = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
st.line_chart(data)

# Adding an image (optional)
st.image("https://via.placeholder.com/500x200", caption="Example Image")

# Sidebar for settings
st.sidebar.title("Settings")
slider_value = st.sidebar.slider("Choose a value", 0, 100, 50)
st.write(f"Slider value is {slider_value}")