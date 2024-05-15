import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv('scoreboard - Sheet1.csv')

# Define a mapping from etapas to images
etapa_to_image = {
    1: 'movimentacao.jpg',
    2: 'fundacao.jpg',
    3: 'estrutura1.jpg',
    4: 'estrutura2.jpg',
    5: 'revestimento1.jpg',
    6: 'revestimento2.jpg',
    7: 'cobertura.jpg',

}

# # Create columns for each participant
# col1, col2, col3 = st.columns(3)
# columns = [col1, col2, col3]

# # Create columns for each participant
col1 = st.columns(1)
columns = [col1]

# Display images according to scores
for i, person in enumerate(['Kaio', 'Pedro', 'Regilane']):
    columns[i].subheader(person)
    score = data[person][0]  # Assuming each person has only one score in the CSV
    image_path = etapa_to_image[score]
    columns[i].image(image_path, caption=f'etapa {score}')

# Add a legend explaining each etapa
st.subheader('Legenda')
for etapa, image in etapa_to_image.items():
    st.write(f'Etapa da obra {etapa}: {image.split(".")[0]}')

