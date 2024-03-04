import socket

s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen(5)
print("Watting for connections")
c, a = s.accept()      #ждёт подключение с-клиентский сокет а-адресс 
print("Connected", a)
data = c.recv(1024)    #размер буфера
print(data)
c.sendall(data)
c.close()
s.close()
