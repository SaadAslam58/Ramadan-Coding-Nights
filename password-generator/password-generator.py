import streamlit as st
import random 
import string


def generate_password(Length, use_digits, use_special):
    characters = string.ascii_letters # It will ad alphabets from (a-z, A-Z) capitle and small both 

    if use_digits:
        characters += string.digits # If selected string.digit will add number from 0-9
    
    if use_special:
        characters += string.punctuation # If selected string.punction add special characters (!,@,#,$ etc.)
    
    return ''.join(random.choice(characters) for _ in range(Length)) 
# .join method join the empty string and,
#  then we are using random function that will allow user to choice random characters
#  it is providing random characters for character variable that we have defined
# _ is specifically telling python that the length is not defined
def password_strength(password):
    length = len(password)


    has_upper_case = any(char in string.ascii_uppercase for char in password)
    has_lower_case = any(char in string.ascii_lowercase for char in password)
    has_special_char = any(char in string.punctuation for char in password)
    has_number = any(char in string.digits for char in password)

    score = sum([has_upper_case,has_lower_case,has_special_char,has_number])

    if length < 7:
        return "Weak", "🔴", "Password too short try! Use at least 7 characters"
    elif score == 2:
        return "Moderate", "🟡", "Try adding digits or special characters"
    elif score == 3:
        return "Strong", "🟢", "Great! Your password is strong"
    elif score >= 4:
        return "Very Strong", "🟢", "Great! Your password is strong"



st.title("🔑 Password Generator")



# We are crating a variable for length 
length = st.slider("Select Password Length", min_value=4, max_value=20, value=12)
# min_value is a parameter by using min_value = 6 we are passing it a argument 
# value is used for defining where will the sidebar starts from

# We are crating a variable for use_digits if user selects it he/she have to include the values 
use_digits = st.checkbox("Include Digits 🔢")
# When the user click on this checkbox the variable that we have defined user_digits will sent a value to use_digits parameter that we have defined in the function

use_special = st.checkbox("Include Special Characters 🛡️")
# Same thing goes with use_special


# A question goes in mind how does the streamlit UI know that it has to include special characters or digits?
# Ans: The parameters that we have passed are being used in the variable because the name of both the values is same so the value will be stored in the parameter that we will use later to display


if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)

    strength, color, feedback = password_strength(password)

    st.title(f"Strength {strength} {color}")
    st.success(f"Generated Password: {password}")
    st.write(f"Password strength: {strength} {color}, feedback: {feedback}")


st.write(f"----")

st.write(f"🔗 Built By [Saad Aslam](https://github.com/SaadAslam58)")

