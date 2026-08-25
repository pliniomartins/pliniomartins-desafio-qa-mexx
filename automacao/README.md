# Automação (Python + Playwright)

Dois scripts de automação usando `pytest-playwright`, cobrindo os fluxos mais importantes do SauceDemo:

- **`test_login_carrinho.py`** — login com `standard_user` e adicionar um produto ao carrinho (TC01 + TC05).
- **`test_compra_completa.py`** — fluxo completo de compra: login, adicionar ao carrinho, checkout, conferência do total (subtotal + taxa), finalização do pedido e geração do PDF (TC06 + TC06-B).

## Como rodar

```bash
cd automacao
pip install pytest-playwright
python -m playwright install chromium
python -m pytest test_login_carrinho.py
python -m pytest test_compra_completa.py
```

Para ver rodando com o navegador visível e mais devagar:

```bash
python -m pytest test_compra_completa.py --headed --slowmo 2000
```
