import requests
import streamlit as st
from streamlit_lottie import st_lottie

if __name__ == '__main__':
    st.set_page_config(
        page_title="Dark Theme Streamlit",
        page_icon=":web:",
        layout="wide",
    )

    # Apply custom styles from CSS file
    st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)

    # Your Streamlit app code goes here
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # ---- LOAD ASSETS ----
    lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Hi, I am Rahul")
        st.title("A Data Analyst From INDIA")
        st.write("I am passionate about using Python to make settings more efficient and effective....")
        st.write("[Learn More >](https://.com)")

    # ---- Contact Me ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Contact Me")
            st.write("##")
            st.write("[gitgub >](https://github.com/rahul67-code)")
            st.write("[replit >](https://replit.com/@rahulgharami67)")
            #st.write("[Gmail >](https://mail.google.com/mail)")

        with right_column:
            st_lottie(lottie_coding, height=200, key="coding")
