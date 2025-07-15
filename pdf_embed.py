
import streamlit as st
import os

def display_pdf_download(subject):
    subject = subject.replace(" ", "")
    pdf_path = f"unit_pdfs/{subject}_Unit_Summary.pdf"
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download Unit Summary (PDF)",
                data=f,
                file_name=f"{subject}_Unit_Summary.pdf",
                mime="application/pdf"
            )
    else:
        st.info("🔧 PDF summary for this subject is coming soon.")
