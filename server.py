import socket

s = socket.socket()
s.listen(5)
s.bind(("127.0.0.1", 500))
c, a = s.accept()
data = c.recv(1024)
print(data)
c.sendall(data)
c.close
s.close
