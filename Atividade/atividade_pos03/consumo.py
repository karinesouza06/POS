import requests
from models import LivroModel

API_URL = "http://127.0.0.1:8000"


def listar_todos_livros():
    response = requests.get(f"{API_URL}/livros")
    livros = response.json()
    
    if not livros:
        print("\nNenhum livro cadastrado.")
    else:
        print("\nLivros cadastrados:")
        for livro in livros:
            print(f"Título: {livro['titulo']}, Ano: {livro['ano']}, Edição: {livro['edicao']}")

def pesquisar_livro_por_titulo():
    titulo = input("\nDigite o título do livro que deseja pesquisar: ").strip()
    if not titulo:
        print("Título não pode ser vazio.")
        return
    
    response = requests.get(f"{API_URL}/livros/{titulo}")
    
    if response.status_code == 404:
        print(f"\nLivro com título '{titulo}' não encontrado.")
        return
    
    livro = response.json()
    print(f"\nLivro encontrado:")
    print(f"Título: {livro['titulo']}, Ano: {livro['ano']}, Edição: {livro['edicao']}")

def cadastrar_livro():
    print("\nCadastro de novo livro:")
    titulo = input("Título: ").strip()
    if not titulo:
        print("Título não pode ser vazio.")
        return
    
    ano = int(input("Ano de publicação: "))
    edicao = int(input("Edição: "))
    
    novo_livro = LivroModel(titulo=titulo, ano=ano, edicao=edicao)
    
    response = requests.post(f"{API_URL}/livros", json=novo_livro.dict())
    
    print(f"\nLivro '{titulo}', ano {ano}, edição número {edicao}, foi cadastrado com sucesso!")

def deletar_livro():
    titulo = input("\nDigite o título do livro que deseja deletar: ").strip()
    if not titulo:
        print("Título não pode ser vazio.")
        return
    check_response = requests.get(f"{API_URL}/livros/{titulo}")
    if check_response.status_code == 404:
        print(f"\nLivro com título '{titulo}' não encontrado.")
        return
    
    response = requests.delete(f"{API_URL}/livros/{titulo}")
    
    print(f"\nLivro '{titulo}' deletado com sucesso!")

def editar_livro():
    titulo = input("\nDigite o título do livro que deseja editar: ").strip()
    if not titulo:
        print("Título não pode ser vazio.")
        return

    check_response = requests.get(f"{API_URL}/livros/{titulo}")
    if check_response.status_code == 404:
        print(f"\nLivro com título '{titulo}' não encontrado.")
        return
    
    livro_atual = check_response.json()
    print("\nDados atuais do livro:")
    print(f"Título: {livro_atual['titulo']}, Ano: {livro_atual['ano']}, Edição: {livro_atual['edicao']}")
    
    print("\nDigite os novos dados (deixe em branco para manter o valor atual):")
    novoTitulo = input(f"Novo título [{livro_atual['titulo']}]: ").strip() or livro_atual['titulo']
    
    novoAno = input(f"Novo ano [{livro_atual['ano']}]: ").strip()
    novoAno = int(novoAno) if novoAno else livro_atual['ano']
    
    novaEdicao = input(f"Nova edição [{livro_atual['edicao']}]: ").strip()
    novaEdicao = int(novaEdicao) if novaEdicao else livro_atual['edicao']
    
    livro_atualizado = {
        "titulo": novoTitulo,
        "ano": novoAno,
        "edicao": novaEdicao
    }
    
    
    requests.delete(f"{API_URL}/livros/{titulo}")
    
    requests.post(f"{API_URL}/livros", json=livro_atualizado)
    
    print(f"\nLivro '{titulo}' atualizado com sucesso!")

def menu():
    while True:
        print("\n==== MENU ====")
        print("1 - Listar todos os livros")
        print("2 - Pesquisar livro por título")
        print("3 - Cadastrar um livro")
        print("4 - Deletar um livro")
        print("5 - Editar um livro")
        print("6 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            listar_todos_livros()
        elif opcao == "2":
            pesquisar_livro_por_titulo()
        elif opcao == "3":
            cadastrar_livro()
        elif opcao == "4":
            deletar_livro()
        elif opcao == "5":
            editar_livro()
        elif opcao == "6":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 6.")

if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Gerenciamento de Livros!")
    menu()