from fastapi import FastAPI, HTTPException
from models import Livro, Usuario, Emprestimo
from typing import List, Optional
from uuid import UUID
from datetime import date

app = FastAPI()

livros_db: List[Livro] = []
usuarios_db: List[Usuario] = []
emprestimos_db: List[Emprestimo] = []

@app.post("/livros/", response_model=Livro)
def cadastrar_livro(livro: Livro):
    livros_db.append(livro)
    return livro

@app.get("/livros/", response_model=List[Livro])
def listar_livros():
    return livros_db

@app.get("/livros/{titulo}", response_model=Livro)
def buscar_livro_por_titulo(titulo: str):
    for livro in livros_db:
        if livro.titulo.lower() == titulo.lower():
            return livro
    return 'Error'

@app.post("/usuarios/", response_model=Usuario)
def cadastrar_usuario(usuario: Usuario):
    usuarios_db.append(usuario)
    return usuario


@app.post("/emprestimos/", response_model=Emprestimo)
def realizar_emprestimo(id_usuario: str, id_livro: str, data_emprestimo: date):
    usuario = buscar_objeto(usuarios_db, id_usuario, "Usuário não encontrado")
    livro = buscar_objeto(livros_db, id_livro, "Livro não encontrado")
    
    if not livro.disponivel:
        return 'Livro já emprestado!'
    
    livro.disponivel = False
    usuario.livros_emprestados.append(id_livro)
    
    emprestimo = Emprestimo(
        id_livro=id_livro,
        id_usuario=id_usuario,
        data_emprestimo=data_emprestimo
    )
    emprestimos_db.append(emprestimo)
    return emprestimo



@app.get("/usuarios/{usuario_id}/livros", response_model=List[Livro])
def listar_livros_emprestados(usuario_id: str):
    usuario = buscar_objeto(usuarios_db, usuario_id, "Usuário não encontrado")
    return [livro for livro_id in usuario.livros_emprestados 
            for livro in livros_db if livro.id == livro_id]
