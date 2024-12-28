import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)



st.markdown(
"""# Card Account System

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
"""
)


with open("./src/Card_DataModel.txt", "r") as file:
   html_content = file.read()
components.html(html_content, width=800, height=600, scrolling=True)







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
