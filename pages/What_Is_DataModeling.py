import streamlit as st

# Function to embed Mermaid diagrams
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

# Streamlit app title
st.title("Understanding Data Modeling")

# Markdown content
st.markdown("""
### What is Data Modeling?

**Data Modeling** is the process of creating a visual representation of a system or dataset to define its structure, relationships, and constraints. It is a critical step in database design and system architecture, providing a blueprint for organizing and managing data efficiently.

---

### **Types of Data Models**

1. **Conceptual Data Model**
   - **Purpose**: High-level view of the system; focuses on business needs.
   - **Key Components**:
     - Entities: Real-world objects or concepts (e.g., *Customer*, *Order*).
     - Relationships: How entities are related (e.g., *Customer places Order*).

2. **Logical Data Model**
   - **Purpose**: Defines detailed attributes and relationships, independent of database systems.
   - **Key Components**:
     - Attributes: Properties of entities (e.g., *Customer Name*, *Order Date*).
     - Primary Keys: Unique identifier for each entity (e.g., *Customer ID*).
     - Foreign Keys: Links between entities (e.g., *Order references Customer*).

3. **Physical Data Model**
   - **Purpose**: Implements the logical model in a specific database system.
   - **Key Components**:
     - Tables, Columns: Database representation of entities and attributes.
     - Indexes, Partitions: Optimizations for performance.
     - Constraints: Rules for data integrity.

---

### Visualization of Data Modeling Levels
""")

# Mermaid diagram for data modeling levels
mermaid_code_levels = """
graph TD
    A[Conceptual Data Model] --> B[Logical Data Model]
    B --> C[Physical Data Model]
    subgraph Examples
        A1[Entities]
        A2[Relationships]
        B1[Attributes]
        B2[Primary & Foreign Keys]
        C1[Tables & Columns]
        C2[Indexes & Constraints]
    end
    A --> A1
    A --> A2
    B --> B1
    B --> B2
    C --> C1
    C --> C2
"""
st.components.v1.html(mermaid_html(mermaid_code_levels), height=400)

# Markdown for Benefits and Example
st.markdown("""
---

### **Benefits of Data Modeling**
1. **Clarity**: Simplifies complex systems into understandable diagrams.
2. **Consistency**: Ensures data integrity and standardization.
3. **Optimization**: Identifies inefficiencies before implementation.
4. **Scalability**: Facilitates future expansions and changes.

---

### **Example: E-commerce Data Model**
""")

# Mermaid diagram for E-commerce Data Model
mermaid_code_ecommerce = """
erDiagram
    CUSTOMER {
        int CustomerID
        string Name
        string Email
        string Phone
    }
    ORDER {
        int OrderID
        int CustomerID
        date OrderDate
        decimal TotalAmount
    }
    PRODUCT {
        int ProductID
        string Name
        decimal Price
        int StockQuantity
    }
    ORDER_ITEM {
        int OrderItemID
        int OrderID
        int ProductID
        int Quantity
        decimal Subtotal
    }
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--o{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : referenced by
"""
st.components.v1.html(mermaid_html(mermaid_code_ecommerce), height=400,scrolling=True)

# Markdown for Conclusion
st.markdown("""
---

### Conclusion

Data modeling is essential for designing robust and scalable systems, ensuring that data is structured efficiently and aligns with business goals. Whether for small applications or enterprise-level systems, understanding its types and techniques is key to success.
""")


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
