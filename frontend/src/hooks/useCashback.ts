import { useState, useEffect, useCallback } from "react";
import { calcularCashback, getHistorico } from "../services/api";

export interface ResultadoCashback {
  id: string;
  ip: string;
  device: string;
  valor_final: number;
  valor_cashback: number;
  tipo_cliente: string;
  valor_compra: number;
  percentual_desconto: number;
  created_at: string;
}

export interface FormData {
  valor: string;
  desconto: string;
  tipoCliente: string;
}

export function useCashback() {
  const [form, setForm] = useState<FormData>({
    valor: "",
    desconto: "",
    tipoCliente: "",
  });

  const [resultado, setResultado] = useState<ResultadoCashback | null>(null);
  const [historico, setHistorico] = useState<ResultadoCashback[]>([]);
  const [loading, setLoading] = useState(false);
  const [loadingHistorico, setLoadingHistorico] = useState(false);
  const [erro, setErro] = useState<string | null>(null);

  const carregarHistorico = useCallback(async () => {
    setLoadingHistorico(true);
    try {
      const data = await getHistorico();
      setHistorico(data);
    } catch {
      setErro("Erro ao carregar histórico.");
    } finally {
      setLoadingHistorico(false);
    }
  }, []);

  useEffect(() => {
    carregarHistorico();
  }, [carregarHistorico]);

  async function calcular() {
    setErro(null);

    if (!form.valor || !form.desconto || !form.tipoCliente) {
      setErro("Preencha todos os campos e selecione o tipo de cliente.");
      return;
    }

    const descontoNum = Number(form.desconto.replace(",", "."));

    if (descontoNum < 0 || descontoNum > 100) {
      setErro("O desconto deve estar entre 0% e 100%.");
      return;
    }

    setLoading(true);
    try {
      const data = await calcularCashback({
        valor_compra: Number(form.valor),
        percentual_desconto: Number(form.desconto),
        tipo_cliente: form.tipoCliente,
      });

      setResultado(data);
      await carregarHistorico();

      setForm({
        valor: "",
        desconto: "",
        tipoCliente: "normal",
      });
    } catch {
      setErro("Erro ao calcular cashback. Verifique a API.");
    } finally {
      setLoading(false);
    }
  }

  function atualizarForm(campo: keyof FormData, valor: string) {
    setForm((prev) => ({ ...prev, [campo]: valor }));
  }

  return {
    form,
    atualizarForm,
    resultado,
    historico,
    loading,
    loadingHistorico,
    erro,
    calcular,
  };
}
