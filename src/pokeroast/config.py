import os
import sys
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        print("❌ CRITICAL ERROR: GEMINI_API_KEY not found.")
        sys.exit(1)
    return key

def get_model_candidates():
    # Read string from env, split by comma, strip spaces
    models_str = os.getenv("GEMINI_MODELS", "models/gemini-1.5-flash")
    return [m.strip() for m in models_str.split(',') if m.strip()]