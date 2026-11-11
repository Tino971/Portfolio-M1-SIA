import os
import streamlit as st


@st.cache_data
def lire_fichier(chemin):
    with open(chemin, "rb") as f:
        return f.read()


@st.dialog("PDF", width="large")
def afficher_pdf(titre, chemin):
    st.write(f"**{titre}**")
    pdf = lire_fichier(chemin)
    st.pdf(pdf, height=650)
    st.download_button("Télécharger", pdf, file_name=os.path.basename(chemin))
