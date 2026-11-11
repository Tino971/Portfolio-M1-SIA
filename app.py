import streamlit as st
from data import PROFIL

st.set_page_config(page_title=PROFIL["nom"], page_icon=":briefcase:", layout="wide")

with open("style.css", encoding="utf-8") as f:
    st.html(f"<style>{f.read()}</style>")

pages = [
    st.Page("pages/home.py", title="À propos", default=True),
    st.Page("pages/projects.py", title="Projets"),
    st.Page("pages/skills.py", title="Compétences"),
    st.Page("pages/contact.py", title="Contact"),
]
nav = st.navigation(pages, position="hidden")

if "visites" not in st.session_state:
    st.session_state.visites = 0
    st.session_state.page = None
if st.session_state.page != nav.title:
    st.session_state.visites += 1
    st.session_state.page = nav.title

with st.sidebar:
    st.image("assets/photo.jpg", width=150)
    st.markdown(f"### {PROFIL['nom']}")
    st.caption(PROFIL["titre"])
    st.divider()
    for page in pages:
        st.page_link(page)
    st.divider()
    st.markdown(f"[GitHub]({PROFIL['github']}) · [LinkedIn]({PROFIL['linkedin']})")
    st.caption(f"Pages visitées :{st.session_state.visites}")

nav.run()
