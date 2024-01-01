import streamlit as st
from streamlit_lottie import st_lottie
import json


@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
def show_intro_page():
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.title("Introduction to predict salary app")
            st.divider()
            st.markdown(
            """    
            ## Predict developer's salary 
            ### _Select features below_
            """
            )
        with col2:
            lottie2 = load_lottiefile("./static/intro.json")
            st_lottie(lottie2,key='intro',height=300,width=400)

    st.divider()
        