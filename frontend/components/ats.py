import streamlit as st


def render_ats(ats_result):
    score = ats_result["ats_score"]

    st.subheader("ATS Analysis")

    st.markdown(
    f"""
    <div class = "ats-hero">

    <div class = "ats-score">
        {score:.0f}%
    </div>

    <div class = "ats-title">
        ATS Readiness
    </div>

    </div>
    """,
        unsafe_allow_html=True
    )

    st.progress(score / 100)

    score = ats_result["ats_score"]

    if score >= 90:
        status = "🟢 Excellent ATS Readiness"

    elif score >= 75:
        status = "🟡 Good ATS Readiness"

    elif score >= 60:
        status = "🟠 Moderate ATS Readiness"

    else:
        status = "🔴 Poor ATS Readiness"

    st.caption(status)


    st.divider()


    left, right = st.columns([1,1], gap="large")

    with left:
        with st.container(border=True, height=350):
            st.markdown("### ✅ Rule Checks")

            for check, status in ats_result["checks"].items():
                # if status:
                #     st.success(check)

                # else:
                #     st.error(check)
                icon = "✅" if status else "❌"

                st.markdown(f"{icon} {check}")
    
    with right:
        with st.container(border=True, height= 350):
            st.markdown("### 📋 Recommendations")

            feedback = ats_result["feedback"]

            if feedback:
                for item in feedback:
                    st.markdown(f"⚠️ {item}")

            else:
                st.markdown("✅ Excellent! No ATS issues detected.")