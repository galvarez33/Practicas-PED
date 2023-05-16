import os
import sys

from cliente import Cliente
from servidor import Server

read_cliente, write_servidor = os.pipe()
read_servidor, write_cliente = os.pipe()

read_cliente = os.fdopen(read_cliente,"rb")
read_servidor = os.fdopen(read_servidor,"rb")
write_cliente = os.fdopen(write_cliente,"wb")
write_servidor = os.fdopen(write_servidor,"wb")

pid = os.fork()

if pid:
    write_cliente.close()
    read_cliente.close()

    servidor = Server(read_servidor,write_servidor)
    servidor.run()
else:
    write_servidor.close()
    read_servidor.close()

    cliente = Cliente(read_cliente,write_cliente)
    cliente.run(f"{sys.argv[1]}\n")
