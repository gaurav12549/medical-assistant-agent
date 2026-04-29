import requests
import streamlit as st
import pandas as pd
from sklearn.naive_bayes import MultinomialNB


def llm_symptom_search(symptoms):
    prompt = f"""
You are a medical assistant.

User symptoms: {', '.join(symptoms)}

Instructions:
- Do NOT ask follow-up questions
- Do NOT ask for more details
- Directly provide an answer

Respond strictly in this format:

Possible conditions:
- ...

Recommended care:
- ...

When to see a doctor:
- ...

Keep the response concise and helpful.
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False                
            },
            timeout=60
        )

        if response.status_code == 200:
            return response.json().get("response", "No response from model.")
        else:
            return f"Ollama error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Ollama connection error: {e}"
    

    
    
# Placeholder: Simple rule-based triage and suggestions
def triage(symptoms):
    # Example rules (expand as needed)
    if 'chest pain' in symptoms and 'shortness of breath' in symptoms:
        return {
            'triage': 'emergency',
            'advice': 'Seek immediate medical attention.',
            'possible_conditions': ['Heart attack', 'Pulmonary embolism'],
            'care': 'Call emergency services or Dial 110.'
        }
    elif 'fever' in symptoms and 'cough' in symptoms:
        return {
            'triage': 'routine',
            'advice': 'Monitor symptoms, rest, and hydrate.',
            'possible_conditions': ['Flu', 'Common cold', 'COVID-19'],
            'care': 'Consider a COVID-19 test if symptoms persist.'
        }
    else:
        return {
            'triage': 'self-care',
            'advice': 'Monitor symptoms. If they worsen, consult a doctor.',
            'possible_conditions': ['Unknown'],
            'care': 'Rest and hydrate.'
        }

st.title('AI-Powered Medical Assistant')
st.write('Enter your symptoms below. The assistant will suggest possible conditions and next steps.')

symptom_input = st.text_input('List your symptoms (comma separated):')

symptoms = [s.strip().lower() for s in symptom_input.split(',') if s.strip()]

col1, col2 = st.columns(2)
with col1:
    if st.button('Analyze (Rule-based)'):
        if symptoms:
            result = triage(symptoms)
            st.subheader('Triage Result:')
            st.write(f"**Triage Level:** {result['triage'].capitalize()}")
            st.write(f"**Advice:** {result['advice']}")
            st.write(f"**Possible Conditions:** {', '.join(result['possible_conditions'])}")
            st.write(f"**Recommended Care/Tests:** {result['care']}")
        else:
            st.warning('Please enter at least one symptom.')
with col2:
   if st.button('Analyze with LLM'):
    if symptoms:
        st.subheader('LLM Medical Assistant Result:')

        with st.spinner("🤖 AI is analyzing your symptoms..."):
            llm_result = llm_symptom_search(symptoms)

        st.write(llm_result)
    else:
        st.warning('Please enter at least one symptom.')