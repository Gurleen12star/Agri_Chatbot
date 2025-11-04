import openai
import os

# Set your OpenAI API key here or as environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-your-key-here")

def get_bot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an agriculture expert helping farmers."},
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "⚠️ Error: Unable to connect to AI model. Check your API key."
