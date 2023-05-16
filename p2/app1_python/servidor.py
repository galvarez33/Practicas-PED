class Server:
    def __init__(self, rp, wp):
        self.rp = rp
        self.wp = wp
        
    def run(self):   
        path = self.rp.readline()
        path = path.decode('utf8').strip()
        print(f"El servidor recibe: {path}")
        self.responder(path)

    def responder(self,path):
        l = []
        try:
            file = open(path,"rb")
            for line in file:
                l.append(line)
                self.wp.write(line)
                self.wp.flush()
            self.wp.close()

        except Exception as e:  
                       
            print(e)
            self.wp.write(f"Error al intentar abrir el fichero: {path}".encode("utf8"))
