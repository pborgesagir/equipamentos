import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("scoreboard - Sheet1.csv")
df.replace({"Squad 1": "Kaio", "Squad 2": "Pedro", "Squad 3": "Regilane"}, inplace=True)

# Function to return the image file based on the score
def get_image(score):
    images = {
        1: "movimentacao.jpg",
        2: "fundacao.jpg",
        3: "estrutura1.jpg",
        4: "estrutura2.jpg",
        5: "alvenaria1.jpg",
        6: "alvenaria2.jpg",
        7: "revestimento1.jpg",
        8: "revestimento2.jpg"
    }
    return images.get(score, None)  # Return None if score is not in 1-8

# Display the data and images
for index, row in df.iterrows():
    st.header(f"{row['Name']}")  # Display the name
    score = max(1, min(8, row['Score']))  # Limit the score between 1 and 8
    image_path = get_image(score)
    if image_path:
        st.image(image_path, caption=f"Score: {score}")

# Space for adding a legend
st.text("Legenda:")
st.text_area("Digite aqui a descrição para as imagens e seus significados.")

