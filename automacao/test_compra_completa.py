# Fluxo completo de compra (TC06 + TC06-B): login -> adicionar produto -> checkout
# -> preencher dados -> finalizar pedido -> gerar PDF do pedido
#
# Cada "expect(...)" abaixo é um ponto de verificação: se algo não acontecer como
# esperado (elemento não aparece, texto errado, etc.), o teste para exatamente
# naquele passo e o pytest mostra um relatório de erro apontando a linha e o motivo.
#
# Como rodar:
#   python -m pytest test_compra_completa.py --headed --slowmo 500
#
# Pra gerar prints/vídeo automaticamente se der erro:
#   python -m pytest test_compra_completa.py --screenshot=only-on-failure --video=retain-on-failure

from playwright.sync_api import Page, expect


def test_compra_completa_ate_gerar_pdf(page: Page):
    # 1. Abrir o site e fazer login
    print("Passo 1: abrindo o site e fazendo login...")
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("OK: login realizado, na página de produtos.")

    # 2. Adicionar o primeiro produto ao carrinho
    print("Passo 2: adicionando produto ao carrinho...")
    page.locator(".inventory_item").nth(0).locator("button").click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    print("OK: produto adicionado, carrinho mostra 1 item.")

    # 3. Ir para o carrinho e clicar em Checkout
    print("Passo 3: indo para o carrinho e iniciando checkout...")
    page.click(".shopping_cart_link")
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    page.click("#checkout")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    print("OK: na tela de checkout (dados pessoais).")

    # 4. Preencher os dados pedidos e continuar
    print("Passo 4: preenchendo nome, sobrenome e CEP...")
    page.fill("#first-name", "Plinio")
    page.fill("#last-name", "Marcus")
    page.fill("#postal-code", "12345")
    page.click("#continue")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    print("OK: dados aceitos, na tela de resumo do pedido.")

    # 5. Conferir se o total bate com subtotal + taxa (checagem extra de qualidade)
    subtotal_texto = page.locator(".summary_subtotal_label").inner_text()
    tax_texto = page.locator(".summary_tax_label").inner_text()
    total_texto = page.locator(".summary_total_label").inner_text()
    subtotal = float(subtotal_texto.replace("Item total: $", ""))
    tax = float(tax_texto.replace("Tax: $", ""))
    total = float(total_texto.replace("Total: $", ""))
    assert abs((subtotal + tax) - total) < 0.01, (
        f"Total não bate: subtotal {subtotal} + tax {tax} deveria ser {subtotal + tax}, "
        f"mas o total exibido foi {total}"
    )
    print(f"OK: total confere (subtotal {subtotal} + tax {tax} = {total}).")

    # 6. Finalizar o pedido
    print("Passo 5: finalizando o pedido...")
    page.click("#finish")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
    print("OK: pedido finalizado, mensagem de confirmação exibida.")

    # 7. Clicar em "Generate PDF Order" e confirmar que o download aconteceu
    print("Passo 6: gerando o PDF do pedido...")
    with page.expect_download() as download_info:
        page.get_by_text("Generate PDF Order").click()
    download = download_info.value
    assert download.suggested_filename.endswith(".pdf"), (
        f"Esperava um arquivo .pdf, mas o download veio como '{download.suggested_filename}'"
    )
    print(f"OK: PDF gerado e baixado com sucesso: {download.suggested_filename}")
