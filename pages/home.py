import streamlit as st
from data import PROFIL, PROJETS, COMPETENCES

# en-tête de la page
st.title(f"Hi, I'm {PROFIL['nom']}")
st.subheader(PROFIL["titre"])

# la bio dans un cadre pour la faire ressortir
with st.container(border=True):
    st.write(PROFIL["bio"])
    # 2 espaces + \n = retour à la ligne, mailto: ouvre la boîte mail quand on clique
    st.markdown(f":material/location_on: {PROFIL['ville']}  \n"
                f":material/mail: [{PROFIL['email']}](mailto:{PROFIL['email']})")
    with open("assets/cv.pdf", "rb") as f:  # "rb" = lecture en binaire, obligatoire pour un PDF
        st.download_button("Download my CV", f, file_name="cv.pdf",
                           icon=":material/download:", type="primary")  # primary = bouton plein

st.divider()

# on parcourt les compétences et on garde celle qui a le plus gros niveau
meilleure, top = "", 0
for comp, niveau in COMPETENCES.items():
    if niveau > top:
        meilleure, top = comp, niveau

# 3 blocs côte à côte ; chacun = un cadre avec le chiffre clé
# et un lien qui ouvre la page correspondante
c1, c2, c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.metric("Projects", len(PROJETS))
        st.page_link("pages/projects.py", label="See my projects", icon=":material/arrow_forward:")
with c2:
    with st.container(border=True):
        st.metric("Skills", len(COMPETENCES))
        st.page_link("pages/skills.py", label="See my skills", icon=":material/arrow_forward:")
with c3:
    with st.container(border=True):
        st.metric("Best skill", meilleure)
        st.page_link("pages/skills.py", label="See all levels", icon=":material/arrow_forward:")
