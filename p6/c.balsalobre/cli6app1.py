import socket, sys, time, os

def cliente():
    direc = ("127.0.0.1", 0)
    server_address = ("localhost", 3001) 
     
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    try:
        fichero = input("Fichero: ")
        sock.send(fichero.encode('utf8'))
 
        while True:
            mensaje = sock.recv(1024)
            if mensaje == b'':
                break
            print(mensaje.decode('utf8'), end="")
    
    finally:
        sock.close()
        print("Socket cerrado")


if __name__ == "__main__":
    
    cliente()