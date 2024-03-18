import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(layout="wide")


# Function to fetch a list of asteroid IDs based on the selected date range
def fetch_asteroid_ids(start_date, end_date, api_key):
    feed_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    response = requests.get(feed_url)
    asteroid_ids = []
    if response.status_code == 200:
        asteroids_data = response.json()['near_earth_objects']
        for date in asteroids_data:
            for asteroid in asteroids_data[date]:
                asteroid_ids.append(asteroid['id'])
    else:
        st.error("Failed to fetch asteroid data. Please check your API key and try again.")
    return asteroid_ids

# Function to fetch detailed information for selected asteroid IDs
def fetch_asteroid_data(asteroid_ids, api_key):
    asteroid_details = []
    for asteroid_id in asteroid_ids:
        details_url = f"https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}?api_key={api_key}"
        response = requests.get(details_url)
        if response.status_code == 200:
            asteroid_details.append(response.json())
        else:
            st.error(f"Failed to retrieve data for asteroid ID {asteroid_id}.")
    return asteroid_details

# Function to fetch asteroid data based on the selected date range without specific IDs
def fetch_asteroids_by_date(start_date, end_date, api_key):
    if end_date:
        feed_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"
    else:
        feed_url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&api_key={api_key}"
    
    response = requests.get(feed_url)
    if response.status_code == 200:
        return response.json()['near_earth_objects']
    else:
        st.error("Failed to fetch asteroid data. Please check your API key and try again.")
        return {}

# Streamlit UI components
st.title("Asteroid Information Finder")

# Your NASA API key
api_key = "IFGC3aVYjVZaWurVkT0T1Qu74IPL10TuqIGc2dek"

# Date range selector
today = datetime.today().date()
week_ago = today - timedelta(days=7)
date_range = st.date_input("Select date range:", [week_ago, today])

start_date = date_range[0].strftime('%Y-%m-%d')
end_date = date_range[1].strftime('%Y-%m-%d') if len(date_range) > 1 else None

asteroid_ids = fetch_asteroid_ids(start_date, end_date, api_key)
selected_ids = st.multiselect("Select Asteroid IDs:", options=asteroid_ids, format_func=lambda x: f"Asteroid {x}")

if st.button("Get Asteroid Information"):
    if selected_ids:
        # Fetch and display detailed information for selected asteroid IDs
        asteroid_data = fetch_asteroid_data(selected_ids, api_key)
        for data in asteroid_data:
            st.write(f"### Asteroid {data['id']} {data['name']}")
            st.json(data)
    else:
        # If no IDs are selected, fetch and display all asteroids data for the selected dates
        asteroids_data = fetch_asteroids_by_date(start_date, end_date, api_key)
        if asteroids_data:
            # Sort the dates to ensure chronological order
            sorted_dates = sorted(asteroids_data.keys())
            for date in sorted_dates:
                st.write(f"### Date: {date}")
                for asteroid in asteroids_data[date]:
                    # Optional: Display the asteroid's name before its detailed JSON data
                    formatted_name = asteroid['name'].strip("[]()")
                    st.write(f"#### {formatted_name}")
                    st.json(asteroid)
