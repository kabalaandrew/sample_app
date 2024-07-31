import streamlit as st
from time import sleep
from navigation import make_sidebar
import psycopg2  # Assuming you're using PostgreSQL
from streamlit_cookies_manager import CookieManager

# Initialize cookie manager
manager = CookieManager() 

make_sidebar()

st.title("Welcome to the UPHIA dashboard")

st.write("Please log in to continue...")

# Database connection details (replace with your actual credentials)
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "Admin"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        return connection
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None
    
@st.cache_data
def authenticate_user(username, password):
    connection = connect_to_db()
    if not connection:
        return False

    cursor = connection.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM users WHERE username = %s AND password = %s",
        (username, password),
    )
    count = cursor.fetchone()[0]
    connection.close()
    return count > 0

def reset_password(username, new_password):
    connection = connect_to_db()
    if not connection:
        return False

    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET password = %s WHERE username = %s", (new_password, username)
    )
    connection.commit()
    connection.close()
    return True

row_input = st.columns((2,1,2,1))
# username input at column 1
with row_input[0]:
    # username input
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if authenticate_user(username, password):
        st.session_state.logged_in = True
        st.success("Logged in successfully!")
        sleep(0.5)
        st.switch_page("pages/home.py")
    else:
        st.error("Incorrect username or password")


# Check for logged in state from cookie
# Use st.session_state for login state
if "logged_in" in st.session_state and st.session_state["logged_in"]:
     st.switch_page("pages/home.py")
else:
    st.session_state.logged_in = False