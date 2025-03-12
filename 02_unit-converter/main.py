import streamlit as st



st.title("⭕Unit Converter")

category = st.selectbox("Select Category",["Length","Weight","Temperature"])

if category == "Length":
    unit = ["Meters", "Kilometers", "Feet", "Inches"]
elif category == "Weight":
    unit = ["Kilograms", "Pounds", "Grams", "Ounces"]
elif category == "Temperature":
    unit = ["Celsius", "Fahrenheit", "Kelvin"]

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From Units", unit)
with col2:
    to_unit = st.selectbox("To Units", unit)

value = st.number_input("Enter a value", min_value=0.0, format="%.2f")
st.write(f"Conversion {from_unit} to {to_unit}")


if st.button("Convert"):
    result = None

    conversion_factors = {
        "Meters": {"Kilometers": 0.001, "Feet": 3.28084, "Inches": 39.3701},
        "Kilometers": {"Meters": 1000, "Feet": 3280.84, "Inches": 39370.1},
        "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Inches": 12},
        "Inches": {"Meters": 0.0254, "Kilometers": 0.0000254, "Feet": 0.0833},
        "Kilograms": {"Grams": 1000, "Pounds": 2.20462},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462},
        "Pounds": {"Kilograms": 0.453592, "Grams": 453.592},
    }

    if category in ["Length", "Weight"]:
        if from_unit == to_unit:
            result = value
        else:
            result = value * conversion_factors[from_unit][to_unit]
    
    elif category == "Temperature":
        if from_unit == to_unit:
            result = value
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value * 5/9) - 32
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value * 5/9) -32 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = (value - 273.15)
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32 - 273.15



    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit} ")
        
st.markdown("""</div>""", unsafe_allow_html= True)
