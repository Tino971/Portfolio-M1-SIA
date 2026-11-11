import os
import streamlit as st
from data import PROJETS
from outils import all_tags, filter_projects, search_projects
from composants import afficher_pdf

st.title("Projects")
st.write("Projects from my apprenticeship, my B.U.T. and my master's degree.")

recherche = st.text_input("Search")

gauche, droite = st.columns([3, 1])
with gauche:
    choisis = st.multiselect("Filter by tag", all_tags(PROJETS))
with droite:
    ordre = st.selectbox("Sort by year", ["Most recent first", "Oldest first"])

projets = filter_projects(PROJETS, choisis)
projets = search_projects(projets, recherche)
projets = sorted(projets, key=lambda p: p["annee"], reverse=(ordre == "Most recent first"))

st.caption(f"{len(projets)} project(s)")

colonnes = st.columns(2)
for i, p in enumerate(projets):
    with colonnes[i % 2]:
        with st.container(border=True, key=f"carte_{i}"):
            if p["image"] and os.path.exists(p["image"]):
                st.image(p["image"])
            st.markdown(f"#### {p['titre']}")
            st.write(p["desc"])
            st.caption(", ".join(p["tags"]) + f" - {p['annee']}")

            if p["pdf"]:
                if st.button("Open the PDF", key="pdf_" + p["titre"]):
                    afficher_pdf(p["titre"], p["pdf"])
            if p["lien"]:
                st.link_button("See the code", p["lien"])
