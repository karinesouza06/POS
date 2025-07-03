from fastapi import FastAPI, HTTPException
from models import LivroModel
from typing import List

app = FastAPI()
livros: List[LivroModel] = []

@app.get("/livros", response_model=List[LivroModel])
def listar_livros():
    return livros

@app.get("/livros/{titulo}", response_model=LivroModel)
def obter_livro_por_titulo(titulo: str):
    for livro in livros:
        if livro.titulo == titulo:
            return livro
    raise HTTPException(404, "Não localizado")

@app.delete("/livros/{titulo}", response_model=LivroModel)
def deletar_livro(titulo: str):
    for id, livro in enumerate(livros):
        if livro.titulo == titulo:
            livros.pop(id)
            return livro
    raise HTTPException(404, "Não localizado")

@app.post("/livros", response_model=LivroModel)
def criar_livro(livro: LivroModel):
    livros.append(livro)
    return livro

@app.put("/livros/{titulo}", response_model=LivroModel)
def atualizar_livro(titulo: str, livro_atualizado: LivroModel):
    for id, livro in enumerate(livros):
        if livro.titulo == titulo:
            livros[id] = livro_atualizado
            return livro_atualizado
    raise HTTPException(404, "Não localizado")