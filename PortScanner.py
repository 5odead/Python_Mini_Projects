print(" ███████████                      █████        █████████                                                             ")
print("░░███░░░░░███                    ░░███        ███░░░░░███                                                            ")
print(" ░███    ░███  ██████  ████████  ███████     ░███    ░░░   ██████   ██████   ████████   ████████    ██████  ████████ ")
print(" ░██████████  ███░░███░░███░░███░░░███░      ░░█████████  ███░░███ ░░░░░███ ░░███░░███ ░░███░░███  ███░░███░░███░░███")
print(" ░███░░░░░░  ░███ ░███ ░███ ░░░   ░███        ░░░░░░░░███░███ ░░░   ███████  ░███ ░███  ░███ ░███ ░███████  ░███ ░░░ ")
print(" ░███        ░███ ░███ ░███       ░███ ███    ███    ░███░███  ███ ███░░███  ░███ ░███  ░███ ░███ ░███░░░   ░███     ")
print(" █████       ░░██████  █████      ░░█████    ░░█████████ ░░██████ ░░████████ ████ █████ ████ █████░░██████  █████    ")
print("░░░░░         ░░░░░░  ░░░░░        ░░░░░      ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░     ")

                                                                                                                     
import socket
import threading
import queue

Target = input("Enter Target IP Address: ") or "192.168.1.1"

try:
    number_threads = int(input("Enter The Number Of Threads (Default Value = 100): ") or 100)
except ValueError:
    number_threads = 100

port_queue = queue.Queue()

for port in range(1, 1024):
    port_queue.put(port)

def worker():
    while not port_queue.empty():
        port = port_queue.get()

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            if sock.connect_ex((Target, port)) == 0:
                print(f"[+] Port {port} is open on {Target}")

            sock.close()
        except:
            pass

        port_queue.task_done()  #Task Done

threads = []
for _ in range(number_threads):
    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("[*] Port scan complete.")

