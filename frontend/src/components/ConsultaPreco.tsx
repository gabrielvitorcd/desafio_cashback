import { useCashback } from "../hooks/useCashback";
import { Historico } from "./Historico";

import styles from "./ConsultaPreco.module.css";
import { useState } from "react";

export function ConsultaPreco() {
  const { form, atualizarForm, resultado, historico, loading, erro, calcular } =
    useCashback();

  const [mostrarHistorico, setMostrarHistorico] = useState(false);

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>💸 Calculadora de Cashback</h1>

      <div className={styles.form}>
        <input
          className="form-input"
          type="number"
          placeholder="Valor da compra"
          value={form.valor}
          onChange={(e) => atualizarForm("valor", e.target.value)}
        />

        <input
          className="form-input"
          type="number"
          placeholder="Desconto (%)"
          value={form.desconto}
          onChange={(e) => atualizarForm("desconto", e.target.value)}
        />

        <div className={styles["tipo-cliente-group"]}>
          <button
            type="button"
            className={`${styles["btn-opcao"]} ${form.tipoCliente === "Normal" ? styles.active : ""}`}
            onClick={() => atualizarForm("tipoCliente", "Normal")}
          >
            Cliente Normal
          </button>

          <button
            type="button"
            className={`${styles["btn-opcao"]} ${form.tipoCliente === "Vip" ? styles.active : ""}`}
            onClick={() => atualizarForm("tipoCliente", "Vip")}
          >
            Cliente VIP
          </button>
        </div>

        <button onClick={calcular} disabled={loading}>
          {loading ? "Calculando..." : "Calcular Cashback"}
        </button>
      </div>

      {erro && <p style={{ color: "red" }}>{erro}</p>}

      {resultado && (
        <div className={styles.result}>
          <p>Valor final: R$ {resultado.valor_final.toFixed(2)}</p>
          <p className={styles.cashback}>
            Cashback: R$ {resultado.valor_cashback.toFixed(2)}
          </p>
          {resultado.valor_compra > 500 && (
            <span className={styles["badge-promo"]}>Cashback Dobrado!</span>
          )}
        </div>
      )}

      {/* Histórico */}
      <button
        className={styles["toggle-historico"]}
        onClick={() => setMostrarHistorico((prev) => !prev)}
      >
        Histórico de consultas
        <span
          className={`${styles.seta} ${mostrarHistorico ? styles["seta-aberta"] : ""}`}
        >
          ▼
        </span>
      </button>

      {mostrarHistorico && <Historico dados={historico || []} />}
    </div>
  );
}
