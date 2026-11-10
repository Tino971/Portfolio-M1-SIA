import os
import streamlit as st
from data import PROJETS
from outils import all_tags, filter_projects

st.title("Projects")
st.write("Projects from my B.U.T. in Data Science and from my master's degree.")
projets = PROJETS

colonnes = st.columns(2)
for i, p in enumerate(projets):
    with colonnes[i % 2]:
        with st.container(border=True):
            if p["image"] and os.path.exists(p["image"]):
                st.image(p["image"])
            st.markdown(f"#### {p['titre']}")
            st.write(p["desc"])
            st.caption(f"{' - '.join(p['tags'])} - {p['annee']}")
            if p["lien"]:
                st.link_button("Voir le projet", p["lien"])
            else:
                st.caption("Projet non publié (projet scolaire)")
