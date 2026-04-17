import { type ResultadoCashback } from "../hooks/useCashback";
import styles from "./Historico.module.css";

interface HistoricoProps {
  dados: ResultadoCashback[];
}

export function Historico({ dados }: HistoricoProps) {
  const formatarDevice = (userAgent: string) => {
    if (!userAgent) return "Desconhecido";
    const ua = userAgent.toLowerCase();
    let sistema = "Desconhecido";
    let navegador = "Navegador";

    if (ua.includes("win")) sistema = "Windows";
    else if (ua.includes("mac")) sistema = "MacOs";
    else if (ua.includes("linux")) sistema = "Linux";
    else if (ua.includes("android")) sistema = "Android";
    else if (ua.includes("iphone") || ua.includes("ipad")) sistema = "iOS";

    if (ua.includes("firefox")) navegador = "Firefox";
    else if (ua.includes("edg")) navegador = "Edge";
    else if (ua.includes("chrome")) navegador = "Chrome";
    else if (ua.includes("safari")) navegador = "Safari";

    return `${navegador} (${sistema})`;
  };

  return (
    <div className={styles.history}>
      <div className={styles.historyList}>
        {dados.map((item) => (
          <div key={item.id} className={styles.historyItem}>
            <p className={styles.deviceInfo}>
              <strong>Device:</strong> {formatarDevice(item.device)}
            </p>

            <p>IP: {item.ip}</p>
            <p>Tipo: {item.tipo_cliente}</p>
            <p>Valor: R$ {item.valor_compra.toFixed(2)}</p>
            <p>Desconto: {item.percentual_desconto}%</p>

            <div className={styles.statusCashback}>
              {item.valor_compra > 500 ? (
                <span className={`${styles.badgeResult} ${styles.premium}`}>
                  🚀 Cashback Dobrado!
                  <p className={styles.cashbackValue}>
                    R$ {item.valor_cashback.toFixed(2)}
                  </p>
                </span>
              ) : (
                <span className={`${styles.badgeResult} ${styles.comum}`}>
                  ✅ Cashback Padrão
                  <p className={styles.cashbackValue}>
                    R$ {item.valor_cashback.toFixed(2)}
                  </p>
                </span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
