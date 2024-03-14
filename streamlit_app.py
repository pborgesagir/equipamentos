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
url = "https://docs.google.com/spreadsheets/d/1CGypJWn35SFD6oYeLmFU1HjMhxJRBpuuVuVeP7y86wo/edit#gid=0"
st.title("EQUIPAMENTOS - Engenharia Clínica")
conn = st.connection("gsheets", type=GSheetsConnection)






# # Function to create a figure
# def create_figure():
#     fig, ax = plt.subplots()
#     ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Sample plot
#     return fig

# # Function to convert figure to PDF bytes
# def fig_to_pdf_bytes(fig):
#     buf = BytesIO()
#     with PdfPages(buf) as pdf:
#         pdf.savefig(fig)
#     buf.seek(0)
#     return buf

# # Streamlit app
# def main():
#     st.title("Chart to PDF Example")

#     # Button to generate PDF
#     if st.button("Generate PDF"):
#         fig = create_figure()
#         pdf_bytes = fig_to_pdf_bytes(fig)
#         st.download_button(
#             label="Download Chart as PDF",
#             data=pdf_bytes,
#             file_name="chart.pdf",
#             mime="application/pdf"
#         )

# if __name__ == "__main__":
#     main()


# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection



df = conn.read(spreadsheet=url, usecols=list(range(12)))
st.dataframe(df)
