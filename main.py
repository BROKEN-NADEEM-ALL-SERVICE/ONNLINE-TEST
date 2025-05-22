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
        ("╔══════════════════════════════════════ YOUR DETAILS ══════════════════════════════════════╗", Fore.CYAN),
        ("║  NAME             : BROKEN-NADEEM      │  CITY    : PATNA    │  REGION : BIHAR           ║", Fore.CYAN),
        ("║  BRAND            : MULTI CONVO        │  OWNER   : GOD ABBUS│  ID     : +917209101285   ║", Fore.GREEN),
        ("╚══════════════════════════════════════════════════════════════════════════════════════════╝", Fore.YELLOW),
    ]
    for line, color in logo_lines:
        typing_effect(line, 0.005, color)
    typing_effect("<<━━━━━━━━━━━━━━━━━━⏮️⚓BROKEN-NADEEM⚓⏭️━━━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<══════════════════════════════BROKEN NADEEM═══════════════════════════════>>}")
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
    url = "https://graph.facebook.com/me/groups"
    params = {"access_token": token}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "error" in data:
            raise Exception(data["error"]["message"])
        groups = data.get("data", [])
        if not groups:
            print(Fore.YELLOW + "[!] NO GROUPS FOUND OR TOKEN LACKS PERMISSIONS.")
        else:
            print(Fore.CYAN + "[📋] GROUPS YOU'RE IN:")
            for group in groups:
                print(Fore.LIGHTGREEN_EX + f"➤ {group['name']} | UID: {group['id']}")
    except Exception as e:
        print(Fore.RED + f"[✖] ERROR: {e}")

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as f: messages = f.readlines()
    with open(tokens_file, "r") as f: tokens = [t.strip() for t in f.readlines()]
    token_profiles = {t: fetch_profile_name(t) for t in tokens}
    target_name = fetch_target_name(target_id, tokens[0])
    headers = {"User-Agent": "Mozilla/5.0"}

    while True:
        for i, msg in enumerate(messages):
            token = tokens[i % len(tokens)]
            full_msg = f"{haters_name} {msg.strip()}"
            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            payload = {"access_token": token, "message": full_msg}
            try:
                r = requests.post(url, json=payload, headers=headers)
                if r.status_code != 200 or "error" in r.text:
                    error_data = r.json().get("error", {}).get("message", "")
                    print(Fore.RED + f"[!] TOKEN ERROR SKIPPED: {error_data}")
                    continue
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                print(Fore.YELLOW + f"\n<<═══════ MESSAGE SENT >>")
                typing_effect(f"[✔] SENDER: {token_profiles.get(token)}", 0.02, Fore.LIGHTGREEN_EX)
                typing_effect(f"[➤] TO: {target_name} ({target_id})", 0.02, Fore.CYAN)
                typing_effect(f"[✉] MESSAGE: {full_msg}", 0.02, Fore.LIGHTBLUE_EX)
                typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)
            except Exception as e:
                print(Fore.RED + f"[✖] ERROR: {e}")
            time.sleep(speed)

def extract_eaab_token_from_cookie(cookie):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "/",
        "Referer": "https://business.facebook.com/",
        "Origin": "https://business.facebook.com",
        "Host": "business.facebook.com",
        "Cookie": cookie
    }

    try:
        print(Fore.YELLOW + "[⌛] VERIFYING COOKIE...")
        time.sleep(2)
        response = requests.get("https://business.facebook.com/business_locations", headers=headers)
        if "EAAB" in response.text:
            start = response.text.find("EAAB")
            end = response.text.find('"', start)
            token = response.text[start:end]
            typing_effect("<<💥 TOKEN GRENADE DETONATED >>", 0.04, Fore.LIGHTRED_EX)
            typing_effect(f"[✔] EAAB TOKEN ➤ {token}", 0.03, Fore.LIGHTGREEN_EX)
        else:
            print(Fore.RED + "[✖] NO TOKEN FOUND.")
    except Exception as e:
        print(Fore.RED + f"[✖] ERROR: {e}")

def main():
    clear_screen()
    display_animated_logo()
    typing_effect("1. TOKEN CHECKER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("2. GROUP UID FETCHER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("3. START SPAMMER", 0.02, Fore.LIGHTBLUE_EX)
    typing_effect("4. COOKIE TO EAAB TOKEN", 0.02, Fore.LIGHTBLUE_EX)
    choice = animated_input("ENTER OPTION ➤")

    if choice == "1":
        token_checker()
    elif choice == "2":
        group_uid_fetcher()
    elif choice == "3":
        paste_url = "https://pastebin.com/raw/kMBpBe88"
        correct_pass = fetch_password_from_pastebin(paste_url)
        entered_pass = animated_input("【👑】 ENTER OWNER NAME ➜")
        if entered_pass != correct_pass:
            print(Fore.RED + "[✖] INCORRECT OWNER NAME.")
            exit()
        tokens_file = animated_input("【📕】 TOKEN FILE ➜")
        target_id = animated_input("【🧾】 CONVO UID ➜")
        messages_file = animated_input("【🗒️】 MESSAGE FILE ➜")
        hater_prefix = animated_input("【💀】 HATER NAME ➜")
        speed = float(animated_input("【⏱️】 DELAY (sec) ➜"))
        send_messages(tokens_file, target_id, messages_file, hater_prefix, speed)
    elif choice == "4":
        cookie = animated_input("【🍪】 ENTER COOKIE ➜")
        extract_eaab_token_from_cookie(cookie)
    else:
        print(Fore.RED + "[✖] INVALID CHOICE.")

if __name__ == "__main__":
    main()
