
CREATE TABLE IF NOT EXISTS public.clientes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nome TEXT,
    tipo_padrao TEXT DEFAULT 'NORMAL',
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public.consultas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ip TEXT NOT NULL,
    device TEXT,
    tipo_cliente TEXT NOT NULL,
    valor_compra NUMERIC(10, 2) NOT NULL,
    percentual_desconto NUMERIC(5, 2) NOT NULL,
    valor_final NUMERIC(10, 2) NOT NULL,
    valor_cashback NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Índice para busca rápida
CREATE INDEX IF NOT EXISTS idx_consultas_ip ON public.consultas(ip);