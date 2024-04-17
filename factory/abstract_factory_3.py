from abc import ABC, abstractmethod

# Abstract Product A: Animal
class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

# Concrete Product A1: Vaca
class Vaca(Animal):
    def emitir_som(self):
        return "Muuu"

# Concrete Product A2: Galinha
class Galinha(Animal):
    def emitir_som(self):
        return "Cocoricó"

# Concrete Product A3: Leão
class Leao(Animal):
    def emitir_som(self):
        return "Rugido"

# Abstract Product B: Habitat
class Habitat(ABC):
    @abstractmethod
    def tipo(self):
        pass

# Concrete Product B1: Habitat de Fazenda
class Fazenda(Habitat):
    def tipo(self):
        return "Habitat de Fazenda"

# Concrete Product B2: Habitat Selvagem
class Selva(Habitat):
    def tipo(self):
        return "Habitat Selvagem"

# Abstract Factory
class FabricaAnimais(ABC):
    @abstractmethod
    def criar_animal(self):
        pass

    @abstractmethod
    def criar_habitat(self):
        pass

# Concrete Factory 1: Fabrica de Animais de Fazenda
class FabricaAnimaisFazenda(FabricaAnimais):
    def criar_animal(self):
        return Vaca()

    def criar_habitat(self):
        return Fazenda()

# Concrete Factory 2: Fabrica de Animais Selvagens
class FabricaAnimaisSelva(FabricaAnimais):
    def criar_animal(self):
        return Leao()

    def criar_habitat(self):
        return Selva()

# Cliente
if __name__ == "__main__":
    fabrica_fazenda = FabricaAnimaisFazenda()
    animal_fazenda = fabrica_fazenda.criar_animal()
    habitat_fazenda = fabrica_fazenda.criar_habitat()
    print(f"Animal da {habitat_fazenda.tipo()}: {animal_fazenda.emitir_som()}")

    fabrica_selva = FabricaAnimaisSelva()
    animal_selva = fabrica_selva.criar_animal()
    habitat_selva = fabrica_selva.criar_habitat()
    print(f"Animal da {habitat_selva.tipo()}: {animal_selva.emitir_som()}")
    
    """
    Neste exemplo:

Animal e Habitat são as interfaces para os tipos de produtos que uma fábrica pode produzir.
Vaca, Galinha e Leao são implementações concretas de Animal.
Fazenda e Selva são implementações concretas de Habitat.
FabricaAnimais é a interface para a fábrica abstrata que pode produzir animais e habitats.
FabricaAnimaisFazenda e FabricaAnimaisSelva são implementações concretas da fábrica que produzem animais de fazenda ou selvagens, respectivamente.

No código cliente (if __name__ == "__main__":), criamos uma instância de FabricaAnimaisFazenda 
para produzir um animal de fazenda e uma instância de FabricaAnimaisSelva para produzir um animal selvagem. 
Em seguida, imprimimos o tipo de habitat e o som que cada animal emite.
Este exemplo mostra como o padrão Abstract Factory permite que você crie famílias de objetos relacionados,
como animais e seus habitats, sem precisar especificar as classes concretas. 
Isso facilita a criação de novas famílias de objetos no futuro sem modificar o código cliente existente.
    """