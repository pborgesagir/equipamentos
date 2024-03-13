import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO

# Function to create a figure
def create_figure():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Sample plot
    return fig

# Function to convert figure to PDF bytes
def fig_to_pdf_bytes(fig):
    buf = BytesIO()
    with PdfPages(buf) as pdf:
        pdf.savefig(fig)
    buf.seek(0)
    return buf

# Streamlit app
def main():
    st.title("Chart to PDF Example")

    # Button to generate PDF
    if st.button("Generate PDF"):
        fig = create_figure()
        pdf_bytes = fig_to_pdf_bytes(fig)
        st.download_button(
            label="Download Chart as PDF",
            data=pdf_bytes,
            file_name="chart.pdf",
            mime="application/pdf"
        )

if __name__ == "__main__":
    main()
