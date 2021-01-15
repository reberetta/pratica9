from datetime import datetime

class Log:
    __data_do_registro:datetime
    __acao:str
    __elemento:str
    __id_:int

    def __init__(self, acao:str, elemento:str, data_do_registro:datetime=None, id_:int=None)->None:
        self.data_do_registro = data_do_registro
        self.acao = acao
        self.elemento = elemento
        self.id_ = id_

    @property
    def data_do_registro(self)->datetime:
        return self.__data_do_registro
    
    @data_do_registro.setter
    def data_do_registro(self, data_do_registro:datetime)->None:
        if data_do_registro == None:
            self.__data_do_registro = datetime.now()
        else:
            self.__data_do_registro = data_do_registro
    
    @property
    def acao(self)->str:
        return self.__acao
    
    @acao.setter
    def acao(self, acao:str)->None:
        self.__acao = acao
    
    @property
    def elemento(self)->str:
        return self.__elemento
    
    @elemento.setter
    def elemento(self, elemento:str)->None:
        self.__elemento = elemento

    @property
    def id_(self)->int:
        return self.__id_
    
    @id_.setter
    def id_(self, id_:int)->None:
        self.__id_ = id_

    def __repr__(self):
        return(f"{self.data_do_registro} : {self.acao} {self.elemento}")