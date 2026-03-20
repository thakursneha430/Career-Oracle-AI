import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from config.settings import Config

def train_model():
    try:
        # 📊 Load dataset
        data = pd.read_csv(Config.DATA_PATH)

        # 🧹 Basic check
        if "text" not in data.columns or "career" not in data.columns:
            raise ValueError("Dataset must contain 'text' and 'career' columns")

        # ✂️ Split input/output
        X_text = data["text"]
        y = data["career"]

        # 🔢 Convert text → numbers
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(X_text)

        # 🤖 Train model
        model = MultinomialNB()
        model.fit(X, y)

        # 💾 Save model
        with open(Config.MODEL_PATH, "wb") as f:
            pickle.dump(model, f)

        with open(Config.VECTORIZER_PATH, "wb") as f:
            pickle.dump(vectorizer, f)

        print("✅ Model trained and saved successfully 🔥")

    except Exception as e:
        print("❌ Error during training:", e)


if __name__ == "__main__":
    train_model()