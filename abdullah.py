#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1500):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
print 'Thanks.'
os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
for e in z + '\n':
sys.stdout.write(e)
sys.stdout.flush()
time.sleep(00000.1)
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;90mWor\x1b[1;92mK\x1b[1;90ming\x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(0.5)



back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;99m▄▄     ▄▄              ▄▄            ▄▄▄▄      ▄▄▄▄                ▄▄
\033[1;91m   ████    ██              ██            ▀▀██      ▀▀██                ██
\033[1;91m  ████    ██▄███▄    ▄███▄██  ██    ██    ██        ██       ▄█████▄  ██▄████▄
\033[1;91m  ██  ██   ██▀  ▀██  ██▀  ▀██  ██    ██    ██        ██       ▀ ▄▄▄██  ██▀   ██
\033[1;91m  ██████   ██    ██  ██    ██  ██    ██    ██        ██      ▄██▀▀▀██  ██    ██
\033[1;91m ▄██  ██▄  ███▄▄██▀  ▀██▄▄███  ██▄▄▄███    ██▄▄▄     ██▄▄▄   ██▄▄▄███  ██    ██
\033[1;91m ▀▀    ▀▀  ▀▀ ▀▀▀      ▀▀▀ ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀      ▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀
\033[1;99m ▄▄                                      ▄▄▄▄      ██
\033[1;91m   ████      ██                            ██▀▀▀      ▀▀
\033[1;91m   ████    ███████    ██▄████   ▄█████▄  ███████    ████
\033[1;91m  ██  ██     ██       ██▀       ▀ ▄▄▄██    ██         ██
\033[1;91m  ██████     ██       ██       ▄██▀▀▀██    ██         ██
\033[1;91m ▄██  ██▄    ██▄▄▄    ██       ██▄▄▄███    ██      ▄▄▄██▄▄▄
\033[1;91m ▀▀    ▀▀     ▀▀▀▀    ▀▀        ▀▀▀▀ ▀▀    ▀▀      ▀▀▀▀▀▀▀▀
"""

####Logo####

logo1 = """
\033[1;99m▄▄     ▄▄              ▄▄            ▄▄▄▄      ▄▄▄▄                ▄▄
\033[1;91m   ████    ██              ██            ▀▀██      ▀▀██                ██
\033[1;91m  ████    ██▄███▄    ▄███▄██  ██    ██    ██        ██       ▄█████▄  ██▄████▄
\033[1;91m  ██  ██   ██▀  ▀██  ██▀  ▀██  ██    ██    ██        ██       ▀ ▄▄▄██  ██▀   ██
\033[1;91m  ██████   ██    ██  ██    ██  ██    ██    ██        ██      ▄██▀▀▀██  ██    ██
\033[1;91m ▄██  ██▄  ███▄▄██▀  ▀██▄▄███  ██▄▄▄███    ██▄▄▄     ██▄▄▄   ██▄▄▄███  ██    ██
\033[1;91m ▀▀    ▀▀  ▀▀ ▀▀▀      ▀▀▀ ▀▀   ▀▀▀▀ ▀▀     ▀▀▀▀      ▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀
\033[1;99m ▄▄                                      ▄▄▄▄      ██
\033[1;91m   ████      ██                            ██▀▀▀      ▀▀
\033[1;91m   ████    ███████    ██▄████   ▄█████▄  ███████    ████
\033[1;91m  ██  ██     ██       ██▀       ▀ ▄▄▄██    ██         ██
\033[1;91m  ██████     ██       ██       ▄██▀▀▀██    ██         ██
\033[1;91m ▄██  ██▄    ██▄▄▄    ██       ██▄▄▄███    ██      ▄▄▄██▄▄▄
\033[1;91m ▀▀    ▀▀     ▀▀▀▀    ▀▀        ▀▀▀▀ ▀▀    ▀▀      ▀▀▀▀▀▀▀▀
"""
logo2 = """
       
       ✴▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇✴ 
       ✴▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇✴
       ✴▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇✴ 
       ✴▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇✴ 
       ✴▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇✴ 
       ✴▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇✴ 
       ✴▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇✴ 
       ✴▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇✴ 
     
\033[1;92m⸎✶◯  *♢  ░░░░[Abduulah] ░░░░  ♢*  ◯✶⸎
\033[1;93m⸎✶◯  *♢  ░░░░[   Atrafi    ]░░░░   ♢*  ◯✶⸎
\033[1;95m⸎✶◯  *♢  ░░░░[   Hacker  ]░░░░  ♢*  ◯✶⸎
\033[1;96m⸎✶◯  *♢    ░░░[      🔝      ]░░░░  ♢*  ◯✶⸎
\x1b[1;94m you have been hacked... 
"""
CorrectUsername = "Abdullah"
CorrectPassword = "hacker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;95mDEVOLPER USERNAME\x1b[1;92m▬▬▬▬▬▬►\x1b[1;94m")
    if (username == CorrectUsername):
    password = raw_input("\033[1;97m \x1b[1;94mDEVOLPER PASSWORD \x1b[1;93m▬▬▬▬▬▬►\x1b[1;95m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:ZABI
    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://t.me/powerhacking2977')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://t.me/powerhacking2977')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    print "\033[1;97m※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※ "
    time.sleep(0.05)
    print "\033[1;97m※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※ "
    time.sleep(0.05)
    print "\033[1;91m[1]\x1b[1;93mALL IN ONE "
    time.sleep(0.05)
    print '\x1b[1;94m[0]\033[1;91m Exit ( Back)'
    print "\033[1;97m※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※ "
    time.sleep(0.05)
    print "\033[1;97m※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※ "
    pilih_login()

def pilih_login():
    bch = raw_input('\n\n \x1b[1;96m>   ')
    if bch == '':
        print '[!] Fill in correctly'
        pilih_login()
    elif bch == '1':
        tik()
    os.system('clear')
    print logo2
    print"\033[1;94m[1]\x1b[1;93mBangladesh"
    time.sleep(0.05)
    print"\033[1;94m[2]\x1b[1;93mUSA"
    time.sleep(0.05)
    print"\033[1;94m[3]\x1b[1;93mU.k"
    time.sleep(0.05)
    print"\033[1;94m[4]\x1b[1;93mIndia"
    time.sleep(0.05)
    print"\033[1;94m[5]\x1b[1;93mBrazil"
    time.sleep(0.05)
    print"\033[1;94m[6]\x1b[1;94mJapan"
    time.sleep(0.05)
    print"\033[1;94m[7]\x1b[1;94mkorea"
    time.sleep(0.05)
    print"\033[1;94m[8]\x1b[1;94mitly"
    time.sleep(0.05)
    print"\033[1;94m[9]\x1b[1;94mspain"
    time.sleep(0.05)
    print"\033[1;94m[10]\x1b[1;94mpoland"
    time.sleep(0.05)
    print '\033[1;94m[11]\x1b[1;95mPakistan'
    time.sleep(0.05)
    print"\033[1;94m[12]\x1b[1;95mindonesia"
    time.sleep(0.05)
    print"\033[1;94m[13]\x1b[1;95mGreece"
    time.sleep(0.05)
    print"\033[1;94m[14]\x1b[1;95mAustrlia"
    time.sleep(0.05)
    print"\033[1;94m[15]\x1b[1;95mCanada"
    time.sleep(0.05)
    print"\033[1;94m[16]\x1b[1;96mCHINA"
    time.sleep(0.05)
    print"\033[1;94m[17]\x1b[1;96mdenmark"
    time.sleep(0.05)
    print"\033[1;94m[18]\x1b[1;96mFrance"
    time.sleep(0.05)
    print"\033[1;94m[19]\x1b[1;96mGermany"
    time.sleep(0.05)
    print"\033[1;94m[20]\x1b[1;96mSarilanka"
    time.sleep(0.05)
    print"\033[1;94m[21]\x1b[1;97mTurkey"
    time.sleep(0.05)
    print"\033[1;94m[22]\x1b[1;97mU.A.E"
    time.sleep(0.05)
    print"\033[1;94m[23]\x1b[1;97mSudia arabia"
    time.sleep(0.05)
    print"\033[1;94m[24]\x1b[1;97misreal"
    time.sleep(0.05)
    print"\033[1;94m[25]\x1b[1;97miran"
    time.sleep(0.05)
    print 45*'-'
    a
