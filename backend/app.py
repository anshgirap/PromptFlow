from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


# Master Template
TEMPLATE = """
Generate a highly effective, platform-optimized image-generation prompt based on the user’s idea.

Target Platform: {platform}

Strict Output Rules:
- Output must be a single 4–6 line descriptive prompt.
- No lists, bullet points, headings, or numbering.
- No questions, disclaimers, or commentary.
- Do NOT mention rules, platforms, or the user.
- Output ONLY the final crafted prompt text.

Platform Style Profiles:
- Gemini: cinematic atmosphere, emotional tone, soft gradients, rich lighting, immersive color flow.
- Midjourney: dense stylistic detail, lens and camera language, lighting physics, texture realism, artistic direction.
- Stable Diffusion: strong keyword-rich phrasing, explicit visual descriptors, lighting terms, environment and subject clarity.
- ChatGPT Image: natural expressive language, simple but vivid visuals, smooth narrative flow, no camera jargon.
- Claude Image: elegant, poetic, emotionally resonant imagery with rich sensory detail.
- DALL·E: clear artistic intent, bold contrasts, strong color palettes, recognizable visual anchors.
- Firefly: stylized composition, color harmony, texture-forward rendering, dramatic highlights.
- Ollama (Local Models): balanced cinematic storytelling, clear visual intent, controlled detail without technical clutter.

Core Scene Architecture:
Every output must clearly imply:
- A primary subject
- A surrounding environment or background
- Lighting direction and quality
- A dominant color mood or palette
- Depth, perspective, or framing

Visual Composition Guidelines:
- Anchor the scene spatially so the subject feels placed, not floating.
- Suggest foreground, midground, and background when possible.
- Use lighting to guide attention and emotion.
- Let color and texture reinforce mood.

General Style Guidelines:
- Expand the idea into a cohesive visual scene, not just a description.
- Maintain a consistent aesthetic identity across the entire prompt.
- Use vivid, cinematic language without becoming verbose.
- Avoid generic or hollow phrasing.
- The final result should read like a professional art direction brief, not a caption.

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
        # Call local Ollama (qwen2.5:1.5b)
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen2.5:1.5b",
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