import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('scoreboard - Sheet1.csv')

# Define a mapping from stages to images
stage_to_image = {
    1: 'movimentacao.jpg',
    2: 'fundacao.jpg',
    3: 'estrutura1.jpg',
    4: 'estrutura2.jpg',
    5: 'alvenaria1.jpg',
    6: 'alvenaria2.jpg',
    7: 'revestimento1.jpg',
    8: 'revestimento2.jpg',
}

# Create columns for each participant
col1, col2, col3 = st.columns(3)
columns = [col1, col2, col3]

# Display images according to scores
for i, person in enumerate(['Kaio', 'Pedro', 'Regilane']):
    columns[i].subheader(person)
    score = data[person][0]  # Assuming each person has only one score in the CSV
    image_path = stage_to_image[score]
    columns[i].image(image_path, caption=f'Stage {score}')

# Add a legend explaining each stage
st.subheader('Legend')
for stage, image in stage_to_image.items():
    st.write(f'Stage {stage}: {image.split(".")[0]}')

