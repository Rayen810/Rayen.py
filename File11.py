import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import random
import urllib3
import json
from tenacity import retry, stop_after_attempt, wait_exponential
from contextlib import contextmanager

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# List of accounts
accounts = [
    "issra2888|issra123456789",
    "elwaerayoub|ayoub123",
    "ayoubelwear|ayoub123",
    "wess.ml|wessml123",
    "nabiljamjem|nabil123456789"
]

# List of sites
sites = [
    {
        "name": "V1",
        "login_url": "https://takipcigir.com/login",
        "send_follower_url": "https://takipcigir.com/tools/send-follower",
        "start_url_template": "https://takipcigir.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V2",
        "login_url": "https://takipcizen.com/login",
        "send_follower_url": "https://takipcizen.com/tools/send-follower",
        "start_url_template": "https://takipcizen.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V3",
        "login_url": "https://takipstar.com/login",
        "send_follower_url": "https://takipstar.com/tools/send-follower",
        "start_url_template": "https://takipstar.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V4",
        "login_url": "https://takipcifox.com/member",
        "send_follower_url": "https://takipcifox.com/tools/send-follower",
        "start_url_template": "https://takipcifox.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V5",
        "login_url": "https://takipciking.com/member",
        "send_follower_url": "https://takipciking.com/tools/send-follower",
        "start_url_template": "https://takipciking.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V6",
        "login_url": "https://bayitakipci.com/memberlogin",
        "send_follower_url": "https://bayitakipci.com/tools/send-follower",
        "start_url_template": "https://bayitakipci.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V7",
        "login_url": "https://fastfollow.in/member",
        "send_follower_url": "https://fastfollow.in/tools/send-follower",
        "start_url_template": "https://fastfollow.in/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V8",
        "login_url": "https://takipcikrali.com/login",
        "send_follower_url": "https://takipcikrali.com/tools/send-follower",
        "start_url_template": "https://takipcikrali.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V9",
        "login_url": "https://takipcimx.net/login",
        "send_follower_url": "https://takipcimx.net/tools/send-follower",
        "start_url_template": "https://takipcimx.net/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V10",
        "login_url": "https://takipciking.net/login",
        "send_follower_url": "https://takipciking.net/tools/send-follower",
        "start_url_template": "https://takipciking.net/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V11",
        "login_url": "https://takipcigen.com/login",
        "send_follower_url": "https://takipcigen.com/tools/send-follower",
        "start_url_template": "https://takipcigen.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V12",
        "login_url": "https://bigtakip.net/login",
        "send_follower_url": "https://bigtakip.net/tools/send-follower",
        "start_url_template": "https://bigtakip.net/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V13",
        "login_url": "https://takipcitime.net/login",
        "send_follower_url": "https://takipcitime.net/tools/send-follower",
        "start_url_template": "https://takipcitime.net/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V14",
        "login_url": "https://takipzan.com/login",
        "send_follower_url": "https://takipzan.com/tools/send-follower",
        "start_url_template": "https://takipzan.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V15",
        "login_url": "https://followersize.net/login",
        "send_follower_url": "https://followersize.net/tools/send-follower",
        "start_url_template": "https://followersize.net/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V16",
        "login_url": "https://birtakipci.net/login",
        "send_follower_url": "https://birtakipci.net/tools/send-follower",
        "start_url_template": "https://birtakipci.net/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V17",
        "login_url": "https://mixtakip.com/login",
        "send_follower_url": "https://mixtakip.com/tools/send-follower",
        "start_url_template": "https://mixtakip.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V18",
        "login_url": "https://instamoda.org/login",
        "send_follower_url": "https://instamoda.org/tools/send-follower",
        "start_url_template": "https://instamoda.org/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V19",
        "login_url": "https://takipcitime.com/login",
        "send_follower_url": "https://takipcitime.com/tools/send-follower",
        "start_url_template": "https://takipcitime.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V20",
        "login_url": "https://birtakipci.com/member",
        "send_follower_url": "https://birtakipci.com/tools/send-follower",
        "start_url_template": "https://birtakipci.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V21",
        "login_url": "https://takipcibase.com/login",
        "send_follower_url": "https://takipcibase.com/tools/send-follower",
        "start_url_template": "https://takipcibase.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V22",
        "login_url": "https://takip88.com/login",
        "send_follower_url": "https://takip88.com/tools/send-follower",
        "start_url_template": "https://takip88.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V23",
        "login_url": "https://followersize.com/member",
        "send_follower_url": "https://followersize.com/tools/send-follower",
        "start_url_template": "https://followersize.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V24",
        "login_url": "https://medyahizmeti.com/member",
        "send_follower_url": "https://medyahizmeti.com/tools/send-follower",
        "start_url_template": "https://medyahizmeti.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V25",
        "login_url": "https://www.hepsitakipci.com/member",
        "send_follower_url": "https://www.hepsitakipci.com/tools/send-follower",
        "start_url_template": "https://www.hepsitakipci.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V26",
        "login_url": "https://takipcimax.com/login",
        "send_follower_url": "https://takipcimax.com/tools/send-follower",
        "start_url_template": "https://takipcimax.com/tools/send-follower/{userID}?formType=send"
    },
    {
        "name": "V27",
        "login_url": "https://takipcimx.com/member",
        "send_follower_url": "https://takipcimx.com/tools/send-follower",
        "start_url_template": "https://takipcimx.com/tools/send-follower/{userID}?formType=send"
    }
]

# Configuration settings
CONFIG = {
    "retry_attempts": 3,
    "min_delay": 1,  # تأخير عشوائي بين 1 و3 ثوانٍ لتجنب الحظر
    "max_delay": 3,
    "min_operation_delay": 2,
    "max_operation_delay": 5,
    "post_success_delay_min": 5,  # تأخير بعد نجاح الإرسال
    "post_success_delay_max": 10
}

# Session management
@contextmanager
def session_manager():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Instagram 146.0.0.27.125 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505FN; a50; exynos9610; en_US; 221134032)',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    })
    try:
        yield session
    finally:
        session.close()

# Site processing function
@retry(stop=stop_after_attempt(CONFIG["retry_attempts"]), wait=wait_exponential(multiplier=1, min=2, max=10))
def process_site(site_name, login_url, send_follower_url, start_url_template, username, password, target_username, stats, repeat_on_success):
    with session_manager() as session:
        # Login
        try:
            login_resp = session.post(login_url, data={"username": username, "password": password}, timeout=10, verify=False)
            time.sleep(random.uniform(CONFIG["min_delay"], CONFIG["max_delay"]))  # تأخير بعد تسجيل الدخول
            if login_resp.status_code != 200:
                print(f" error: Failed to connect to {site_name} ❌ ")
                stats["failed"] += 1
                return False
            print(f" OK: Logged in to {site_name} ✅")
        except requests.exceptions.RequestException as e:
            print(f" error: Connection issue with {site_name} ❌ ")
            stats["failed"] += 1
            return False

        while True:
            try:
                # Access the send follower page
                page_resp = session.get(send_follower_url, timeout=10, verify=False)
                time.sleep(random.uniform(CONFIG["min_delay"], CONFIG["max_delay"]))  # تأخير بعد الوصول إلى الصفحة
                if page_resp.status_code != 200:
                    print(f" error: Failed to access the send follower page ❌ ")
                    stats["failed"] += 1
                    return False
                print(" OK: Accessed the send page ✅")

                # Parse the page
                soup = BeautifulSoup(page_resp.text, "html.parser")
                form = None
                # Search for the "Kullanıcıyı Bul" button
                for f in soup.find_all("form"):
                    btn = f.find("button", string=lambda t: t and "Kullanıcıyı Bul" in t)
                    if btn:
                        form = f
                        break
                # Search for the "username" field
                if not form:
                    for f in soup.find_all("form"):
                        if f.find("input", {"name": "username"}):
                            form = f
                            break
                # First form if other methods fail
                if not form:
                    form = soup.find("form")
                
                if not form:
                    print(" error: Form not found ❌ ")
                    stats["failed"] += 1
                    return False
                print(" OK: Form found ✅")

                # Prepare form data
                action = urljoin(send_follower_url, form.get("action", send_follower_url))
                post_data = {input_tag.get("name"): input_tag.get("value", "") for input_tag in form.find_all("input") if input_tag.get("name")}
                post_data["username"] = target_username

                # Submit the form
                submit_resp = session.post(action, data=post_data, timeout=10, verify=False)
                time.sleep(random.uniform(CONFIG["min_delay"], CONFIG["max_delay"]))  # تأخير بعد إرسال النموذج
                if submit_resp.status_code != 200:
                    print(" error: Failed to submit the form ❌ ")
                    stats["failed"] += 1
                    return False
                print(" OK: Form submitted 📤")

                # Parse form response
                soup2 = BeautifulSoup(submit_resp.text, "html.parser")
                adet_input = soup2.find("input", {"name": "adet"})
                userID_input = soup2.find("input", {"name": "userID"})
                userName_input = soup2.find("input", {"name": "userName"})

                if not all([adet_input, userID_input, userName_input]):
                    print(" error: Required fields not found ❌ ")
                    stats["failed"] += 1
                    return False

                # Prepare data for sending followers
                start_url = start_url_template.format(userID=userID_input.get("value"))
                start_post_data = {
                    "adet": adet_input.get("value", "50"),
                    "userID": userID_input.get("value"),
                    "userName": userName_input.get("value")
                }

                # Send followers
                start_resp = session.post(start_url, data=start_post_data, timeout=10, verify=False)
                time.sleep(random.uniform(CONFIG["min_delay"], CONFIG["max_delay"]))  # تأخير بعد إرسال المتابعين

                # Parse JSON response
                try:
                    response_json = start_resp.json()
                    status = response_json.get("status")
                    message = response_json.get("message", "")
                    followers_sent = response_json.get("followers_sent", None)

                    if status == "success" and "Başarılı" in message:
                        print(f"🚀 Start: OK {start_resp.status_code} - {message}")
                        if followers_sent:
                            print(f" 📊 Sent {followers_sent} followers")
                            stats["followers_sent"] += int(followers_sent)
                        stats["successful"] += 1
                        # Add random delay after successful follower send
                        time.sleep(random.uniform(CONFIG["post_success_delay_min"], CONFIG["post_success_delay_max"]))
                        if repeat_on_success:
                            time.sleep(random.uniform(CONFIG["min_operation_delay"], CONFIG["max_operation_delay"]))
                            continue
                        return True
                    elif "Takipçi Eklenemedi. Takipçi krediniz kalmadı!" in message:
                        print(f" error: Failed to send followers - {message} ❌ ")
                        stats["failed"] += 1
                        return True
                    else:
                        print(f" error: Failed to send followers - {message} ❌ ")
                        stats["failed"] += 1
                        return False
                except json.JSONDecodeError:
                    print(f" error: Non-JSON response - {start_resp.status_code} ❌ ")
                    stats["failed"] += 1
                    return False
                except Exception as e:
                    print(f" error: Issue parsing response - {e} ❌ ")
                    stats["failed"] += 1
                    return False
            except requests.exceptions.RequestException as e:
                print(f" error: Connection issue with {site_name} ❌ ")
                stats["failed"] += 1
                return False

def main(target_username):
    repeat_on_success = False
    stats = {"successful": 0, "failed": 0, "followers_sent": 0}
    # Iterate over sites
    for site in sites:
        print(f"\n{'='*60}\n 🌐 Site: \033[2;32m{site['name']}\033[2;00m\n{'='*60}")
        print(f" 📦 Site: {site['name']} - Being tested with all accounts")

        # Iterate over accounts
        for acc in accounts:
            if "|" not in acc:
                print(f" error: Invalid account format - {acc} ❌ ")
                stats["failed"] += 1
                continue
            username, password = acc.split("|")
            if not username or not password:
                print(f" error: Username or password empty - {acc} ❌ ")
                stats["failed"] += 1
                continue
            print(f" 📦 Login: {site['name']}")
            process_site(
                site_name=site['name'],
                login_url=site["login_url"],
                send_follower_url=site["send_follower_url"],
                start_url_template=site["start_url_template"],
                username=username,
                password=password,
                target_username=target_username,
                stats=stats,
                repeat_on_success=repeat_on_success
            )
            time.sleep(random.uniform(CONFIG["min_delay"], CONFIG["max_delay"]))

        time.sleep(random.uniform(CONFIG["min_delay"] * 2, CONFIG["max_delay"] * 2))

    # Display statistics
    print(f"\n{'='*60}\n 📊 Final Statistics:")
    print(f" ✅ Successful operations: {stats['successful']}")
    print(f" ❌ Failed operations: {stats['failed']}")
    print(f" 📈 Total followers sent: {stats['followers_sent']}\n{'='*60}")

if __name__ == "__main__":
    target_username = input('\033[1;91m ➛ ').strip()
    os.system('clear')
    main(target_username)
