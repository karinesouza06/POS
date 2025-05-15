from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import date

class Livro(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    titulo: str
    autor: str
    ano_publicacao: int
    disponivel: bool = True

class Usuario(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nome: str
    livros_emprestados: List[UUID] = []

class Emprestimo(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    id_livro: UUID
    id_usuario: UUID
    data_emprestimo: date
    data_devolucao: Optional[date] = None