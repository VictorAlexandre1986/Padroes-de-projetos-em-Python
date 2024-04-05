

class Singleton(object):
    '''
    Padrão de projeto utilizando quando é necessário apenas uma instancia, 
    como por exemplo conexão com o banco de dados,
    fila de impressão etc.
    '''   
    
    def __new__(cls):
        if not hasattr(cls, 'isinstance'):
            cls.instance = super(Singleton, cls)
            print(f'Criando um objeto {cls.instance}')
        return cls.instance


if __name__ =='__main__':
    s1 = Singleton()
    print(f'Instancia 1 {id(s1)}')
    
    s2 = Singleton()
    print(f'Instancia 2 {id(s2)}')