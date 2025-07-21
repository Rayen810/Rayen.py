import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# ========== ألوان ==========
Z = '\033[1;31m'
F = '\033[2;32m'
C = "\033[1;97m"
B = '\033[2;36m'
Y = '\033[1;34m'
S = '\033[1;37m'
CYAN = "\033[1;36m"

# ========== لوجو ==========vvnb
def logo():
    return f"""\033[1;92m
           [ 𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 ✰22 𝚉𝚎𝚛𝚘 𝚃𝚛𝚊𝚌𝚎 ℝ~~𝔾 ︎☠︎︎]\n
{C}  > 𝙼𝚢 𝙽𝚊𝚖𝚎 : {CYAN} 𖤍 𝚁𝚊𝚢𝚎𝚗 𖤍 
"""

# ========== الحسابات ==========
accounts = [
    "san_achref|achref1234",
    "911_____maeb|maeb123",
    "najemeddinechangel|najem123456789",
    "yassine_ben_yoness|yassine123456789",
    "_azizchouchene|aziz12345",
    "habibelghoulbhiri|habib12345"
]

# ========== وظائف ==========و
def clear():
    os.system('clear')

def show_menu():
    clear()
    print(logo())
    
    print(f"\033[1;33m» \033[0m\033[1;41m إرسال متابعين (𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜) - 1 \033[0m\n")
    print(f"\033[1;33m» \033[0m\033[1;41m   إرسال لايكات (𝚃𝚒𝚔𝚝𝚘𝚔 𝙻𝚒𝚔𝚎𝚜) - 2 \033[0m\n")
    print(f"\033[1;33m» \033[0m\033[1;41m   إرسال مشاهدات (𝚃𝚒𝚔𝚝𝚘𝚔 𝚅𝚒𝚎𝚠) - 3 \033[0m\n")
    print(f"\033[1;33m» \033[0m\033[1;41m   خروج (𝙴𝚡𝚒𝚝) - 0 \033[0m\n")

    return input(' \033[1;91m  ➛  \033[1;92m ') 

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
operation_counter = 1  # عداد تسجيل الدخولhhggggf

def show_header(target_username):
    
    print("\033[2;00m")
    print("\n" + "=" * 60)
    print(f" \033[2;00m📱 𝙼𝚢 - 𝚄𝚜𝚎𝚛 :\033[2;32m {target_username}\033[2;00m")
    print("=" * 60)


def process_site(site_name, login_url, send_follower_url, start_url_template, username, password, target_username, operation_counter):
    show_header(target_username)
    print(f"\n\n  𝙻𝚘𝚐𝚒𝚗\033[1;33m [{operation_counter}] 📦 \033[1;00m")

    session = requests.Session()
    login_resp = session.post(login_url, data={"username": username, "password": password}, verify=False)
    if login_resp.status_code != 200:
        print(f"\n    𝙤𝙣𝙡𝙞𝙣𝙚 : 📡 ")
        return

    page_resp = session.get(send_follower_url, verify=False)
    if page_resp.status_code != 200:
        print(f"{Z} 𝙴𝚛𝚛𝚘𝚛 𝚕𝚘𝚊𝚍 𝚜𝚎𝚗𝚍-𝚏𝚘𝚕𝚕𝚘𝚠𝚎𝚛 𝚙𝚊𝚐𝚎 ❌ - {site_name}")
        return
    print("  𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 ✓ ")

    soup = BeautifulSoup(page_resp.text, "html.parser")
    form = None
    for f in soup.find_all("form"):
        btn = f.find("button", string=lambda t: t and "Kullanıcıyı Bul" in t)
        if btn:
            form = f
            break

    if not form:
        print(f"{Z}  𝚎𝚛𝚛𝚘𝚛 ❌ \033[1;00m ")
        return

    action = form.get("action") or send_follower_url
    if not action.startswith("http"):
        action = urljoin(send_follower_url, action)

    post_data = {input_tag.get("name"): input_tag.get("value", "") for input_tag in form.find_all("input") if input_tag.get("name")}
    post_data["username"] = target_username

    submit_resp = session.post(action, data=post_data, verify=False)
    if submit_resp.status_code != 200:
        print(f"{Z}  𝚎𝚛𝚛𝚘𝚛 ❌ \033[1;00m ")
        return
    print("  𝙾𝙺 📤  ")
    

    soup2 = BeautifulSoup(submit_resp.text, "html.parser")
    adet = soup2.find("input", {"name": "adet"}).get("value", "888")
    userID = soup2.find("input", {"name": "userID"}).get("value", None)
    userName = soup2.find("input", {"name": "userName"}).get("value", None)

    if not userID or not userName:
        print(f"{Z}  𝚎𝚛𝚛𝚘𝚛 ❌ ")
        return

    start_url = start_url_template.format(userID=userID)
    start_data = {
        "adet": adet,
        "userID": userID,
        "userName": userName
    }
    start_resp = session.post(start_url, data=start_data, verify=False)
    if start_resp.status_code == 200:
        print("  𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚛𝚜 : 𝙾𝙺 🚀 ")
    else:
        print(f"🚀 𝙵𝚊𝚒𝚕 ({start_resp.status_code})")
    time.sleep(5)
    

    
    
    
    
    
    
def process_takipcimx(username, password, target_username, operation_counter):
    process_site(
        site_name="takipcimx.net",
        login_url="https://takipcimx.net/login",
        send_follower_url="https://takipcimx.net/tools/send-follower",
        start_url_template="https://takipcimx.net/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
def process_bayitakipci(username, password, target_username, operation_counter):
    process_site(
        site_name="bayitakipci.com",
        login_url="https://bayitakipci.com/memberlogin",
        send_follower_url="https://bayitakipci.com/tools/send-follower",
        start_url_template="https://bayitakipci.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )

def process_takipcikrali(username, password, target_username, operation_counter):
    process_site(
        site_name="takipcikrali.com",
        login_url="https://takipcikrali.com/login",
        send_follower_url="https://takipcikrali.com/tools/send-follower",
        start_url_template="https://takipcikrali.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    

    
def process_takipcikingnet(username, password, target_username, operation_counter):
    process_site(
        site_name="takipciking.net",
        login_url="https://takipciking.net/login",
        send_follower_url="https://takipciking.net/tools/send-follower",
        start_url_template="https://takipciking.net/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_platintakipci(username, password, target_username, operation_counter):
    process_site(
        site_name="platintakipci.com",
        login_url="https://platintakipci.com/member",
        send_follower_url="https://platintakipci.com/tools/send-follower",
        start_url_template="https://platintakipci.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_takipcigen(username, password, target_username, operation_counter):
    process_site(
        site_name="takipcigen.com",
        login_url="https://takipcigen.com/login",
        send_follower_url="https://takipcigen.com/tools/send-follower",
        start_url_template="https://takipcigen.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_bigtakip(username, password, target_username, operation_counter):
    process_site(
        site_name="bigtakip.net",
        login_url="https://bigtakip.net/login",
        send_follower_url="https://bigtakip.net/tools/send-follower",
        start_url_template="https://bigtakip.net/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )

def process_takipcitime(username, password, target_username, operation_counter):
    process_site(
        site_name="takipcitime.net",
        login_url="https://takipcitime.net/login",
        send_follower_url="https://takipcitime.net/tools/send-follower",
        start_url_template="https://takipcitime.net/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_takipzan(username, password, target_username, operation_counter):
    process_site(
        site_name="takipzan.com",
        login_url="https://takipzan.com/login",
        send_follower_url="https://takipzan.com/tools/send-follower",
        start_url_template="https://takipzan.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_followersize_net(username, password, target_username, operation_counter):
    process_site(
        site_name="followersize.net",
        login_url="https://followersize.net/login",
        send_follower_url="https://followersize.net/tools/send-follower",
        start_url_template="https://followersize.net/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    
def process_birtakipci(username, password, target_username, operation_counter):
    process_site(
        site_name="birtakipci.net",
        login_url="https://birtakipci.net/login",
        send_follower_url="https://birtakipci.net/tools/send-follower",
        start_url_template="https://birtakipci.net/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    
def process_mixtakip(username, password, target_username, operation_counter):
    process_site(
        site_name="mixtakip.com",
        login_url="https://mixtakip.com/login",
        send_follower_url="https://mixtakip.com/tools/send-follower",
        start_url_template="https://mixtakip.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )

def process_instamoda(username, password, target_username, operation_counter):
    process_site(
        site_name="instamoda.org",
        login_url="https://instamoda.org/login",
        send_follower_url="https://instamoda.org/tools/send-follower",
        start_url_template="https://instamoda.org/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    
    
def process_takipcitime_com(username, password, target_username, operation_counter):
    process_site(
        site_name="takipcitime.com",
        login_url="https://takipcitime.com/login",
        send_follower_url="https://takipcitime.com/tools/send-follower",
        start_url_template="https://takipcitime.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
def process_birtakipci_com(username, password, target_username, operation_counter):
    process_site(
        site_name="birtakipci.com",
        login_url="https://birtakipci.com/member",
        send_follower_url="https://birtakipci.com/tools/send-follower",
        start_url_template="https://birtakipci.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_takipcibase(username, password, target_username, operation_counter):
    process_site(
        site_name="takipcibase.com",
        login_url="https://takipcibase.com/login",
        send_follower_url="https://takipcibase.com/tools/send-follower",
        start_url_template="https://takipcibase.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    
def process_takip88(username, password, target_username, operation_counter):
    process_site(
        site_name="takip88.com",
        login_url="https://takip88.com/login",
        send_follower_url="https://takip88.com/tools/send-follower",
        start_url_template="https://takip88.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    #1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣1️⃣
def process_followersize_com(username, password, target_username, operation_counter):
    process_site(
        site_name="followersize.com",
        login_url="https://followersize.com/member",
        send_follower_url="https://followersize.com/tools/send-follower",
        start_url_template="https://followersize.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    

    
    
    #2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣2️⃣
def process_medyahizmeti(username, password, target_username, operation_counter):
    process_site(
        site_name="medyahizmeti.com",
        login_url="https://medyahizmeti.com/member",
        send_follower_url="https://medyahizmeti.com/tools/send-follower",
        start_url_template="https://medyahizmeti.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    
def process_hepsitakipci(username, password, target_username, operation_counter):#1111113️⃣3️⃣3️⃣3️⃣3️⃣3️⃣3️⃣3️⃣3️⃣3️⃣
    process_site(
        site_name="hepsitakipci.com",
        login_url="https://www.hepsitakipci.com/member",
        send_follower_url="https://www.hepsitakipci.com/tools/send-follower",
        start_url_template="https://www.hepsitakipci.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    

def process_tiktok_like(username, password, video_url):
    session = requests.Session()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0"
    }
    login_resp = session.post("https://followersize.com/member",
                              data={"username": username, "password": password},
                              headers=headers, verify=False)
    if login_resp.status_code != 200:
        print(f"{Z}❌ خطأ تسجيل دخول {username}")
        return

    print("\n\033[2;00m" + "=" * 60)
    print(f"\n\033[1;31m 𝚜𝚎𝚗𝚝 𝙻𝚒𝚔𝚜 𝚝𝚘 𝚟𝚒𝚍𝚎𝚘 (لايكلات) : \033[2;32m{video_url} 👁️ \033[1;00m\n")
    print("=" * 60)
    print("")
    post_data = {"mediaUrl": video_url, "adet": "20"}
    send_resp = session.post("https://followersize.com/tools/send-tiktok-like?formType=send",
                             data=post_data, headers=headers, verify=False)
    if send_resp.status_code == 200:
        print(f"")
    else:
        print(f"Erro")
    time.sleep(2)

def process_tiktok_view(username, password, video_url):
    session = requests.Session()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0"
    }
    login_resp = session.post("https://followersize.com/member",
                              data={"username": username, "password": password},
                              headers=headers, verify=False)
    if login_resp.status_code != 200:
        print(f"❌ فشل تسجيل الدخول {username}")
        return

    
    print("\n\033[2;00m" + "=" * 60)
    print(f"\n\033[1;31m 𝚜𝚎𝚗𝚝 𝚅𝚒𝚎𝚠𝚜 𝚝𝚘 𝚟𝚒𝚍𝚎𝚘 (مشاهدات) : \033[2;32m{video_url} 👁️ \033[1;00m\n")
    print("=" * 60)
    print("")
    post_data = {"mediaUrl": video_url, "adet": "500"}
    send_resp = session.post("https://followersize.com/tools/send-tiktok-view?formType=send",
                             data=post_data, headers=headers, verify=False)
    if send_resp.status_code == 200:
        print(f"")
    else:
        print(f"❌ error")
    time.sleep(1.5)
    
def process_takipcizencom(username, password, target_username, operation_counter):#9
    process_site(
        site_name="takipcizen.com",
        login_url="https://takipcizen.com/login",
        send_follower_url="https://takipcizen.com/tools/send-follower",
        start_url_template="https://takipcizen.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    
def process_takipstarcom(username, password, target_username, operation_counter):#8
    process_site(
        site_name="takipstar.com",
        login_url="https://takipstar.com/login",
        send_follower_url="https://takipstar.com/tools/send-follower",
        start_url_template="https://takipstar.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_takipcikingcom(username, password, target_username, operation_counter):#7
    process_site(
        site_name="takipciking.com",
        login_url="https://takipciking.com/member",
        send_follower_url="https://takipciking.com/tools/send-follower",
        start_url_template="https://takipciking.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
    
def process_takipcigir(username, password, target_username, operation_counter):#6
    process_site(
        site_name="takipcigir.com",
        login_url="https://takipcigir.com/login",
        send_follower_url="https://takipcigir.com/tools/send-follower",
        start_url_template="https://takipcigir.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )

def process_takipcimx_com(username, password, target_username, operation_counter):#4
    process_site(
        site_name="takipcimx.com",
        login_url="https://takipcimx.com/member",
        send_follower_url="https://takipcimx.com/tools/send-follower",
        start_url_template="https://takipcimx.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    

    
def process_takipcimax(username, password, target_username, operation_counter):#3
    process_site(
        site_name="takipcimax.com",
        login_url="https://takipcimax.com/login",
        send_follower_url="https://takipcimax.com/tools/send-follower",
        start_url_template="https://takipcimax.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )#&&

    

def process_bigtakip_com(username, password, target_username, operation_counter):#2
    process_site(
        site_name="bigtakip.com",
        login_url="https://bigtakip.com/member",
        send_follower_url="https://bigtakip.com/tools/send-follower",
        start_url_template="https://bigtakip.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )
    
def process_fastfollow(username, password, target_username, operation_counter):#1
    process_site(
        site_name="fastfollow.in",
        login_url="https://fastfollow.in/member",
        send_follower_url="https://fastfollow.in/tools/send-follower",
        start_url_template="https://fastfollow.in/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username,
        operation_counter=operation_counter
    )

# ========== القائمة ==========jjنjjbb
while True:
    option = show_menu()

    if option == "1":
        clear()
        print(logo())
        print("")

        target_username = input(f'{CYAN} 🧾 ᴜsᴇʀ  \033[1;00m: \033[1;92m ').strip()
        clear()
        print(logo())
        operation_counter = 1  # إعادة التهيئة هنhا
        for acc in accounts:
            username, password = acc.split("|")
            
            
            process_followersize_com(username, password, target_username, operation_counter)
            operation_counter += 1
            process_medyahizmeti(username, password, target_username, operation_counter)
            operation_counter += 1   
            process_hepsitakipci(username, password, target_username, operation_counter)
            operation_counter += 1
            
            process_instamoda(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcitime_com(username, password, target_username, operation_counter)
            operation_counter += 1
            process_birtakipci_com(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcibase(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takip88(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcitime(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipzan(username, password, target_username, operation_counter)
            operation_counter += 1
            process_followersize_net(username, password, target_username, operation_counter)
            operation_counter += 1
            process_birtakipci(username, password, target_username, operation_counter)
            operation_counter += 1
            process_mixtakip(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcikrali(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcikingnet(username, password, target_username, operation_counter)#
            operation_counter += 1





            process_fastfollow(username, password, target_username, operation_counter)
            operation_counter += 1#
            process_bigtakip_com(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcimx_com(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcimax(username, password, target_username, operation_counter)
            operation_counter += 1
            
            process_takipcigir(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcikingcom(username, password, target_username, operation_counter)
            operation_counter += 1
            
            process_takipstarcom(username, password, target_username, operation_counter)
            operation_counter += 1
            
            process_takipcizencom(username, password, target_username, operation_counter)
            operation_counter += 1#





            process_platintakipci(username, password, target_username, operation_counter)
            operation_counter += 1
            
            process_takipcigen(username, password, target_username, operation_counter)
            operation_counter += 1
            process_bigtakip(username, password, target_username, operation_counter)
            operation_counter += 1
            process_takipcimx(username, password, target_username, operation_counter)
            operation_counter += 1
            process_bayitakipci(username, password, target_username, operation_counter)
            operation_counter += 1
            
            
            
            
            
    elif option == "2":
        clear()
        print(logo())
        video_url = input(" 𝙻𝚒𝚗𝚔  𝚟𝚒𝚍𝚎𝚘  (𝚃𝚒𝚔𝚝𝚘𝚔 𝙻𝚒𝚔𝚜) 🎥 : ").strip()
        clear()
        
        for acc in accounts:
            username, password = acc.split("|")
            process_tiktok_like(username, password, video_url)
        input("\n✅ انتهى الإرسال! اضغط Enter للعودة للقائمة.")

    elif option == "3":
        clear()
        print(logo())
        video_url = input(" 𝙻𝚒𝚗𝚔  𝚟𝚒𝚍𝚎𝚘  (𝚃𝚒𝚔𝚝𝚘𝚔 𝚅𝚒𝚎𝚠) 🎥 : ").strip()
        clear()
        
        for acc in accounts:
            username, password = acc.split("|")
            process_tiktok_view(username, password, video_url)
        input("\n✅ تم إرسال المشاهدات! اضغط Enter للعودة للقائمة.")
    elif option == "0":
        print("👋 إلى اللقاء!")
        break
    else:
        input("❌ خيار غير صالح! اضغط Enter للمحاولة مجدداً.")
        
        
        #'+'-6'تتjvvhggfvvnhh
