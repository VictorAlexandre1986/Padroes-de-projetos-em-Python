from abc import ABC, abstractmethod

# Abstract Product A: Smartphone
class Smartphone(ABC):
    @abstractmethod
    def modelo(self):
        pass

# Concrete Product A1: Smartphone Samsung
class SamsungSmartphone(Smartphone):
    def modelo(self):
        return "Samsung Galaxy S21"

# Concrete Product A2: Smartphone Apple
class AppleSmartphone(Smartphone):
    def modelo(self):
        return "iPhone 13"

# Abstract Product B: Laptop
class Laptop(ABC):
    @abstractmethod
    def modelo(self):
        pass

# Concrete Product B1: Laptop Dell
class DellLaptop(Laptop):
    def modelo(self):
        return "Dell XPS 13"

# Concrete Product B2: Laptop HP
class HPLaptop(Laptop):
    def modelo(self):
        return "HP Spectre x360"

# Abstract Factory
class LojaEletronicos(ABC):
    @abstractmethod
    def criar_smartphone(self):
        pass

    @abstractmethod
    def criar_laptop(self):
        pass

# Concrete Factory 1: Loja de Eletrônicos Samsung
class LojaSamsung(LojaEletronicos):
    def criar_smartphone(self):
        return SamsungSmartphone()

    def criar_laptop(self):
        return DellLaptop()

# Concrete Factory 2: Loja de Eletrônicos Apple
class LojaApple(LojaEletronicos):
    def criar_smartphone(self):
        return AppleSmartphone()

    def criar_laptop(self):
        return HPLaptop()

# Cliente
if __name__ == "__main__":
    loja_samsung = LojaSamsung()
    smartphone_samsung = loja_samsung.criar_smartphone()
    laptop_samsung = loja_samsung.criar_laptop()
    print("Modelo do Smartphone Samsung:", smartphone_samsung.modelo())
    print("Modelo do Laptop Dell:", laptop_samsung.modelo())

    print("-----------------------")

    loja_apple = LojaApple()
    smartphone_apple = loja_apple.criar_smartphone()
    laptop_hp = loja_apple.criar_laptop()
    print("Modelo do Smartphone Apple:", smartphone_apple.modelo())
    print("Modelo do Laptop HP:", laptop_hp.modelo())