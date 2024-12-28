import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas


st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)


# # Accessing the database credentials
# db_credentials = st.secrets["db_credentials"]

# if 'account' not in st.session_state:
#     st.session_state.account = db_credentials["account"]
# if 'role' not in st.session_state:
#     st.session_state.role = db_credentials["role"]
# if 'warehouse' not in st.session_state:
#     st.session_state.warehouse = db_credentials["warehouse"]
# if 'database' not in st.session_state:
#     st.session_state.database = db_credentials["database"]
# if 'schema' not in st.session_state:
#     st.session_state.schema = db_credentials["schema"]
# if 'user' not in st.session_state:
#     st.session_state.user = db_credentials["user"]
# if 'password' not in st.session_state:
#     st.session_state.password = db_credentials["password"]
# if 'weatherapi_key' not in st.session_state:
#     st.session_state.weatherapi_key = db_credentials["weatherapi_key"]
# if 'google_api_key' not in st.session_state:
#     st.session_state.google_api_key = db_credentials["google_api_key"]
    

# def store_credentials():
#     st.session_state.account = db_credentials["account"]
#     st.session_state.role = db_credentials["role"]
#     st.session_state.warehouse = db_credentials["warehouse"]
#     st.session_state.database = db_credentials["database"]
#     st.session_state.schema = db_credentials["schema"]
#     st.session_state.user = db_credentials["user"]
#     st.session_state.password = db_credentials["password"]

# def create_snowflake_connection():
#     try:
#         conn = snowflake.connector.connect(
#             account=st.session_state.account,
#             role=st.session_state.role,
#             warehouse=st.session_state.warehouse,
#             database=st.session_state.database,
#             schema=st.session_state.schema,
#             user=st.session_state.user,
#             password=st.session_state.password,
#             client_session_keep_alive=True
#         )
#         st.toast("Connection to Snowflake successfully!", icon='🎉')
#         time.sleep(.5)
#         st.balloons()
#     except Exception as e:
#         st.error(f"Error connecting to Snowflake: {str(e)}")
#     return conn

# def execute_query(query):
#     try:
#         conn = snowflake.connector.connect(
#             account=st.session_state.account,
#             role=st.session_state.role,
#             warehouse=st.session_state.warehouse,
#             database=st.session_state.database,
#             schema=st.session_state.schema,
#             user=st.session_state.user,
#             password=st.session_state.password,
#             client_session_keep_alive=True
#         )
#         cursor = conn.cursor()
#         cursor.execute(f"USE DATABASE {st.session_state.database}")
#         cursor.execute(f"USE SCHEMA {st.session_state.schema}")
#         cursor.execute(query)
#         result = cursor.fetchall()
#         columns = [col[0] for col in cursor.description]
#         conn.close()
#         result_df = pd.DataFrame(result, columns=columns)
#         return result_df
#     except Exception as e:
#         st.error(f"Error executing query: {str(e)}")
#         return None


st.markdown(
"""# Star Schema Design for a Card Account System

## Overview
You are tasked with designing a **star schema data model** for a **Card Account system** for a specific credit card product. This system manages card accounts, tracks balances, and monitors issued cards and their usage.

### Key System Details:
1. **Primary Cardholder**:
   - Each card account is managed by a primary cardholder, who owns the card account.
2. **Issued Plastic Cards**:
   - Multiple plastic cards can be issued to individuals selected by the primary cardholder.
   - Each individual has their own assigned plastic card.
3. **Daily Balances**:
   - The system tracks daily outstanding balances for the primary cardholder's account.
4. **Credit Limits**:
   - Each issued plastic card has a defined credit limit linked to the individual it is issued to.

---

## Requirements

1. **Track daily snapshots** of outstanding balances for each card account on a daily basis.  
2. **Monitor plastic cards issued** to individuals by the primary cardholder, along with their respective credit limits.  
3. **Analyze credit limits, balances, and usage patterns** across time and issued cards.  
4. Use a **star schema design**, with appropriate fact and dimension tables, to support efficient querying and reporting.  

---

## Schema Design

### **Fact Table**
- **Fact_Card_Transactions**:
  - Tracks daily transactions and balances at the account and card level.

| Column Name               | Data Type  | Description                                   |
|---------------------------|------------|-----------------------------------------------|
| Transaction_ID            | INT        | Unique identifier for each transaction.       |
| Card_Key                  | INT        | Foreign key to the `Dim_Card` table.          |
| Account_Key               | INT        | Foreign key to the `Dim_Account` table.       |
| Transaction_Date          | DATE       | Date of the transaction or balance snapshot.  |
| Total_Purchases           | DECIMAL    | Total purchase amount for the day.            |
| Total_Payments            | DECIMAL    | Total payment amount for the day.             |
| Outstanding_Balance       | DECIMAL    | Remaining balance after transactions.         |
| Credit_Utilization_Pct    | DECIMAL    | Percentage of credit limit utilized.          |

---

### **Dimension Tables**
1. **Dim_Account**:
   - Stores details about the primary cardholder's account.

| Column Name       | Data Type  | Description                                   |
|-------------------|------------|-----------------------------------------------|
| Account_Key       | INT        | Primary key for the account.                 |
| Account_ID        | VARCHAR    | Unique identifier for the account.           |
| Primary_Cardholder| VARCHAR    | Name of the primary cardholder.              |
| Account_Open_Date | DATE       | Date when the account was opened.            |
| Account_Status    | VARCHAR    | Status of the account (e.g., Active, Closed).|

2. **Dim_Card**:
   - Stores details about each issued plastic card.

| Column Name      | Data Type  | Description                                   |
|------------------|------------|-----------------------------------------------|
| Card_Key         | INT        | Primary key for the card.                    |
| Card_ID          | VARCHAR    | Unique identifier for the plastic card.      |
| Account_Key      | INT        | Foreign key to the `Dim_Account` table.      |
| Issued_To        | VARCHAR    | Name of the individual holding the card.     |
| Credit_Limit     | DECIMAL    | Credit limit assigned to the card.           |
| Issue_Date       | DATE       | Date the card was issued.                    |

3. **Dim_Date**:
   - Stores details for date-based analytics.

| Column Name      | Data Type  | Description                                   |
|------------------|------------|-----------------------------------------------|
| Date_Key         | INT        | Surrogate key for the date.                  |
| Transaction_Date | DATE       | Actual date.                                 |
| Year             | INT        | Year of the date.                            |
| Month            | INT        | Month of the date.                           |
| Day              | INT        | Day of the date.                             |

---

## Relationships

- **Dim_Account** → **Fact_Card_Transactions** (`Account_Key`).  
- **Dim_Card** → **Fact_Card_Transactions** (`Card_Key`).  
- **Dim_Date** → **Fact_Card_Transactions** (`Transaction_Date`).

---

## Summary
This star schema design enables efficient querying and reporting on:
- Daily outstanding balances.  
- Credit utilization trends.  
- Usage patterns of issued cards across time.  
The schema is optimized for analytics and supports flexibility for future extensions.  
"""
)








st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white; # Adjust this for expander header color
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white; # Expander content color
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer="""<style>

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #2C1E5B;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/" target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)  
