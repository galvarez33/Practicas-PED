class Cliente:
    def __init__(self, read_pipe, write_pipe):
        self.read_pipe = read_pipe
        self.write_pipe = write_pipe
        
    def run(self):
        self.write_pipe.write(b"Solicitud de hora\n")
        self.write_pipe.flush()
        respuesta = self.read_pipe.read().decode().rstrip()
        print(respuesta)
       