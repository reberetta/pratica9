class Seller:
    nome:str
    email:str
    telefone:str
    id_:int
    def __init__(self, nome:str, email:str, telefone:str, id_:int=None)->None:
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.id_ = id_

    
    @property
    def nome(self)->str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str)->None:
        self.__nome = nome 

    
    @property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email(self, email:str)->None:
        self.__email = email


    @property
    def telefone(self)->str:
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone:str)->None:
        self.__telefone = telefone

    
    @property
    def id_(self)->int:
        return self.__id_
    
    @id_.setter
    def id_(self, id_:int)->None:
        self.__id_ = id_