import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time

# ================= ألوان ====================
Z = '\033[1;31m'  # أحمر
F = '\033[2;32m'  # أخضر
C = "\033[1;97m"  # أبيض
B = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # أزرق
S = '\033[1;37m'  # رمادي
CYAN = "\033[1;36m"  # سماوي للزخرفة

# ================ لوجو ======================
def logo():
    return f"""
{F}                  [ 𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 _ 𝚉𝚎𝚛𝚘 𝚃𝚛𝚊𝚌𝚎 ℝ/𝔾]

{C} > 𝙼𝚢 𝙽𝚊𝚖𝚎 : {Z}اكودي _ سكس من مؤخرة 🤦
"""

# ============== قائمة الحسابات ==============
accounts = [
    "tyty235182023|Rayen@111a",
    "haifahjayeij|haifahaifa",
    "aziz_douissa|aziz2006",
    "+21627980987|thara123456789",
    "oussama_ait.45|oussama1234",
    "tns.heeedyyyyl|hadil@123",
    "najemeddinechangel|najem123456789",
    "youssef_bellehirch|youssef123456",
    "alijbeli888|ali123456",
    "yahyaoui.menyar|menyarmenyar",
    "_a_z_i_z_20|azizaziz1",
    "adem_hmaydi|adem12345",
    "farah.998362|farah1234",
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

# =============== دوال المساعدة ================
def clear():
    os.system('clear')

def show_header(identifier):
    print("\n" + "=" * 60)
    print(f" 📱 𝙼𝚢 - 𝚄𝚜𝚎𝚛 : {F}{identifier}{C}")
    print("=" * 60)

def show_menu():
    clear()
    print(logo())
    print("1️⃣  إرسال متابعين")
    print("2️⃣  إرسال لايكات (TikTok Like)")
    print("3️⃣  خيار ثالث (قريبًا)")
    print("0️⃣  خروج")
    choice = input("\nاختر خيارك: ")
    return choice

# ============ دوال الإرسال العامة ============
def process_site(site_name, login_url, send_follower_url, start_url_template, username, password, target_username):
    session = requests.Session()
    print(f"\n📦 𝙻𝚘𝚐𝚒𝚗 : {username}")

    login_resp = session.post(login_url, data={"username": username, "password": password})
    if login_resp.status_code != 200:
        print(f" ❌ فشل تسجيل الدخول - {site_name}")
        return

    page_resp = session.get(send_follower_url)
    if page_resp.status_code != 200:
        print(f" ❌ فشل تحميل صفحة النموذج - {site_name}")
        return

    soup = BeautifulSoup(page_resp.text, "html.parser")
    form = None
    for f in soup.find_all("form"):
        btn = f.find("button", string=lambda t: t and "Kullanıcıyı Bul" in t)
        if btn:
            form = f
            break

    if not form:
        print(" ❌ النموذج غير موجود")
        return

    action = urljoin(send_follower_url, form.get("action", ""))
    post_data = {tag.get("name"): tag.get("value", "") for tag in form.find_all("input") if tag.get("name")}
    post_data["username"] = target_username

    submit_resp = session.post(action, data=post_data)
    if submit_resp.status_code != 200:
        print(" ❌ فشل في إرسال النموذج")
        return

    soup2 = BeautifulSoup(submit_resp.text, "html.parser")
    adet = soup2.find("input", {"name": "adet"})
    userID = soup2.find("input", {"name": "userID"})
    userName = soup2.find("input", {"name": "userName"})

    if not userID or not userName:
        print(" ❌ لم يتم استخراج معلومات الحساب")
        return

    start_url = start_url_template.format(userID=userID.get("value"))
    start_post_data = {
        "adet": adet.get("value") if adet else "5000",
        "userID": userID.get("value"),
        "userName": userName.get("value")
    }

    start_resp = session.post(start_url, data=start_post_data)
    if start_resp.status_code == 200:
        print(f" ✅ تم الإرسال إلى {target_username}")
    else:
        print(f" ❌ فشل الإرسال - {start_resp.status_code}")

    time.sleep(2)

def process_followersize(username, password, target_username):
    process_site(
        site_name="followersize.com",
        login_url="https://followersize.com/member",
        send_follower_url="https://followersize.com/tools/send-follower",
        start_url_template="https://followersize.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username
    )

def process_takipcikrali(username, password, target_username):
    process_site(
        site_name="takipcikrali.com",
        login_url="https://takipcikrali.com/login",
        send_follower_url="https://takipcikrali.com/tools/send-follower",
        start_url_template="https://takipcikrali.com/tools/send-follower/{userID}?formType=send",
        username=username,
        password=password,
        target_username=target_username
    )

# ============ دالة إرسال لايكات (مؤقتة) ============
def process_tiktok_like(username, password, video_url):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Infinix X692 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.67 Mobile Safari/537.36"
    }
    session = requests.Session()
    login_url = "https://takipcikrali.com/login"
    send_url = "https://takipcikrali.com/tools/send-tiktok-like?formType=send"

    print(f"\n🔐 تسجيل الدخول للحساب: {username}")
    login_resp = session.post(login_url, data={"username": username, "password": password}, headers=headers)
    if login_resp.status_code != 200:
        print(f"❌ فشل تسجيل الدخول للحساب {username}")
        return

    print(f"📹 إرسال لايكات إلى: {video_url}")
    post_data = {
        "mediaUrl": video_url,
        "adet": "20"
    }

    send_resp = session.post(send_url, data=post_data, headers=headers)
    if send_resp.status_code == 200:
        print(f"❤️‍🔥 تم إرسال لايكات بنجاح من {username}")
    else:
        print(f"❌ فشل الإرسال من {username}")
    time.sleep(2)
# =============== القائمة الرئيسية ===============



#######
def process_tiktok_view(username, password, video_url):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Infinix X692 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.67 Mobile Safari/537.36"
    }
    session = requests.Session()
    login_url = "https://takipcikrali.com/login"
    send_url = "https://takipcikrali.com/tools/send-tiktok-view?formType=send"

    print(f"\n🔐 تسجيل الدخول للحساب: {username}")
    login_resp = session.post(login_url, data={"username": username, "password": password}, headers=headers)
    if login_resp.status_code != 200:
        print(f"❌ فشل تسجيل الدخول للحساب {username}")
        return

    print(f"🎬 إرسال مشاهدات إلى: {video_url}")
    post_data = {
        "mediaUrl": video_url,
        "adet": "500"
    }

    send_resp = session.post(send_url, data=post_data, headers=headers)
    if send_resp.status_code == 200:
        print(f"👁️‍🗨️ تم إرسال مشاهدات بنجاح من {username}")
    else:
        print(f"❌ فشل إرسال المشاهدات من {username}")
    time.sleep(5)

#####
while True:
    option = show_menu()

    if option == "1":
        clear()
        print(logo())
        target_username = input(f'{CYAN} 🧾 ᴜsᴇʀ : ').strip()
        clear()
        show_header(target_username)
        for acc in accounts:
            username, password = acc.split("|")
            process_followersize(username, password, target_username)
            process_takipcikrali(username, password, target_username)
        input("\n✅ اكتملت العملية! اضغط Enter للعودة للقائمة.")

    elif option == "2":
        clear()
        print(logo())
        video_url = input("🎥 أدخل رابط الفيديو: ").strip()
        clear()
        show_header(video_url)
        for acc in accounts:
            username, password = acc.split("|")
            process_tiktok_like(username, password, video_url)
        input("\n✅ انتهى الإرسال! اضغط Enter للعودة للقائمة.")

    elif option == "3":
        clear()
        print(logo())
        video_url = input("🎬 أدخل رابط الفيديو (TikTok View): ").strip()
        clear()
        show_header(video_url)
        for acc in accounts:
            username, password = acc.split("|")
            process_tiktok_view(username, password, video_url)
        input("\n✅ تم إرسال المشاهدات! اضغط Enter للعودة للقائمة.")
    elif option == "0":
        print("👋 إلى اللقاء!")
        break
    else:
        input("❌ خيار غير صالح! اضغط Enter للمحاولة مجدداً.")
