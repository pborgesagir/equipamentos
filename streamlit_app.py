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
st.title("EQUIPAMENTOS - Engenharia Clínica")

# Establish connection using Streamlit's GSheetsConnection
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from a specific sheet named "METRICAS"
# This line assumes `conn.read()` can accept a parameter to specify the sheet name, which is not explicitly stated in your example
# If `conn.read()` does not support this, you would need to check the documentation for the correct method to specify a sheet name
df = conn.read(spreadsheet=url, sheet_name="METRICAS", usecols=list(range(12)))

# Display the DataFrame in Streamlit
st.dataframe(df)
