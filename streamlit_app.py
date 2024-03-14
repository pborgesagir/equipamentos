import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO
from streamlit_gsheets import GSheetsConnection

# Set Streamlit page configuration
st.set_page_config(
    page_title='Equipamentos - GCINFRA',
    layout='wide',
    page_icon="https://media.licdn.com/dms/image/C4D0BAQHXylmAyGyD3A/company-logo_200_200/0/1630570245289?e=2147483647&v=beta&t=Dxas2us5gteu0P_9mdkQBwJEyg2aoc215Vrk2phu7Bs",
    initial_sidebar_state='auto'
)

# Google Sheets URL
url = "https://docs.google.com/spreadsheets/d/1GswNpQuhhc6udp59clV5s6dDnBfFF91rofaRbMsDdT0/edit#gid=704841034"
# Centered title using HTML tags
st.markdown("<h1 style='text-align: center;'>GESTÃO DE RECURSO PARA INVESTIMENTO</h1>", unsafe_allow_html=True)


# Adding a centered subtitle with larger font size using HTML
st.markdown("""
    <div style='text-align: center; font-size: 36px;'>
        <b>SOF - DCOL - GCINFRA</b>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# st.sidebar.image('index.png', width=150)
st.sidebar.title(f"Bem-vindo, {name}")
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, worksheet="METRICAS", usecols=list(range(12)))

# Display the DataFrame in Streamlit
st.dataframe(df)
