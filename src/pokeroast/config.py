import os
import streamlit as st
from dotenv import load_dotenv

# Load local .env (does nothing on cloud, essential for local)
load_dotenv()

def get_api_key():
    """
    Retrieves API Key from Local Env or Streamlit Secrets.
    """
    # 1. Try Local .env first
    key = os.getenv("GOOGLE_API_KEY")
    
    # 2. If not found locally, try Streamlit Secrets (Cloud)
    if not key:
        try:
            if "GOOGLE_API_KEY" in st.secrets:
                key = st.secrets["GOOGLE_API_KEY"]
        except FileNotFoundError:
            pass # We are local and no secrets.toml exists
        except Exception:
            pass

    # 3. Validation
    if not key:
        st.error("❌ CRITICAL: GOOGLE_API_KEY not found in .env or Secrets.")
        st.stop()
        
    return key

def get_model_candidates():
    """
    Retrieves the comma-separated list of models from Env/Secrets.
    """
    # 1. Try Local .env
    models_str = os.getenv("GEMINI_MODELS")
    
    # 2. Try Streamlit Secrets
    if not models_str:
        try:
            if "GEMINI_MODELS" in st.secrets:
                models_str = st.secrets["GEMINI_MODELS"]
        except:
            pass
            
    # 3. Parse string into list
    if models_str:
        # Split by comma, strip whitespace, remove empty strings
        candidates = [m.strip() for m in models_str.split(',') if m.strip()]
        
        clean_list = []
        for m in candidates:
            if m.startswith("models/"):
                clean_list.append(m.replace("models/", ""))
            else:
                clean_list.append(m)
        return clean_list
    
    # 4. Emergency Fallback (Only if variable is totally missing)
    st.warning("⚠️ variable GEMINI_MODELS is missing. Using default fallback.")
    return ["gemini-2.0-flash"]