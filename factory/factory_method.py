from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):
    
    @abstractmethod
    def __repr__(self):
        pass
    
class SecaoPessoal(Secao):
    
    def __repr__(self):
        return 'Seção Pessoal'
    
class SecaoAlbum(Secao):
    
    def __repr__(self):
        return 'Seção Album'

class SecaoProjeto(Secao):
    
    def __repr__(self):
        return 'Seção Projeto'
    
class SecaoPublicacao(Secao):
    
    def __repr__(self):
        return 'Seção Publicação'
    

class Perfil(metaclass=ABCMeta):
    
    def __init__(self):
        self.secoes=[]
        self.criar_perfil()
    
    def get_secoes(self):
        return self.secoes
    
    def add_secao(self, secao):
        self.secoes.append(secao)
        
class Linkedin(Perfil):
    
    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPublicacao())
        
        
class Facebook(Perfil):
    
    def criar_perfil(self):
        self.add_secao(SecaoAlbum())
        self.add_secao(SecaoPessoal())

if __name__ =='__main__':
    rede_social = input('Qual rede social voce deseja criar o perfil [Linkedin, Facebook]')

    perfil = eval(rede_social)()
    
    print(f'Criando o perfil no {type(perfil).__name__}')
    print(f'O perfil tem as seções {perfil.get_secoes()}')