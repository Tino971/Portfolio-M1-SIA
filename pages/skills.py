import pandas as pd
import streamlit as st
from data import COMPETENCES, LANGUES, PARCOURS, EXPERIENCES

st.title("Compétences")

tab1, tab2 = st.tabs(["Compétences", "Parcours"])

with tab1:
    for comp, niveau in COMPETENCES.items():
        st.progress(niveau / 100, text=f"{comp} - {niveau}/100")

    st.subheader("Graphique")
    df = pd.DataFrame({"compétence": list(COMPETENCES.keys()),
                       "niveau": list(COMPETENCES.values())})
    st.bar_chart(df, x="compétence", y="niveau")

    st.subheader("Langues")
    for langue, niveau in LANGUES.items():
        st.write(f"**{langue}** : {niveau}")

with tab2:
    st.subheader("Formation")
    for annees, diplome in PARCOURS:
        st.write(f"**{annees}** : {diplome}")

    st.subheader("Expériences professionnelles")
    for annees, poste, entreprise in EXPERIENCES:
        st.write(f"**{annees}** : {poste}, {entreprise}")
