import os
import google.generativeai as genai

def explain_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    
    if len(content) > 8000:
        print("File is too large to process. Please provide a smaller file.")
        content = content[:8000]  # Truncate to first 8000 characters

    prompt = f"""
    Jelaskan isi file berikut ini secara ringkas dan mudah dimengerti oleh mahasiswa informatika.
    Tambahkan juga insight singkat kalau ada kesalahan atau potensi optimasi di dalamnya.
    
    === ISI FILE ===
    {content}
    """

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        print("\n📘 Penjelasan dari Gemini:\n")
        print(response.text)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")