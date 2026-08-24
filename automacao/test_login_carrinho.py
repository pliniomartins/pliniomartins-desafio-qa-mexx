# TC01 + TC05 — Login com credenciais válidas e adicionar produto ao carrinho
# Fluxo: abre o site -> faz login -> adiciona o primeiro produto ao carrinho
# -> confirma que o ícone do carrinho mostra "1"
#
# Como rodar:
#   pip install pytest-playwright --break-system-packages
#   playwright install chromium
#   pytest test_login_carrinho.py

from playwright.sync_api import Page, expect


def test_login_e_adicionar_produto_ao_carrinho(page: Page):
    # 1. Abrir o site
    page.goto("https://www.saucedemo.com")

    # 2. Preencher usuário e senha
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")

    # 3. Clicar em "Login"
    page.click("#login-button")

    # 4. Confirmar que caiu na página de produtos
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 5. Clicar em "Add to cart" no primeiro produto da lista
    page.locator(".inventory_item").nth(0).locator("button").click()

    # 6. Confirmar que o ícone do carrinho agora mostra "1"
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
