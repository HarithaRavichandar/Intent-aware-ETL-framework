from flask import Blueprint, request, jsonify, current_app
from flask import send_from_directory
from app.orchestrator.engine import run_pipeline
from app.ai.qa import ask_question
import os

main = Blueprint("main", __name__)


# Serve UI correctly
@main.route("/")
def home():
    return current_app.send_static_file("index.html")


# Upload API
@main.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    intent = request.form["intent"]

    path = os.path.join("uploads", file.filename)
    file.save(path)

    result = run_pipeline(path, intent)

    return jsonify(result)


# Chatbot API
@main.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    summary = data["summary"]
    question = data["question"]

    answer = ask_question(summary, question)

    return jsonify({"answer": answer})
