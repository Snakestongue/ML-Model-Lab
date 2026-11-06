import streamlit as st
st.title ("Hello World") #large title
st.write("Welcome!") #numbers & data or test
st.header("About this project!") #small title
st.text("This is where my project will go!") # normal text
st.success("Woop") # green text + green background
st.error("oops")# red text + red background

# a textbox for number input
number_inp = st.number_input(
    "Area calculator",
    min_value = 1, #min
    max_value = 100000, #max
    value=1781 #text displayed before input
)

#same but a slider
sliders = st.slider(
    "Perimiter calculator",
    min_value=1,
    max_value=10000,
    value=1481
)

text_inp = st.text_input("Enter your name")

selects = st.selectbox(
    "Choose subjects",
    ["Math", "Science", "history"]
)

if st.button("Click"):
    st.write("You clickeed the button.")

c1 = st.checkbox("Hi 1")
c2 = st.checkbox("Hi 2")

st.write("C1:", c1)#true or false
st.write("C2:", c2)
st.write("You chose:", selects)
st.write("Area:", number_inp, "sq ft")
st.write("Bedrooms:", sliders)
st.write("Hello:", text_inp)