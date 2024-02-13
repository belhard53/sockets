import socket



HOST = (socket.gethostname(), 7771)
#HOST = ('37.212.67.67', 7771)
#HOST = ('192.168.0.5', 7771)
#print(HOST)
sock = socket.socket()
sock.connect(HOST)


req = b"GET / HTTP/1.1"
sock.send(req)
#sent = 0
# while sent <len(req):
#     sent = sent + sock.send(req[sent:])
    
#sock.sendall(req)
#print("отрпавленно байт", sock.send(req))

#f = open(r'd:\test.txt', 'rb')
#sock.sendfile(f)
#f.close()

data = sock.recv(1024)
print(data)

sock.close()



