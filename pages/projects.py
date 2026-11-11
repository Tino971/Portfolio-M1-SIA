import os
import streamlit as st
from data import PROJETS
from outils import tous_les_tags, filtrer_projets, chercher_projets
from composants import afficher_pdf

st.title("Projets")
st.write("Des projets de mon alternance, de mon B.U.T. et de mon master.")

recherche = st.text_input("Rechercher")

gauche, droite = st.columns([3, 1])
with gauche:
    choisis = st.multiselect("Filtrer par tag", tous_les_tags(PROJETS))
with droite:
    ordre = st.selectbox("Trier par année", ["Plus récents d'abord", "Plus anciens d'abord"])

projets = filtrer_projets(PROJETS, choisis)
projets = chercher_projets(projets, recherche)
projets = sorted(projets, key=lambda p: p["annee"], reverse=(ordre == "Plus récents d'abord"))

st.caption(f"{len(projets)} projet(s)")

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
                if st.button("Ouvrir le PDF", key="pdf_" + p["titre"]):
                    afficher_pdf(p["titre"], p["pdf"])
            if p["lien"]:
                st.link_button("Voir le code", p["lien"])
