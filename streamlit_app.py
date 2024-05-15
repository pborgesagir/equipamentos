import streamlit as st
import pandas as pd
import os

# Define the mapping from scores to image filenames
score_to_image = {
    1: "movimentacao.jpg",
    2: "fundacao.jpg",
    3: "estrutura1.jpg",
    4: "estrutura2.jpg",
    5: "alvenaria1.jpg",
    6: "alvenaria2.jpg",
    7: "revestimento1.jpg",
    8: "revestimento2.jpg"
}

# Load the CSV file
@st.cache
def load_data():
    df = pd.read_csv("/mnt/data/scoreboard - Sheet2.csv")
    return df

df = load_data()

# Display images for each squad
for index, row in df.iterrows():
    stage = row['Score']
    if stage in score_to_image:
        image_path = score_to_image[stage]
        if os.path.exists(image_path):
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(image_path, use_column_width=True)
            with col2:
                st.write(f"{row['Squad']}: Stage {stage}")
        else:
            st.error(f"Image for stage {stage} not found at {image_path}")

# Display legend
st.subheader("Legend")
st.write("""
1 - Movimentação de Terra: Preparação do terreno para construção.
2 - Fundação: Estrutura de suporte da construção.
3 - Estrutura 1º Andar: Construção do primeiro andar.
4 - Estrutura 2º Andar: Construção do segundo andar.
5 - Alvenaria 1º Andar: Tijolos e blocos do primeiro andar.
6 - Alvenaria 2º Andar: Tijolos e blocos do segundo andar.
7 - Acabamento 1º Andar: Revestimentos e acabamentos do primeiro andar.
8 - Acabamento 2º Andar: Revestimentos e acabamentos do segundo andar.
""")
