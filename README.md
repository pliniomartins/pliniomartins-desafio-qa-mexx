# Desafio Técnico — Estágio em Teste de Software (Mexx / CMTECH)

Testador: Plinio
Aplicação testada: [SauceDemo](https://www.saucedemo.com/)
Data: 24/08/2026

## Nota sobre metodologia

Este material foi montado com apoio de IA (Claude) para estruturar o raciocínio, organizar os casos de teste e escrever o esqueleto da automação. Os itens marcados como **[A CONFIRMAR]** ainda precisam ser executados manualmente na aplicação antes da entrega — a IA não tinha acesso de rede para navegar ao vivo no SauceDemo neste ambiente, então as hipóteses de bug abaixo vêm de comportamento conhecido/documentado publicamente sobre este site (ele é usado exatamente para prática de QA e tem "bugs" propositalmente plantados em alguns usuários de teste). Antes de entregar, siga o `guia-de-verificacao.md` (leva uns 25-30 min) para confirmar cada resultado com suas próprias palavras e evidências — isso também é o que a empresa está avaliando: sua própria investigação.

---

## 1. Casos de teste

### TC01 — Login com credenciais válidas
| Campo | Descrição |
|---|---|
| Cenário | Login com usuário e senha válidos (`standard_user`) |
| Passos | 1. Acessar saucedemo.com. 2. Preencher usuário `standard_user`. 3. Preencher senha `secret_sauce`. 4. Clicar em "Login". |
| Resultado esperado | Usuário é redirecionado para a página de produtos (`inventory.html`) |
| Resultado obtido | [A CONFIRMAR] |
| Status | [Pendente] |

### TC02 — Login com senha inválida
| Campo | Descrição |
|---|---|
| Cenário | Login com usuário válido e senha incorreta |
| Passos | 1. Acessar saucedemo.com. 2. Preencher usuário `standard_user`. 3. Preencher senha `senha_errada`. 4. Clicar em "Login". |
| Resultado esperado | Sistema não realiza login e exibe mensagem de erro informando que usuário e senha não conferem, sem expor qual dos dois campos está incorreto (boa prática de segurança) |
| Resultado obtido | [A CONFIRMAR] |
| Status | [Pendente] |

### TC03 — Login com campos em branco
| Campo | Descrição |
|---|---|
| Cenário | Tentar login sem preencher usuário nem senha |
| Passos | 1. Acessar saucedemo.com. 2. Deixar usuário e senha em branco. 3. Clicar em "Login". |
| Resultado esperado | Sistema bloqueia o envio e exibe mensagem "Username is required" |
| Resultado obtido | [A CONFIRMAR] |
| Status | [Pendente] |

### TC04 — Login com usuário bloqueado (locked_out_user)
| Campo | Descrição |
|---|---|
| Cenário | Login com um usuário que deveria estar bloqueado pelo sistema |
| Passos | 1. Acessar saucedemo.com. 2. Preencher usuário `locked_out_user`. 3. Preencher senha `secret_sauce`. 4. Clicar em "Login". |
| Resultado esperado | Sistema impede o acesso e exibe mensagem clara informando que o usuário foi bloqueado |
| Resultado obtido | [A CONFIRMAR] |
| Status | [Pendente] |

### TC05 — Adicionar produto ao carrinho
| Campo | Descrição |
|---|---|
| Cenário | Adicionar um produto ao carrinho e verificar o contador |
| Passos | 1. Login com `standard_user`. 2. Clicar em "Add to cart" no primeiro produto listado. 3. Observar o ícone do carrinho. |
| Resultado esperado | O botão muda para "Remove" e o ícone do carrinho passa a exibir o número "1" |
| Resultado obtido | [A CONFIRMAR] |
| Status | [Pendente] |

### TC06 — Checkout completo com dados válidos
| Campo | Descrição |
|---|---|
| Cenário | Fluxo completo de compra, do login até a confirmação do pedido |
| Passos | 1. Login com `standard_user`. 2. Adicionar 2 produtos ao carrinho. 3. Ir ao carrinho e clicar em "Checkout". 4. Preencher nome, sobrenome e CEP válidos. 5. Clicar em "Continue". 6. Conferir resumo do pedido (subtotal, taxa, total). 7. Clicar em "Finish". |
| Resultado esperado | Pedido é concluído e a página exibe a mensagem "Thank you for your order!" com o ícone de confirmação |
| Resultado obtido | [A CONFIRMAR] |
| Status | [Pendente] |

### TC07 — Checkout com campo obrigatório vazio
| Campo | Descrição |
|---|---|
| Cenário | Tentar avançar no checkout sem preencher o sobrenome |
| Passos | 1. Login com `standard_user`. 2. Adicionar 1 produto ao carrinho. 3. Ir ao checkout. 4. Preencher apenas nome e CEP, deixando sobrenome vazio. 5. Clicar em "Continue". |
| Resultado esperado | Sistema não avança e exibe mensagem "Error: Last Name is required" |
| Resultado obtido | [A CONFIRMAR] |
| Status | [Pendente] |

### TC08 — Comportamento visual do usuário problem_user
| Campo | Descrição |
|---|---|
| Cenário | Verificar se as imagens dos produtos são exibidas corretamente para o usuário `problem_user` |
| Passos | 1. Login com `problem_user` / `secret_sauce`. 2. Observar as imagens de todos os produtos na página de inventário. |
| Resultado esperado | Cada produto exibe sua própria imagem, todas diferentes entre si |
| Resultado obtido | [A CONFIRMAR — hipótese: pode haver imagens repetidas/erradas para todos os produtos] |
| Status | [Pendente] |

### TC09 — Ordenação de preços (Price: low to high)
| Campo | Descrição |
|---|---|
| Cenário | Verificar se a ordenação por preço funciona corretamente com `problem_user` |
| Passos | 1. Login com `problem_user`. 2. No dropdown de ordenação, selecionar "Price (low to high)". 3. Conferir a ordem dos preços exibidos. |
| Resultado esperado | Produtos ficam ordenados do menor para o maior preço |
| Resultado obtido | [A CONFIRMAR — hipótese: a ordenação pode não refletir a opção selecionada] |
| Status | [Pendente] |

### TC10 — Tempo de resposta com performance_glitch_user
| Campo | Descrição |
|---|---|
| Cenário | Medir o tempo de carregamento após login com um usuário conhecido por lentidão |
| Passos | 1. Acessar saucedemo.com. 2. Login com `performance_glitch_user` / `secret_sauce`. 3. Cronometrar o tempo entre o clique em "Login" e o carregamento completo da página de produtos. |
| Resultado esperado | Carregamento em tempo similar ao `standard_user` (poucos segundos) |
| Resultado obtido | [A CONFIRMAR — hipótese: atraso perceptível de vários segundos] |
| Status | [Pendente] |

### TC11 — Remoção de item do carrinho com error_user
| Campo | Descrição |
|---|---|
| Cenário | Verificar se é possível remover um item do carrinho com o usuário `error_user` |
| Passos | 1. Login com `error_user`. 2. Adicionar 2 produtos ao carrinho. 3. Ir ao carrinho. 4. Clicar em "Remove" em um dos itens. |
| Resultado esperado | O item é removido da lista e o contador do carrinho é atualizado |
| Resultado obtido | [A CONFIRMAR — hipótese: o botão "Remove" pode não funcionar corretamente] |
| Status | [Pendente] |

---

## 2. Problemas encontrados

*A preencher após a verificação manual (`guia-de-verificacao.md`). Use o modelo abaixo para cada problema real confirmado:*

```
### [Título curto do problema]
- Como reproduzir: passo a passo
- Resultado esperado: ...
- Resultado obtido: ...
- Evidência: [link/print/gif]
- Severidade sugerida: baixa / média / alta
```

Hipóteses a investigar (baseadas em comportamento publicamente conhecido do SauceDemo, precisam ser confirmadas ou descartadas):
1. `problem_user` pode exibir a mesma imagem para produtos diferentes.
2. `problem_user` pode ter a ordenação de preços quebrada.
3. `error_user` pode falhar ao remover itens do carrinho.
4. `performance_glitch_user` pode ter atraso significativo no carregamento após login.
5. `visual_user` pode apresentar diferenças visuais/layout em relação ao `standard_user`.

---

## 3. Análise do cenário

**Situação:** durante o teste do processo de compra, ao finalizar o pedido o sistema apresenta uma mensagem de erro, mas aparentemente o pedido foi criado mesmo assim.

Meus próximos passos para investigar essa situação seriam:

**1. Reproduzir e isolar o problema.** Primeiro eu tentaria reproduzir o erro de forma consistente, repetindo exatamente os mesmos passos (mesmo usuário, mesmos produtos, mesmos dados de checkout) para saber se é um comportamento sistemático ou intermitente. Isso já muda bastante a investigação: um erro que acontece sempre é mais fácil de rastrear do que um que aparece só às vezes (o que pode indicar problema de concorrência, timeout ou race condition).

**2. Confirmar se o pedido foi realmente criado.** "Aparentemente foi criado" precisa virar uma certeza. Eu verificaria isso de duas formas: pela interface (por exemplo, se existisse um histórico de pedidos ou uma confirmação por e-mail) e, se eu tivesse acesso, diretamente no banco de dados ou via chamada à API para ver se o registro do pedido existe, com quais dados e em qual status.

**3. Olhar o que aconteceu "por baixo do capô".** Eu abriria as ferramentas de desenvolvedor do navegador (aba Network e Console) durante uma nova tentativa, para ver: qual requisição foi feita ao finalizar o pedido, qual foi a resposta do servidor (código de status HTTP, corpo da resposta), se houve algum erro de JavaScript no console, e se a mensagem de erro exibida na tela é uma mensagem genérica de front-end ou reflete de fato uma resposta de erro vinda do back-end.

**4. Verificar se é um problema de exibição (falso negativo) ou um problema real de dados.** Existe uma diferença importante entre "o sistema mostrou um erro por engano, mas está tudo certo" (um bug de UI/mensagem) e "o pedido foi criado de forma incompleta, duplicada ou inconsistente" (um bug mais sério, que pode gerar cobrança indevida, estoque incorreto, ou pedido duplicado). Eu tentaria descobrir em qual desses dois grupos o problema se encaixa, porque a gravidade e a urgência são bem diferentes.

**5. Testar variações.** Eu tentaria reproduzir o erro variando alguns fatores: usuários diferentes, produtos diferentes, quantidades diferentes, conexão de rede mais lenta (para simular timeout), múltiplas tentativas seguidas (para testar duplo clique ou duplo envio). Isso ajuda a isolar se o problema está ligado a um caso específico ou é generalizado.

**6. Verificar se o pedido pode ser duplicado.** Um cenário clássico nesse tipo de erro é o usuário, ao ver a mensagem de erro, tentar finalizar a compra de novo — o que pode gerar dois pedidos criados para uma única intenção de compra. Eu testaria especificamente esse caminho.

**7. Documentar tudo e comunicar com clareza.** Eu registraria passos exatos de reprodução, a mensagem de erro completa (com print/gravação), a evidência de que o pedido foi criado (com print ou dado do banco/API), a requisição e resposta relevantes, e classificaria a severidade — porque criar um pedido válido mas informar erro ao usuário é um problema sério: o cliente pode desistir da compra, tentar de novo e ser cobrado duas vezes, ou simplesmente perder a confiança no site. Eu levaria isso para o time de desenvolvimento com o máximo de contexto possível para acelerar a correção.

Resumindo: a ideia central é não aceitar “aparentemente foi criado” como resposta — reproduzir, confirmar com dados concretos (não só pela tela), investigar a comunicação entre front-end e back-end, e entender se é um problema de mensagem ou um problema real de integridade dos dados.

---

## 4. API (opcional)

Não realizado nesta entrega — foco ficou no teste exploratório, casos de teste e automação. [Se quiser, dá pra fazer depois: ver observação no final deste arquivo.]

---

## 5. Automação

Um dos cenários (TC06 — checkout completo com dados válidos) foi automatizado com **Playwright**. O script está em `automacao/checkout.spec.js`.

Como rodar:
```bash
cd automacao
npm install
npx playwright install chromium   # se ainda não tiver o navegador instalado
npx playwright test
```

**Importante:** o ambiente onde este material foi preparado não tinha acesso de rede ao saucedemo.com, então o script não pôde ser executado e confirmado por aqui — rode localmente antes de entregar para garantir que passa.

---

## 6. Qual foi o cenário mais interessante?

*A preencher por você depois da verificação manual — depende do que você realmente encontrar. Alguns candidatos fortes, com base no que a aplicação promete testar (a dica do e-mail sobre os usuários de teste): o comportamento do `problem_user` (porque é um bug "disfarçado" — a aplicação parece funcionar normalmente à primeira vista, e o problema só aparece quando você compara produtos entre si com atenção) ou a análise do cenário de erro no checkout (porque mistura teste funcional com raciocínio de investigação, não é só "clicar e ver se deu certo").*

---

## Observações finais

- Casos marcados **[A CONFIRMAR]** foram preenchidos com o resultado esperado, mas o resultado obtido, status e evidências devem ser preenchidos após execução manual — siga `guia-de-verificacao.md`.
- Depois de confirmar tudo, apague esta seção de "Nota sobre metodologia" e as observações finais se preferir uma entrega mais enxuta — elas existem só para deixar claro, para você, o que já está pronto e o que falta.
