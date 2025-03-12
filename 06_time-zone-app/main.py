import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


# List of available time zones
Time_Zones = [
     "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Create app title
st.title("Time Zone Applications")

# Create a multi-select dropdown for choosing time zones
selected_time_zone = st.multiselect(
    "Selected time zone",Time_Zones, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("Selected Time Zone")
for tz in selected_time_zone:

    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display timezone and its current time
    st.write(f"**{tz}**: {current_time}")

# Create section for time conversion
st.subheader("Convert Time Between Time Zones")

# Create time input field with current time as default
current_time = st.time_input("Convert TIme", value=datetime.now().time())

# Dropdown to select source timezone
from_tz = st.selectbox("From Time Zones", Time_Zones, index=0)

# Dropdown to select target timezone
to_tz = st.selectbox("To Time Zones", Time_Zones, index=1)

# Create convert button and handle conversion
if st.button("Convert Time Zones"):

    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))

    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

    # Display the converted time with success message
    st.success(f"Converted Time {to_tz}: {converted_time}")





