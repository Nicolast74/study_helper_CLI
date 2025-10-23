from colorama import Fore, Style, init
from helper import ask_gemini
from file_reader import explain_file

init(autoreset=True)

def main():
    while True:
        print("\n=== Study Helper CLI ===")
        print("1. Tanya topik ke Gemini")
        print("2. Jelaskan file di direktori project")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            prompt = input("Tanya: ")
            response = ask_gemini(prompt)
            print(f"\n{Fore.CYAN}Jawaban Gemini:{Style.RESET_ALL}\n{response}")
        elif choice == "2":
            file_path = input("Masukkan nama file (contoh: main.py): ")
            explain_file(file_path)
        elif choice == "3":
            print("Sampai jumpa, semangat belajar 🔥")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()