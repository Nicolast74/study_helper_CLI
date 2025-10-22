from colorama import Fore, Style, init
from helper import ask_gemini

init(autoreset=True)

def main():
    print(Style.BRIGHT + Fore.CYAN + "\n=== Study Helper CLI ===\n")
    print("Tanya ke aku apa aja, tentang kuliah, tugas, quiz, atau topik belajar lainnya!")
    print("Ketik 'exit' atau 'quit' untuk keluar.\n")
    
    while True:
        topic = input(Style.BRIGHT + Fore.YELLOW + "Masukkan topik kamu: ")

        if topic.lower() in ['exit', 'quit']:
            print(Fore.CYAN + "sampai jumpa, semangat belajarnya 🤗🤗🤗")
            break
        prompt =f"jelaskan tentang {topic}"
        try:
            asnwer = ask_gemini(prompt)
            print(Style.BRIGHT + Fore.GREEN + "\nPenjalasan : \n" + Style.RESET_ALL + asnwer + "\n")
        except Exception as e:
            print(Fore.RED + f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()