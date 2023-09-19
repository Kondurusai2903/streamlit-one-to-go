import streamlit as st
st.title("Hello Streamlit")
st.header("hi streamlit, I am new bie")
st.subheader("subheader- streamlit")
st.text("hello , I am sai konduru")

st.markdown("#hi")
st.markdown("##hi")
st.markdown("###hi")
st.markdown("####hi")
st.markdown("#####hi")

st.success("I am going to be a data scientist")

st.info("For that I want to work hard")

st.warning("Don't be inactive or overconfident")

st.error("Error!")
exp=ZeroDivisionError("Division is not possible with zero")
st.exception(exp)
st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))
st.write("1+2+3","=",1+2+3)

st.write("1*2*3","=",1*2*3)

st.code('i=10\n'
        'for i in range(i):\n'
        '\tprint(i)')
st.subheader("select the programming languages")
st.checkbox("python")
st.checkbox("C++")
st.subheader("select:")
radiobutton=st.radio("select",("male","female","others"))
if radiobutton=="male":
    st.write("you're a male")
elif radiobutton=="female":
    st.write("you're a female")
elif radiobutton=="others":
    st.write("you're a others ")

st.subheader("select Box")
selectbox=st.selectbox("Data Science:",["Data Analysis","Web Scraping","Machince learning","Computer Vision"])

st.write("you are selected",selectbox)

st.subheader("Button")
button=st.button("Click Me")
if button:
    st.write("you have click the button")

st.subheader("Slider")
slider=st.slider("select the volume",1,100)
if slider:
    st.write("your valume is",slider)
#-------------------------------taking the user input-------------------------------------------
st.subheader("Text input")
name=st.text_input("Enter your Name:")
if name:
    st.write("Hi ", name)
#-------------------------------taking the user input-------------------------------------------
st.text_input("Enter your password:",type="password")
#-------------------------------taking the number_input-------------------------------------------
st.subheader("Number input")
number=st.number_input("select your age",18,110)
st.write("your's age is",number)
#-------------------------------taking the Date_input-------------------------------------------
st.subheader("Date Input")
st.date_input("Date")

st.subheader("time Input")
st.time_input("Date")
