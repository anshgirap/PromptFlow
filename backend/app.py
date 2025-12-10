from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    user_prompt = data.get("prompt", "")

    if not user_prompt.strip():
        return jsonify({"error": "Prompt is empty"}), 400

    try:
        # ollama call (Gemma3:4b)
        response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": (
            "Expand this idea into a polished, cinematic, descriptive 4–6 line AI image-generation prompt. "
            "Avoid questions, lists, or explanations. Output only the final expanded prompt.\n\n"
            f"Idea: {user_prompt}"
        ),
        "stream": False
        }
    )

        data = response.json()
        expanded_prompt = data.get("response", "").strip()

        if not expanded_prompt:
            return jsonify({"error": "No response returned from the local model"}), 500

        return jsonify({"expanded_prompt": expanded_prompt})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)