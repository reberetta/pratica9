class Marketplace:
    nome:str
    descricao:str
    id_:int

    def __init__(self, nome:str, descricao:str, id_:int=None)->None:
        self.nome = nome
        self.descricao = descricao
        self.id_ = id_
    

    @property
    def nome(self)->str:
        return self.__nome

    @nome.setter
    def nome(self, nome:str)->None:
        self.__nome = nome

    
    @property
    def descricao(self)->str:
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao:str)->None:
        self.__descricao = descricao

        
    @property
    def id(self)->str:
        return self.__id
    
    @id.setter
    def id(self, id:int)->None:
        self.__id = id

    
    def __repr__(self):
        return f"Nome: {self.nome}"