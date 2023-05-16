import os

class Cliente:
    def __init__(self,rp, wp):
        self.rp = rp
        self.wp = wp
        
    def run(self,path):
        path = path.encode('utf-8')
        self.wp.write(path)
        self.wp.flush() #si no hay flush se queda esperando
        
        while True: 
            line = self.rp.readline()
            if not line:
                break
            os.write(1, line)
        self.wp.close()

