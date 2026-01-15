
# SYSTEM_PROMPT = """
# You are an assistant that extracts structured meeting booking information.

# Rules:
# - Output ONLY valid JSON
# - Do not explain anything
# - Do not guess missing values
# - If information is missing, set the field to null
# - Dates must be in YYYY-MM-DD
# - Times must be in 24-hour HH:MM format
# - Participants must be a list of lowercase names

# Supported intents:
# - book_offline_meeting
# - book_online_meeting
# """
import json
import ollama

SYSTEM_PROMPT = """
You are an assistant that classifies meeting booking intent.

Output ONLY valid JSON.

Possible intents:
- book_offline_meeting
- book_online_meeting
- unknown

Do not extract dates, times, room names, or participants.
Only classify intent.
"""

def call_llm(message: str) -> dict:
    try:
        response = ollama.chat(
            model="phi3:mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ]
        )

        return json.loads(response["message"]["content"])

    except Exception as e:
        print("LOCAL LLM FAILED:", e)
        return { "intent": "unknown" }
