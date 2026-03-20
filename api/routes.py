from flask import Blueprint, render_template, request, jsonify
from model.predictor import predict_career

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@main.route("/predict", methods=["POST"])
def predict():
    interests = request.form.get("interests", "").lower()
    skills = request.form.get("skills", "").lower()
    personality = request.form.get("personality", "").lower()

    result = predict_career(interests, skills, personality)

    return render_template("index.html", result=result)


@main.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json()

    interests = data.get("interests", "")
    skills = data.get("skills", "")
    personality = data.get("personality", "")

    result = predict_career(interests, skills, personality)

    return jsonify(result)