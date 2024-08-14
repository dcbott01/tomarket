import requests
import time
from colorama import Fore, Style, init
import json
from datetime import datetime, timedelta
import random

# Initialize Colorama
init()

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,en-US;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://mini-app.tomarket.ai',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://mini-app.tomarket.ai/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': 'Android',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36',
    'x-requested-with': 'org.telegram.messenger.web'
}

def get_balance(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/user/balance'
    headers['Authorization'] = token
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

def claim_daily(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/daily/claim'
    headers['Authorization'] = token
    payload = {"game_id": "fa873d13-d831-4d6f-8aee-9cff7a1d0db1"}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def start_farming(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/farm/start'
    headers['Authorization'] = token
    payload = {"game_id": "53b22103-c7ff-413d-bc63-20f6fb806a07"}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None
    
def claim_farming(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/farm/claim'
    headers['Authorization'] = token
    payload = {"game_id": "53b22103-c7ff-413d-bc63-20f6fb806a07"}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def play_game(token):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/game/play'
    headers['Authorization'] = token
    payload = {"game_id": "59bcd12e-04e2-404c-a172-311a0084587d"}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def claim_game(token, point):
    url = 'https://api-web.tomarket.ai/tomarket-game/v1/game/claim'
    headers['Authorization'] = token
    payload = {"game_id": "59bcd12e-04e2-404c-a172-311a0084587d", "points": point}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json(), response.status_code
    except json.JSONDecodeError:
        print(f"JSON Decode Error: Token Invalid")
        return None, None
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None, None

def get_random_color():
    return random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])

def print_welcome_message():
    print(r"""
 
  _  _   _    ____  _   ___    _   
 | \| | /_\  |_  / /_\ | _ \  /_\  
 | .` |/ _ \  / / / _ \|   / / _ \ 
 |_|\_/_/ \_\/___/_/ \_\_|_\/_/ \_\
                                   

    """)
    print(Fore.GREEN + Style.BRIGHT + "TOMARKET BOT")
    print(Fore.CYAN + Style.BRIGHT + "Jajanin dong orang baik :)")
    print(Fore.YELLOW + Style.BRIGHT + "0x5bc0d1f74f371bee6dc18d52ff912b79703dbb54")
    print(Fore.RED + Style.BRIGHT + "Update Link: https://github.com/dcbott01/tomarket")
    print(Fore.BLUE + Style.BRIGHT + "Tukang Rename MATI AJA")

def main():
    tokens = []
    try:
        with open('tokens.txt', 'r') as token_file:
            tokens = token_file.readlines()
    except FileNotFoundError:
        pass

    while True:
        print_welcome_message()
        for i, token in enumerate(tokens):
            token = token.strip()
            print(f"{Fore.YELLOW+Style.BRIGHT}======== Processing Account {i + 1} of {len(tokens)} ========")

            print(f"{Fore.YELLOW+Style.BRIGHT}Getting balance..", end="\r", flush=True)
            balance_response = get_balance(token)
            if balance_response is not None:
                balance = float(balance_response['data'].get('available_balance'))
                balance = int(balance)  # Convert to integer to remove decimal part
                tiket = balance_response['data'].get('play_passes')
                print(f"{get_random_color()}{Style.BRIGHT}[ Balance ]: {balance} {Style.RESET_ALL}           ", flush=True)
                print(f"{get_random_color()}{Style.BRIGHT}[ Tiket ]: {tiket} {Style.RESET_ALL}           ", flush=True)
                print(f"{Fore.YELLOW+Style.BRIGHT}[ Daily ]: Claiming.. {Style.RESET_ALL}", end="\r", flush=True)
                time.sleep(2)
                daily, daily_status_code = claim_daily(token)
                if daily_status_code == 400:
                    if daily['message'] == 'already_check':
                        day = daily['data']['check_counter']
                        point = daily['data']['today_points']
                        print(f"{get_random_color()}{Style.BRIGHT}[ Daily ]: Day {day} Already checkin | {point} Point{Style.RESET_ALL}", flush=True)
                    else:
                        print(f"{Fore.RED+Style.BRIGHT}[ Daily ]: Gagal {daily} {Style.RESET_ALL}", flush=True)
                elif daily_status_code == 200:
                    day = daily['data']['check_counter']
                    point = daily['data']['today_points']
                    print(f"{get_random_color()}{Style.BRIGHT}[ Daily ]: Day {day} Claimed | {point} Point{Style.RESET_ALL}", flush=True)
                else:
                    print(f"{Fore.RED+Style.BRIGHT}[ Daily ]: Gagal {daily} {Style.RESET_ALL}", flush=True)

                print(f"{Fore.YELLOW+Style.BRIGHT}[ Farming ]: Checking.. {Style.RESET_ALL}", end="\r", flush=True)
                time.sleep(2)
                farming, farming_status_code = start_farming(token)
                if farming_status_code == 200:
                    end_time = datetime.fromtimestamp(farming['data']['end_at'])
                    remaining_time = end_time - datetime.now()
                    hours, remainder = divmod(remaining_time.total_seconds(), 3600)
                    minutes, _ = divmod(remainder, 60)
                    print(f"{get_random_color()}{Style.BRIGHT}[ Farming ]: Started. Claim in: {int(hours)} jam {int(minutes)} menit {Style.RESET_ALL}", flush=True)
                    if datetime.now() > end_time:
                        print(f"{Fore.YELLOW+Style.BRIGHT}[ Farming ]: Claiming.. {Style.RESET_ALL}", end="\r", flush=True)
                        claim_response, claim_status_code = claim_farming(token)
                        if claim_status_code == 200:
                            poin = claim_response["data"]["claim_this_time"]
                            print(f"{get_random_color()}{Style.BRIGHT}[ Farming ]: Success Claim Farming! Reward: {poin} {Style.RESET_ALL}       ", flush=True)
                            print(f"{Fore.YELLOW+Style.BRIGHT}[ Farming ]: Starting.. {Style.RESET_ALL}", end="\r", flush=True)
                            time.sleep(2)
                            farming, farming_status_code = start_farming(token)
                            if farming_status_code == 200:
                                end_time = datetime.fromtimestamp(farming['data']['end_at'])
                                remaining_time = end_time - datetime.now()
                                hours, remainder = divmod(remaining_time.total_seconds(), 3600)
                                minutes, _ = divmod(remainder, 60)
                                print(f"{get_random_color()}{Style.BRIGHT}[ Farming ]: Started. Claim in: {int(hours)} jam {int(minutes)} menit {Style.RESET_ALL}", flush=True)

                        else:
                            print(f"{Fore.RED+Style.BRIGHT}Failed to claim farming: {claim_response} {Style.RESET_ALL}          ", flush=True)
                elif farming_status_code == 500:
                    if farming['message'] == 'game already started':
                        end_time = datetime.fromtimestamp(farming['data']['end_at'])
                        remaining_time = end_time - datetime.now()
                        hours, remainder = divmod(remaining_time.total_seconds(), 3600)
                        minutes, _ = divmod(remainder, 60)
                        print(f"{Fore.CYAN+Style.BRIGHT}[ Farming ]: Already Started. Claim in: {int(hours)} jam {int(minutes)} menit {Style.RESET_ALL}", flush=True)
                        
                        # Check if current time is past end_time
                        if datetime.now() > end_time:
                            print(f"{Fore.YELLOW+Style.BRIGHT}[ Farming ]: Claiming.. {Style.RESET_ALL}", end="\r", flush=True)
                            claim_response, claim_status_code = claim_farming(token)
                            if claim_status_code == 200:
                                poin = claim_response["data"]["claim_this_time"]
                                print(f"{get_random_color()}{Style.BRIGHT}Success claim farming! Reward: {poin} {Style.RESET_ALL}", flush=True)
                                print(f"{Fore.YELLOW+Style.BRIGHT}[ Farming ]: Starting.. {Style.RESET_ALL}", end="\r", flush=True)
                                time.sleep(2)
                                farming, farming_status_code = start_farming(token)
                                if farming_status_code == 200:
                                    end_time = datetime.fromtimestamp(farming['data']['end_at'])
                                    remaining_time = end_time - datetime.now()
                                    hours, remainder = divmod(remaining_time.total_seconds(), 3600)
                                    minutes, _ = divmod(remainder, 60)
                                    print(f"{get_random_color()}{Style.BRIGHT}[ Farming ]: Started. Claim in: {int(hours)} jam {int(minutes)} menit {Style.RESET_ALL}", flush=True)

                            else:
                                print(f"{Fore.RED+Style.BRIGHT}Failed to claim farming: {claim_response} {Style.RESET_ALL}", flush=True)
                    else:
                        print(f"{get_random_color()}{Style.BRIGHT}[ Farming ]: Error. {farming} {Style.RESET_ALL}", flush=True)
                else:
                    print(f"{get_random_color()}{Style.BRIGHT}[ Farming ]: Error {farming} {Style.RESET_ALL}", flush=True)
                
                while tiket > 0:
                    print(f"{get_random_color()}{Style.BRIGHT}[ Game ]: Starting Game..", end="\r", flush=True)
                    play, play_status = play_game(token)
                    if play_status != 200:
                        print(f"{Fore.RED+Style.BRIGHT}[ Game ]: Failed to start game!       {Style.RESET_ALL}", flush=True)
                    else:
                        print(f"{get_random_color()}{Style.BRIGHT}[ Game ]: Game Started! {Style.RESET_ALL}                      ", flush=True)
                        for _ in range(30):
                            print(f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])+Style.BRIGHT}[ Game ]: Playing game, waktu sisa {30 - _} detik {Style.RESET_ALL}", end="\r", flush=True)
                            time.sleep(1)
                        print(f"{Fore.YELLOW+Style.BRIGHT}[ Game ]: Game Berakhir! Claiming..                                       ", end="\r", flush=True)
                        point = random.randint(400, 600)
                        claim, claim_status = claim_game(token, point)
                        if claim_status != 200:
                            print(f"{Fore.RED+Style.BRIGHT}[ Game ]: Failed to claim game points! {Style.RESET_ALL}", flush=True)
                        else:
                            print(f"{get_random_color()}{Style.BRIGHT}[ Game ]: Success. Mendapatkan {point} Poin {Style.RESET_ALL}                    ", flush=True)

                        tiket -= 1

        print(Fore.BLUE + Style.BRIGHT + f"\n==========SEMUA AKUN TELAH DI PROSES==========\n",  flush=True)    
        for _ in range(1800):
            minutes, seconds = divmod(1800 - _, 60)
            print(f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])+Style.BRIGHT}==== [ Semua akun telah diproses, Looping berikutnya {minutes} menit {seconds} detik ] ===={Style.RESET_ALL}", end="\r", flush=True)
            time.sleep(1)         
        
if __name__ == "__main__":
    main()
