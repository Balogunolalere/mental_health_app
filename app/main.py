import streamlit as st
import pandas as pd
from database import init_db, get_all_daily_logs, get_chat_history, insert_chat_message, clear_chat_history, delete_all_data
from ai_chat import get_ai_response, get_chat_analysis
from data_visualization import create_line_plot, create_radar_chart, create_word_cloud
from daily_log import render_daily_log_page
from utils import render_home_page, set_page_style

def main():
    st.set_page_config(page_title="Mental Health Management App")
    init_db()
    set_page_style()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page", ["Home", "Daily Log", "Visualize Data", "Chat with AI", "Chat History"])

    if page == "Home":
        render_home_page()
    elif page == "Daily Log":
        render_daily_log_page()
    elif page == "Visualize Data":
        render_visualize_data_page()
    elif page == "Chat with AI":
        render_chat_with_ai_page()
    elif page == "Chat History":
        render_chat_history_page()

def render_visualize_data_page():
    st.title("Visualize Data")
    data = get_all_daily_logs()
    df = pd.DataFrame(data, columns=["id", "Date", "Mood", "Serenity", "Sleep", "Productivity", "Enjoyment", "Notes"])
    df["Date"] = pd.to_datetime(df["Date"])
    df["average"] = df[["Mood", "Serenity", "Sleep", "Productivity", "Enjoyment"]].mean(axis=1)

    st.subheader("Mental Health Data")
    st.write(df[["id", "Date", "Mood", "Serenity", "Sleep", "Productivity", "Enjoyment", "average", "Notes"]])

    if st.button("Delete all data"):
        delete_all_data()
        st.success("All data deleted successfully!")
        st.experimental_rerun()

    st.subheader("Mental Health Scores Over Time")
    fig = create_line_plot(df, "Mental Health Scores Over Time", "Date", ["Mood", "Serenity", "Sleep", "Productivity", "Enjoyment"])
    st.plotly_chart(fig)

    st.subheader("Average Mental Health Scores by Category")
    fig = create_radar_chart(df, ["Mood", "Serenity", "Sleep", "Productivity", "Enjoyment"])
    st.plotly_chart(fig)

    st.subheader("Average Mental Health Score Over Time")
    fig = create_line_plot(df, "Average Mental Health Score Over Time", "Date", ["average"])
    st.plotly_chart(fig)

    st.subheader("Word Cloud of Notes")
    fig = create_word_cloud(df)
    if fig:
        st.pyplot(fig)

def render_chat_with_ai_page():
    st.title("Chat with AI")
    
    chat_container = st.container()
    
    with chat_container:
        chat_history = get_chat_history()
        for row in chat_history:
            if row[1] == 'user':
                st.markdown(f"<div class='user-bubble'>{row[2]}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='ai-bubble'>{row[2]}</div>", unsafe_allow_html=True)

    with st.form(key='chat_form'):
        user_input = st.text_area("Enter your message")
        submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
            insert_chat_message("user", user_input)

            system_prompt = """You are a knowledgeable and compassionate AI advisor focused strictly on mental health and well-being. You are to engage with users in a caring and empathetic manner while offering guidance, suggestions, and information aimed solely at promoting positive mental health. This includes providing coping strategies, lifestyle recommendations, and support related exclusively to mental health issues such as stress, anxiety, depression, emotional regulation, and overall psychological well-being.
            You are designed solely to address queries that fall entirely within the narrow scope of mental health and wellness. If a user asks any question falling even partially outside of this extremely limited domain, which is beyond your intended strict capabilities, you are to politely but firmly decline to provide any information or assistance whatsoever, as that would be unrelated to mental health. You are not to offer to redirect them to any other resources or professionals, as that could still indirectly provide information beyond your strict mental health boundaries. Your primary and only purpose is to support users' mental well-being through compassionate yet utterly confined advice and relevant information strictly within the sole area of mental health expertise."""

            ai_response = get_ai_response(user_input, system_prompt)
            insert_chat_message("assistant", ai_response)

            # Update chat display
            with chat_container:
                st.markdown(f"<div class='user-bubble'>{user_input}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='ai-bubble'>{ai_response}</div>", unsafe_allow_html=True)

def render_chat_history_page():
    st.title("Chat History")
    chat_history = get_chat_history()
    chat_df = pd.DataFrame(chat_history, columns=["id", "role", "content"])
    st.write(chat_df)

    if st.button("Clear History"):
        clear_chat_history()
        st.success("Chat history cleared successfully!")
        st.experimental_rerun()

    if st.button("Analyze Chat History"):
        user_messages = ' '.join([message[2] for message in chat_history if message[1] == 'user'])
        analysis_results = get_chat_analysis(user_messages)
        
        st.subheader("Analysis Report")
        st.write(analysis_results[0])
        
        st.subheader("Mental Health Score")
        st.write(analysis_results[1])
        
        st.subheader("Key Topics")
        st.write(analysis_results[2])

if __name__ == "__main__":
    main()