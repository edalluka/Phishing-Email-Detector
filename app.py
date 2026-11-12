
import streamlit as st
from detector import analyze_email


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Phishing Detector",
    page_icon="🛡️",
    layout="wide"
)


# DASHBOARD HEADER
st.title("🛡️ Phishing Email Detector")
st.caption("CYBERSECURITY ANALYSIS PLATFORM")
st.markdown("---")

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0B1120;
    color: #F1F5F9;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Text areas */
.stTextArea textarea {
    background-color: #172033;
    color: #FFFFFF;
    border: 1px solid #334155;
    border-radius: 10px;
}

/* Buttons */
div.stButton > button {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
}

/* Buttons on hover */
div.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #172033;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #334155;
}

/* Progress bar */
.stProgress > div > div > div {
    background-color: #3B82F6;
}

</style>
""", unsafe_allow_html=True)



# SIDEBAR
st.sidebar.title("Navigation")
st.sidebar.write("Email Security Scanner")
st.sidebar.info(
    "Analyze email messages and identify "
    "potential phishing indicators."
)


# EMAIL INPUT
st.subheader("Email Analysis")

email = st.text_area(
    "Paste your email message below:",
    height=200,
    placeholder="Paste an email message here..."
)


# ANALYZE BUTTON
analyze_button = st.button(
    "🔍 Analyze Email",
    use_container_width=True
)


# EMAIL ANALYSIS
if analyze_button:

    if not email.strip():
        st.warning("Please enter an email first!")

    else:
        score, risk, findings = analyze_email(email)

        # RESULTS
        st.markdown("---")
        st.subheader("Analysis Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Risk Score", f"{score}/100")

        with col2:
            st.metric("Risk Classification", risk)

        with col3:
            st.metric("Indicators Found", len(findings))

        # RISK PROGRESS BAR
        st.write("Risk Level")
        st.progress(min(score, 100) / 100)

        # RISK CLASSIFICATION MESSAGE
        if risk == "Phishing":
            st.error("Potential phishing email detected!")

        elif risk == "Suspicious":
            st.warning(
                "Suspicious email. Further investigation recommended."
            )

        else:
            st.success(
                "No major keyword-based warnings detected."
            )

        # DETECTION FINDINGS
        st.markdown("---")
        st.subheader("Detection Findings")

        if findings:
            for finding in findings:
                st.write("•", finding)

        else:
            st.write("No indicators detected.")

        # DISCLAIMER
        st.caption(
            "This tool uses heuristic keyword detection. "
            "A low score does not guarantee that an email is safe."
        )
