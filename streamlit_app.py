import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("scoreboard - Sheet1.csv")

# Mapping of scores to images
image_dict = {
    1: "movimentacao.jpg",
    2: "fundacao.jpg",
    3: "estrutura1.jpg",
    4: "estrutura2.jpg",
    5: "alvenaria1.jpg",
    6: "alvenaria2.jpg",
    7: "revestimento1.jpg",
    8: "revestimento2.jpg"
}

# Displaying the scoreboard
st.title("Scoreboard")

for index, row in df.iterrows():
    st.subheader(f"{row['Squad']}")
    score = row['Score']
    if 1 <= score <= 8:
        st.image(image_dict[score], width=300)
    else:
        st.error("Score out of range. Please ensure the score is between 1 and 8.")

# Legend for images
st.sidebar.header("Legend")
st.sidebar.write("""
- **Movimentação**: Initial stages of movement and preparation.
- **Fundação**: Laying the foundation.
- **Estrutura 1 & 2**: Building the structure.
- **Alvenaria 1 & 2**: Masonry work.
- **Revestimento 1 & 2**: Surface finishing.
""")

# Instructions to save this script as 'scoreboard.py' and run it using Streamlit
st.write("Save this script as 'scoreboard.py' and run it using the command: `streamlit run scoreboard.py`")
