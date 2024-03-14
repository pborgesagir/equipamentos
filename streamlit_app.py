import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO
from streamlit_gsheets import GSheetsConnection

st.set_page_config(
    page_title='Equipamentos - GCINFRA',
    layout='wide',
    page_icon="https://media.licdn.com/dms/image/C4D0BAQHXylmAyGyD3A/company-logo_200_200/0/1630570245289?e=2147483647&v=beta&t=Dxas2us5gteu0P_9mdkQBwJEyg2aoc215Vrk2phu7Bs",
    initial_sidebar_state='auto'
)
url = "https://docs.google.com/spreadsheets/d/1GswNpQuhhc6udp59clV5s6dDnBfFF91rofaRbMsDdT0/edit#gid=704841034"
st.title("EQUIPAMENTOS - Engenharia Clínica")
conn = st.connection("gsheets", type=GSheetsConnection)



df = conn.read(spreadsheet=url, usecols=list(range(12)))
st.dataframe(df)
