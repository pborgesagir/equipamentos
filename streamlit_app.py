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
    7: "cobertura.jpg",
}

# Stage descriptions
stage_descriptions = {
    1: "Movimentação de Terra: Preparação e nivelamento do terreno.",
    2: "Fundação: Estruturação da base da construção.",
    3: "Estrutura 1º andar: Construção do primeiro andar.",
    4: "Estrutura 2º andar e cobertura: Construção do segundo andar e finalização do teto.",
    5: "Revestimento 1º andar: Montagem das paredes e revestimento do primeiro andar.",
    6: "Revestimento 2º andar: Montagem das paredes e revestimento do segundo andar.",
    7: "Acabamento: Entrega da obra.",

}

# Set the current stage here
current_stage = 2  # Change this number to reflect the current stage

# Display the title
st.title("Placar Envolvente - GCINFRA")

# Display the image
if current_stage in image_files:
    image = Image.open(image_files[current_stage])
    st.image(image, width=400)  # Set the width to 400 pixels
    st.write(stage_descriptions[current_stage])  # Display the stage description
else:
    st.error("Invalid stage number. Please choose a number between 1 and 8.")

# Display legend
st.subheader("Legenda das Etapas:")
for stage, description in stage_descriptions.items():
    st.write(f"{stage}: {description}")
