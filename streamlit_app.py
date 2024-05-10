import streamlit as st
from PIL import Image
from streamlit_server_state import server_state, server_state_lock

# Initialize the server state for scores if not already present
if 'scores' not in server_state:
    server_state['scores'] = {'squad1': 0, 'squad2': 0, 'squad3': 0}

# Function to update score
def update_score(squad, change):
    with server_state_lock['scores']:
        server_state['scores'][squad] += change
        if server_state['scores'][squad] < 0:
            server_state['scores'][squad] = 0

# Load avatar images
avatar1 = Image.open("avatar1.jpg")
avatar2 = Image.open("avatar2.jpg")
avatar3 = Image.open("avatar3.jpg")

# Streamlit layout
st.title("Squad Scoreboard")

# Squad 1
col1, col2, col3, col4 = st.columns([1, 2, 1, 2])
with col1:
    st.image(avatar1, width=50)
with col2:
    st.subheader("Squad 1")
with col3:
    if st.button("➖", key="dec_squad1"):
        update_score('squad1', -1)
    st.subheader(server_state['scores']['squad1'])
    if st.button("➕", key="inc_squad1"):
        update_score('squad1', 1)

# Squad 2
col1, col2, col3, col4 = st.columns([1, 2, 1, 2])
with col1:
    st.image(avatar2, width=50)
with col2:
    st.subheader("Squad 2")
with col3:
    if st.button("➖", key="dec_squad2"):
        update_score('squad2', -1)
    st.subheader(server_state['scores']['squad2'])
    if st.button("➕", key="inc_squad2"):
        update_score('squad2', 1)

# Squad 3
col1, col2, col3, col4 = st.columns([1, 2, 1, 2])
with col1:
    st.image(avatar3, width=50)
with col2:
    st.subheader("Squad 3")
with col3:
    if st.button("➖", key="dec_squad3"):
        update_score('squad3', -1)
    st.subheader(server_state['scores']['squad3'])
    if st.button("➕", key="inc_squad3"):
        update_score('squad3', 1)
