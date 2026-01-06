import warnings
import json
import google.generativeai as genai
import streamlit as st
from .config import get_api_key, get_model_candidates

warnings.filterwarnings("ignore")

# Configure GenAI immediately with the retrieved key
genai.configure(api_key=get_api_key())

def generate_roast_data(team_list: list[str], game_context: str = "General Pokemon") -> dict:
    # Load models dynamically from config
    candidates = get_model_candidates()
    
    prompt = f"""
    You are a competitive Pokemon veteran. The user is playing: **{game_context}**.
    Analyze this team: {', '.join(team_list)}.
    Goal: Roast them based on the specific meta/bosses of {game_context}.
    Return ONLY JSON: {{ "roast": "...", "worst_pokemon": "..." }}
    """
    
    errors = []
    
    for model_name in candidates:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except Exception as e:
            # Logs for your dashboard
            print(f"⚠️ {model_name} Failed: {e}")
            errors.append(f"{model_name}: {e}")
            continue

    return {
        "roast": f"SYSTEM FAILURE. Logs: {' || '.join(errors)}",
        "worst_pokemon": "System Error"
    }