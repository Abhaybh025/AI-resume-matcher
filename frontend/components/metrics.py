import streamlit as st

def render_metrics(
    analysis,
    ats_result
):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "Overall Score",
            analysis["overall_score"],
            "🎯"
        )

    with col2:
        metric_card(
            "Semantic Score",
            analysis["semantic_score"],
            "🧠"
        )

    with col3:
        metric_card(
            "Skill Score",
            analysis["skill_score"],
            "🛠️"
        )

    with col4:
        metric_card(
            "ATS Score",
            ats_result["ats_score"],
            "📄"
        )


def get_class(score):
    if score >= 80:
        return "metric-good", "Excellent"

    elif score >= 60:
        return "metric-medium", "Moderate"

    return "metric-bad", "Needs Work"


def metric_card(title, value, icon):

    css_class, status = get_class(value)

    st.markdown(
        f"""
<div class="metric-card {css_class}">

<div class="metric-icon">{icon}</div>

<div class="metric-value">
{value:.1f}%
</div>

<div class="metric-title">
{title}
</div>

<div class="metric-progress">

<div class="metric-fill"
style="width:{value}%">
</div>

</div>

<div class="metric-status">
{status}
</div>

</div>
""",
        unsafe_allow_html=True
    )