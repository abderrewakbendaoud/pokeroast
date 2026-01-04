import requests
import streamlit as st
import json
import os
import random

SHAME_FILE = "hall_of_shame.json"

# --- GAME VERSION MAPPING ---
GAME_DEX_MAP = {
    "Red/Blue/Yellow": 2,       # Kanto
    "Gold/Silver/Crystal": 3,   # Johto
    "Ruby/Sapphire/Emerald": 4, # Hoenn
    "Diamond/Pearl/Platinum": 5,# Sinnoh
    "Black/White": 8,           # Unova
    "X/Y": 12,                  # Kalos
    "Sun/Moon": 16,             # Alola
    "Sword/Shield": 27,         # Galar
    "Scarlet/Violet": 31,       # Paldea
    "National Dex (All)": 1     # No limits
}

@st.cache_data(ttl=3600, show_spinner=False)
def get_all_pokemon_names():
    """Fetches ALL pokemon names (Fallback for National Dex)."""
    url = "https://pokeapi.co/api/v2/pokemon?limit=2000"
    try:
        response = requests.get(url)
        return [p['name'] for p in response.json()['results']]
    except:
        return []

@st.cache_data(ttl=3600, show_spinner=False)
def get_pokemon_by_game(game_name):
    """Fetches ONLY pokemon available in the selected game."""
    pokedex_id = GAME_DEX_MAP.get(game_name, 1)
    
    # If National Dex, just return everything
    if pokedex_id == 1:
        return get_all_pokemon_names()
    
    url = f"https://pokeapi.co/api/v2/pokedex/{pokedex_id}"
    try:
        data = requests.get(url).json()
        # Extract names from the pokedex entries
        valid_names = [entry['pokemon_species']['name'] for entry in data['pokemon_entries']]
        return valid_names
    except:
        return []

@st.cache_data(ttl=3600, show_spinner=False)
def get_pokemon_details(name):
    if not name: return None
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            data = response.json()
            return {
                "sprite": (data['sprites']['other']['showdown']['front_default'] or 
                           data['sprites']['other']['official-artwork']['front_default'] or 
                           data['sprites']['front_default']),
                "stats": {i['stat']['name']: i['base_stat'] for i in data['stats']},
                "types": [t['type']['name'] for t in data['types']],
                "cry": data.get('cries', {}).get('latest', None)
            }
    except:
        return None
    return None

@st.cache_data(ttl=3600*24)
def get_type_matchups():
    """Fetches the damage relations for all 18 types."""
    type_chart = {}
    all_types = ["normal", "fire", "water", "grass", "electric", "ice", "fighting", "poison", "ground", 
                 "flying", "psychic", "bug", "rock", "ghost", "dragon", "steel", "dark", "fairy"]
    
    for t in all_types:
        try:
            url = f"https://pokeapi.co/api/v2/type/{t}"
            data = requests.get(url).json()
            relations = data['damage_relations']
            
            multipliers = {at: 1.0 for at in all_types}
            for mod in relations['double_damage_from']: multipliers[mod['name']] = 2.0
            for mod in relations['half_damage_from']: multipliers[mod['name']] = 0.5
            for mod in relations['no_damage_from']: multipliers[mod['name']] = 0.0
            
            type_chart[t] = multipliers
        except: pass
    return type_chart

@st.cache_data(ttl=3600, show_spinner=False)
def get_counter_pokemon(threat_type, valid_pokemon_list):
    """
    Finds a Pokemon that resists the threat_type AND exists in the current game.
    """
    try:
        # 1. Ask API: Who resists this threat?
        url = f"https://pokeapi.co/api/v2/type/{threat_type.lower()}"
        data = requests.get(url).json()
        
        relations = data['damage_relations']
        resisting_types = [t['name'] for t in relations['half_damage_to']] + \
                          [t['name'] for t in relations['no_damage_to']]
        
        if not resisting_types: return "Bidoof" 

        # 2. Pick a random resisting type
        chosen_type = random.choice(resisting_types)
        
        type_url = f"https://pokeapi.co/api/v2/type/{chosen_type}"
        type_data = requests.get(type_url).json()
        
        # 3. Get all pokemon of that type
        type_roster = [p['pokemon']['name'] for p in type_data['pokemon']]
        
        # 4. INTERSECTION: Only keep ones that are in the user's game
        # If valid_pokemon_list is huge (National Dex), set intersection is fast.
        hirable = list(set(type_roster) & set(valid_pokemon_list))
        
        if hirable:
            return random.choice(hirable)
            
    except:
        return "Ditto"
    
    return "Magikarp" # Fallback

# --- HISTORY UTILS ---
def save_shame_entry(team, roast_data):
    entry = {
        "team": team,
        "roast": roast_data.get("roast", ""),
        "worst_pokemon": roast_data.get("worst_pokemon", "")
    }
    history = load_shame_history()
    history.insert(0, entry)
    history = history[:50]
    with open(SHAME_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_shame_history():
    if not os.path.exists(SHAME_FILE): return []
    try:
        with open(SHAME_FILE, "r") as f: return json.load(f)
    except: return []