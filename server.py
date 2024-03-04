import socket
import threading


def handle(s):
    while True:
        data = s.recv(1024)  # размер буфера
        if not data:
            s.close()
            break
        print(data)
        s.sendall(data)


s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen(5)
print("Watting for connections")
try:
    while True:
        c, a = s.accept()  # ждёт подключение с-клиентский сокет а-адресс
        print("Connected", a)
        t = threading.Thread(target=handle, args=(c,))  # создаём поток
        t.start()
finally:
    s.close()
