from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    user_prompt = data.get("prompt", "")

    if not user_prompt.strip():
        return jsonify({"error": "Prompt is empty"}), 400

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative prompt generator for AI image tools."},
                {"role": "user", "content": f"Make a detailed 4-6 line prompt for this idea: {user_prompt}"}
            ],
            temperature=0.8,
            max_tokens=200
        )

        expanded_prompt = response.choices[0].message.content.strip()
        return jsonify({"expanded_prompt": expanded_prompt})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)