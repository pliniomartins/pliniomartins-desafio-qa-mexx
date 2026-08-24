// TC01 — Login com credenciais válidas (standard_user)
// Esse é o teste mais simples possível: abre o site, preenche usuário e senha,
// clica em Login, e confirma que caiu na página de produtos.
//
// Como rodar:
//   npm install
//   npx playwright install chromium
//   npx playwright test login.spec.js

const { test, expect } = require('@playwright/test');

test('login com credenciais válidas redireciona para a página de produtos', async ({ page }) => {
  // 1. Abrir o site
  await page.goto('https://www.saucedemo.com');

  // 2. Preencher usuário e senha
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'secret_sauce');

  // 3. Clicar em "Login"
  await page.click('#login-button');

  // 4. Confirmar que a URL mudou para a página de produtos (inventory.html)
  await expect(page).toHaveURL(/inventory\.html/);
});
