import socket
import threading
import select
import time

# ---------- not block server loop----------------

# def handle(s):

#     data = s.recv(1024)  # размер буфера
#     if not data:
#         connections.remove(s)
#         s.close()
#         return
#     print(data)
#     s.sendall(data)

# s = socket.socket()
# s.setblocking(False)  # неблокирующий сокет
# s.bind(("127.0.0.1", 5000))
# s.listen(5)
# connections = [s]
# print("Watting for connections")
# try:
#     while True:
#         r_s, _, _ = select.select(
#             connections, [], []
#         )  # список сокетов готовых для: чтения / записи/ с ошибками
#         for r in r_s:
#             if r == s:
#                 c, a = s.accept()  # ждёт подключение с-клиентский сокет а-адресс
#                 print("Connected", a)
#                 connections.append(c)
#             else:
#                 handle(r)
# finally:
#     s.close()

# -----thread server---------------------------------


def handle(s):

    while True:
        try:
            s.sendall(b"Hello")
        except BrokenPipeError:
            break
        time.sleep(0.5)


s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen(5)
print("Watting for connections")
try:
    while True:

        c, a = s.accept()  # ждёт подключение с-клиентский сокет а-адресс
        print("Connected", a)
        t = threading.Thread(target=handle, args=(c,))
        t.start()
finally:
    s.close()
