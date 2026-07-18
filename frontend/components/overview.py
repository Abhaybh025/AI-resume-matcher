import streamlit as st

# helper function
def bullets(icon, text):

    return f"""
    <div class = "bullet-item">
        <span class = "bullet-icon">{icon}</span>
        <span>{text}</span>
    </div>
"""

def render_overview(analysis):

    score = analysis["overall_score"]

    st.subheader("Overall Resume Analysis")

    st.markdown(
    f"""
    <div class="score-section">
        <div class="big-score">
            {score:.1f}%
    </div>

    <div class="score-label">
        Overall Match Score
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.progress(score/100)

    if score >= 90:
        status = "🟢 Excellent Match"

    elif score >= 75:
        status = "🟡 Good Match"

    elif score >= 60:
        status = "🟠 Moderate Match"

    else:
        status = "🔴 Needs Improvement"

    st.caption(status)

    st.divider()


    # Strengths and Weaknesses
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Strengths")
        
        if analysis["strengths"]:
            for strength in analysis["strengths"]:
                st.success(strength)
        
        else:
            st.info("No Strengths detected.")

    with col2:
        st.markdown("### Improvements")

        if analysis["weaknesses"]:
           for weakness in analysis["weaknesses"]:
                st.warning(weakness)
        else:
            st.info("No Improvements needed.")

        

    st.divider()


    # Matched, Missing, Extra Skills
    st.subheader("Quick Statistics")

    matched = analysis["matched_skills"]
    missing = analysis["missing_skills"]
    extra = analysis["extra_skills"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
        f"""
        <div class = "stat-card">
            <div class = "stat-title">
                ✓ Matched Skills
        </div>

        <div class="stat-value">
            {len(matched)}
        </div>

        </div>  
        """,
        unsafe_allow_html=True
        )

    with col2:
        st.markdown(
        f"""
        <div class = "stat-card">
            <div class = "stat-title">
              ✓ Missing Skills
        </div>

        <div class="stat-value">
            {len(missing)}
        </div>

        </div>  
        """,
        unsafe_allow_html=True
        )

    with col3:
        st.markdown(
        f"""
        <div class = "stat-card">
            <div class = "stat-title">
              ✓ Extra Skills
        </div>

        <div class="stat-value">
            {len(extra)}
        </div>

        </div>  
        """,
        unsafe_allow_html=True
        )