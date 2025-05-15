from fastapi import FastAPI
from typing import List
from models import Livro, Usuario, Emprestimo
import uuid 

acervo:List[Livro]=[]

app = FastAPI()

@app.post("/livros", response_model=Livro)
def cadastrar_livro(livro:Livro):
    livro.uuid = uuid.uuid4()
    acervo.append(livro)
    return livro

@app.get("/livros", response_model=List[Livro])
def listar_livros():
    return acervo