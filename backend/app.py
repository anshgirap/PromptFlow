from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Hugging Face Router Config

HF_URL = "https://router.huggingface.co/v1/chat/completions"
HF_MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"
HF_TOKEN = os.environ.get("HF_TOKEN")


HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

# Prompt Template

TEMPLATE = """You are a professional AI prompt engineer whose job is to transform rough, unclear, or weak user input into a precise, high-quality, results-driven prompt.

The rewritten prompt should be optimized for this target platform:
{platform}

Your goal is to make the user’s intent clearer, more structured, and more effective so that the chosen AI platform produces a significantly better result.

You must follow ALL of these rules:

• Output a single rewritten prompt — no explanations, no analysis, no commentary  
• Do not include lists, bullet points, or numbered steps  
• Do not include quotation marks  
• Do not include headings  
• Do not mention the user, rules, or yourself  
• Do not repeat the input — improve it  

The rewritten prompt must:
- Be clearer than the original  
- Be more specific than the original  
- Preserve the user’s intent  
- Remove ambiguity  
- Add useful constraints where appropriate  
- Use natural, professional language  

If the input is vague, infer the most likely intent and make it concrete.  
If the input is short, expand it.  
If the input is messy, clean it up.  
If the input is detailed, refine and sharpen it.

Adapt tone, structure, and phrasing to match the selected platform when relevant.

The output should feel like something written by a skilled professional who knows exactly how to get the best possible result from an AI.

User input:
{user_prompt}

"""

# Hugging Face Call

def call_hf(prompt):
    payload = {
        "model": HF_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 400
    }

    for _ in range(5):
        try:
            r = requests.post(HF_URL, headers=HEADERS, json=payload, timeout=60)
            data = r.json()
        except Exception as e:
            return None, str(e)

        # HF router error
        if "error" in data:
            msg = data["error"].get("message", "")
            if "loading" in msg.lower():
                time.sleep(5)
                continue
            return None, msg

        try:
            return data["choices"][0]["message"]["content"], None
        except:
            return None, f"Bad response: {data}"

    return None, "Model did not load in time"

# API Endpoint

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    user_prompt = data.get("prompt", "")
    platform = data.get("platform", "Generic")

    if not user_prompt.strip():
        return jsonify({"error": "Prompt is empty"}), 400

    final_prompt = TEMPLATE.format(
        platform=platform,
        user_prompt=user_prompt
    )

    result, error = call_hf(final_prompt)

    if error:
        return jsonify({"error": error}), 500

    return jsonify({
        "expanded_prompt": result.strip()
    })

# Run

if __name__ == "__main__":
    app.run(debug=True)