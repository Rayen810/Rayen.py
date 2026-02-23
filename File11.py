import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import warnings
import json
import re

# إخفاء تحذيرات SSL
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

# الألوان في الترمينال#:-
GREEN = "\033[92m"
RED   = "\033[91m"
RESET = "\033[0m"

# قائمة الروابط الدقيقة لصفحة الدخول
LOGIN_PAGES = [
    "https://takipcigir.com/login",
    "https://takipcizen.com/login",
    "https://takipstar.com/login",
    "https://takipcifox.com/member",
    "https://takipciking.com/member",
    "https://bayitakipci.com/memberlogin",
    "https://fastfollow.in/member",
    "https://takipcikrali.com/login",
    "https://takipcimx.net/login",
    "https://takipciking.net/login",
    "https://takipcigen.com/login",
    "https://bigtakip.net/login",
    "https://takipcitime.net/login",
    "https://takipzan.com/login",
    "https://followersize.net/login",
    "https://birtakipci.net/login",
    "https://mixtakip.com/login",
    "https://takipcitime.com/login",
    "https://birtakipci.com/member",
    "https://takipcibase.com/login",
    "https://takip88.com/login",
    "https://followersize.com/member",
    "https://medyahizmeti.com/member",
    "https://www.hepsitakipci.com/member",
    "https://instamoda.org/login",
    "https://takipcimx.com/member",
    "https://takipcimax.com/login",
]
  #  "cha_hine.2017|chahine1234",--
    #  "wa.lid5221|walidwalid"
    #"youssefkh116|youssef12345",
       #:+ "youssefkh116|youssef12345",
          # "mk.hamza_03|hamza123",85
          #''
accounts = [
    "___2deeem|adem123456789",
    "am_____ir07|amiramir",#&&&
    "amirfehri07|amiramir",
    "oussama_madimagh|oussama123456789",
    "zied_zaidoun22|zied123456789",
    "elhemelhedi|elhem123456",
    "chaabanewalid525|walid123456789",
    "samar_ben_hassin|samar123456789",
    "rgesmi30|rayen123456",#&&&
    "fehri__amir|amiramir",
    "o_ghaoui|omar123456789",
    "mohamed_aziz_ben_attia|aziz12345",
    "mohamed_arshad838|arshad12345",

    "oialidwalid|oialidoialid",
    "z.maleeeeeek|malek123456789",


]

#;jj
target_username = input("أدخل اسم المستخدم المسjjjتهدف: ").strip()
if not target_username:
    print("❌ لم تدخل يوزر → توقف")
    exit()

print(f"\nالمستهدف: {target_username}")
print(f"عدد الحسابات: {len(accounts)}\n")

print("بدء الدورات اللانهائية ... (Ctrl+C للإيقاف)\n")

cycle = 0

while True:
    cycle += 1
    print(f"\n━━━━━━━━━━ الدورة رقم {cycle} ━━━━━━━━━━\n")

    for i, login_url in enumerate(LOGIN_PAGES, 1):
        
        site_alias = f"V{i}🌀"
        
        print(f"  الموقع: {site_alias}")

        for j, acc in enumerate(accounts, 1):
            account_alias = f"🔥V{j}"
            print(f"    الحساب: {account_alias}")

            try:
                username, password = [x.strip() for x in acc.split("|")]

                session = requests.Session()
                session.verify = False

                # 1. تسجيل الدخول
                login_data = {"username": username, "password": password}
                resp_login = session.post(login_url, data=login_data, timeout=800)

                if resp_login.status_code != 200:
                    print(f"      ✗ تسجيل دخول فشل ({resp_login.status_code})")
                    continue

                # 2. صفحة إرسال المتابعين
                base_url = "/".join(login_url.split("/")[:3])
                send_follower_url = f"{base_url}/tools/send-follower"

                resp_page = session.get(send_follower_url, timeout=800)
                if resp_page.status_code != 200:
                    print(f"      ✗ صفحة send-follower غير متاحة ({resp_page.status_code})")
                    continue

                soup = BeautifulSoup(resp_page.text, "html.parser")

                form = None
                for f in soup.find_all("form"):
                    btn = f.find("button", string=lambda t: t and "Kullanıcıyı Bul" in (t or ""))
                    if btn:
                        form = f
                        break

                if not form:
                    print("      ✗ ما وجدت فورم Kullanıcıyı Bul")
                    continue

                action = form.get("action") or send_follower_url
                if not action.startswith("http"):
                    action = urljoin(send_follower_url, action)

                post_data = {}
                for inp in form.find_all(["input", "textarea"]):
                    name = inp.get("name")
                    if name:
                        post_data[name] = inp.get("value", "")

                post_data["username"] = target_username

                resp_submit = session.post(action, data=post_data, timeout=800)
                if resp_submit.status_code != 200:
                    print(f"      ✗ طلب البحث فشل ({resp_submit.status_code})")
                    continue

                time.sleep(3)

                soup2 = BeautifulSoup(resp_submit.text, "html.parser")

                adet = "50"
                adet_tag = soup2.find("input", {"name": "adet"})
                if adet_tag and adet_tag.get("value"):
                    adet = adet_tag["value"]

                userID = None
                userID_tag = soup2.find("input", {"name": "userID"})
                if userID_tag and userID_tag.get("value"):
                    userID = userID_tag["value"]

                userName = None
                userName_tag = soup2.find("input", {"name": "userName"})
                if userName_tag and userName_tag.get("value"):
                    userName = userName_tag["value"]

                if not userID or not userName:
                    print("      ✗ فشل استخراج userID أو userName")
                    continue

                # الطلب النهائي
                start_url = f"{base_url}/tools/send-follower/{userID}?formType=send"
                start_data = {"adet": adet, "userID": userID, "userName": userName}

                resp_start = session.post(start_url, data=start_data, timeout=800)

                print(f"      → Start: {resp_start.status_code}")

                try:
                    json_match = re.search(r'\{.*\}', resp_start.text, re.DOTALL)
                    if json_match:
                        data = json.loads(json_match.group(0))
                        st = data.get("status", "").lower()

                        if st == "success":
                            print(f"        {GREEN}success{RESET}")
                        elif st == "error":
                            print(f"        {RED}Error{RESET}")
                        else:
                            print("        حالة غير معروفة")
                    else:
                        print("        (لا يوجد JSON واضح)")
                except:
                    print("        (مشكلة في قراءة الرد)")

                time.sleep(3)

            except Exception as e:
                print(f"      ⚠ خطأ")
                continue

        print("  ────────────────────────────────")

    print(f"\nانتهت الدورة {cycle} → انتظار 10 ثوانٍ قبل إعادة البدء ...\n")
    time.sleep(10)
