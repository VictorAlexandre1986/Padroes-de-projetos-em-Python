from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    _engine = None
    _session = None

    def __init__(self, db_path):
        self.db_path = db_path
        self._engine = create_engine(f'sqlite:///{db_path}')
        self._session = sessionmaker(bind=self._engine)

    @property
    def session(self):
        if not self._session:
            self._session = sessionmaker(bind=self._engine)
        return self._session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def cadastrar(self,session,nome ):
        # Exemplo de interação com o banco de dados
        new_user = User(name=nome)
        session.add(new_user)
        session.commit()
        print('Cadastrou com sucesso')

    def select_all(self,session):
        users = session.query(User).all()
        for user in users:
          print(user.name)
    
    def select_nome(self,session,nome):
        users = session.query(User).filter(User.name.like(f'%{nome}%')).all()
        for user in users:
            print(user.name)
            
    def update(self, session, nome, novo_nome):
        user_to_update = session.query(User).filter_by(name=nome).first()
        if user_to_update:
            user_to_update.name = novo_nome
            session.commit()
    
    def delete_um_usuario(self, session, nome):
        user_to_delete = session.query(User).filter_by(name=nome).first()
        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()

        # Select para verificar o delete
        deleted_users = session.query(User).filter_by(name=nome).all()
        if not deleted_users:
            print(f"Usuário {nome} foi deletado com sucesso!")
            
    def deletar_mais_de_usuario(self,session,nome):
        user_to_delete = session.query(User).filter_by(name=nome).all()
        for user in user_to_delete:
            if user:
                session.delete(user)
                session.commit()
                print(f"Usuário '{nome}' foi deletado com sucesso!")
            else:
                print(f"Usuário '{nome}' não encontrado.")

if __name__ == "__main__":
    db = Database("example.db")
    session = db.session

    # Cria as tabelas no banco de dados, se ainda não existirem
    Base.metadata.create_all(db._engine)

    user = User();
    user.cadastrar(session, 'Victor')
    user.cadastrar(session, 'Alexandre')

    user.select_all(session)
    
    user.select_nome(session,'Victor')
    
    user.update(session,'Victor','Seila')
    
    user.select_all(session)
  
    session.close()