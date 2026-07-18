import streamlit as st


def render_banner(overall_score):

    if overall_score >= 80:
        status = "🟢 Strong Match"

    elif overall_score >= 60:
        status = "🟡 Moderate Match"

    else:
        status = "🔴 Needs Improvement"

    st.success(
        f"""
### ✅ Analysis Complete

Your resume has been successfully analyzed against the Job Description.

**{status}**

"""
    )