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
    
    
    def criar_animal(self, tipo_animal):
        animal =  eval(tipo_animal)()
        return animal.falar()
        
if __name__=='__main__':
    fab = FabricaDeAnimais()
    animal = input('Qual animal você quer que eu fale ? [Cachorro, Gato, Pombo]')
    obj = fab.criar_animal(animal)
    