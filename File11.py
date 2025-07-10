import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import os,sys,uuid,re,random,time,string,json

# ألوان للطباعة (اختياري)
Z = '\033[1;31m' # احمر
R = '\033[1;31m' # احمر
X = '\033[1;33m' # اصفر
F = '\033[2;32m' # اخضر
C = "\033[1;97m" # ابيض
B = '\033[2;36m'# سمائي
Y = '\033[1;34m' # ازرق فاتح


#─━─━─━─━Find User Agent─━──━─━#

    
#─━─━─━─━COLOUR SYS━─━─━─━─#
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
ver ='\033[92;1m7.0\033[93;1m'
#─━─━─━─━LOGO SYS─━─━─━─━─#

#» \033[1;33m1\033[0m -    ⠀⠀⠀⠀⠀   \033[1;41m
logo = (f"""\n                  \033[2;32m   [ 𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐅𝐨𝐥𝐥𝐨𝐰𝐫𝐞𝐬 _ 𝚉𝚎𝚛𝚘 𝚃𝚛𝚊𝚌𝚎 ℝ/𝔾]\033[4;00m\n\n
\033[1;97m >  \033[1;3 𝙼𝚢 𝙽𝚊𝚖𝚎 \033[1;3: \033[1;41m +216 - 𝚁𝚊𝚢𝚎𝚗 \033[2;00m
""")
def linex():
        print(f"\33[1;37m==============================================""")

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os


# الحسابات username|passwordcjchhccgcgcgcg
accounts = [
    "aziz_douissa|aziz2006",
    "alijbeli888|ali123456",
    "zied_zaidoun22|zied12345678",
    "adem_hmaydi|adem12345",
    "bensidhoumhoussem|houssem123",
    "yassine_ben_yoness|yassine123456789",
    "amirrr__prvvv|amir12345",
    "ba.ssem6342|bassem123",
    "911_____maeb|maeb123",
    "asil_elharari|asil12",
   
    "rajmohan__negi|rajmohan11",
    "ma3ak_________youssef|youssef12",
    "hama_abdelati|hamahama",
    "aymenmaster27|aymen12",
    "_azizchouchene|aziz12345",
    "brahim_adamben|adam123",
    "maryem_.bacha|mariem12345678",
    "rawen.bahrouni|rawen123",
    "+21656329481|ahlem123"
]

def clear():
    os.system('clear')

print(logo)    
target_username = input('\033[1;91m ➛ ').strip()
clear()


print(logo)    

operation_counter = 1

def show_header():
    print("\n" + "=" * 60)
    print(f" 📱 𝙼𝚢 - 𝚄𝚜𝚎𝚛 :\033[2;32m {target_username}\033[2;00m")
    print("=" * 60)

def process_site(site_name, login_url, send_follower_url, start_url_template, username, password):
    global operation_counter
    show_header()
    print(f"\n📦 𝙻𝚘𝚐𝚒𝚗 \033[1;33m {operation_counter} \033[1;00m")
    operation_counter += 1

    print(f"\n    𝙤𝙣𝙡𝙞𝙣𝙚 : 📡 ")
    session = requests.Session()

    # تسجيل الدخول
    login_resp = session.post(login_url, data={"username": username, "password": password})
    if login_resp.status_code != 200:
        print(f"{Z} 𝙻𝚘𝚐𝚒𝚗 𝙵𝚊𝚒𝚕 ❌ - {site_name}")
        return

    # دخول صفحة إرسال المتابعين
    page_resp = session.get(send_follower_url)
    if page_resp.status_code != 200:
        print(f"{Z} 𝙴𝚛𝚛𝚘𝚛 𝚕𝚘𝚊𝚍 𝚜𝚎𝚗𝚍-𝚏𝚘𝚕𝚕𝚘𝚠𝚎𝚛 𝚙𝚊𝚐𝚎 ❌ - {site_name}")
        return
    print("  𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 ✓ ")

    soup = BeautifulSoup(page_resp.text, "html.parser")

    # البحث عن الفورم الذي يحتوي على زر "Kullanıcıyı Bul"
    form = None
    for f in soup.find_all("form"):
        btn = f.find("button", string=lambda t: t and "Kullanıcıyı Bul" in t)
        if btn:
            form = f
            break

    if not form:
        print(f"{Z} 𝚎𝚛𝚛𝚘𝚛 ❌ \033[1;00m ")
        return

    action = form.get("action") or send_follower_url
    if not action.startswith("http"):
        action = urljoin(send_follower_url, action)

    post_data = {}
    for input_tag in form.find_all("input"):
        name = input_tag.get("name")
        if name:
            post_data[name] = input_tag.get("value", "")
    post_data["username"] = target_username

    # إرسال الفورم الأول
    submit_resp = session.post(action, data=post_data)
    if submit_resp.status_code != 200:
        print(f"{Z} 𝚂𝚞𝚋𝚖𝚒𝚝 𝚏𝚘𝚛𝚖 𝚏𝚊𝚒𝚕 ❌ - {site_name} ")
        return
    print("  𝙾𝙺 📤  ")
    time.sleep(8)

    soup2 = BeautifulSoup(submit_resp.text, "html.parser")
    adet_input = soup2.find("input", {"name": "adet"})
    userID_input = soup2.find("input", {"name": "userID"})
    userName_input = soup2.find("input", {"name": "userName"})

    adet = adet_input.get("value") if adet_input else "5000"
    userID = userID_input.get("value") if userID_input else None
    userName = userName_input.get("value") if userName_input else None

    if not userID or not userName:
        print(f"{Z} 𝚎𝚛𝚛𝚘𝚛 ❌ \033[1;00m ")
        return

    # إرسال المتابعين (Start)
    start_url = start_url_template.format(userID=userID)
    start_post_data = {
        "adet": adet,
        "userID": userID,
        "userName": userName
    }

    start_resp = session.post(start_url, data=start_post_data)
    if start_resp.status_code == 200:
        print("  𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚜 : 𝙾𝙺 🚀 ")
    else:
        print(f"🚀 𝙵𝚘𝚕𝚕𝚘𝚠𝚎𝚜 : 𝙵𝚊𝚒𝚕 {start_resp.status_code} ")
    time.sleep(10)

def process_followersize(username, password):
    process_site(
        site_name="followersize.com",
        login_url="https://followersize.com/member",
        send_follower_url="https://followersize.com/tools/send-follower",
        start_url_template="https://followersize.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password
    )

def process_takipcikrali(username, password):
    process_site(
        site_name="takipcikrali.com",
        login_url="https://takipcikrali.com/login",
        send_follower_url="https://takipcikrali.com/tools/send-follower",
        start_url_template="https://takipcikrali.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password
    )

# تنفيذ العملية لكل حساب وموقع بالترتيب المطلوبhju
for acc in accounts:
    username, password = acc.split("|")
    process_followersize(username, password)
    process_takipcikrali(username, password)
