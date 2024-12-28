import streamlit as st
import streamlit.components.v1 as components

st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)


st.title("Data Modeling Process Flowchart")
st.subheader("Visualization of the Phases in Data Modeling")

with open("./src/steps.txt", "r") as file:
    html_content = file.read()




# Display the HTML content as an embedded diagram in Streamlit
components.html(html_content, width=800, height=600, scrolling=True)





st.markdown("""
# Detailed Data Modeling Steps

## Phase 1: Requirements Gathering
1. Identify Business Requirements
   - Interview stakeholders
   - Review existing documentation
   - Define scope and objectives
   - Document use cases

2. Document Data Sources
   - List all current data sources
   - Identify data formats
   - Document data volumes
   - Note update frequencies

3. Define Data Objects
   - List main business entities
   - Define entity characteristics
   - Document dependencies
   - Identify critical data elements

4. Identify Relationships
   - Map business processes
   - Document data flow
   - Identify entity interactions
   - Define cardinality rules

## Phase 2: Conceptual Modeling
1. Create Entity List
   - Name entities clearly
   - Define entity purposes
   - Document entity descriptions
   - Validate with business users

2. Define Entity Relationships
   - Map entity connections
   - Define relationship types
   - Document cardinality
   - Create relationship matrix

3. Document Business Rules
   - Define data constraints
   - Document validation rules
   - Specify calculations
   - List dependencies

## Phase 3: Logical Modeling
1. Define Attributes
   - List all attributes per entity
   - Define data domains
   - Document descriptions
   - Set nullable properties

2. Establish Primary Keys
   - Choose key strategy
   - Define composite keys
   - Document key constraints
   - Set uniqueness rules

3. Apply Normalization
   - Apply 1NF (First Normal Form)
   - Progress to 2NF
   - Implement 3NF
   - Consider BCNF where needed

## Phase 4: Physical Modeling
1. Choose Database Platform
   - Select DBMS
   - Consider scalability
   - Review performance needs
   - Check compatibility

2. Define Tables and Columns
   - Create table definitions
   - Set column properties
   - Define default values
   - Document table relationships

3. Implement Constraints
   - Set primary keys
   - Define foreign keys
   - Add check constraints
   - Create unique constraints

## Phase 5: Implementation
1. Generate DDL Scripts
   - Create table scripts
   - Define indexes
   - Set constraints
   - Document deployment steps

2. Testing
   - Create test data
   - Validate relationships
   - Test constraints
   - Performance testing

3. Deployment
   - Review change impact
   - Schedule deployment
   - Execute scripts
   - Validate deployment
""")







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
