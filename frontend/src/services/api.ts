const API_URL = "https://desafio-cashback-api.onrender.com";

export async function calcularCashback(dados: {
  valor_compra: number;
  percentual_desconto: number;
  tipo_cliente: string;
}) {
  const res = await fetch(`${API_URL}/cashback/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(dados),
  });

  if (!res.ok) throw new Error("Erro na requisição");
  return res.json();
}

export async function getHistorico() {
  const res = await fetch(`${API_URL}/cashback/historico`);
  if (!res.ok) throw new Error("Erro ao buscar histórico");
  return res.json();
}
