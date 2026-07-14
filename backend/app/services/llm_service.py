import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_with_llm(message):

    prompt = f"""
You are a cybersecurity expert.

Analyze the following message.

Message:
{message}

Return:
1. Whether it is phishing.
2. Explain why.
3. Give safety advice.

Keep your answer under 120 words.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini Error: {str(e)}"