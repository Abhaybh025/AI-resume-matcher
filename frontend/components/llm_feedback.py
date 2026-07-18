import streamlit as st

def render_llm_feedback(response):

    st.subheader("Overall Evaluation")
    st.write(response.overall_evaluation)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Strengths")

        for item in response.strengths:
            st.success(item)

    with col2:

        st.subheader("Weaknesses")

        for item in response.weaknesses:
            st.error(item)

    st.divider()

    st.subheader("Resume Improvements")

    for item in response.resume_improvements:
        st.info(item)

    st.divider()

    st.subheader("ATS Improvements")

    for item in response.ats_improvements:
        st.warning(item)

    st.divider()

    st.subheader("Final Recommendation")

    st.success(response.final_recommendation)