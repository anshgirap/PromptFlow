# PromptFlow ⚡

A refined, platform-aware prompt generator designed to convert simple ideas into high-quality image generation prompts.  
Built with a cinematic UI, smooth interactions, and support for all major AI image models.

---

## 📸 Overview

PromptFlow produces optimized 4–6 line prompts tailored for each generation platform.  
The goal is consistency, clarity and style that matches how each platform interprets prompts.

---

## 🎯 Supported Platforms

| Platform              | Style Focus                                              |
| --------------------- | -------------------------------------------------------- |
| **Gemini**            | Cinematic, atmospheric, soft color and lighting language |
| **Midjourney**        | Lens terms, artistic direction, detailed textures        |
| **Stable Diffusion**  | Keyword-rich, structured descriptors                     |
| **ChatGPT Image Gen** | Natural phrasing, expressive but simple                  |
| **Claude**            | Poetic, elegant, emotional tone                          |
| **DALL·E**            | Strong contrast, vibrant visuals, clear intent           |
| **Firefly**           | Stylized color harmony and dramatic accents              |
| **Ollama (Local)**    | Balanced cinematic detail without technical jargon       |

---

## ✨ Features

### 🔹 Multi-Platform Prompt Optimization

Each output is automatically styled based on the selected generator.

### 🔹 Glassmorphism UI

Floating gradients  
Soft shadows  
Smooth dropdown animations  
Responsive layout

### 🔹 Local Processing

Runs on **Ollama**, avoiding API usage limits or billing.

### 🔹 Fast Output

Simple idea → Polished final prompt in seconds.

---

## 🛠 Tech Stack

**Frontend**

- HTML
- CSS
- JavaScript

**Backend**

- Python
- Flask
- Ollama local inference

---

## 📁 Project Structure

```
PromptFlow/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env (ignored)
│
├── frontend/
│   ├── index.html
│   ├── logos/
│       ├── logo.png
│       └── logosmall.png
│
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/anshgirap/PromptFlow.git
cd PromptFlow
```

### 2. Install backend dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3. Install Ollama

Download from https://ollama.com

Pull a model (example):

```bash
ollama pull gemma:2b
```

### 4. Start the backend

```bash
python app.py
```

### 5. Open the frontend

Open `frontend/index.html` in any browser.

---

## 🧠 How PromptFlow Works

1. User enters an idea.
2. User selects the platform from a custom dropdown.
3. Backend injects the idea into a curated template.
4. Ollama generates a polished, platform-styled output.
5. Result fades in through a smooth, glass UI component.

---

## ⚙ Customization

You can modify platform rules inside **app.py** under the template block.  
This lets you change tone, complexity or artistic style instantly.

---

## 📄 License

MIT License

---

## ⭐ Support

If you find PromptFlow helpful, consider starring the project.  
It motivates future updates and improvements.
