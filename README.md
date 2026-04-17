# 💸 Calculadora de Cashback - Fintech

![Status](https://img.shields.io/badge/Status-Concluído-success)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)

Este projeto foi desenvolvido como resolução de um **Desafio Técnico**. Trata-se de um sistema financeiro (Fullstack) que simula o cálculo e o registro de _cashbacks_ para clientes de uma Fintech, aplicando diferentes regras de negócio com base no perfil do usuário e valor da compra.

<p align="center">
  <img src="docs/images/preview_screenshot.png" width="100%" alt="Print da Tela Inicial">
</p>

## ✨ Funcionalidades

- **Cálculo Dinâmico:** Calcula o valor final e o cashback com base no desconto aplicado e no tipo de cliente.
- **Validação de Dados:** Bloqueio de inputs inválidos (ex: descontos negativos ou acima de 100%) direto no frontend para otimização de requisições.
- **Renderização Condicional:** Selos visuais dinâmicos (ex: 🚀 _Cashback Dobrado_ para compras acima de R$ 500).
- **Rastreamento de Origem:** Captura de IP e tratamento do `User-Agent` (Device) para identificar o navegador e sistema operacional da transação (ex: _Firefox (Linux)_).
- **Histórico em Tempo Real:** Listagem das últimas consultas com scroll estilizado, alimentada pelo banco de dados.
- **UI/UX** Interface focada em conversão com tema "Dark Mode" moderno, feedbacks visuais (Hover/Active).

## 💼 Regras de Negócio Implementadas

A lógica central da calculadora obedece aos seguintes critérios:

1. **Tipos de Cliente:** Diferenciação entre "Cliente Normal" e "Cliente VIP" (impactando diretamente na API de cálculo).
2. **Desconto Limitado:** O percentual de desconto não pode ser menor que 0% nem maior que 100%.
3. **Cashback Dobrado:** Compras que ultrapassam o valor de R$ 500,00 recebem uma bonificação promocional visual e matemática no sistema.

## 🛠️ Tecnologias Utilizadas

**Frontend:**

- React.js (Hooks, Renderização Condicional)
- TypeScript (Tipagem rigorosa, Interfaces)
- Vite (Build tool)

**Backend:**

- Python 3
- FastAPI (Rotas, Validação de Schemas com Pydantic)
- Supabase / PostgreSQL (Banco de Dados em Nuvem)

## 🏗️ Estrutura e Arquitetura do Frontend

O projeto foi refatorado focando em **Clean Code** e separação de responsabilidades:

- **`useCashback.ts`**: Hook customizado que isola toda a regra de estado (`useState`), validações e chamadas à API (`fetch`).
- **`ConsultaPreco.tsx`**: Componente principal que gerencia o formulário de entrada.
- **`Historico.tsx`**: Componente isolado (com CSS Module próprio) responsável por renderizar e formatar a lista de transações recentes.
