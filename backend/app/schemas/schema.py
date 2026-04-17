from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HistoricoCreate(BaseModel):
    tipo_cliente: str          # "vip" ou "normal"
    valor_compra: float
    percentual_desconto: float
    ip: Optional[str] = None   # preenchido pelo backend se omitido

class HistoricoResponse(BaseModel):
    id: str
    ip: str
    tipo_cliente: str
    valor_compra: float
    percentual_desconto: float
    valor_final: float
    valor_cashback: float
    device: Optional[str] = None
    created_at: datetime