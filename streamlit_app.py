import streamlit as st
from PIL import Image


Set Streamlit page configuration
st.set_page_config(
    page_title='Placar Envolvente - GCINFRA',
    layout='wide',
    page_icon="https://media.licdn.com/dms/image/C4D0BAQHXylmAyGyD3A/company-logo_200_200/0/1630570245289?e=2147483647&v=beta&t=Dxas2us5gteu0P_9mdkQBwJEyg2aoc215Vrk2phu7Bs",
    initial_sidebar_state='auto'
)

# Map stage numbers to image files
image_files = {
    1: "movimentacao.jpg",
    2: "fundacao.jpg",
    3: "estrutura1.jpg",
    4: "estrutura2.jpg",
    5: "alvenaria1.jpg",
    6: "alvenaria2.jpg",
    7: "revestimento1.jpg",
    8: "revestimento2.jpg"
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
