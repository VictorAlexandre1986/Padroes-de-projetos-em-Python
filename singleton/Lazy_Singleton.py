class Singleton:
    
    __instance = None
    
    def __init__(self):
        if not Singleton.__instance:
            '''
                1º Essa condição é executada por causa de tentar instaciar S1
                2º Essa condição é executada no momento que Singleton.get_instance() é executado, esse 
                método chama o método init, como a variavel __instance ainda não tem 
                objeto ele cai nessa condição de novo
            '''
            print('O metodo __init__ foi chamado')
        else:
            '''
                Cai nessa condição quando tenta instanciar s2 , 
                ele verifica que existe um objeto ja criado por 
                causa do Singleton.get_instance() ter sido executado anteriormente
            '''
            print(f'A instancia ja foi criada: {self.get_instance()} ')
            
    
    @classmethod
    def get_instance(cls):
        #Verifica que não existe instancia na variavel __instance
        if not cls.__instance:
            #Instancia a classe e atribui a variavel __instance
            cls.__instance = Singleton() 
        #Retorna a variavel com o objeto
        return cls.__instance
    
    
if __name__=='__main__':
    
    s1 = Singleton() # A classe é iniciada mas o objeto não é criado...  
    
    print(f'Objeto criado agora:  {Singleton.get_instance()}')    
    
    s2 = Singleton() # A instância já criada
        