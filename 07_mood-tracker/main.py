import pandas as pd # Pandas are used for accessing file paths and for chnging there data and for saving data in files
import datetime 
import streamlit as st
import csv
import os # If wanted to read, write something on system lvl, you have to use os module

# Created a variable 
MOOD_FILE = 'mood_logs.csv'

# Function for loading data from csv file
def load_mood_data():

    # Checked if the pasth exist or not
    if not os.path.exists(MOOD_FILE):

        # If not exist create it using pandas dataframe class   
        return pd.DataFrame(columns=["Date","Mood"])
    
    # Reads & return the existing mood data  
    return pd.read_csv(MOOD_FILE)

# Function for saving mood data into csv file
def save_mood_data(date, mood):

    # Opens the mood_logs.csv in append mode, 'a' in python means append mode
    with open(MOOD_FILE, "a") as file:

        # writer object will help to write data into csv file
        writer = csv.writer(file)

        # writerow method will write the data into csv file in the form of list
        writer.writerow([date, mood])

# Streamlit app
st.title("I'm a Mood Tracker🫡")

# Get current date and time
date = datetime.date.today()

st.subheader("How are you feeling today?🤔")

# Selectbox method will let user select their mood from the given options eg: list of moods.
mood = st.selectbox("Select Your Mood", ["Happy", "Sad", "Neutral", "Angry", "Stressed"])

# Button will log the mood when clicked by user. If button is clicked, it will call save_mood_data function and display success message.
if st.button("Log Mood"):
    
    # Calling the save_mood_data function to log the mood data into csv file.
    save_mood_data(date,mood)

    # Display success message after logging the mood data.
    st.success("Mood Logged Successfully")

# store the lood_mood_data in a variable for further calling purposes
save_mood = load_mood_data()

# If save_mood dataframe is not empty, it means user has logged moods before.
if not save_mood.empty:

    st.subheader("Your Mood Logs")

    # Converting string to object using to_datetime function, Reason python is a object oriented language and requires object for most cases like for the bar_chart that we have created required a object
    save_mood["Date"] = pd.to_datetime(save_mood["Date"])
    
    # groupby method checks the frequency on which date user mood was happy, sad etc
    # count method counts the number of times each mood was logged 
    mood_count = save_mood.groupby("Mood").count()["Date"]

    # Bar chart will display the number times each mood was selected and days 
    st.bar_chart(mood_count)

    st.write("----")
    st.subheader(f"🔗 Built By [Saad Aslam](https://github.com/SaadAslam58)")