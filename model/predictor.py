import pickle
import requests
from config.settings import Config
from utils.helpers import combine_inputs

# 🔄 Load model and vectorizer once
try:
    with open(Config.MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(Config.VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)

except Exception as e:
    print("Error loading model:", e)
    model = None
    vectorizer = None


# 🔮 LLM Explanation using Ollama (Mistral)
def get_llm_explanation(career, interests, skills, personality):
    try:
        prompt = f"""
        You are a mystical career oracle 🔮.

        A user has:
        Interests: {interests}
        Skills: {skills}
        Personality: {personality}

        The predicted career is: {career}

        Explain in a short, magical, and human-like way why this career suits them.
        """

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        return "🔮 The oracle is silent... (Make sure Ollama is running)"


# 🧠 Main Prediction Function
def predict_career(interests, skills, personality):

    # ⚠️ Check if model loaded
    if model is None or vectorizer is None:
        return {
            "career": "Model not loaded",
            "reason": "Please train the model first",
            "confidence": 0
        }

    try:
        # 🧹 Clean + combine input
        text = combine_inputs(interests, skills, personality)

        # 🔢 Convert to vector
        X = vectorizer.transform([text])

        # 🎯 Predict
        prediction = model.predict(X)[0]

        # 📊 Confidence
        try:
            probs = model.predict_proba(X)
            confidence = max(probs[0])
        except:
            confidence = 0.75

        # 🔮 Get LLM explanation
        explanation = get_llm_explanation(
            prediction, interests, skills, personality
        )

        return {
            "career": prediction,
            "reason": explanation,
            "confidence": round(confidence * 100, 2)
        }

    except Exception as e:
        return {
            "career": "Error",
            "reason": str(e),
            "confidence": 0
        }