import pandas as pd
import streamlit as st
from data import COMPETENCES, LANGUES, PARCOURS, EXPERIENCES

st.title("Skills")

# deux onglets : on écrit le contenu de chacun dans son bloc "with"
tab1, tab2 = st.tabs(["Skills", "Education"])

with tab1:
    # une barre par compétence ; st.progress veut un nombre entre 0 et 1
    for comp, niveau in COMPETENCES.items():
        st.progress(niveau / 100, text=f"**{comp}** — {niveau}/100")

    st.subheader("Overview")
    # un tableau pandas avec 2 colonnes : skill et level
    df = pd.DataFrame({"skill": list(COMPETENCES.keys()),
                       "level": list(COMPETENCES.values())})
    st.bar_chart(df, x="skill", y="level")

    st.subheader("Languages")
    for langue, niveau in LANGUES.items():
        st.markdown(f"**{langue}** — {niveau}")

with tab2:
    st.subheader("Education")
    # chaque élément de PARCOURS est un tuple (période, diplôme) qu'on "déballe"
    for periode, diplome in PARCOURS:
        st.markdown(f"**{periode}** — {diplome}")

    st.subheader("Work experience")
    for periode, poste, boite in EXPERIENCES:
        st.markdown(f"**{periode}** — {poste}, *{boite}*")
