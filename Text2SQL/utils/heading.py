import streamlit as st 
from PIL import Image

image = Image.open('./Peerlist.png')
# 
def display_header():
    """
    description: This function takes care of displaying the widget
    """
    left_column_width = 1
    right_column_width = 6

    # Create two columns
    left_column, right_column = st.columns([left_column_width, right_column_width])

    # Add content to the left column
    with left_column:
        st.image(image, width = 100)


    # Add content to the right column
    with right_column:
        st.title("Peerlist Explore")

