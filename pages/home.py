import streamlit as st
from data import PROFIL, PROJETS, COMPETENCES, ALTERNANCE
from composants import afficher_pdf

st.title(f"Hi, I'm {PROFIL['nom']}")
st.subheader(PROFIL["titre"])

with st.container(border=True):
    st.write(PROFIL["bio"])
    st.markdown(f"{PROFIL['ville']}  \n[{PROFIL['email']}](mailto:{PROFIL['email']})")

    with st.container(horizontal=True):
        with open("assets/cv.pdf", "rb") as f:
            st.download_button("Download my CV", f, file_name="cv.pdf", type="primary")
        if st.button("Contact me"):
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
        st.metric("Projects", len(PROJETS))
        st.page_link("pages/projects.py", label="See my projects")
with c2:
    with st.container(border=True):
        st.metric("Skills", len(COMPETENCES))
        st.page_link("pages/skills.py", label="See my skills")
with c3:
    with st.container(border=True):
        st.metric("Best skill", meilleure)
        st.page_link("pages/skills.py", label="See my skills")

st.subheader("Apprenticeship")
with st.container(border=True, key="carte_alternance"):
    gauche, droite = st.columns([3, 2], vertical_alignment="center")
    with gauche:
        st.image(ALTERNANCE["image"])
    with droite:
        st.markdown(f"**{ALTERNANCE['titre']}**")
        st.write(ALTERNANCE["texte"])
        if st.button("Open the PDF"):
            afficher_pdf(ALTERNANCE["titre"], ALTERNANCE["pdf"])
