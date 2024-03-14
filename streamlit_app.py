import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import streamlit.components.v1 as components
import pygwalker as pyg
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import re
import streamlit_authenticator as stauth 
import pickle
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import base64
import time
from reportlab.lib.utils import ImageReader
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Set Streamlit page configuration
st.set_page_config(
    page_title='Equipamentos - GCINFRA',
    layout='wide',
    page_icon="https://media.licdn.com/dms/image/C4D0BAQHXylmAyGyD3A/company-logo_200_200/0/1630570245289?e=2147483647&v=beta&t=Dxas2us5gteu0P_9mdkQBwJEyg2aoc215Vrk2phu7Bs",
    initial_sidebar_state='auto'
)

#testing authentication
# --- USER AUTHENTICATION ---


names = ["Peter Parker", "Rebecca Miller", "Pedro Borges", "Arthur Pires", "Kaio Razotto", "Vitor Peixoto", "Claudemiro Dourado", "Izabela Lopes", "Fernando Souza", "Michelle Bonfim", "Gerson Rodrigues", "Mônica Guimarães", "Pedro Andrade", "Jéssyca de Paula", "Rafael Souza"]
usernames = ["pparker", "rmiller", "pborges", "arthur.pires", "kaio.razotto", "vitor.peixoto", "claudemiro.dourado", "izabela.lopes", "fernando.souza", "michelle.bonfim", "gerson.rodrigues", "monica.guimaraes", "pedro.andrade", "jessyca.depaula", "rafael.souza"]


# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=1)

name, authentication_status, username = authenticator.login("Login de acesso: Gestão de Equipamentos - GCINFRA", "main")

if authentication_status == False:
    st.error("Usuário/senha está incorreto")

if authentication_status == None:
    st.warning("Por favor, insira usuário e senha")

if authentication_status:


    # Google Sheets URL
    url = "https://docs.google.com/spreadsheets/d/1GswNpQuhhc6udp59clV5s6dDnBfFF91rofaRbMsDdT0/edit#gid=704841034"
    # Centered title using HTML tags
    st.markdown("<h1 style='text-align: center;'>EQUIPAMENTOS -  Engenharia Clínica</h1>", unsafe_allow_html=True)
    
    
    # Adding a centered subtitle with larger font size using HTML
    st.markdown("""
        <div style='text-align: center; font-size: 36px;'>
            <b>SOF - DCOL - GCINFRA</b>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.sidebar.image('index.png', width=150)
    st.sidebar.title(f"Bem-vindo, {name}")
    conn = st.connection("gsheets", type=GSheetsConnection)
    
    df = conn.read(spreadsheet=url, worksheet="METRICAS", usecols=list(range(13)))
    df = df.sort_values("fechamento")


    # Convert the "fechamento" column to datetime with errors='coerce'
    df["fechamento"] = pd.to_datetime(df["fechamento"], format='%m/%d/%Y %H:%M:%S', errors='coerce')


    
    # Filter out rows where the date could not be parsed (NaT)
    df = df.dropna(subset=["fechamento"])
    
    # Extract year, month, and quarter
    df["Year"] = df["fechamento"].dt.year
    df["Month"] = df["fechamento"].dt.month
    df["Quarter"] = df["fechamento"].dt.quarter
    df["Semester"] = np.where(df["fechamento"].dt.month.isin([1, 2, 3, 4, 5, 6]), 1, 2)
    
    # Create a "Year-Quarter" column
    df["Year-Quarter"] = df["Year"].astype(str) + "-Q" + df["Quarter"].astype(str)
    
    # If you want to create a "Year-Month" column, you can use the following line
    df["Year-Month"] = df["fechamento"].dt.strftime("%Y-%m")
    
    # Create a "Year-Semester" column
    df["Year-Semester"] = df["Year"].astype(str) + "-S" + df["Semester"].astype(str)
    
    # Assuming 'empresa' and 'OS' are columns in your DataFrame for concatenation
    # df["empresa+OS"] = df["empresa"] + '-' + df["OS"]
    
    # Sort the unique values in ascending order
    unique_year_month = sorted(df["Year-Month"].unique())
    unique_year_quarter = sorted(df["Year-Quarter"].unique())
    unique_year_semester = sorted(df["Year-Semester"].unique())
    unique_year = sorted(df["Year"].unique())
    
    # Add "All" as an option for both filters
    unique_year_month.insert(0, "Todos")
    unique_year_quarter.insert(0, "Todos")
    unique_year_semester.insert(0, "Todos")
    unique_year.insert(0, "Todos")


    # Define the list of "empresa" values and add "Todos" as an option
    desired_empresa = df["empresa"].unique().tolist()
    desired_empresa.insert(0, "Todos")
    
    empresa = st.sidebar.multiselect("UNIDADE", desired_empresa, default=desired_empresa[0])


    # Define the list of "familia" values and add "Todos" as an option
    desired_numero_familia = df["familia"].unique().tolist()
    desired_numero_familia.insert(0, "Todos")
    
    # Create a filter for selecting "familia"
    numero_familia = st.sidebar.multiselect("FAMÍLIA", desired_numero_familia, default=desired_numero_familia[0])

    # Define the list of "tipomanutencao" values and add "Todos" as an option
    desired_numero_tipomanutencao = df["tipomanutencao"].unique().tolist()
    desired_numero_tipomanutencao.insert(0, "Todos")
    
    # Create a filter for selecting "tipomanutencao"
    numero_tipomanutencao = st.sidebar.multiselect("TIPO DE MANUTENÇÃO", desired_numero_tipomanutencao, default=desired_numero_tipomanutencao[0])


    # Define the list of "setor" values and add "Todos" as an option
    desired_numero_setor = df["setor"].unique().tolist()
    desired_numero_setor.insert(0, "Todos")
    
    # Create a filter for selecting "setor"
    numero_setor = st.sidebar.multiselect("SETOR", desired_numero_setor, default=desired_numero_setor[0])

    
    
    # Create a sidebar for selecting filters (Assuming you're using Streamlit)
   
    month = st.sidebar.selectbox("Mês", unique_year_month)
    quarter = st.sidebar.selectbox("Trimestre", unique_year_quarter)
    semester = st.sidebar.selectbox("Semestre", unique_year_semester)
    year = st.sidebar.selectbox("Ano", unique_year)
    
    # Filter the DataFrame based on the selections
    if month == "Todos":
        month_filtered = df
    else:
        month_filtered = df[df["Year-Month"] == month]
    
    if quarter == "Todos":
        filtered_df = month_filtered
    else:
        filtered_df = month_filtered[month_filtered["Year-Quarter"] == quarter]
    
    if semester == "Todos":
        filtered_df = filtered_df
    else:
        filtered_df = filtered_df[filtered_df["Year-Semester"] == semester]
    
    if year == "Todos":
        filtered_df = filtered_df
    else:
        filtered_df = filtered_df[filtered_df["Year"] == year]




    if empresa and empresa != ["Todos"]:
        filtered_df = filtered_df[filtered_df["empresa"].isin(empresa)]
    
    if numero_familia and numero_familia != ["Todos"]:
        filtered_df = filtered_df[filtered_df["familia"].isin(numero_familia)]
    
    if numero_setor and numero_setor != ["Todos"]:
        filtered_df = filtered_df[filtered_df["setor"].isin(numero_setor)]


    authenticator.logout("Logout", "sidebar")
    
    
    
    col1 = st.columns(1)[0]
    col2, col3 = st.columns(2)
    col4 = st.columns(1)[0]
    col5 = st.columns(1)[0]
    col6 = st.columns(1)[0]
    col7 = st.columns(1)[0]
    col8 = st.columns(1)[0]


    # Import necessary libraries (Plotly) - already imported in your provided code

    # Count the occurrences of each 'tipomanutencao'
    tipomanutencao_counts = filtered_df['tipomanutencao'].value_counts().reset_index()
    tipomanutencao_counts.columns = ['tipomanutencao', 'count']
    
    # Create a horizontal bar chart
    fig = px.bar(tipomanutencao_counts,
                 x='count',
                 y='tipomanutencao',
                 orientation='h',  # This makes the bar chart horizontal
                 title='Apresentação de Serviços',
                 labels={'count': 'Quantidade', 'tipomanutencao': 'Tipo de Manutenção'},
                 template='plotly_white')  # Use a clean template
    
    # Improve layout
    fig.update_layout(xaxis_title="Quantidade",
                      yaxis_title="Tipo de Manutenção",
                      yaxis={'categoryorder': 'total ascending'},  # Sort bars by count
                      title_x=0.5)  # Center the chart title
    
    # Display the chart in the specified column
    col1.plotly_chart(fig, use_container_width=True)


    
    # Assuming 'abertura' is the number of opened requests and 'fechamento' is the number of closed requests
    # Group by 'Year-Month' and calculate the counts
    monthly_data = filtered_df.groupby('Year-Month').agg({'abertura':'count', 'fechamento':'count'}).reset_index()
    


    
    # Create the bar chart for opened and closed requests
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=monthly_data['Year-Month'],
        y=monthly_data['abertura'],
        name='Abertas',
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=monthly_data['Year-Month'],
        y=monthly_data['fechamento'],
        name='Fechadas',
        marker_color='lightsalmon'
    ))
    
    
    
    # Set the title and labels
    fig.update_layout(
        title='Atendimento de manutenções corretivas',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Número de OS',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    
    # Show the figure in the Streamlit app
    col2.plotly_chart(fig, use_container_width=True)


    # Calculate the total number of opened requests per month
    # Assuming 'abertura' represents the 'opened' status in your data
    opened_requests_per_month = filtered_df.groupby('Year-Month')['abertura'].count().reset_index()
    opened_requests_per_month.columns = ['Year-Month', 'Opened']
    
    # Calculate the total number of closed requests per month
    # Assuming 'fechamento' represents the 'closed' status in your data
    closed_requests_per_month = filtered_df.groupby('Year-Month')['fechamento'].count().reset_index()
    closed_requests_per_month.columns = ['Year-Month', 'Closed']
    
    # Merge the two dataframes on 'Year-Month'
    monthly_performance = pd.merge(opened_requests_per_month, closed_requests_per_month, on='Year-Month')
    
    # Calculate the percentage of closed requests
    monthly_performance['Closure Rate'] = (monthly_performance['Closed'] / monthly_performance['Opened']) * 100
    
    # Plot the line chart
    fig = px.line(monthly_performance, x='Year-Month', y='Closure Rate', title='Performance of Closure Rate Over Time')
    
    # Add a horizontal line for the goal (Meta) at 85%
    fig.add_hline(y=85, line_dash="dash", line_color="red", annotation_text="Meta 85%", annotation_position="bottom right")
    
    # Enhance layout
    fig.update_layout(xaxis_title="Year-Month",
                      yaxis_title="Closure Rate (%)",
                      yaxis=dict(tickformat=".0f"),  # Format y-axis tick labels as integers
                      legend=dict(title="Legend"),
                      title_x=0.5)  # Center the chart title
    
    # Display the chart
    col3.plotly_chart(fig, use_container_width=True)



    
   
    
    

    # Ensure 'cadastro' and 'instalacao' are in datetime format
    filtered_df['cadastro'] = pd.to_datetime(filtered_df['cadastro'], errors='coerce')
    filtered_df['instalacao'] = pd.to_datetime(filtered_df['instalacao'], errors='coerce')
    
    # Determine the oldest date between 'cadastro' and 'instalacao' for each equipment
    filtered_df['oldest_date'] = filtered_df[['cadastro', 'instalacao']].min(axis=1)
    
    # Calculate the age of the equipment in days (or in your preferred time unit)
    filtered_df['equipment_age'] = (datetime.now() - filtered_df['oldest_date']).dt.days
    
    # Filter for 'CORRETIVA' in 'tipomanutencao'
    corretiva_df = filtered_df[filtered_df['tipomanutencao'] == 'CORRETIVA']
    
    # Group by 'tag' and count the occurrences of "CORRETIVA"
    corretiva_count = corretiva_df.groupby('tag').size().reset_index(name='corretiva_count')
    
    # Merge back to get ages and families for each tag
    corretiva_with_age = pd.merge(corretiva_count, filtered_df[['tag', 'equipment_age', 'familia']].drop_duplicates(), on='tag')
    
    # Calculate MTBF (assuming corretiva_count > 0 to avoid division by zero)
    corretiva_with_age['MTBF'] = corretiva_with_age['equipment_age'] / corretiva_with_age['corretiva_count']
    
    # Calculate the average MTBF for each 'familia'
    avg_mtbf_per_familia = corretiva_with_age.groupby('familia')['MTBF'].mean().reset_index()
    
    # Sort the results for better visualization
    avg_mtbf_per_familia = avg_mtbf_per_familia.sort_values('MTBF', ascending=False)
    
    # Plot the bar chart for average MTBF per familia
    fig = px.bar(avg_mtbf_per_familia, x='familia', y='MTBF',
                 title='Average MTBF per Familia',
                 labels={'MTBF': 'Average MTBF', 'familia': 'Familia'},
                 template='plotly_white')
    
    # Enhance layout
    fig.update_layout(xaxis_title="Familia",
                      yaxis_title="Average MTBF",
                      title_x=0.5)  # Center the chart title
    
    # Display the chart in col5
    col5.plotly_chart(fig, use_container_width=True)











    
    
    # Display the DataFrame in Streamlit
    st.dataframe(filtered_df)
