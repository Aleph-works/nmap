"""
Make a program that scans the port on a local host in the network and prints the corresponding port service name,
so for example port 80 will print "80/http", and 22 prints "22/ssh"
"""

import socket
import threading
import time

host = input("Enter host: ")
thread_count = int(input("Enter threads: "))
port_range_start = int(input("Enter start port range: "))
port_range_end = int(input("Enter end port range: "))
start_time = time.time()

def scan(thread_index):
    global is_done
    port = thread_index
    while port < port_range_end:
        prev_port = port
        port += thread_count
        s = socket.socket()
        s.settimeout(0.5)
        # print(f"{thread_index} is scanning {prev_port}\n")
        try:
            s.connect((host, prev_port))
        except:
            continue
        try:
            service = socket.getservbyport(prev_port)
        except:
            service = "unknown"
        print(f"\nFound open port: {prev_port}/{service}")
    
    if thread_index == thread_count - 1 + port_range_start:
        timed = time.time() - start_time
        print(f"Done! ({timed} sec)")

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

print("Scanning...")
for start_port in range(0, thread_count):
    thread = threading.Thread(target=scan, args=(start_port + port_range_start,))
    thread.start()
