import socket, sys

def cliente():
    
    direc = ("127.0.0.1", 0)
    server_address = ("localhost", 6351) 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(direc)

    try:
        fichero = input("Fichero: ")
        sock.sendto(fichero.encode('utf8'), server_address)
 
        while True:
            mensaje, direc = sock.recvfrom(1024)
            if not mensaje:
                break
            print(mensaje.decode('utf8'), end = "")
            sock.sendto("ACK".encode('utf8'), server_address)
    
    finally:
        sock.close()
        print("Socket cerrado")


if __name__ == "__main__":
    
    cliente()