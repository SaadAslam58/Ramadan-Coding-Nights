import streamlit as st
import requests
from fastapi import FastAPI
import random

app = FastAPI()

# Define a list of jokes under a single category "exam"
pakistani_jokes = [
    {
        "category": "exam",
        "joke": "Teacher: 'What do you want to be when you grow up?'\nStudent: 'Tension-free.'"
    },
    {
        "category": "exam",
        "joke": "Q: Why did the student bring a ladder to school?\nA: Because they wanted to go to high school!"
    },
    {
        "category": "exam",
        "joke": "Q: Why did the math book look sad?\nA: Because it had too many problems."
    }
]

@app.get("/pakistani_jokes")
def pak_jokes():
    joke = random.choice(pakistani_jokes)
    return {"category": joke["category"], "joke": joke["joke"]}
    


def fetch_random_joke():
    try:
        responce = requests.get("http://127.0.0.1:8000/docs#/default/pak_jokes_pakistani_jokes_get")
        if responce.status_code == 200:
            data = responce.json()
            return f"{data['setup']} \n\n {data['punchline']}"
        else:
            return "Failed to fetch joke. Please try again."
    except:
        return "Failed to fetch API."
    
def main():
    st.title("Random Joke Generator")
    st.subheader("Click the button below to generate a random joke.")

    if st.button("Generate Joke"):
        joke = fetch_random_joke()
        st.success(joke)

if __name__ == "__main__":
    main()