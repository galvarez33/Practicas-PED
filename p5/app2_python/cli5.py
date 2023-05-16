import sys
import socket
import setproctitle

# Cambiar el nombre del proceso
setproctitle.setproctitle("cli5")

# Verificar que el nombre haya sido cambiado
print(f"\nNombre actual del proceso: {setproctitle.getproctitle()}\n")

class Cliente:
    
    def __init__(self):
        pass
        
        
    def ejecutar(self,entrada):

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', 12345)
        
        if entrada.lower() == "cerrar":
            mensaje = "Cerrando..."
            print(mensaje)
            sock.sendto(entrada.encode(),server_address)
        

        
        elif entrada.lower() == "hora":   
            mensaje = "Solicitud de hora\n"
            sock.sendto(entrada.encode(),server_address)
            print("solicitud enviada")
            respuesta, _ = sock.recvfrom(1024)
            respuesta = respuesta.decode()
            print(f"La hora recibida es: {respuesta}")
        
        else:
            sock.sendto(entrada.encode(),server_address)
            respuesta, _ = sock.recvfrom(1024)
            print(f"\n{respuesta.decode()}")


        sock.close()
  

if __name__ == '__main__':
    
    cliente = Cliente()

    while True:
        entrada = input ("Desea recibir HORA o CERRAR : ")
        cliente.ejecutar(entrada)
        break
            

        
