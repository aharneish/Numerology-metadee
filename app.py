
# --- Streamlit web app for Devotional Numerology ---
import streamlit as st
from numerology import get_numerology_profile
from llm_inference import generate_report


# Set up Streamlit page and header
st.set_page_config(page_title="Devotional Numerology Report", page_icon="🔮", layout="centered")
st.title("🔮 Devotional Numerology Chat")
st.markdown("""
Enter your full name and date of birth to receive a personalized numerology report, generated with spiritual insights.
""")


# Input form for user details
with st.form("numerology_form"):
    full_name = st.text_input("Full Name", "")
    dob = st.text_input("Date of Birth (YYYY-MM-DD)", "")
    submitted = st.form_submit_button("Get My Report")


# Handle form submission and display results
if submitted:
    if not full_name.strip():
        st.error("Please enter your full name.")
    else:
        try:
            # Generate numerology profile
            profile = get_numerology_profile(full_name, dob)
            st.markdown("""
            <div style='background-color:#f9f9fa;padding:1.5em;border-radius:10px;margin-bottom:1em;border:1px solid #e0e0e0;color:#222;'>
            <b>Name:</b> {name}<br>
            <b>Date of Birth:</b> {dob}<br>
            <b>Life Path:</b> {life_path}<br>
            <b>Destiny:</b> {destiny}<br>
            <b>Soul Urge:</b> {soul_urge}<br>
            <b>Master Number:</b> {is_master}
            </div>
            """.format(
                name=profile['name'],
                dob=profile['dob'],
                life_path=profile['life_path'],
                destiny=profile['destiny'],
                soul_urge=profile['soul_urge'],
                is_master="Yes" if profile['is_master'] else "No"
            ), unsafe_allow_html=True)

            # Generate and display the LLM-based report
            with st.spinner("Consulting the spiritual guide..."):
                prompt = f"Generate a devotional numerology report for the following profile: {profile}"
                report = generate_report(prompt)
            st.markdown("""
            <div style='background-color:#f9f9fa;border-radius:10px;padding:1.5em 1em 1.5em 2em;box-shadow:0 2px 8px #0001;margin-top:1em;border:1px solid #e0e0e0;color:#222;'>
            <b>Spiritual Numerology Report:</b><br><br>
            {report}
            </div>
            """.format(report=report), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")
