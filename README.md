# IRS Calculator API v1

Simulador de cálculo de IRS v1.
Inclui cálculo de rendimento coletável, deduções e coleta líquida.
Este projeto foi desenhado para que quem consumir possa obter um cálculo aproximado sobre o IRS a pagar,
baseado nos rendimentos da categoria-A obtidos no ano de 2025

# Estrutura de request
### 🔹 Exemplo de request/response
```markdown
## Exemplo de request

POST /api/v1/irs/simulate
```json
{
  "gross_income": 50000,
  "dependents": 2,
  "professional_order": true,
  "tax_year": 2024
}