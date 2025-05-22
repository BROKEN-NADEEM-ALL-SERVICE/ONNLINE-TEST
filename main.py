import requests
import time
import os
from colorama import init, Fore

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
        ("( (    /|  (  ___  )  (  __  \\   (  ____ \\  (  ____ \\  (       )      (  ___  )  ( \\        \\   /", Fore.YELLOW),
        ("|  \\  ( |  | (   ) |  | (  \\  )  | (    /  | (    /  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN),
        ("|   \\ | |  | () |  | |   ) |  | (      | (      | || || |      | () |  | |           | |   ", Fore.CYAN),
        ("| (\\ ) |  |  ___  |  | |   | |  |  __)     |  __)     | |()| |      |  ___  |  | |           | |   ", Fore.CYAN),
        ("| | \\   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN),
        ("| )  \\  |  | )   ( |  | (/  )  | (\\  | (\\  | )   ( |      | )   ( |  | (\\ ) (", Fore.YELLOW),
        ("|/    ))  |/     |  (/   (/  (/  |/     |      |/     |  (/ _/", Fore.YELLOW),
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

def extract_eaab_token_from_cookie(cookie):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Referer": "https://business.facebook.com/",
        "Host": "business.facebook.com",
        "Origin": "https://business.facebook.com",
        "Cookie": cookie
    }
    try:
        response = requests.get("https://business.facebook.com/business_locations", headers=headers)
        eaab_token = None
        if "EAAB" in response.text:
            start = response.text.find("EAAB")
            end = response.text.find('"', start)
            eaab_token = response.text[start:end]
        if eaab_token:
            print(Fore.GREEN + f"[✔] EAAB TOKEN EXTRACTED: {eaab_token}")
        else:
            print(Fore.RED + "[✖] FAILED TO EXTRACT EAAB TOKEN.")
    except Exception as e:
        print(Fore.RED + f"[✖] ERROR: {e}")

def main():
    clear_screen()
    display_animated_logo()
    typing_effect("Choose Mode:", 0.02, Fore.LIGHTMAGENTA_EX)
    typing_effect("1. TOKEN CHECKER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("2. CONVO GROUP UID FETCHER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("3. START MESSAGE SPAMMER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("4. COOKIE TO EAAB TOKEN", 0.02, Fore.LIGHTBLUE_EX)
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
            print(Fore.RED + "[✖] Incorrect OWNER NAME. Exiting.")
            exit(1)
        tokens_file = animated_input("【📕】 ENTER TOKEN FILE ➜")
        target_id = animated_input("【🖇️】 ENTER CONVO UID ➜")
        messages_file = animated_input("【📃】 ENTER MESSAGE FILE ➜")
        haters_name = animated_input("【🖊️】 ENTER HATER NAME PREFIX ➜")
        speed = float(animated_input("【⏱️】 DELAY BETWEEN MESSAGES (seconds) ➜"))
        send_messages(tokens_file, target_id, messages_file, haters_name, speed)
    elif choice == "4":
        cookie = animated_input("【🍪】 ENTER FACEBOOK COOKIE ➜")
        extract_eaab_token_from_cookie(cookie)
    else:
        print(Fore.RED + "[✖] INVALID CHOICE.")

if __name__ == "__main__":
    main()
