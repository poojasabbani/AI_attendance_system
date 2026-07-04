import streamlit as st

def header_home():

    logo_url="https://pub-1f9b302966c1432cb7e60b324f799175.r2.dev/ChatGPT%20Image%20Jul%203%2C%202026%2C%2005_10_06%20PM.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-botton:30px; margin-top:30px">
            <img src='{logo_url}' style='width:300px; height:300px';/>
            <h1 style: 'text-align:center; color:e8e3ff'>ATTEND AI</h1>
        </div>
        """,unsafe_allow_html=True)
def header_dashboard():

    logo_url="https://pub-1f9b302966c1432cb7e60b324f799175.r2.dev/ChatGPT%20Image%20Jul%203%2C%202026%2C%2005_10_06%20PM.png"
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='width:85px; height:85px';/>
            <h2 style: 'text-align:left; color:5865F2'>ATTEND AI</h2>
        </div>
        """,unsafe_allow_html=True)