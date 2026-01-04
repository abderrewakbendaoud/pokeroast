import warnings
import json
import google.generativeai as genai
from google.api_core import exceptions
from .config import get_api_key, get_model_candidates

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

genai.configure(api_key=get_api_key())

def generate_roast_data(team_list: list[str], game_context: str = "General Pokemon") -> dict:
    """
    Returns a dict: {'roast': str, 'worst_pokemon': str}
    Now aware of the game version!
    """
    candidates = get_model_candidates()
    
    # CONTEXTUAL PROMPT
    prompt = f"""
    You are a competitive Pokemon veteran. 
    The user is playing: **{game_context}**.
    
    Analyze this team: {', '.join(team_list)}.

    Your Goal:
    1. Roast them based on the specific meta/bosses of {game_context}.
       - If they are playing Emerald, mention Wattson or the Battle Frontier.
       - If Platinum, mention Cynthia's Garchomp or the Distortion World.
       - If Scarlet/Violet, mention Tera Raids or Area Zero.
    2. Be toxic but accurate.
    
    Return ONLY JSON:
    {{
        "roast": "Your mean paragraph here...",
        "worst_pokemon": "ExactNameFromList"
    }}
    """
    
    for model_name in candidates:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            text = response.text.replace("```json", "").replace("```", "").strip()
            return json.loads(text)
        except:
            continue

    return {"roast": "AI Failure. Your team broke the matrix.", "worst_pokemon": team_list[0]}