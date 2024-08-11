import streamlit as st

def render_home_page():
    st.title("Mental Health Management App")
    st.write("Welcome to our Mental Health Management App! Here, you can track your daily mental health scores across various categories. Additionally, you can visualize your data and chat with our AI consultant for personalized guidance and recommendations.")

    st.subheader("Recent Articles on Mental Health")
    st.markdown("""
    <style>
    .article-link {
        color: blue;
        text-decoration: underline;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

    articles = [
        {"title": "How to Cope With Anxiety and Stress", "link": "https://www.healthline.com/nutrition/16-ways-relieve-stress-anxiety"},
        {"title": "Depression: What It Is, Symptoms, Causes, Treatment and Self-Help", "link": "https://www.healthline.com/health/depression"},
        {"title": "Building Better Mental Health", "link": "https://www.helpguide.org/articles/mental-health/building-better-mental-health.htm"},
        {"title": "Improving Mental Health During the Pandemic", "link": "https://www.mayoclinic.org/diseases-conditions/coronavirus/in-depth/mental-health-covid-19/art-20482731"},
        {"title": "Mindfulness for Mental Health", "link": "https://www.healthline.com/health/mental-health/how-to-cope-with-anxiety"},
        {"title": "The Mental Health Benefits of Exercise", "link": "https://www.helpguide.org/articles/healthy-living/the-mental-health-benefits-of-exercise.htm"},
        {"title": "How to Practice Self-Compassion", "link": "https://positivepsychology.com/how-to-practice-self-compassion/"},
        {"title": "The Power of Gratitude in Combating Anxiety and Depression", "link": "https://adaa.org/learn-from-us/from-the-experts/blog-posts/consumer/gratitude-mental-health-game-changer"},
        {"title": "The Importance of Sleep for Mental Health", "link": "https://www.sleepfoundation.org/mental-health"},
        {"title": "Building Resilience: How to Move Forward After Hardship", "link": "https://www.apa.org/topics/resilience/building-your-resilience"}
    ]

    for article in articles:
        st.markdown(f"<a href='{article['link']}' target='_blank' class='article-link'>{article['title']}</a>", unsafe_allow_html=True)

def set_page_style():
    st.markdown("""<style>
    .user-bubble {
        background-color: #0084ff;
        color: white;
        padding: 10px;
        border-radius: 15px;
        margin-right: 50px;
        margin-bottom: 10px;
        display: inline-block;
        clear: both;
    }

    .ai-bubble {
        background-color: #f1f1f1;
        color: black;
        padding: 10px;
        border-radius: 15px;
        margin-left: 50px;
        margin-bottom: 10px;
        display: inline-block;
        clear: both;
    }
    </style>""", unsafe_allow_html=True)