# PromptFlow ⚡

PromptFlow is a platform-aware AI prompt generator that transforms simple ideas into high-quality, image-generation prompts tailored for different AI models 🎨

It focuses on clarity, consistency, and visual intent, adapting prompt structure and tone based on how each platform interprets prompts.

---

## 🖼 Preview

![PromptFlow UI](./assets/preview/promptflow-preview.png)

---

## 📸 Overview

Different image generation models interpret prompts in very different ways.  
PromptFlow solves this by intelligently reshaping prompts to feel native to each platform.

The output is a clean, expressive **4–6 line prompt** that avoids over-engineering while still delivering strong visual results.

---

## 🎯 Supported Platforms

| Platform                 | Prompt Style                                        |
| ------------------------ | --------------------------------------------------- |
| Gemini                   | Cinematic, atmospheric, mood-driven descriptions    |
| Midjourney               | Artistic direction, lighting, textures, lens detail |
| Stable Diffusion         | Structured, keyword-rich visual descriptors         |
| ChatGPT Image Generation | Natural language, expressive and simple             |
| Claude                   | Elegant, emotionally rich imagery                   |
| DALL·E                   | Clear intent, vibrant contrasts                     |
| Firefly                  | Stylized color harmony and dramatic accents         |
| Ollama (Local)           | Balanced cinematic detail, minimal jargon           |

---

## ✨ Key Features

### 🔹 Platform-Aware Prompt Generation

Each prompt is dynamically optimized based on the selected image generation platform.

### 🔹 Minimal, Premium UI

- Glassmorphism design
- Floating gradient background
- Smooth dropdown and fade transitions

### 🔹 Local Inference

Runs fully on **Ollama**, avoiding API limits, billing, or external dependencies 🔒

### 🔹 Fast Workflow

Simple idea → polished final prompt in seconds ⚡

---

## 🛠 Tech Stack

**Frontend**

- HTML
- CSS
- JavaScript

**Backend**

- Python
- Flask
- Ollama

---

## 📁 Project Structure

```text
PromptFlow/
│
├── assets/
│   ├── promptflow-preview.png
│   └── logos/
│       ├── logo.png
│       └── logosmall.png
│
├── frontend/
│   └── index.html
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── README.md
└── LICENSE
```
