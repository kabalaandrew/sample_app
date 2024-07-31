import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages
from streamlit_cookies_manager import CookieManager

def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]


def make_sidebar():
    with st.sidebar:
        st.image("https://images.freeimages.com/image/previews/cad/heartlink-logo-5690179.jpg?fmt=webp&h=350",
                 use_column_width=True)
        st.title("📊 UPHIA Dashboard")
        #st.logo()
        #st.write("")
        #st.write("")
             

        if st.session_state.get("logged_in", False):
            st.page_link("pages/home.py", label="Progress Dashboard", icon="📉")
            st.page_link("pages/reports.py", label="Reports", icon="🗂️")

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "dashboard_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("dashboard_app.py")


def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.switch_page("dashboard_app.py")