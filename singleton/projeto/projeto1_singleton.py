import sqlite3

class Singleton(type):
    
    __instance = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]
    
class DataBase(metaclass=Singleton):
        
    connection = None
    
    def connect(self):
        if self.connection is None:
            print('Ainda nao tem conexao, vamos cria-la')
            self.connection = sqlite3.connect('geek.db')
            self.cursor = self.connection.cursor()
        return self.cursor
    
    
if __name__=='__main__':
    db1 = DataBase()
    db1.connect()

    db2 = DataBase()
    db2.connect()


    