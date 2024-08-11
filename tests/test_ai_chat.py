import pytest
from unittest.mock import patch
from app.ai_chat import get_ai_response, get_chat_analysis

@pytest.fixture
def mock_groq_response():
    class MockResponse:
        def __init__(self, content):
            self.choices = [type('obj', (object,), {'delta': type('obj', (object,), {'content': content})()})]

    return MockResponse

@patch('app.ai_chat.client.chat.completions.create')
def test_get_ai_response(mock_create, mock_groq_response):
    mock_create.return_value = [mock_groq_response("Test response")]
    response = get_ai_response("Test input", "Test prompt")
    assert response == "Test response"
    mock_create.assert_called_once()

@patch('app.ai_chat.get_ai_response')
def test_get_chat_analysis(mock_get_ai_response):
    mock_get_ai_response.side_effect = ["Analysis report", "5", "keyword1, keyword2"]
    analysis = get_chat_analysis("Test user messages")
    assert len(analysis) == 3
    assert analysis[0] == "Analysis report"
    assert analysis[1] == "5"
    assert analysis[2] == "keyword1, keyword2"
    assert mock_get_ai_response.call_count == 3