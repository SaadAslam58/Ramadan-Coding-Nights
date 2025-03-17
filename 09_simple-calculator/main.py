import streamlit as st

st.title("Simple Calculator 📱")
def main():

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter a number 🔢", value=0.00, format="%.2f", help="Input your first number")    
    with col2:
        num2 = st.number_input("Enter another number 🔢", value=0.00, help="Input your second number")

    operation = st.selectbox("Choose a operation",["Addition (➕)", "Subtraction (➖)", "Division (➗)", 
                            "Multiplication (✖️)"], help="Choose an operation to perform")
    if st.button("Perform"):
        try:
            if operation == "Addition (➕)":
                result = num1 + num2
                symbol =  "+"
            elif operation == "Subtraction (➖)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (✖️)":
                result = num1 * num2
                symbol = "x"
            else:
                if num2 == 0:
                    st.error("Cannot divide any value by zero!")
                    return
                    
                result = num1 / num2
                symbol = "/"

            st.success(f"{num1} {symbol} {num2} = {result}")

        except Exception as e:
            st.error(F"An error occured {e}")

if __name__ == "__main__":
    main()
        
st.write(f"----")

st.write(f"🔗 Built By [Saad Aslam](https://github.com/SaadAslam58)")