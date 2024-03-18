import streamlit as st
st.set_page_config(page_title="NASA NEOWS Data Viewer", page_icon="🌌", layout="wide")

def run():
    # Title and Introduction
    st.write("# Welcome to the NASA NEOWS Data Viewer 🌌")
    st.write("### Your gateway to exploring near-Earth objects (NEOs) 🚀🪨")

    # Project Summary
    st.markdown("""
    This platform is designed to provide an easy way for users to view and explore raw data from the NASA Near Earth Object Web Service (NEOWS). Our goal is to make space data accessible and understandable, allowing everyone from enthusiasts to researchers to dive into the vast universe of asteroid information.
    
    **Features include:**
    - **Date Range Selection:** Choose a specific range of dates to explore asteroids that were close to Earth during that period.
    - **Asteroid Details:** View detailed information about each asteroid, including its size, velocity, distance from Earth, and more.
    - **Interactive Exploration:** Utilize filters and selectors to narrow down your search and explore the data in an interactive manner.
    """)

    # About NEOWS
    st.markdown("""
    ### What is NEOWS?
    The Near Earth Object Web Service (NEOWS) is a RESTful web service provided by NASA to offer information about near-Earth asteroids. It includes data on asteroid close approaches to Earth and allows users to search for specific asteroids or browse the dataset to discover new findings. NEOWS is maintained by NASA's Center for Near-Earth Object Studies (CNEOS).
    
    For more information, visit the [NASA API Portal](https://api.nasa.gov/).
    """)

    # Footer
    st.markdown("""
    ---
    **Explore. Discover. Learn.** Join us on a journey through the cosmos as we uncover the mysteries of the universe, one asteroid at a time.
    """)

if __name__ == "__main__":
    run()
