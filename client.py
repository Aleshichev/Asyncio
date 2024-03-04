import socket
import time

s = socket.socket()
s.connect(("127.0.0.1", 5000))
try:
    while True:
        s.sendall(b"Hello")
        data = s.recv(1024)
        print(data)
        time.sleep(2)
finally:
    s.close()
