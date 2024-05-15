import streamlit as st
from PIL import Image
from streamlit_server_state import server_state, server_state_lock
import pandas as pd

# Load initial scores from CSV
score_data = pd.read_csv("scoreboard - Sheet1.csv")
initial_scores = score_data.iloc[0].to_dict()

# Initialize the server state for scores if not already present
if 'scores' not in server_state:
    server_state['scores'] = initial_scores

# Function to display the corresponding image based on the score
def display_image(score):
    images = {
        1: "movimentacao.jpg",
        2: "fundacao.jpg",
        3: "estrutura1.jpg",
        4: "estrutura2.jpg",
        5: "alvenaria1.jpg",
        6: "alvenaria2.jpg",
        7: "revestimento1.jpg",
        8: "revestimento2.jpg",
    }
    image_path = images.get(score, "default.jpg")  # default image if score is out of range
    return Image.open(image_path)

# Streamlit layout
st.title("Squad Scoreboard")

# Squad scores
for name, score in server_state['scores'].items():
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.image(display_image(score), width=100)  # Display image based on the score
    with col2:
        st.subheader(name)  # Display squad name
    with col3:
        st.subheader(score)  # Display squad score
