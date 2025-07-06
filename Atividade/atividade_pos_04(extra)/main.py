from fastapi import FastAPI, HTTPException
import pandas as pd


pedidos = pd.read_csv('20250702_Pedidos_csv_2025.csv', sep=';', encoding='utf-16')


pedidos['IdPedido'] = pedidos['IdPedido'].astype(str)

app = FastAPI()

@app.get("/pedido/{id_pedido}")
def get_pedido(id_pedido: str):
  
    pedido = pedidos[pedidos['IdPedido'] == id_pedido]
    
    if pedido.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    

    return pedido.to_dict(orient='records')[0]

