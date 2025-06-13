# ml_model/gpt_module.py
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual key

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return "Sorry, I couldn't connect to OpenAI."
