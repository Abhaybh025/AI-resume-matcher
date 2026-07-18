import streamlit as st

def render_skills(analysis):

    matched = sorted(
        [skill.title() for skill in analysis["matched_skills"]]
    )

    missing = sorted(
        [skill.title() for skill in analysis["missing_skills"]]
    )

    extra = sorted(
        [skill.title() for skill in analysis["extra_skills"]]
    )

    st.subheader("Skills Analysis")

    matched_col, missing_col, extra_col = st.columns(3)

    with matched_col:
        with st.container(border=True, height=350):
            st.markdown(
                f"### 🟢 Matched Skills({len(matched)})"
            )

            if analysis["matched_skills"]:
                for skill in matched:
                    st.success(skill)
            
            else:
                st.warning("No matching skills found.")

    with missing_col:
        with st.container(border=True, height=350):
            st.markdown(
                f"### 🔴 Missing Skills({len(missing)})"
            )

            if analysis["missing_skills"]:
                for skill in missing:
                    st.error(skill)
            
            else:
                st.success("🎉 Excellent! No missing skills detected.")

    with extra_col:
        with st.container(border=True, height=350):
            st.markdown(
                f"### 🔵 Extra Skills({len(extra)})"
            )

            if analysis["extra_skills"]:
                for skill in extra:
                    st.info(skill)
            
            else:
                st.info("No additional skills detected.")

    