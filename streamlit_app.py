import streamlit as st
from PIL import Image

# Map stage numbers to image files
image_files = {
    1: "movimentacao.jpg",
    2: "fundacao.jpg",
    3: "estrutura1.jpg",
    4: "estrutura2.jpg",
    5: "revestimento1.jpg",
    6: "revestimento2.jpg",
    7: "cobertura.jpg"
}

# Stage descriptions
stage_descriptions = {
    1: "Movimentação de Terra: Preparação e nivelamento do terreno.",
    2: "Fundação: Estruturação da base da construção.",
    3: "Estrutura 1º andar: Construção do primeiro andar.",
    4: "Estrutura 2º andar e cobertura: Construção do segundo andar e finalização do teto.",
    5: "Alvenaria 1º andar: Montagem das paredes do primeiro andar.",
    6: "Alvenaria 2º andar: Montagem das paredes do segundo andar.",
    7: "Acabamento 1º andar: Finalização interna do primeiro andar.",
    8: "Acabamento 2º andar: Finalização interna do segundo andar."
}

# Set the current stage here
current_stage = 3  # Change this number to reflect the current stage

# Display the image
if current_stage in image_files:
    image = Image.open(image_files[current_stage])
    st.image(image, use_column_width=True)  # Display image to fill the column
    st.write(stage_descriptions[current_stage])  # Display the stage description
else:
    st.error("Invalid stage number. Please choose a number between 1 and 8.")
