# IRS Calculator API v1

Simulador de cálculo de IRS v1.
Inclui cálculo de rendimento coletável, deduções (nesta fase apenas considerando deduções por dependentes sem os limites por idade) e coleta líquida.
Este projeto foi desenhado para que quem consumir possa obter um cálculo aproximado sobre o IRS a pagar,
baseado nos rendimentos da categoria-A obtidos no ano de 2025

## Pré-requisitos
- python3.14+
- pip
- virtualenv

# instalação

Antes de rodar a aplicação faça:
- 1. Clonar o repositório
```bash
git clone https://github.com/samulolo/irs.git
- 2. Criar e clonar um ambiente virtual
- python -m venv venv (MACOS)
- virtual env venv (WINDOS)

- 3. Instalar as dependências
- pip install -r requirements.txt


---

### 🔹 Como executar
```markdown
## Executar a aplicação

```bash
# rodar o servidor local
uvicorn main:app --reload




# Estrutura de request
### 🔹 Exemplo de request/response
```markdown
## Exemplo de request

POST /api/irs/v1
```json
{
  "gross_income": 50000,
  "dependents": 2,
  "professional_order": true,
  "tax_year": 2024
}