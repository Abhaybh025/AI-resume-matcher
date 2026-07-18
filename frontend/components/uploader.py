import streamlit as st

def upload_resume():

    st.markdown("#### 📄 Resume")
    st.caption("Drag & Drop or click Upload ")

    resume = st.file_uploader(
        label = "Upload Resume",
        type=['pdf'],
        max_upload_size=2,
        label_visibility="collapsed"
    )

    if resume:
        st.markdown(
            """
            <div class="upload-status success">
                ✅ Ready for Analysis
            </div>
            """,
            unsafe_allow_html=True
        )

    return resume


def get_job_description_input():
    title_col, radio_col = st.columns([2,1])
    
    with title_col:
        st.markdown("#### 💼 Job Description")
        st.caption("Paste text or Upload ")

    with radio_col:
        option = st.radio(
            "",
            [
            "Paste",
            "Upload"
            ],
            horizontal= True,
            label_visibility="collapsed"
    )

    if option == "Paste":
        jd_text = st.text_area(
            label = "Paste Job Description",
            height= 300,
            placeholder= "Paste the complete Job Description here...",
            label_visibility="collapsed"
        )

        return "text", jd_text
    
    else:
        uploaded_file = st.file_uploader(
            label = "Upload",
            type=['txt','pdf'],
            max_upload_size= 2,
            label_visibility="collapsed"
        )

        if uploaded_file:
            st.markdown(
                """
                <div class="upload-status success">
                    ✅ Ready for Analysis
                </div>
                """,
                unsafe_allow_html=True
            )

        return "file", uploaded_file 