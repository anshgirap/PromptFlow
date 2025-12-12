from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


# Master Template
TEMPLATE = """
Generate a highly effective, platform-optimized image generation prompt based on the user's idea.

Target Platform: {platform}

Strict Output Rules:
- Final output must be a single 4–6 line descriptive prompt.
- No lists, bullet points, headings, or numbered steps.
- No questions, disclaimers, or extra commentary.
- Do NOT mention rules, platforms, or the user.
- Output ONLY the final crafted prompt text.

Platform Style Profiles:
- Gemini: cinematic mood, atmospheric detail, soft gradients, emotional tone, vivid color flow.
- Midjourney: dense descriptive phrasing, lens/camera terminology, lighting physics, texture realism, artistic style cues.
- Stable Diffusion: strong keyword-rich phrasing, explicit style tags, lighting adjectives, environmental clarity.
- ChatGPT Image: natural descriptive prose, expressive yet simple visuals, no camera jargon, smooth narrative flow.
- Claude Image: elegant, poetic, emotionally resonant imagery with rich sensory detail.
- DALL·E: clear artistic direction, bold contrasts, distinctive color palettes, recognizable visual anchors.
- Firefly: stylized composition, color harmony, bold textures, dramatic highlights and accents.
- Ollama (Local Models): balanced cinematic storytelling, avoid overly technical syntax, clear visual intent.

General Style Guidelines:
- Build strong atmosphere and mood.
- Emphasize lighting, textures, color palette, environment, and emotional tone.
- Expand the idea into a cohesive visual scene with clear aesthetic direction.
- Maintain natural, fluid prose without over-describing.

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