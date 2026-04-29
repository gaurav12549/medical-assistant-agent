🧠 AI-Powered Medical Assistant

An intelligent medical assistant that combines rule-based triage + local LLM (Ollama) to analyze user symptoms and provide safe, structured health guidance.

🚀 Features
🔍 Symptom Analysis
Accepts user input (comma-separated symptoms)
Cleans and normalizes input for processing
⚖️ Dual Decision System
✅ Rule-Based Triage
Fast and deterministic
Categorizes cases into:
Emergency
Routine
Self-care
Provides immediate actionable advice
🤖 LLM-Based Analysis (Local AI)

Powered by Ollama:

Runs fully offline (no internet required)
No API key, billing, or quota limits
Supports models like:
llama3
mistral (faster alternative)
📋 Structured AI Output

The AI is guided to always return:

Possible conditions
Recommended care
When to see a doctor

👉 Ensures consistent, useful responses (no unnecessary follow-up questions)

🎨 Enhanced User Experience
⏳ Loader animation during AI processing (st.spinner)
🌙 Dark theme UI using .streamlit/config.toml
✨ Smooth UI animations (CSS-based)
🧾 Clean, structured output display
🛡️ Safety-First Design
Avoids definitive diagnoses
Encourages professional medical consultation
Emergency detection handled via rule-based system
🏗️ Tech Stack
Language: Python 3
Frontend/UI: Streamlit
LLM Runtime: Ollama
ML (optional): Scikit-learn
HTTP Client: Requests
📂 Project Structure
medical-assistant/
│
├── app.py                  # Main Streamlit application
├── .streamlit/
│   └── config.toml         # Theme configuration (dark mode)
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the repository
git clone <your-repo-url>
cd medical-assistant
2️⃣ Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Install & Run Ollama

Install Ollama from:
👉 https://ollama.com

Start the service:

ollama serve

Pull a model:

ollama pull llama3
5️⃣ Run the application
streamlit run app.py

Open in browser:

http://localhost:8501
🔍 How It Works
🧩 Workflow
User Input → Symptom Parsing →
    ├── Rule-Based Engine → Triage Result
    └── Ollama LLM → Detailed Medical Guidance
🤖 LLM Integration Example
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
)
🎨 UI Configuration
Dark Theme (.streamlit/config.toml)
[theme]
base="dark"
primaryColor="#4CAF50"
backgroundColor="#0e1117"
secondaryBackgroundColor="#262730"
textColor="#ffffff"
Loader Example
with st.spinner("🤖 AI is analyzing your symptoms..."):
    llm_result = llm_symptom_search(symptoms)
🚨 Emergency Handling Example
if 'chest pain' in symptoms and 'shortness of breath' in symptoms:

Output:

Emergency triage
Suggest calling 108 / 112 (India)
⚠️ Disclaimer
This tool is for informational purposes only
It does not provide medical diagnosis
Always consult a qualified healthcare professional for serious conditions
🔮 Future Enhancements
💬 Chat-based conversational UI
🧠 Multi-turn context awareness
📊 Symptom severity scoring
🌐 API backend (FastAPI)
🐳 Docker deployment
📱 Mobile-friendly UI
🧠 Key Learnings
Local LLMs require strong prompt engineering
Combining rules + AI improves reliability
UI/UX improvements (loader, theme, animations) enhance usability
🤝 Contributing

Contributions are welcome:

Add more triage rules
Improve UI/UX
Integrate better or optimized models