// TC01 + TC05 — Login com credenciais válidas e adicionar produto ao carrinho
// Fluxo: abre o site -> faz login -> adiciona o primeiro produto ao carrinho
// -> confirma que o ícone do carrinho mostra "1"
//
// Como rodar:
//   npm install
//   npx playwright install chromium
//   npx playwright test login_carrinho.spec.js

const { test, expect } = require('@playwright/test');

test('login e adicionar produto ao carrinho atualiza o contador para 1', async ({ page }) => {
  // 1. Abrir o site
  await page.goto('https://www.saucedemo.com');

  // 2. Preencher usuário e senha
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'secret_sauce');

  // 3. Clicar em "Login"
  await page.click('#login-button');

  // 4. Confirmar que caiu na página de produtos
  await expect(page).toHaveURL(/inventory\.html/);

  // 5. Clicar em "Add to cart" no primeiro produto da lista
  //    (.inventory_item pega cada "cartão" de produto; nth(0) pega o primeiro; "button" é o botão dentro dele)
  await page.locator('.inventory_item').nth(0).locator('button').click();

  // 6. Confirmar que o ícone do carrinho agora mostra "1"
  await expect(page.locator('.shopping_cart_badge')).toHaveText('1');
});
