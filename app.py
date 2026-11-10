import streamlit as st
from data import PROFIL  # tout le contenu du site vient de data.py

# réglages de l'onglet du navigateur (titre + icône) et page en pleine largeur
st.set_page_config(page_title=PROFIL["nom"], page_icon=":briefcase:", layout="wide")

# les 4 pages du site, default=True -> celle qui s'ouvre en premier
pages = [
    st.Page("pages/home.py", title="About me", icon=":material/person:", default=True),
    st.Page("pages/projects.py", title="Projects", icon=":material/code:"),
    st.Page("pages/skills.py", title="Skills", icon=":material/bar_chart:"),
    st.Page("pages/contact.py", title="Contact", icon=":material/mail:"),
]
# position="hidden" cache le menu auto (sinon il se met tout en haut, avant la photo)
nav = st.navigation(pages, position="hidden")

# tout ce qui est dans ce bloc va dans la barre de gauche
with st.sidebar:
    st.image("assets/photo.jpg", width=150)
    st.markdown(f"### {PROFIL['nom']}")  # ### = petit titre en Markdown
    st.caption(PROFIL["titre"])  # caption = texte petit et gris
    st.divider()
    # on refait le menu à la main, sous la photo : un lien par page
    for page in pages:
        st.page_link(page)
    st.divider()
    # liens vers mes profils, en Markdown : [texte](adresse)
    st.markdown(f"[GitHub]({PROFIL['github']}) · [LinkedIn]({PROFIL['linkedin']})")

nav.run()  # lance la page choisie
