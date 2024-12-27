import streamlit as st
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path
import time
import pandas as pd
from PIL import Image
from io import BytesIO
import requests 

st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)

st.set_page_config(
  page_title="Learn Data Modeling",
  page_icon="🇮🇳",
  layout="wide",
  initial_sidebar_state="expanded",
) 

# --- Info ---
pg1 = st.Page(
    "pages/What_Is_DataModeling.py",
    title="What_Is_DataModeling",
    icon=":material/cognition:",
    default=True,
)

#How
pg2 = st.Page(
    "pages/Detail_Steps_to_Build_a_Data_Model.py",
    title="Detail Steps to Build a DataModel",
    icon=":material/construction:",
)

#Examples
pg3 = st.Page(
    "pages/Card_Account_system.py",
    title="Card Account system",
    icon=":material/credit_card:",
)



pg = st.navigation(
    {
        "Info": [What_Is_DataModeling],
        "How": [Detail_Steps_to_Build_a_Data_Model],
        "Examples": [Card_Account_system],
    }
)


pg.run()
