import socket
from time import sleep
import sys



def index():
    f = open('1.html', 'r', encoding='utf-8')
    res = f.read()        
    f.close()
    return res.encode()

def hello():
     return "Hello PYTHON!!!"

def ico():   
    with open('favicon.ico', 'rb') as f:           
        return f.read()
    
def send_file(file_name, conn):
    try:
        with open(file_name.strip('/'), 'rb') as f:           
            conn.send(OK)
            conn.send(f.read())
    except IOError:
        print('нет файла')
        conn.send(ERR_404)


HOST = (socket.gethostname(), 7771)

OK = b'HTTP/1.1 200 OK\r\n\r\n'
ERR_404 = b'HTTP/1.1 404 Not Found\r\n\r\n'

# SOCK_DGRAM - UDP,  
# SOCK_STREAM - TCP, 
# AF_INET - ip v4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ip адрес, TCP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(HOST)
sock.listen()
print("---start---")
while True:
        print("слушаю....")
        conn, addr = sock.accept()        
        # conn.send("hello from server".encode('utf-8'))
        #print('---new data----', "\n", addr, "\n", conn, "\n", sock)
        
        
        # while True:            
        #     data = conn.recv(2)                
        #     if not data:
        #         break
        #     print(data.decode())
        
        data = conn.recv(4096).decode().split('\n')
        print(*data, sep='\n')
        method, addr, ver = data[0].split()
        print(method, addr, ver, sep='\n')
        #conn.send(b'HTTP/1.0 200 OK\n\nHello World')
        
        
        if addr=="/":
            print("indeeex")
            #res = f"{OK}"             
            conn.send(OK)
            conn.send(index())
        elif addr=='/favicon.ico':
            print('favicon')            
            conn.send(OK)            
            send_file('/favicon.ico', conn)
        elif addr[-4:] in ['.jpg','.png','.gif']:
            print('picture')
            send_file(addr, conn)
        else:
            print('errrrr')
            conn.send(ERR_404)
            

        
        
        #conn.send(res.encode("utf-8"))
        # 
        print('Close')
        conn.close()
        
            
                 
                

    
 
    

#GET / HTTP/1.1




 