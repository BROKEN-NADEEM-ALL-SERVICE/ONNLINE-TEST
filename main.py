import requests
import time
import os
import sys
import uuid
import threading
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_animated_logo():
    clear_screen()
    logo_lines = [
        (" _          _______    ______     _______    _______    _______        _______    _         ", Fore.YELLOW),
        ("( (    /|  (  ___  )  (  __  \   (  ____ \  (  ____ \  (       )      (  ___  )  ( \        \   /", Fore.YELLOW),
        ("|  \  ( |  | (   ) |  | (  \  )  | (    \/  | (    \/  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN),
        ("|   \ | |  | () |  | |   ) |  | (      | (      | || || |      | () |  | |           | |   ", Fore.CYAN),
        ("| (\ \) |  |  ___  |  | |   | |  |  __)     |  __)     | |()| |      |  ___  |  | |           | |   ", Fore.CYAN),
        ("| | \   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN),
        ("| )  \  |  | )   ( |  | (/  )  | (/\  | (/\  | )   ( |      | )   ( |  | (/\ ) (", Fore.YELLOW),
        ("|/    ))  |/     \|  (/   (/  (/  |/     \|      |/     \|  (/ \_/", Fore.YELLOW),
        ("         ╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────────────────╮", Fore.CYAN),
        ("         │                 【•】 YOUR COUNTRY  ➤ INDIA                                   │", Fore.CYAN),
        ("         │                 【•】 YOUR REGION   ➤ BIHAR                                   │", Fore.CYAN),
        ("         │                 【•】 YOUR CITY     ➤ PATNA                                   │", Fore.CYAN),
        ("         ╰────────────────────────────< ~ COUNTRY ~  >────────────────────────────────────╯", Fore.CYAN),
        ("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗", Fore.YELLOW),
        ("║  NAME             : BROKEN-NADEEM           GOD ABBUS               RAKHNA                      ║", Fore.CYAN),
        ("║  RULLEX           : PATNA ON FIRE           KARNE PE               SAB GOD                      ║", Fore.GREEN),
        ("║  FORM 🏠          : BIHAR-PATNA             APPEARED               ABBUS BANA                   ║", Fore.CYAN),
        ("║  BRAND            : MULTI CONVO             HATA DIYA              HAI BILKUL                   ║", Fore.GREEN),
        ("║  GitHub           : BROKEN NADEEM           JAAEGA YE              KOI BHI HO                   ║", Fore.CYAN),
        ("║  WHATSAP          : +917209101285           BAAT YWAD              GOD ABBUS NO                 ║", Fore.GREEN),
        ("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝", Fore.YELLOW),
    ]
    for line, color in logo_lines:
        typing_effect(line, 0.005, color)
    typing_effect("               <<━━━━━━━━━━━━━━━━━━⏮️⚓𝘽𝙍𝙊𝙆𝙀𝙉-𝙉𝘼𝘿𝙀𝙀𝙈⚓⏭️━━━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<══════════════════════════════════════BROKEN NADEEM HERE═══════════════════════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)

def fetch_profile_name(access_token):
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except requests.exceptions.RequestException:
        return "Unknown"

def fetch_target_name(target_id, access_token):
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except requests.exceptions.RequestException:
        return "Unknown Target"

def token_checker():
    token = animated_input("【🔑】 ENTER ACCESS TOKEN TO CHECK ➜")
    profile = fetch_profile_name(token)
    if profile == "Unknown":
        print(Fore.RED + "[✖] INVALID TOKEN.")
    else:
        print(Fore.GREEN + f"[✔] VALID TOKEN. PROFILE NAME: {profile}")

def group_uid_fetcher():
    token = animated_input("【🔑】 ENTER VALID TOKEN ➜")
    url = "https://graph.facebook.com/me/groups"
    params = {"access_token": token}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        groups = data.get("data", [])
        if not groups:
            print(Fore.YELLOW + "[!] NO GROUPS FOUND OR TOKEN LACKS PERMISSIONS.")
        else:
            print(Fore.CYAN + "[📋] GROUPS YOU'RE IN:")
            for group in groups:
                print(Fore.LIGHTGREEN_EX + f"➤ {group['name']} | UID: {group['id']}")
    except Exception as e:
        print(Fore.RED + f"[✖] ERROR FETCHING GROUPS: {str(e)}")

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]
    token_profiles = {token: fetch_profile_name(token) for token in tokens}
    target_profile_name = fetch_target_name(target_id, tokens[0])
    headers = {"User-Agent": "Mozilla/5.0"}
    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"
            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                print(Fore.YELLOW + f"\n<<═══════BROTHER══════NADEEM DONE══════SAHIL DONE══════>>")
                typing_effect(f"[🎉] MESSAGE {message_index + 1} SENT!", 0.02, Fore.CYAN)
                typing_effect(f"[👤] SENDER: {sender_name}", 0.02, Fore.WHITE)
                typing_effect(f"[📩] TARGET: {target_profile_name} ({target_id})", 0.02, Fore.MAGENTA)
                typing_effect(f"[📨] MESSAGE: {full_message}", 0.02, Fore.LIGHTGREEN_EX)
                typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)
                print(Fore.YELLOW + f"<<═══════BROTHER══════NADEEM DONE══════SAHIL DONE══════>>\n")
            except requests.exceptions.RequestException:
                continue
            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting...\n")

def show_loader(stop_event):
    loader_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    i = 0
    while not stop_event.is_set():
        print(Fore.YELLOW + f"\r[⏳] LOADING {loader_chars[i % len(loader_chars)]}", end='', flush=True)
        time.sleep(0.1)
        i += 1
    print("\r" + " " * 30, end="\r")

def offline_spammer():
    token_file = animated_input("【📕】 ENTER TOKEN FILE ➜")
    target_id = animated_input("【🖇️】 ENTER CONVO UID ➜")
    hater_name = animated_input("【🖊️】 ENTER HATER NAME ➜")
    message_file = animated_input("【📝】 ENTER MESSAGE FILE ➜")
    delay = float(animated_input("【⏰】 ENTER DELAY (sec) ➜"))
    unique_key = str(uuid.uuid4())[:8]
    print(Fore.LIGHTMAGENTA_EX + f"\n[🔑] YOUR UNIQUE STOP KEY: {unique_key} (TO STOP: touch .stop_{unique_key})\n")

    stop_event = threading.Event()
    loader_thread = threading.Thread(target=show_loader, args=(stop_event,))
    loader_thread.start()

    try:
        with open(message_file, "r") as mf:
            messages = mf.readlines()
        with open(token_file, "r") as tf:
            tokens = [t.strip() for t in tf.readlines()]
        token_profiles = {t: fetch_profile_name(t) for t in tokens}
        target_profile = fetch_target_name(target_id, tokens[0])
    except Exception as e:
        stop_event.set()
        loader_thread.join()
        print(Fore.RED + f"[✖] ERROR: {str(e)}")
        return

    stop_event.set()
    loader_thread.join()
    print(Fore.GREEN + "\n[✔] LOADING COMPLETE. STARTING SPAMMER...\n")

    try:
        while True:
            for idx, msg in enumerate(messages):
                token = tokens[idx % len(tokens)]
                sender = token_profiles.get(token, "Unknown")
                full_msg = f"{hater_name} {msg.strip()}"
                url = f"https://graph.facebook.com/v17.0/t_{target_id}"
                headers = {"User-Agent": "Mozilla/5.0"}
                data = {"access_token": token, "message": full_msg}
                try:
                    response = requests.post(url, json=data, headers=headers)
                    response.raise_for_status()
                    print(Fore.GREEN + f"[{idx+1}] SENT BY: {sender} ➤ MESSAGE: {full_msg}")
                except:
                    print(Fore.RED + f"[!] FAILED TO SEND BY: {sender}")
                time.sleep(delay)
                if os.path.exists(f".stop_{unique_key}"):
                    print(Fore.RED + f"\n[✋] STOP FILE DETECTED. EXITING...")
                    os.remove(f".stop_{unique_key}")
                    return
    except KeyboardInterrupt:
        print(Fore.RED + "\n[✋] MANUAL INTERRUPT. EXITING...")

def main():
    clear_screen()
    display_animated_logo()
    typing_effect("Choose Mode:", 0.02, Fore.LIGHTMAGENTA_EX)
    typing_effect("1. TOKEN CHECKER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("2. CONVO GROUP UID FETCHER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("3. START MESSAGE SPAMMER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("4. OFFLINE TERMUX SPAMMER", 0.02, Fore.LIGHTBLUE_EX)
    choice = animated_input("Enter your choice [1/2/3/4] ➜")

    if choice == "1":
        token_checker()
    elif choice == "2":
        group_uid_fetcher()
    elif choice == "3":
        pastebin_url = "https://pastebin.com/raw/kMBpBe88"
        correct_password = fetch_password_from_pastebin(pastebin_url)
        entered_password = animated_input("【👑】 ENTER OWNER NAME ➜")
        if entered_password != correct_password:
            print(Fore.RED + "[x] Incorrect OWNER NAME. Exiting.")
            exit(1)
        tokens_file = animated_input("【📕】 ENTER TOKEN FILE ➜")
        target_id = animated_input("【🖇️】 ENTER CONVO UID ➜")
        haters_name = animated_input("【🖊️】 ENTER HATER NAME ➜")
        messages_file = animated_input("【📝】 ENTER MESSAGE FILE ➜")
        speed = float(animated_input("【⏰】 ENTER DELAY (sec) ➜"))
        send_messages(tokens_file, target_id, messages_file, haters_name, speed)
    elif choice == "4":
        offline_spammer()
    else:
        print(Fore.RED + "[!] Invalid Choice.")

if __name__ == "__main__":
    main()
