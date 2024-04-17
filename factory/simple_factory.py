from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    
    @abstractmethod
    def falar(self):
        pass
    
class Cachorro(Animal):
    
    def falar(self):
        print('Au au')
        
class Gato(Animal):
    
    def falar(self):
        print('Miau')        


class Pombo(Animal):
    
    def falar(self):
        print('Pruu')

        
class FabricaDeAnimais:
    
    @staticmethod
    def criar_animal(tipo_animal):
        if tipo_animal == 'cachorro':
            return Cachorro()
        elif tipo_animal == 'gato':
            return Gato()
        elif tipo_animal == 'pombo':
            return Pombo()
        else:
            return None
        
if __name__=='__main__':
    cachorro = FabricaDeAnimais.criar_animal('cachorro')
    cachorro.falar()
    
    gato = FabricaDeAnimais.criar_animal('gato')
    gato.falar()
    
    pombo = FabricaDeAnimais.criar_animal('pombo')
    pombo.falar()
    
    