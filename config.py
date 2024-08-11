import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_KEY')
DATABASE_NAME = 'mental_health.db'
AI_MODEL = "llama3-70b-8192"