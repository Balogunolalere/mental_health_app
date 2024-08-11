# Mental Health Management App

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [Testing](#testing)
8. [Project Structure](#project-structure)
9. [Usage Guide](#usage-guide)
10. [Contributing](#contributing)
11. [License](#license)

## Introduction

The Mental Health Management App is a comprehensive tool designed to help users track, visualize, and improve their mental well-being. This application provides a user-friendly interface for daily mood logging, data visualization, and AI-powered chat support for mental health-related queries.

## Features

- **Daily Log**: Record daily mental health metrics including mood, serenity, sleep quality, productivity, and enjoyment.
- **Data Visualization**: View trends and patterns in your mental health data through interactive charts and graphs.
- **AI Chat Support**: Engage with an AI-powered chatbot for mental health guidance and support.
- **Chat History**: Review past conversations with the AI chatbot.
- **Data Analysis**: Get insights into your mental health patterns based on your chat history and daily logs.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7+
- pip (Python package manager)
- A Groq API key for AI chat functionality

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Balogunolalere/mental_health_app.git
   cd mental_health_app
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your Groq API key to the `.env` file:
   ```
   GROQ_KEY=your_groq_api_key_here
   ```

## Running the Application

To run the Streamlit app, use the following command from the project root directory:

```
streamlit run app/main.py
```

The application will start, and you can access it through your web browser at `http://localhost:8501`.

## Testing

To run the test suite, use the following command from the project root directory:

```
pytest tests/
```

## Project Structure

```
mental_health_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── ai_chat.py
│   ├── data_visualization.py
│   ├── daily_log.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_database.py
│   ├── test_ai_chat.py
│   └── test_data_visualization.py
├── config.py
├── requirements.txt
├── README.md
└── .env
```

## Usage Guide

1. **Home Page**: Provides an overview of the app and links to recent mental health articles.

2. **Daily Log**: 
   - Select a date
   - Use sliders to rate your mood, serenity, sleep quality, productivity, and enjoyment
   - Add notes about your day
   - Click "Submit" to save your entry

3. **Visualize Data**:
   - View your mental health data in table format
   - Explore line charts showing trends over time
   - Check out the radar chart for average scores by category
   - See a word cloud generated from your daily notes

4. **Chat with AI**:
   - Type your mental health-related questions or concerns
   - Receive responses from the AI chatbot
   - Continue the conversation as needed

5. **Chat History**:
   - Review past conversations with the AI
   - Analyze your chat history for insights into your mental health patterns

## Contributing

Contributions to the Mental Health Management App are welcome. Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/Feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some Feature'`)
5. Push to the branch (`git push origin feature/Feature`)
6. Open a Pull Request


For any additional questions or support, please open an issue in the GitHub repository.