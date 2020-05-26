"""UDP listen and read.

Listen UDP traffic on port _p and read 1024 bytes into buffer _b.

Source: programming-idioms.org
"""

# Implementation author: awesmubarak
# Created on 2019-09-26T19:14:27.532845Z
# Last modified on 2019-09-26T19:28:59.877508Z
# Version 2

import socket

UDP_IP = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, p))
while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print("received message:", data)
