import os
import socket
import setproctitle
import time

#Cambiar el nombre del proceso
setproctitle.setproctitle("serv5")

# Verificar que el nombre haya sido cambiado
print(f"Nombre actual del proceso: {setproctitle.getproctitle()}")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('localhost', 12345))

print("Esperando conexiones...")

while True:
    data, addr = sock.recvfrom(1024)
    
    if data.decode().lower() == "cerrar":
        print("cerrando servidor")
        break
        
        
        
    elif data.decode().lower() == "hora":
        print('\nSolicitud de hora recibida en %s' % time.asctime())
        respuesta = time.strftime('%H:%M:%S') + '\n'
        sock.sendto(respuesta.encode(), addr)
        

    else:
        mensaje = "Entrada no reconocida\n"
        sock.sendto(mensaje.encode(), addr)
sock.close()

    


    
        
    
    
