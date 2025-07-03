from pydantic import BaseModel
from datetime import date
from typing import List

class LivroModel(BaseModel):
    titulo:str
    ano:int
    edicao:int