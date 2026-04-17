from fastapi import APIRouter, Depends, Request, HTTPException
from app.schemas.schema import HistoricoCreate, HistoricoResponse
from app.service.service import calcular_cashback
from app.database import get_supabase

router = APIRouter(prefix="/cashback", tags=["Cashback"])


@router.post("/", response_model=HistoricoResponse)
async def calcular_e_registrar(
    request: Request,
    dados: HistoricoCreate,
    supabase=Depends(get_supabase)
):
    resultado = calcular_cashback(
        dados.valor_compra,
        dados.percentual_desconto,
        dados.tipo_cliente
    )

    payload = {
        "ip": dados.ip or request.client.host,
        "tipo_cliente": dados.tipo_cliente,
        "valor_compra": dados.valor_compra,
        "percentual_desconto": dados.percentual_desconto,
        "valor_final": resultado["valor_final"],
        "valor_cashback": resultado["valor_cashback"],
        "device": request.headers.get("user-agent")
    }

    try:
        response = supabase.table("consultas").insert(payload).execute()
        if not response.data:
            raise HTTPException(status_code=400, detail="Erro ao inserir no banco")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/historico", response_model=list[HistoricoResponse])
async def listar_historico(
    request: Request,
    supabase=Depends(get_supabase)
):

    try:
        response = (
            supabase.table("consultas")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))