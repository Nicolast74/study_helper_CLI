import os
import json
import google.generativeai as genai
from colorama import Fore, Style, init
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

HISTORY_FILE = "history.json"

def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = genai.GenerativeModel("gemini-2.0-flash").generate_content(prompt)
    return response.text

def save_history(prompt, response):
    import json, os
    history_file = "history.json"

    # kalau file belum ada, bikin file baru
    if not os.path.exists(history_file):
        with open(history_file, "w") as f:
            json.dump([], f)

    # baca data lama, tapi kalau file kosong → gunakan list kosong
    with open(history_file, "r") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            history = []

    history.append({
        "prompt": prompt,
        "response": response
    })

    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

    print("✅ History berhasil disimpan!\n")


def show_history():
    """Tampilkan semua riwayat pertanyaan & jawaban"""
    if not os.path.exists(HISTORY_FILE):
        print("Belum ada history 😶")
        return

    # cek dulu ukuran file
    if os.path.getsize(HISTORY_FILE) == 0:
        print("Belum ada history 😶")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
    
    for i, item in enumerate(history, start=1):
        print(f"\n{i}. Prompt: {item['prompt']}\nJawaban:\n{item['response']}\n{'-'*40}")