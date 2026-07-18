import streamlit as st

def render_sidebar():
    st.sidebar.title("AI Resume Matcher")
    # st.sidebar.markdown("---")
    st.sidebar.info(
        """
        Upload a Resume and compare it with Job Description.
        
        Supports:  
        -> Resume PDF  
        -> Pasted JD  
        -> JD TXT  
        """
    )