import socket
import threading
import select


def handle(s):

    data = s.recv(1024)  # размер буфера
    if not data:
        connections.remove(s)
        s.close()
        return
    print(data)
    s.sendall(data)


s = socket.socket()
s.setblocking(False)  # неблокирующий сокет
s.bind(("127.0.0.1", 5000))
s.listen(5)
connections = [s]
print("Watting for connections")
try:
    while True:
        r_s, _, _ = select.select(
            connections, [], []
        )  # список сокетов готовых для: чтения / записи/ с ошибками
        for r in r_s:
            if r == s:
                c, a = s.accept()  # ждёт подключение с-клиентский сокет а-адресс
                print("Connected", a)
                connections.append(c)
            else:
                handle(r)
finally:
    s.close()
