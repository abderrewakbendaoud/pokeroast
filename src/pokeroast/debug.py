import google.generativeai as genai
from .config import get_api_key

def check_models():
    key = get_api_key()
    print(f"🔑 API Key loaded: {key[:5]}...{key[-3:]}") # Prints start/end to verify it's not empty
    
    genai.configure(api_key=key)

    print("\n📡 CONTACTING GOOGLE SERVERS TO LIST MODELS...")
    try:
        # We ask for ALL models, not just generative ones
        for m in genai.list_models():
            # filter for models that can actually generate text
            if 'generateContent' in m.supported_generation_methods:
                print(f"✅ AVAILABLE: {m.name}")
            else:
                print(f"❌ (Not for text): {m.name}")
                
    except Exception as e:
        print(f"\n💀 FATAL ERROR CONNECTING TO API: {e}")

if __name__ == "__main__":
    check_models()