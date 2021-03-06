import streamlit as st
import sys
from os import path

sys.path.append(path.abspath('../'))

import function


def tag():
    tag = ["about"]
    date = "09/2021"
    lecture_time = "2"
    key = "welcome"
    title = "Hi, come to see my blog !?!!"
    extra = ""
    preview = """This is the beginning of my blog, come to see !"""
    return tag, date, lecture_time, key, title, extra, preview


def article():
    article = """
Hi, welcome here ! This is my blog.  
Since, I began to create programmes, games and others code stuff I always would like to have somewhere to share them. 
So I start this place, the Xtra Orbitals platform !  

Also, another goal was to have a place to put articles, blog articles, a place where I can write the way I want, 
without any formal writing style and with an english as bad/good as I feel.  

Last year, I start to wrote articles for the website [Full Stack Quantum Computation](https://fullstackquantumcomputation.tech/). 
I'll continue to write for them, I like their philosophy and their open science mood. They are also nice quantum mates. 
The articles, I'll write here will be less quantum specific but more personal and about any technology not only quantum.  

Finally, I want to share here what I do day to day, my experiments, hackatons, challenges, ...  

<br><br>
PS: I'm actually in the mood, if the solution doesn't exist, make your own. So this blog is from A to Z made by myself, 
it's not a blog CMS who already exist. I used streamlit for the web interface.
    """
    st.write(article, unsafe_allow_html=True)


def preview():
    tags, date, lecture_time, key, title, extra, preview = tag()

    function.metadata(tags, date, lecture_time, key, title, extra)

    with st.expander(preview):
        article()
        st.markdown(str("[go to up](#" + key + ")"))
