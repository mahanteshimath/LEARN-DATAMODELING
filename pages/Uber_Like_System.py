import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)



st.markdown(
"""# Uber like System

## Overview

1. Core User Components:
- Users (passengers) with profiles, ratings, and payment methods
- Drivers with profiles, documents, schedules, and earnings tracking
- Vehicles with detailed specifications and service type eligibility

2. Ride Management:
- Rides with complete trip details, pricing, and status tracking
- Service Types (UberX, Black, etc.) with specific pricing rules
- Real-time tracking and status updates
- Surge pricing based on demand and location

3. Financial Systems:
- Payments with detailed fare breakdowns
- Driver earnings calculations and payouts
- Multiple payment methods support
- Promotional system with discounts and offers

4. Support & Safety:
- Customer support ticket system
- Emergency contacts
- Driver documentation and verification
- Safety ratings and feedback

5. Operational Features:
- Driver scheduling and availability
- Service area management
- Vehicle inspections and requirements
- Trip history and analytics

The model is designed to handle:
- Real-time operations (ride matching, tracking)
- Complex pricing (base fare, surge, promotions)
- Multi-party transactions (user, driver, platform)
- Safety and compliance requirements
- Customer support and dispute resolution

"""
)


with open("./src/uber.txt", "r") as file:
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
