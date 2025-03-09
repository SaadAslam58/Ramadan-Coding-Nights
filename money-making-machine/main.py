import streamlit as st
import random
import time 
import requests

amount = random.randint(1, 100)
tab1, tab2, tab3 = st.tabs(["💰 Tab1", "💼 Tab2", "🌟 Tab3"])
# Money Generator
with tab1:

    st.title("Free Ka Pesa 💵")
    st.write("Random amount will be generated for your withdrawals")

    if st.button('💸 Generate Money'):
        time.sleep(1)
        st.success(f"The amount is ${amount}")    

with tab2:
# Quote Generator
    st.title("Side Hustles 💡")
    st.write("Side hustles to improve your life financially.")
    def get_side_hustle():
        responce = requests.get('http://127.0.0.1:8000/side_hustles?apiKey=123456789')
        data = responce.json()
        return data["side_hustles"]

    side_hustle = get_side_hustle()

    if st.button('📝 Generate Quote'):
        time.sleep(1)
        st.info(f"Side Hustle: {side_hustle}")

# Money Quote Generator
with tab3:
    st.title("Motivational Quotes 🌈")
    st.write("Random motivational quotes will be generated for your life")
    def get_money_quotes():
        responce = requests.get('http://127.0.0.1:8000/money_quotes?apiKey=123456789')
        data = responce.json()
        return data["money_quotes"]

    money = get_money_quotes()

    if st.button("💬 Get money quotes"):
        time.sleep(1)
        st.info(f"Your quote: {money}")

st.write("----")
st.subheader(f"🔗 Built By [Saad Aslam](https://github.com/SaadAslam58)")
