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


# Accessing the database credentials
db_credentials = st.secrets["db_credentials"]

if 'account' not in st.session_state:
    st.session_state.account = db_credentials["account"]
if 'role' not in st.session_state:
    st.session_state.role = db_credentials["role"]
if 'warehouse' not in st.session_state:
    st.session_state.warehouse = db_credentials["warehouse"]
if 'database' not in st.session_state:
    st.session_state.database = db_credentials["database"]
if 'schema' not in st.session_state:
    st.session_state.schema = db_credentials["schema"]
if 'user' not in st.session_state:
    st.session_state.user = db_credentials["user"]
if 'password' not in st.session_state:
    st.session_state.password = db_credentials["password"]
if 'weatherapi_key' not in st.session_state:
    st.session_state.weatherapi_key = db_credentials["weatherapi_key"]
if 'google_api_key' not in st.session_state:
    st.session_state.google_api_key = db_credentials["google_api_key"]
    

def store_credentials():
    st.session_state.account = db_credentials["account"]
    st.session_state.role = db_credentials["role"]
    st.session_state.warehouse = db_credentials["warehouse"]
    st.session_state.database = db_credentials["database"]
    st.session_state.schema = db_credentials["schema"]
    st.session_state.user = db_credentials["user"]
    st.session_state.password = db_credentials["password"]

def create_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            account=st.session_state.account,
            role=st.session_state.role,
            warehouse=st.session_state.warehouse,
            database=st.session_state.database,
            schema=st.session_state.schema,
            user=st.session_state.user,
            password=st.session_state.password,
            client_session_keep_alive=True
        )
        st.toast("Connection to Snowflake successfully!", icon='🎉')
        time.sleep(.5)
        st.balloons()
    except Exception as e:
        st.error(f"Error connecting to Snowflake: {str(e)}")
    return conn

def execute_query(query):
    try:
        conn = snowflake.connector.connect(
            account=st.session_state.account,
            role=st.session_state.role,
            warehouse=st.session_state.warehouse,
            database=st.session_state.database,
            schema=st.session_state.schema,
            user=st.session_state.user,
            password=st.session_state.password,
            client_session_keep_alive=True
        )
        cursor = conn.cursor()
        cursor.execute(f"USE DATABASE {st.session_state.database}")
        cursor.execute(f"USE SCHEMA {st.session_state.schema}")
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        conn.close()
        result_df = pd.DataFrame(result, columns=columns)
        return result_df
    except Exception as e:
        st.error(f"Error executing query: {str(e)}")
        return None
import streamlit as st

# Function to embed Mermaid diagrams as HTML
def mermaid_html(mermaid_code):
    return f"""
    <div class="mermaid">
    {mermaid_code}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    """

# Mermaid flowchart code
flowchart_code = """
flowchart TD
    subgraph "Phase 1: Requirements Gathering"
        A[Start] --> B[Identify Business Requirements]
        B --> C[Document Data Sources]
        C --> D[Define Data Objects]
        D --> E[Identify Relationships]
    end

    subgraph "Phase 2: Conceptual Modeling"
        E --> F[Create Entity List]
        F --> G[Define Entity Relationships]
        G --> H[Document Business Rules]
        H --> I[Review with Stakeholders]
    end

    subgraph "Phase 3: Logical Modeling"
        I --> J[Define Attributes]
        J --> K[Establish Primary Keys]
        K --> L[Set Foreign Keys]
        L --> M[Apply Normalization]
        M --> N[Validate Business Rules]
    end

    subgraph "Phase 4: Physical Modeling"
        N --> O[Choose Database Platform]
        O --> P[Define Tables and Columns]
        P --> Q[Set Data Types]
        Q --> R[Create Indexes]
        R --> S[Implement Constraints]
    end

    subgraph "Phase 5: Implementation"
        S --> T[Generate DDL Scripts]
        T --> U[Create Test Data]
        U --> V[Perform Testing]
        V --> W[Deploy to Production]
    end

    style A fill:#f9f,stroke:#333
    style W fill:#9f9,stroke:#333
    
    %% Add relationship lines
    B --> |"Inputs"| F
    G --> |"Influences"| K
    H --> |"Guides"| M
    M --> |"Shapes"| P
    N --> |"Validates"| S
"""

# Streamlit content
st.title("Data Modeling Process Flowchart")
st.subheader("Visualization of the Phases in Data Modeling")

# Display the Mermaid Diagram
st.components.v1.html(mermaid_html(flowchart_code), height=800)











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
