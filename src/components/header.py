import streamlit as st

def header_home():

    logo_url="https://pub-1f9b302966c1432cb7e60b324f799175.r2.dev/ChatGPT%20Image%20Jul%203%2C%202026%2C%2005_10_06%20PM.png"
    st.markdown(f"""
        <div>
            <img src='{logo_url}' style='width:300px; height:300px';/>
        </div>
        """,unsafe_allow_html=True)