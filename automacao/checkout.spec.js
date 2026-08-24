// TC06 — Checkout completo com dados válidos (standard_user)
// Automatiza o fluxo: login -> adicionar 2 produtos -> checkout -> confirmação
//
// Como rodar:
//   npm install
//   npx playwright install chromium
//   npx playwright test

const { test, expect } = require('@playwright/test');

const BASE_URL = 'https://www.saucedemo.com';

test('checkout completo com dados válidos gera confirmação do pedido', async ({ page }) => {
  // 1. Login com usuário válido
  await page.goto(BASE_URL);
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'secret_sauce');
  await page.click('#login-button');
  await expect(page).toHaveURL(/inventory\.html/);

  // 2. Adicionar dois produtos ao carrinho
  const addToCartButtons = page.locator('.inventory_item button');
  await addToCartButtons.nth(0).click();
  await addToCartButtons.nth(1).click();
  await expect(page.locator('.shopping_cart_badge')).toHaveText('2');

  // 3. Ir para o carrinho e iniciar checkout
  await page.click('.shopping_cart_link');
  await expect(page).toHaveURL(/cart\.html/);
  await page.click('#checkout');
  await expect(page).toHaveURL(/checkout-step-one\.html/);

  // 4. Preencher dados válidos
  await page.fill('#first-name', 'Plinio');
  await page.fill('#last-name', 'Marques');
  await page.fill('#postal-code', '12345-000');
  await page.click('#continue');
  await expect(page).toHaveURL(/checkout-step-two\.html/);

  // 5. Conferir que o total bate com subtotal + taxa
  const subtotalText = await page.locator('.summary_subtotal_label').innerText();
  const taxText = await page.locator('.summary_tax_label').innerText();
  const totalText = await page.locator('.summary_total_label').innerText();

  const subtotal = parseFloat(subtotalText.replace(/[^0-9.]/g, ''));
  const tax = parseFloat(taxText.replace(/[^0-9.]/g, ''));
  const total = parseFloat(totalText.replace(/[^0-9.]/g, ''));

  expect(Math.abs(subtotal + tax - total)).toBeLessThan(0.01);

  // 6. Finalizar pedido
  await page.click('#finish');
  await expect(page).toHaveURL(/checkout-complete\.html/);
  await expect(page.locator('.complete-header')).toHaveText(/Thank you for your order/i);
});
