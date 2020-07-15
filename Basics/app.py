import streamlit as st

# Text/Title
st.title("Streamlit tutorial")

# Header/Subheader
st.header("This is a header")
st.subheader("Ths is a subheader")

# Text
st.text("Hello Streamlit")

# markdown
st.markdown("### This is a Markdown")

# Error/Colorful Text
st.success("Successful")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error")
st.exception("NameError('name three not defined')")

# Get Help/Info about Python
st.help(range)

# Writing text SUPER FUNCTION
st.write("--Text--")
st.write(range(0,10))

# Images
from PIL import Image
img = Image.open("avengers.jpg")
st.image(img, width=500, caption="Infinity War")

# Videos
vid_file = open("pes.mp4","rb").read()
st.video(vid_file)

# Audio
audio_file = open("james.mp3","rb").read()
st.audio(audio_file,format='audio/mp3')

# Widget

# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio button
status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success("You are active")

else:
    st.warning("Inactive, Activate")

# Select Box
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Doctor", "Businessman"])
st.write("You selected this option ", occupation)

# MultiSelect
location = st.multiselect("Where do you work?",("London","New York", "Melbourne","Berlin"))
st.write("You selected ", len(location), "locations")

# Slider
level = st.slider("What is your level",1,5)

# Button
st.button("Simple Button")

if st.button("About"):
    st.text("Streamlit is cool")

# Text Input
firstname = st.text_input("Enter Your FirstName","Type Here...")
if st.button("Submit"):
    result = firstname.title()
    st.success(result)

# Text Area
msg = st.text_area("Enter Your message","Type Here...")
if st.button("Submit",key="s2"):
    result = msg.title()
    st.success(result)

# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time
time = st.time_input("The time is",datetime.time())

# Displaying JSON
st.text("Display JSON")
st.json({'name':"Manan", 'gender' : 'male'})

# Display raw code

## method 1
st.text("Display Raw Code : Method 1")
st.code("import numpy as np")

## method 2
st.text("Display Raw Code : Method 2")
with st.echo():
    # This will also show the comments
    import pandas as pd
    df = pd.DataFrame()

# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting.."):
    time.sleep(5)
st.success("Finished !!")

# Balloons
st.balloons()

# SIDEBARS
st.sidebar.header("About")

st.sidebar.text("This is Streamlit Tutorial")

# Functions

@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())

# Plots
st.pyplot()

# Data Frames
st.DataFrame(df)

# Tables
st.table(df)