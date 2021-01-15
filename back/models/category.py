class Category:
    nome: str
    descricao: str
    id_: int

    def __init__(self, nome: str, descricao: str, id_: int = None) -> None: 
        self.id_ = id_
        self.nome = nome
        self.descricao = descricao

    @property
    def nome(self)->str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @property
    def descricao(self)->str:
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao:str):
        self.__descricao = descricao

    @property
    def id_(self)->int:
        return self.__id_
    
    @id_.setter
    def id_(self, id_:int):
        self.__id_ = id_
