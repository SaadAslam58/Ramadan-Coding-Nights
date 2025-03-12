import random
import time
import streamlit as st

# Created a list and inside that list we have created a dictionary
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
]


# Use markdown to create a styled title with an icon
st.markdown("<h1 style='text-align: center;'><i class='fas fa-question-circle'></i>📝 Welcome to Quiz App</h1>", unsafe_allow_html=True)

# Initialize a random question if none exists in the session state. We use session_state for storing and reusing variables, similar to useState() in React. By utilizing session_state, our inputs are stored in the web browser, allowing us to access them easily without causing a rerender of the app.
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# get the current question stored in the session_state 
question = st.session_state.current_question


# Displaying the question to the use in form of subheader
st.subheader(question["question"])

#Displaying the options to the user stored in sesssion state for 
selected_options = st.radio("Select one of the following options", question["options"], key="answer")


# Displaying a submit button to check the answer and rerun the app with a new question if submitted.
if st.button("Submit Answer"):
    if selected_options == question["answer"]:
        st.success(question["answer"] + " Is the correct answer!")
        st.balloons()
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])

    time.sleep(3)

    st.session_state.current_question = random.choice(questions)

    st.rerun()

st.write(f"----")

st.write(f"🔗 Built By [Saad Aslam](https://github.com/SaadAslam58)")
