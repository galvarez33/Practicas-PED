import socket, sys, time, os

def cliente():
     
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(server_address)

    try:
        fichero = input("Fichero: ")
        sock.send(fichero.encode('utf8'))
 
        while True:
            mensaje = sock.recv(1024)
            if mensaje == b'':
                break
            print(mensaje.decode('utf8'))
    
    finally:
        sock.close()
        print("Socket cerrado")


if __name__ == "__main__":
    
    server_address = '/tmp/s_p4_balsalobre'
    
    cliente()