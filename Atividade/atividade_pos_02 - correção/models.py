from pydantic import BaseModel 

class Livro(BaseModel):
    uuid:str
    titulo:str 
    autor:str
