import streamlit as st
from visual import profile
from visual import experiences
from visual import education
from visual import publications
from visual import projects
import function
import common

st.set_page_config(
    page_title="Resume",
    page_icon=":page_with_curl:",
    layout="wide",
    initial_sidebar_state="auto",
)

common.css()

# Init var
lang = "english"
base_url = (
    "https://raw.githubusercontent.com/mickahell/mickahell/main/cv/json/" + lang + "/"
)
index_page = "index"

# Download json
# Everything here are in cache
# Calcul index
index = function.dl_json(base_url, index_page)
db = index["index"]
cv_fr = (
    "<form action="
    + db["resume_fr"]
    + "><input type='submit' value='FR: CV pdf' /></form>"
)
cv_en = (
    "<form action="
    + db["resume_en"]
    + "><input type='submit' value='EN: Resume pdf' /></form>"
)
# Calcul entire visual
info = function.dl_json(base_url, db["profile"]["key"])
exp = function.dl_json(base_url, db["experiences"]["key"])
edu = function.dl_json(base_url, db["education"]["key"])
publi = function.dl_json(base_url, db["publications"]["key"])
projec = function.dl_json(base_url, db["projects"]["key"])
# Profile pic
photo_profile = function.dl_img(
    img_url=info["profile"]["photo_url"], dest="data/profile.png"
)

# Filter
index_filter, exp_col, edu_col, publi_col, projects_col = st.columns(5)
index_filter.write("##### Filter")
exp_box = exp_col.checkbox("Experiences", True)
edu_box = edu_col.checkbox("Education", True)
publi_box = publi_col.checkbox("Publications", True)
projects_box = projects_col.checkbox("Projects", True)
st.write("---")

# Profile
profile.profile(json_data=info, _photo_profile=photo_profile)

# Experiences
if exp_box:
    with st.container():
        experiences.exp(json_data=exp, base_url=base_url)

# Education
if edu_box:
    with st.container():
        education.edu(json_data=edu)
    with st.container():
        education.cert(json_data=edu)

# Publications
if publi_box:
    with st.container():
        publications.publi(json_data=publi)
    with st.container():
        publications.blog(json_data=publi)

# Projects
if projects_box:
    with st.container():
        projects.projects(json_data=projec)

# PDF access
st.sidebar.write("---")

cvfr_col, cven_col = st.sidebar.columns(2)
cvfr_col.write(cv_fr, unsafe_allow_html=True)
cven_col.write(cv_en, unsafe_allow_html=True)

# Clear cache
st.sidebar.write("---")
if st.sidebar.button("Clear cache !"):
    st.experimental_memo.clear()
    photo_refresh = function.dl_img(
        img_url=info["profile"]["photo_url"], dest="data/profile.png", force=True
    )
