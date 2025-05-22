import os
import uuid
import time
import requests
import sys
import multiprocessing
from colorama import init, Fore

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<══════════════════════════════BROKEN NADEEM HERE══════════════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def display_animated_logo():
    clear_screen()
    typing_effect("<<━━━━━━BROKEN NADEEM WELCOMES YOU━━━━━━>>", 0.01, Fore.YELLOW)
    time.sleep(1)

def read_tokens(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def read_messages(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def send_message(token, convo_uid, message):
    url = f"https://graph.facebook.com/v18.0/{convo_uid}/messages"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "messaging_type": "MESSAGE_TAG",
        "tag": "ACCOUNT_UPDATE",
        "recipient": f'{{"thread_key":"{convo_uid}"}}',
        "message": f'{{"text":"{message}"}}'
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.status_code, response.text
    except Exception as e:
        return 0, str(e)

def spammer_process(tokens_file, convo_uid, hater_name, message_file, delay, stop_key):
    tokens = read_tokens(tokens_file)
    messages = read_messages(message_file)
    index = 0
    while True:
        for token in tokens:
            message = messages[index % len(messages)]
            status, _ = send_message(token, convo_uid, message)
            print(Fore.CYAN + f"[SENT] {message[:30]}... | Token: {token[:10]} | Status: {status}")
            index += 1
            time.sleep(float(delay))

def start_persistent_spammer():
    tokens_file = animated_input("【📕】 ENTER TOKEN FILE ➜")
    convo_uid = animated_input("【🖇️】 ENTER CONVO UID ➜")
    hater_name = animated_input("【🖊️】 ENTER HATER NAME ➜")
    message_file = animated_input("【📝】 ENTER MESSAGE FILE ➜")
    delay = animated_input("【⏰】 ENTER DELAY (sec) ➜")

    stop_key = str(uuid.uuid4())[:8]
    p = multiprocessing.Process(target=spammer_process, args=(tokens_file, convo_uid, hater_name, message_file, delay, stop_key))
    p.start()

    with open("stop_keys.txt", "a") as f:
        f.write(f"{stop_key}:{p.pid}\n")

    print(Fore.GREEN + f"[✔] SPAMMER STARTED SUCCESSFULLY.")
    print(Fore.CYAN + f"[🔑] STOP KEY: {stop_key}")
    print(Fore.YELLOW + "Use NOUMBER 5 and enter this key to stop the spammer anytime.")

def stop_spammer():
    stop_key = animated_input("【⛔】 ENTER STOP KEY ➜")

    if not os.path.exists("stop_keys.txt"):
        print(Fore.RED + "[✖] NO SPAMMERS RUNNING.")
        return

    found = False
    with open("stop_keys.txt", "r") as f:
        lines = f.readlines()

    with open("stop_keys.txt", "w") as f:
        for line in lines:
            key, pid = line.strip().split(":")
            if key == stop_key:
                try:
                    os.kill(int(pid), 9)
                    print(Fore.GREEN + f"[✔] SPAMMER STOPPED (PID: {pid})")
                    found = True
                except Exception as e:
                    print(Fore.RED + f"[✖] ERROR STOPPING PROCESS: {e}")
            else:
                f.write(line)

    if not found:
        print(Fore.RED + "[✖] INVALID STOP KEY.")

def main():
    display_animated_logo()
    typing_effect("Choose Mode:", 0.02, Fore.LIGHTMAGENTA_EX)
    typing_effect("1. TOKEN CHECKER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("2. CONVO GROUP UID FETCHER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("3. START MESSAGE SPAMMER (MANUAL)", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("4. START MESSAGE SPAMMER (NONSTOP) - NOUMBER 4", 0.02, Fore.LIGHTGREEN_EX)
    typing_effect("5. STOP MESSAGE SPAMMER (STOP KEY) - NOUMBER 5", 0.02, Fore.LIGHTRED_EX)
    choice = animated_input("Enter your choice [1/2/3/4/5] ➜")

    if choice == "4":
        start_persistent_spammer()
    elif choice == "5":
        stop_spammer()
    else:
        print(Fore.RED + "[!] Other features not included in this version.")

if __name__ == "__main__":
    multiprocessing.set_start_method('fork')  # For UNIX systems
    main()
