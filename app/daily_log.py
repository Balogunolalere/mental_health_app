import streamlit as st
from database import insert_daily_log

def render_daily_log_page():
    st.title("Daily Log")
    date = st.date_input("Date")
    mood = st.slider("Mood", 0.0, 10.0, 5.0, 0.1)
    serenity = st.slider("Serenity", 0.0, 10.0, 5.0, 0.1)
    sleep = st.slider("Sleep", 0.0, 10.0, 5.0, 0.1)
    productivity = st.slider("Productivity", 0.0, 10.0, 5.0, 0.1)
    enjoyment = st.slider("Enjoyment", 0.0, 10.0, 5.0, 0.1)
    notes = st.text_area("Notes")

    if st.button("Submit"):
        insert_daily_log(date, mood, serenity, sleep, productivity, enjoyment, notes)
        st.success("Entry submitted successfully!")