import os

class Config:
    # 🔐 Secret key for Flask (important for security)
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"

    # 📂 Model paths
    MODEL_PATH = os.path.join("model", "model.pkl")
    VECTORIZER_PATH = os.path.join("model", "vectorizer.pkl")

    # 📊 Data path
    DATA_PATH = os.path.join("data", "careers.csv")

    # ⚙️ App settings
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False