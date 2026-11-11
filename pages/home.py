import streamlit as st
from data import PROFIL, PROJETS, COMPETENCES, ALTERNANCE
from composants import afficher_pdf

st.title(f"Bonjour, je suis {PROFIL['nom']}")
st.subheader(PROFIL["titre"])

with st.container(border=True):
    st.write(PROFIL["bio"])
    st.markdown(f"{PROFIL['ville']}  \n[{PROFIL['email']}](mailto:{PROFIL['email']})")

    with st.container(horizontal=True):
        with open("assets/cv.pdf", "rb") as f:
            st.download_button("Télécharger mon CV", f, file_name="cv.pdf", type="primary")
        if st.button("Me contacter"):
            st.switch_page("pages/contact.py")

st.divider()

meilleure = ""
top = 0
for comp, niveau in COMPETENCES.items():
    if niveau > top:
        meilleure = comp
        top = niveau

c1, c2, c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.metric("Projets", len(PROJETS))
        st.page_link("pages/projects.py", label="Voir mes projets")
with c2:
    with st.container(border=True):
        st.metric("Compétences", len(COMPETENCES))
        st.page_link("pages/skills.py", label="Voir mes compétences")
with c3:
    with st.container(border=True):
        st.metric("Meilleure compétence", meilleure)
        st.page_link("pages/skills.py", label="Voir mes compétences")

st.subheader("Alternance")
with st.container(border=True, key="carte_alternance"):
    gauche, droite = st.columns([3, 2], vertical_alignment="center")
    with gauche:
        st.image(ALTERNANCE["image"])
    with droite:
        st.markdown(f"**{ALTERNANCE['titre']}**")
        st.write(ALTERNANCE["texte"])
        if st.button("Ouvrir le PDF"):
            afficher_pdf(ALTERNANCE["titre"], ALTERNANCE["pdf"])
