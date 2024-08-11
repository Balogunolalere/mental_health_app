import groq
from config import GROQ_API_KEY, AI_MODEL
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = groq.Groq(api_key=GROQ_API_KEY)

def get_ai_response(user_input, system_prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            model=AI_MODEL,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=True,
        )
        ai_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                ai_response += chunk.choices[0].delta.content
        return ai_response
    except Exception as e:
        logger.error(f"Error in AI response: {e}")
        return "I apologize, but I'm unable to provide a response at the moment. Please try again later."

def get_chat_analysis(user_messages):
    prompts = [
        "Analyze the user's mental health based on their previous chats. Provide a concise report (50-150 words) with key points [Observations, Potential Issues, Recommendations]. Use professional language and avoid mentioning specific mental health conditions or making diagnoses.",
        "On a scale of 1 to 10, where 1 represents optimal mental well-being and 10 indicates significant challenges, provide a numerical assessment of the user's mental health based on their previous chats. Respond with only the numerical score.",
        "Extract 5-10 keywords from the user's previous chats that may indicate areas of focus for mental well-being. List the keywords separated by commas."
    ]
    
    responses = []
    for prompt in prompts:
        response = get_ai_response(user_messages, prompt)
        responses.append(response)
    
    return responses