import pandas as pd

pedidos = pd.read_csv('20250702_Pedidos_csv_2025.csv', sep=';', encoding='utf-16')
pedidos['IdPedido'] = pedidos['IdPedido'].astype(str)

def consultar_pedido():
    id_pedido = input("Digite o ID do pedido: ").strip()
    
    pedido = pedidos[pedidos['IdPedido'] == id_pedido]
    
    if pedido.empty:
        print("\nErro 404: Pedido não encontrado")
    else:

        dados = pedido.iloc[0]
        print("\nDados do Pedido:")
        print(f"ID: {dados['IdPedido']}")
        print(f"Protocolo: {dados['ProtocoloPedido']}")
        print(f"Esfera: {dados['Esfera']}")
        print(f"UF: {dados['UF']}")
        print(f"Município: {dados['Municipio']}")
        print(f"Órgão Destinatário: {dados['OrgaoDestinatario']}")
        print(f"Situação: {dados['Situacao']}")
        print(f"Data Registro: {dados['DataRegistro']}")
        print(f"Prazo Atendimento: {dados['PrazoAtendimento']}")
        print(f"Prorrogado: {dados['FoiProrrogado']}")
        print(f"Reencaminhado: {dados['FoiReencaminhado']}")
        print(f"Forma Resposta: {dados['FormaResposta']}")
        print(f"Origem: {dados['OrigemSolicitacao']}")
        print(f"ID Solicitante: {dados['IdSolicitante']}")
        print(f"Assunto: {dados['AssuntoPedido']}")
        print(f"Subassunto: {dados['SubAssuntoPedido']}")
        print(f"Tags: {dados['Tag']}")
        print(f"Data Resposta: {dados['DataResposta']}")
        print(f"Decisão: {dados['Decisao']}")
        print(f"Especificação Decisão: {dados['EspecificacaoDecisao']}")

if __name__ == "__main__":
    consultar_pedido()