import streamlit as st
import pandas as pd

# Load data from CSV
df = pd.read_csv("scoreboard - Sheet1.csv")

# Define a dictionary linking scores to image filenames
image_dict = {
    1: "movimentacao.jpg",
    2: "fundacao.jpg",
    3: "estrutura1.jpg",
    4: "estrutura2.jpg",
    5: "revestumento1.jpg",
    6: "revestimento2.jpg",
    7: "cobertura.jpg"
}

# Define a dictionary for legends
legend_dict = {
    1: "Movimentação de Terra - Preparing the site for construction.",
    2: "Fundação - Laying the foundation.",
    3: "Estrutura 1º andar - Constructing the first floor structure.",
    4: "Estrutura 2º andar e cobertura - Constructing the second floor and roof.",
    5: "Alvenaria 1º andar - Building the walls for the first floor.",
    6: "Alvenaria 2º andar - Building the walls for the second floor.",
    7: "Acabamento 1º andar - Finishing the first floor.",
    8: "Acabamento 2º andar - Finishing the second floor."
}

# Display the information
for index, row in df.iterrows():
    st.header(f"Stage for {row['Name']}")
    stage = row['Stage']
    if stage in image_dict:
        st.image(image_dict[stage], caption=f"Stage {stage}")
        st.write(legend_dict[stage])
