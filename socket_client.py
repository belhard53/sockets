import socket



HOST = (socket.gethostname(), 7771)
#print(HOST)
sock = socket.socket()
sock.connect(HOST)


req = b"GET / HTTP/1.1"
sock.send(req)

# пересылка по несколько блоков
#sent = 0
# while sent <len(req):
#     sent = sent + sock.send(req[sent:])
    
# тоже самое но одним методом
#sock.sendall(req)
#print("отрпавленно байт", sock.send(req))

# пересылка файла
#f = open(r'd:\test.txt', 'rb')
#sock.sendfile(f)
#f.close()

data = sock.recv(1024)
print(data)

sock.close()



