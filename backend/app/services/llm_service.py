import os
import json

from dotenv import load_dotenv
from google import genai

from rag.retriever import retrieve_context
from rag.prompts import build_security_prompt

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_with_llm(message):

    try:
        # Retrieve relevant cybersecurity knowledge
        context, sources = retrieve_context(message)

        # Build prompt
        prompt = build_security_prompt(message, context)

        # Models to try (fallback if one is unavailable)
        models = [
            "gemini-3.5-flash",
            "gemini-3.1-flash-lite",
            "gemini-2.5-flash-lite"
        ]

        last_error = None

        for model_name in models:

            try:

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                text = response.text.strip()

                # Remove markdown code blocks if Gemini returns them
                if text.startswith("```json"):
                    text = text.replace("```json", "").replace("```", "").strip()

                elif text.startswith("```"):
                    text = text.replace("```", "").strip()

                # Convert JSON string into Python dictionary
                llm_result = json.loads(text)

                # Add matched knowledge files
                llm_result["matched_knowledge"] = sources

                return llm_result

            except Exception as e:
                print(f"{model_name} failed: {e}")
                last_error = str(e)

        # All Gemini models failed
        return {
            "attack_type": "Unknown",
            "risk_level": "UNKNOWN",
            "confidence": 0,
            "warning_signs": [],
            "recommended_actions": [],
            "explanation": f"Gemini unavailable: {last_error}",
            "matched_knowledge": sources
        }

    except Exception as e:

        return {
            "attack_type": "System Error",
            "risk_level": "UNKNOWN",
            "confidence": 0,
            "warning_signs": [],
            "recommended_actions": [],
            "explanation": str(e),
            "matched_knowledge": []
        }