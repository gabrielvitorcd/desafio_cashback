from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware  # ← adiciona
from app.database import get_supabase
from app.routers import cashback_router

app = FastAPI(
    title="Cashback Fintech API",
    description="API para cálculo e histórico de cashback",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://desafio-cashback-pied.vercel.app"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(cashback_router.router)

@app.get("/")
def read_root():
    return {"message": "Cashback Fintech API está online 🚀"}

@app.get("/test-db")
def test_db(supabase = Depends(get_supabase)):
    try:
        response = supabase.table("consultas").select("*").limit(1).execute()
        return {
            "status": "conectado",
            "plataforma": "Supabase SDK",
            "tabela_consultas": "OK"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro de conexão: {str(e)}")