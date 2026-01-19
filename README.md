# PromptFlow ⚡

PromptFlow is a **platform-aware AI prompt optimizer** that transforms simple ideas into high-quality, task-ready prompts tailored for different AI platforms and models 🚀

It focuses on clarity, intent alignment, and structural optimization by adapting prompt style and tone based on how each platform interprets instructions.

---

## 🖼 Preview

![PromptFlow UI](./assets/preview/promptflow-preview.png)

---

## 📌 Overview

Different AI platforms respond best to different prompting styles.  
A prompt that works well on ChatGPT may perform poorly on Claude or Gemini.

PromptFlow solves this by intelligently reshaping prompts so they feel **native to each platform**—whether you're generating text, images, code, analysis, or creative content.

The output is a clean, expressive, and structured prompt optimized for:

- accuracy
- clarity
- reasoning quality
- creativity
- platform behavior

—all without manual re-engineering.

---

## 🎯 Supported Platforms

| Platform            | Optimization Style                                       |
| ------------------- | -------------------------------------------------------- |
| ChatGPT             | Clear instruction-following with structured reasoning    |
| Gemini              | Context-rich, analytical, and conversational             |
| Claude              | Thoughtful, detailed, and precise task-oriented prompts  |
| Midjourney          | Artistic direction and creative visual instruction       |
| Stable Diffusion    | Keyword-rich structured visual descriptors               |
| DALL·E              | Direct, intent-focused generation prompts                |
| Firefly             | Stylized creative optimization                           |
| Hugging Face Models | General-purpose prompts tuned for transformer-based LLMs |

---

## ✨ Key Features

### 🔹 Platform-Aware Prompt Engineering

Each prompt is dynamically optimized based on the selected AI platform to maximize output quality and relevance.

### 🔹 Multi-Purpose Optimization

PromptFlow supports prompt engineering for:

- Content creation
- Coding assistance
- Research queries
- Brainstorming
- Analysis tasks
- Creative writing
- Image generation prompts

### 🔹 Minimal, Premium UI

- Glassmorphism design
- Floating gradient background
- Smooth dropdown and fade transitions

### 🔹 Cloud-Based Intelligence

- Powered by **Hugging Face Inference API**
- No local models required
- Fast, scalable, and reliable processing

### 🔹 Hosted Backend

The backend is fully deployed on **Render**, ensuring:

- High availability
- Zero local setup
- Production-grade performance

### 🔹 Fast Workflow

Simple idea → optimized platform-ready prompt in seconds ⚡

---

## 🛠 Tech Stack

**Frontend**

- HTML
- CSS
- JavaScript

**Backend**

- Python
- Flask
- Hugging Face Inference API
- Render (Cloud Hosting)

---

## 🚀 How to Run PromptFlow

### Prerequisites

- Python 3.9+
- A Hugging Face account and API key

---

### 1️⃣ Clone the repository

git clone https://github.com/anshgirap/PromptFlow.git  
cd PromptFlow

---

### 2️⃣ Install backend dependencies

cd backend  
pip install -r requirements.txt

---

### 3️⃣ Configure Environment Variables

Create a `.env` file inside the backend folder:

HUGGINGFACE_API_KEY=your_api_key_here  
RENDER_BACKEND_URL=your_render_backend_url

---

### 4️⃣ Start the backend server locally (optional)

python app.py

The Flask server will run on:

http://127.0.0.1:5000

---

### 5️⃣ Open the frontend

Open the file directly in your browser:

frontend/index.html

No build step required.

---

## 📁 Project Structure

PromptFlow/

├── assets/  
│ ├── logos/  
│ │ ├── logo.png  
│ │ └── logosmall.png  
│ │  
│ └── preview/  
│ └── promptflow-preview.png  
│  
├── backend/  
│ ├── app.py  
│ └── requirements.txt  
│  
├── frontend/  
│ └── index.html  
│  
├── README.md  
└── LICENSE

---

## 🧠 How It Works

1. The user enters a short idea or instruction.
2. A target AI platform is selected from the dropdown.
3. The backend applies platform-specific optimization rules.
4. The Hugging Face API generates a refined prompt.
5. The optimized result appears instantly in the UI.

---

## ⚙ Customization

Prompt behavior can be adjusted inside `app.py` by editing the platform template rules.

This allows easy tuning of:

- tone
- complexity
- creativity level
- structure
- verbosity

—without modifying the frontend.

---

## ⭐ Support

If you find PromptFlow useful, consider starring the repository.  
It helps the project grow and encourages future improvements 🚀
