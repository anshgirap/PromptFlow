from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


# Master Template
TEMPLATE = """
Generate a highly-effective, platform-optimized image-generation prompt based on the user's idea.

Target Platform: {platform}

Rules:
- Output must be 4–6 lines only.
- No lists, bullet points, or numbered items.
- No questions or suggestions.
- Do NOT mention the rules, the user, or the platform directly.
- Output ONLY the final prompt.

Platform Style Requirements:
- Gemini: cinematic, richly descriptive, soft aesthetic language, mood + color + lighting focus.
- Midjourney: detailed stylistic descriptors, lens/camera terms, lighting, textures, atmosphere, artistic direction.
- Stable Diffusion: strong descriptive keywords, style tags, lighting, textures, character/environment details.
- ChatGPT Image Generation: natural language, expressive but simple descriptions, less technical, no camera jargon.
- Claude Image Generation: elegant, emotionally rich, artistic imagery with descriptive flow.
- DALL·E: clear artistic intent, vibrant descriptive elements, strong visual contrasts.
- Firefly: stylized artistic direction, color harmony, texture-forward, dramatic accents.
- Ollama Local Models: balanced cinematic detail, avoid over-technical phrasing, clear aesthetic intent.

General Style Guidelines:
- Include atmosphere, mood, colors, textures, lighting style, visual tone.
- Expand the idea into an expressive, visually compelling prompt.
- Maintain consistent, natural-flowing prose.

Idea: {user_prompt}
"""


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    user_prompt = data.get("prompt", "")
    platform = data.get("platform", "Generic")

    if not user_prompt.strip():
        return jsonify({"error": "Prompt is empty"}), 400

    # Build prompt using template
    final_prompt = TEMPLATE.format(platform=platform, user_prompt=user_prompt)

    try:
        # Call local Ollama (Gemma3:4b)
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": final_prompt,
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