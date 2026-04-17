import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_supabase

class MockSupabase:
    class Table:
        def __init__(self, name):
            self.name = name
        
        def insert(self, payload):
            self.payload = payload
            return self
        
        def select(self, query):
            return self
            
        def order(self, column, desc=True):
            return self

        def execute(self):
            class Response:
                def __init__(self, data):
                    self.data = data
            
            mock_item = {
                "id": "mock-uuid-123", 
                "created_at": "2026-04-17T11:20:00Z",
                "ip": "127.0.0.1",
                "tipo_cliente": "VIP",
                "valor_compra": 600.0,
                "percentual_desconto": 0.0,
                "valor_final": 600.0,
                "valor_cashback": 66.0,
                "device": "Pytest-Mock"
            }
            if hasattr(self, 'payload'):
                # Para o POST, mesclamos o que foi enviado com o mock_item
                return Response([{**mock_item, **self.payload}])
            
            return Response([mock_item])


    def table(self, name):
        return self.Table(name)






def override_get_supabase():
    return MockSupabase()

app.dependency_overrides[get_supabase] = override_get_supabase

client = TestClient(app)

def test_deve_calcular_e_registrar_cashback_com_sucesso():
    payload = {
        "valor_compra": 600.0,
        "percentual_desconto": 0,
        "tipo_cliente": "VIP",
        "ip": "127.0.0.1"
    }
    
    response = client.post("/cashback/", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["valor_cashback"] == 66.0
    assert data["valor_final"] == 600.0
    assert "id" in data

def test_deve_listar_historico():
    response = client.get("/cashback/historico")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_erro_ao_inserir_no_supabase():
    class MockErro:
        def table(self, name):
            raise Exception("Erro de conexão")

    app.dependency_overrides[get_supabase] = lambda: MockErro()
    
    response = client.post("/cashback/", json={"valor_compra": 100, "percentual_desconto": 0, "tipo_cliente": "normal"})
    
    assert response.status_code == 500
    assert "Erro de conexão" in response.json()["detail"]
    
    
    app.dependency_overrides[get_supabase] = override_get_supabase