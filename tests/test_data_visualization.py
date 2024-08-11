import pytest
import pandas as pd
from app.data_visualization import create_line_plot, create_radar_chart, create_word_cloud

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=5),
        'Mood': [7, 6, 8, 7, 9],
        'Serenity': [6, 7, 7, 8, 8],
        'Sleep': [8, 7, 9, 8, 9],
        'Productivity': [7, 8, 8, 9, 9],
        'Enjoyment': [8, 7, 9, 8, 10],
        'Notes': ['Good day', 'Feeling stressed', 'Relaxed', 'Productive', 'Great day']
    })

def test_create_line_plot(sample_df):
    fig = create_line_plot(sample_df, "Test Plot", "Date", ["Mood", "Serenity"])
    assert fig.layout.title.text == "Test Plot"
    assert len(fig.data) == 2
    assert fig.data[0].name == "Mood"
    assert fig.data[1].name == "Serenity"

def test_create_radar_chart(sample_df):
    categories = ["Mood", "Serenity", "Sleep", "Productivity", "Enjoyment"]
    fig = create_radar_chart(sample_df, categories)
    assert fig.layout.title.text == "Average Mental Health Scores by Category"
    assert len(fig.data) == 1
    assert fig.data[0].theta == categories

def test_create_word_cloud(sample_df):
    fig = create_word_cloud(sample_df)
    assert fig is not None
    assert fig.get_size() == (800, 800)

def test_create_word_cloud_empty_notes():
    empty_df = pd.DataFrame({'Notes': []})
    fig = create_word_cloud(empty_df)
    assert fig is None