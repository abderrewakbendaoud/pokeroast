# 🚀 Team Rocket's Tactical Analysis Terminal

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.41-FF4B4B?logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange?logo=google-gemini&logoColor=white)
![PokeAPI](https://img.shields.io/badge/Data-PokeAPI-yellow?logo=pokemon&logoColor=black)

A Pokemon Team Bullying Dashboard that uses GenAI and Data Science to mathematically prove why your team is failing.

**The Problem:** Competitive Pokemon players often build teams based on "vibes" rather than data, leading to undetected compound weaknesses and embarrassing losses.

**The Solution:** An AI-powered "Tactical Terminal" that acts as a toxic HR department—analyzing team synergy, roasting specific failures via TTS, and mathematically calculating the optimal "Hire/Fire" strategy to fix the roster.

---

## 📸 Capabilities
* **Roast-O-Matic (TTS):** Uses Google Gemini to generate a visceral, game-aware roast of the user's team, read aloud by a robotic text-to-speech engine.
* **The Survival Matrix:** A dynamic, 12-point color scale Heatmap that calculates compound defensive vulnerabilities (e.g., identifying a collective 6x weakness to Ice).
* **The Headhunter Algorithm:** Automated "HR Department" logic that identifies the biggest liability (Fire) and queries the PokeAPI for a mathematically perfect counter-pick (Hire).
* **Game-Aware Intelligence:** Adapts advice and valid Pokémon lists based on the selected game version (from *Red/Blue* to *Scarlet/Violet*).
* **Bill's PC:** Tracks every "Weakest Link" identified in previous sessions, creating a visual "Hall of Shame."

## 🛠 Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Logic** | Python 3.11 | Core application logic |
| **AI Model** | Google Gemini 2.0 Flash | Context-aware roasting & meta analysis |
| **Frontend** | Streamlit | Custom CSS "Rocket Theme" UI |
| **Data** | PokeAPI | Real-time stats, sprites, and type charts |
| **Viz** | Plotly | Interactive Heatmaps & Radar Charts |
| **Audio** | pyttsx3 | Offline Text-to-Speech engine |

## 🚀 Quick Start
```bash
# 1. Clone the repo
git clone [https://github.com/maxykoin/pokeroast.git](https://github.com/maxykoin/pokeroast.git)
cd pokeroast

# 2. Install dependencies (Using uv for speed)
uv sync

# 3. Set up your API Key
# Create a .env file and add your Google Gemini Key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# 4. Check Available Models
# Run the debug tool to see which Gemini models your key can access
uv run python src/pokeroast/debug.py

# 5. Configure Model
# Add the working model ID from the debug output to your .env
echo "GEMINI_MODELS=models/gemini-2.0-flash-exp" >> .env

# 6. Launch the Terminal
uv run streamlit run src/pokeroast/app.py
```

## 🧠 System Architecture
The application is built on a modular "Headhunter" architecture:
1.  **Context Injection:** The user selects a game version (e.g., *Emerald*), which filters the valid Pokémon dataset and primes the LLM with specific meta-knowledge (e.g., "Wattson's Gym").
2.  **Compound Math Engine:** We fetch the Type Chart from PokeAPI and calculate a cumulative damage multiplier for the entire 6-stack team against all 18 attacking types.
3.  **Algorithmic Recruitment:**
    * **Fire Logic:** Finds the team member contributing the most variance to the team's highest threat score.
    * **Hire Logic:** Performs a set intersection between the game's valid Dex and the list of Pokémon that resist the identified threat to find a valid counter-pick.

---

<div align="center">

### Built with ❤️ by [Nina Cunha](https://github.com/maxykoin)

**Data Science · Industrial Automation · Software Engineering**

[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/nscunha/)
[![GitHub](https://img.shields.io/badge/Follow-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/maxykoin)

</div>

---