🧠 Study Helper CLI

**Study Helper CLI** is a simple Python-based command-line tool that helps you study smarter with the power of **Google Gemini AI**.  
It allows you to ask questions, get explanations for code files, and automatically save your Q&A history for future review.

---

✨ Features

- 🔹 Ask any topic to Gemini AI  
- 🔹 Get explanations for local code files  
- 🔹 Automatically store all questions and answers in `history.json`  
- 🔹 View your entire study history directly from the CLI  
- 🔹 Beautiful colorized terminal output (powered by `colorama`)

---

🧰 Setup Instructions

1️⃣ Clone the repository
```bash
git clone https://github.com/USERNAME/study_helper_CLI.git
cd study_helper_CLI
```
2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
If you don't have a requirements.txt file yet, you can generate it manually:
```bash
pip install colorama google-generativeai
pip freeze > requirements.txt
```
🔑 Configure Your API Key

Create a .env file in the project root and add:
```env
GOOGLE_API_KEY=your_api_key_here
```
Or set it directly from your terminal:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```
🚀 Usage

Run the app:
```bash
python main.py
```