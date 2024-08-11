import plotly.graph_objs as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import timedelta

def create_line_plot(df, title, x_col, y_cols):
    fig = go.Figure()
    for col in y_cols:
        fig.add_trace(go.Scatter(x=df[x_col], y=df[col], mode='lines', name=col))
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Score",
        xaxis_tickformat="%Y-%m-%d",
        xaxis_range=[df[x_col].min(), df[x_col].max() + timedelta(days=1)]
    )
    return fig

def create_radar_chart(df, categories):
    scores = [df[category].mean() for category in categories]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=categories,
        fill='toself',
        name="Mental Health Scores"
    ))
    fig.update_layout(
        title="Average Mental Health Scores by Category",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )
        )
    )
    return fig

def create_word_cloud(df):
    if df["Notes"].notna().any():
        words = ' '.join(df["Notes"].dropna())
        wordcloud = WordCloud(width=800, height=800,
                              background_color='white',
                              stopwords=None,
                              min_font_size=10).generate(words)
        fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
        ax.imshow(wordcloud)
        ax.axis("off")
        plt.tight_layout(pad=0)
        return fig
    return None