# PromptFlow ⚡

PromptFlow is a platform-aware AI prompt generator that transforms simple ideas into high-quality, image-generation prompts tailored for different AI models 🎨

It focuses on clarity, consistency, and visual intent by adapting prompt structure and tone based on how each platform interprets prompts.

---

## 🖼 Preview

![PromptFlow UI](./assets/preview/promptflow-preview.png)

---

## 📸 Overview

Different image generation models respond best to different prompt styles.  
PromptFlow solves this by intelligently reshaping prompts so they feel native to each platform.

The output is a clean, expressive **4–6 line prompt** that balances detail and readability without over-engineering.

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
| Ollama (Local)           | Balanced cinematic detail with minimal jargon       |

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
- Ollama (local LLM inference)

---

## 🚀 How to Run PromptFlow

### Prerequisites

- Python 3.9+
- Ollama installed and running
- A supported Ollama model (example: gemma)

---

### 1️⃣ Clone the repository

```bash
git clone https://github.com/anshgirap/PromptFlow.git
cd PromptFlow
```

---

### 2️⃣ Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

### 3️⃣ Install and run Ollama

Download Ollama from:  
https://ollama.com

Pull a model:

```bash
ollama pull gemma
```

Ensure Ollama is running locally on:

```
http://localhost:11434
```

---

### 4️⃣ Start the backend server

```bash
python app.py
```

The Flask server runs on:

```
http://127.0.0.1:5000
```

---

### 5️⃣ Open the frontend

Open the file directly in your browser:

```
frontend/index.html
```

No build step required.

---

## 📁 Project Structure

```text
PromptFlow/
│
├── assets/
│   ├── logos/
│   │   ├── logo.png
│   │   └── logosmall.png
│   │
│   └── preview/
│       └── promptflow-preview.png
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── README.md
└── LICENSE
```

---

## 🧠 How It Works

1. The user enters a short idea.
2. A target platform is selected from the dropdown.
3. The backend applies platform-specific prompt rules.
4. Ollama generates a refined image prompt.
5. The result appears with smooth UI transitions.

---

## ⚙ Customization

Prompt behavior can be adjusted inside `app.py` by editing the platform template rules.

This allows easy tuning of tone, complexity, and artistic emphasis without changing the frontend.

---

## ⭐ Support

If you find PromptFlow useful, consider starring the repository.  
It helps the project grow and encourages future improvements 🚀
