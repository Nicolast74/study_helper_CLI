# main.py
from colorama import Fore, Style, init
from helper import ask_gemini, save_history, show_history
from file_reader import explain_file

init(autoreset=True)

def main():
    print(Style.BRIGHT + Fore.CYAN + "\n=== AI Study Helper ===")
    while True:
        print("\n1. Tanya topik ke Gemini")
        print("2. Jelaskan file di direktori project")
        print("3. Lihat riwayat jawaban")
        print("4. Keluar")
        choice = input(Fore.YELLOW + "Pilih menu: ").strip()

        if choice == "1":
            topic = input("Topikmu: ").strip()
            if not topic:
                print(Fore.RED + "Masukkan topik dulu ya.")
                continue
            response = ask_gemini(topic)
            if response is None:
                print(Fore.RED + "Gagal mendapatkan jawaban dari Gemini.")
            else:
                print(Fore.GREEN + "\n🧠 Jawaban Gemini:\n" + Style.RESET_ALL + response + "\n")
                save_history(topic, response)

        elif choice == "2":
            file_path = input("Masukkan nama file (contoh: main.py): ").strip()
            if not file_path:
                print(Fore.RED + "Nama file kosong.")
                continue
            response = explain_file(file_path)
            if response:
                save_history(f"Jelaskan file {file_path}", response)

        elif choice == "3":
            show_history()

        elif choice == "4":
            print(Fore.CYAN + "Sampai jumpa, semangat belajar 🔥")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid.")

if __name__ == "__main__":
    main()