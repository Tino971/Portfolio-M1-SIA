import pandas as pd
import streamlit as st
from data import COMPETENCES, LANGUES, PARCOURS, EXPERIENCES

st.title("Skills")

tab1, tab2 = st.tabs(["Skills", "Education"])

with tab1:
    for comp, niveau in COMPETENCES.items():
        st.progress(niveau / 100, text=f"{comp} - {niveau}/100")

    st.subheader("Chart")
    df = pd.DataFrame({"skill": list(COMPETENCES.keys()),
                       "level": list(COMPETENCES.values())})
    st.bar_chart(df, x="skill", y="level")

    st.subheader("Languages")
    for langue, niveau in LANGUES.items():
        st.write(f"**{langue}** : {niveau}")

with tab2:
    st.subheader("Education")
    for annees, diplome in PARCOURS:
        st.write(f"**{annees}** : {diplome}")

    st.subheader("Work experience")
    for annees, poste, entreprise in EXPERIENCES:
        st.write(f"**{annees}** : {poste}, {entreprise}")
