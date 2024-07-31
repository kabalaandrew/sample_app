from navigation import make_sidebar
import streamlit as st
import pandas as pd 
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# st.markdown("""
#         <style>
#                .block-container {
#                     padding-top: 1.5rem;
#                     padding-bottom: 0rem;
#                     padding-left: 0rem;
#                     padding-right: 0rem;
#                 }
#         </style>
#         """, unsafe_allow_html=True)

#dataset_url = r"C:\Pythondef set_page_config():

# @st.experimental_memo
# def get_data() -> pd.DataFrame:
#     return pd.read_excel(dataset_url, index_col=0,parse_dates = True)

#df = get_data()

make_sidebar()

@st.cache_resource
def get_secret_content():
    # create KPI metrics
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label="EAs listed ✅",
        value=round(10),
        
    )

    kpi2.metric(
        label="EAs pending ⌛",
        value=int(200),
        
    )

    kpi3.metric(
        label="Percent completed '%",
        value=int(200),
        
    )
    kpi4.metric(
        label="Duplicate EAs ⚠️",
        value=int(round(0,2)),
        
    )


    #return 
st.header("Household listing dashboard")



#st.write(get_secret_content())

get_secret_content()
