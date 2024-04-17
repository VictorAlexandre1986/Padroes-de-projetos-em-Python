from abc import ABC, abstractmethod

# Abstract Product A: Motor
class Motor(ABC):
    @abstractmethod
    def tipo(self):
        pass

# Concrete Product A1: Motor Elétrico
class MotorEletrico(Motor):
    def tipo(self):
        return "Motor Elétrico"

# Concrete Product A2: Motor a Gasolina
class MotorGasolina(Motor):
    def tipo(self):
        return "Motor a Gasolina"

# Abstract Product B: Carro
class Carro(ABC):
    @abstractmethod
    def detalhes(self):
        pass

# Concrete Product B1: Carro Elétrico
class CarroEletrico(Carro):
    def __init__(self, motor):
        self.motor = motor

    def detalhes(self):
        return f"Carro Elétrico com {self.motor.tipo()}"

# Concrete Product B2: Carro a Gasolina
class CarroGasolina(Carro):
    def __init__(self, motor):
        self.motor = motor

    def detalhes(self):
        return f"Carro a Gasolina com {self.motor.tipo()}"

# Abstract Factory
class FabricaCarro(ABC):
    @abstractmethod
    def criar_motor(self):
        pass

    @abstractmethod
    def criar_carro(self):
        pass

# Concrete Factory 1: Fabrica de Carros Elétricos
class FabricaCarroEletrico(FabricaCarro):
    def criar_motor(self):
        return MotorEletrico()

    def criar_carro(self):
        return CarroEletrico(self.criar_motor())

# Concrete Factory 2: Fabrica de Carros a Gasolina
class FabricaCarroGasolina(FabricaCarro):
    def criar_motor(self):
        return MotorGasolina()

    def criar_carro(self):
        return CarroGasolina(self.criar_motor())

# Cliente
if __name__ == "__main__":
    fabrica_carro_eletrico = FabricaCarroEletrico()
    carro_eletrico = fabrica_carro_eletrico.criar_carro()
    print(carro_eletrico.detalhes())

    fabrica_carro_gasolina = FabricaCarroGasolina()
    carro_gasolina = fabrica_carro_gasolina.criar_carro()
    print(carro_gasolina.detalhes())
    
    """
    Neste exemplo:

Motor e Carro são as interfaces para os tipos de produtos que uma fábrica pode produzir.
MotorEletrico e MotorGasolina são implementações concretas de Motor.
CarroEletrico e CarroGasolina são implementações concretas de Carro.
FabricaCarro é a interface para a fábrica abstrata que pode produzir motores e carros.
FabricaCarroEletrico e FabricaCarroGasolina são implementações concretas da fábrica que 

produzem motores e carros elétricos ou a gasolina, respectivamente.
Quando o código cliente (a parte no if __name__ == "__main__":) quer criar um carro, 
ele simplesmente instancia uma fábrica concreta (FabricaCarroEletrico ou FabricaCarroGasolina)
e usa essa fábrica para criar um carro. A fábrica cuida de criar o motor apropriado para o tipo de carro.
Isso mantém o código do cliente desacoplado das classes concretas de carro e motor, permitindo fácil 
extensão para novos tipos de carros e motores no futuro.
    """