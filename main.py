import requests
import time
import os
import sys
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
        (" _          _______    ______     _______    _______    _______        _______    _         _________", Fore.YELLOW),
        ("( (    /|  (  ___  )  (  __  \\   (  ____ \\  (  ____ \\  (       )      (  ___  )  ( \\        \\__   __/", Fore.YELLOW),
        ("|  \\  ( |  | (   ) |  | (  \\  )  | (    \\/  | (    \\/  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN),
        ("|   \\ | |  | (___) |  | |   ) |  | (__      | (__      | || || |      | (___) |  | |           | |   ", Fore.CYAN),
        ("| (\\ \\) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |      |  ___  |  | |           | |   ", Fore.CYAN),
        ("| | \\   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN),
        ("| )  \\  |  | )   ( |  | (__/  )  | (____/\\  | (____/\\  | )   ( |      | )   ( |  | (____/\\ ___) (___", Fore.YELLOW),
        ("|/    )_)  |/     \\|  (______/   (_______/  (_______/  |/     \\|      |/     \\|  (_______/ \\_______/", Fore.YELLOW),
        ("               <<━━━━━━━━━━━━━━━━━━⏮️⚓𝘽𝙍𝙊𝙆𝙀𝙉-𝙉𝘼𝘿𝙀𝙀𝙈⚓⏭️━━━━━━━━━━━━━━━━━>>", Fore.YELLOW)
    ]
    for line, color in logo_lines:
        typing_effect(line, 0.005, color)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<══════════════════════════════════════BROKEN NADEEM HERE═══════════════════════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def fetch_profile_name(access_token):
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except:
        return "Unknown"

def fetch_target_name(target_id, access_token):
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except:
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
    try:
        response = requests.get("https://graph.facebook.com/me/groups", params={"access_token": token})
        data = response.json()
        groups = data.get("data", [])
        if not groups:
            print(Fore.YELLOW + "[!] NO GROUPS FOUND OR TOKEN LACKS PERMISSIONS.")
        else:
            print(Fore.CYAN + "[📋] GROUPS YOU'RE IN:")
            for group in groups:
                print(Fore.LIGHTGREEN_EX + f"➤ {group['name']} | UID: {group['id']}")
    except Exception as e:
        print(Fore.RED + f"[✖] ERROR: {e}")

def disconnect_fuker_urls():
    typing_effect("【⚠️】 ENTER 4 FUKER URLs TO DISCONNECT", 0.02, Fore.YELLOW)
    for i in range(4):
        url = animated_input(f"[URL {i+1}] ➜")
        typing_effect(f"Disconnecting {url}...", 0.02, Fore.RED)
        time.sleep(1)
        typing_effect(f"【✔】 DISCONNECTED: {url}", 0.02, Fore.GREEN)

def post_loader_spammer():
    tokens_file = animated_input("【📕】 ENTER TOKEN FILE ➜")
    post_uid = animated_input("【🧿】 ENTER PUBLIC POST UID ➜")
    hater_name = animated_input("【💀】 ENTER HATER NAME ➜")
    speed = float(animated_input("【⏰】 ENTER DELAY (sec) ➜"))
    messages_file = animated_input("【📝】 ENTER MESSAGE FILE ➜")

    with open(tokens_file, "r") as tf:
        tokens = [token.strip() for token in tf.readlines()]
    with open(messages_file, "r") as mf:
        messages = mf.readlines()

    token_profiles = {token: fetch_profile_name(token) for token in tokens}

    index = 0
    while True:
        token = tokens[index % len(tokens)]
        name = token_profiles.get(token, "Unknown")
        message = f"{hater_name} {messages[index % len(messages)].strip()}"
        try:
            response = requests.post(f"https://graph.facebook.com/{post_uid}/comments", data={
                "access_token": token,
                "message": message
            })
            response.raise_for_status()
            typing_effect(f"[📤] SENT BY: {name} ➜ {message}", 0.01, Fore.LIGHTGREEN_EX)
        except Exception as e:
            typing_effect(f"[✖] FAILED TO SEND BY {name}", 0.01, Fore.RED)
        index += 1
        time.sleep(speed)

def main():
    clear_screen()
    display_animated_logo()
    typing_effect("Choose Mode:", 0.02, Fore.LIGHTMAGENTA_EX)
    typing_effect("1. TOKEN CHECKER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("2. GROUP UID FETCHER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("3. MESSAGE SPAMMER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("4. FUKER URL DISCONNECTOR", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("5. POST LOADER SPAMMER", 0.02, Fore.LIGHTBLUE_EX)

    choice = animated_input("ENTER YOUR CHOICE [1/2/3/4/5] ➜")

    if choice == "1":
        token_checker()
    elif choice == "2":
        group_uid_fetcher()
    elif choice == "3":
        pastebin_url = "https://pastebin.com/raw/kMBpBe88"
        owner = requests.get(pastebin_url).text.strip()
        user_owner = animated_input("【👑】 ENTER OWNER NAME ➜")
        if user_owner != owner:
            typing_effect("[✖] WRONG OWNER NAME.", 0.02, Fore.RED)
            return
        tokens_file = animated_input("【📕】 ENTER TOKEN FILE ➜")
        target_id = animated_input("【🧿】 ENTER CONVO UID ➜")
        hater_name = animated_input("【💀】 ENTER HATER NAME ➜")
        messages_file = animated_input("【📝】 ENTER MESSAGE FILE ➜")
        speed = float(animated_input("【⏰】 ENTER DELAY (sec) ➜"))
        send_messages(tokens_file, target_id, messages_file, hater_name, speed)
    elif choice == "4":
        disconnect_fuker_urls()
    elif choice == "5":
        post_loader_spammer()
    else:
        typing_effect("INVALID CHOICE. EXITING.", 0.02, Fore.RED)

if __name__ == "__main__":
    main()
