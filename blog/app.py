import streamlit as st
import menu
import function


st.set_page_config(page_title="Blog", page_icon=":space_invader:", layout='wide', initial_sidebar_state='auto')

menu.css()
menu.menu_app()

title = """
<div align="center">
    <h1>My Blog</h1>
</div>
<br /><br />
"""
st.markdown(title, unsafe_allow_html=True)

POSTS = function.get_articles()

for i in POSTS:
    i.preview()

st.write("---")
function.author()
