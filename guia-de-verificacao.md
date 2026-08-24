# Guia de verificação manual (± 25-30 min)

Siga na ordem. Pra cada passo, só anote no README.md: o que aconteceu de fato ("Resultado obtido"), se passou ou falhou ("Status": Passou / Falhou), e tire um print quando for algo relevante (salve em uma pasta `evidencias/`).

Dica de print rápido: no Windows, `Win + Shift + S`. No Mac, `Cmd + Shift + 4`. Ou grave um GIF curto com o ShareX/Loom se o comportamento for melhor mostrado em vídeo (ex: a lentidão do performance_glitch_user).

## Bloco 1 — Login (TC01 a TC04) — ~5 min
1. Abra https://www.saucedemo.com/
2. **TC01**: usuário `standard_user`, senha `secret_sauce`, clique Login. Confirme se foi para a tela de produtos. Print.
3. Clique em "Logout" (menu hambúrguer no canto superior esquerdo).
4. **TC02**: usuário `standard_user`, senha `senha_errada`, clique Login. Leia a mensagem de erro exata que aparece e copie o texto.
5. **TC03**: limpe os dois campos, clique Login sem preencher nada. Leia a mensagem de erro.
6. **TC04**: usuário `locked_out_user`, senha `secret_sauce`, clique Login. Leia a mensagem de erro. Print.

## Bloco 2 — Carrinho e checkout (TC05 a TC07) — ~8 min
7. Login com `standard_user`.
8. **TC05**: clique "Add to cart" no primeiro produto. O botão virou "Remove"? O ícone do carrinho (canto superior direito) mostra "1"?
9. Adicione mais um produto (agora 2 no carrinho). Clique no ícone do carrinho.
10. **TC06**: clique "Checkout", preencha nome/sobrenome/CEP com dados válidos, "Continue", confira o resumo (subtotal, tax, total — os valores batem: subtotal + tax = total?), clique "Finish". Apareceu "Thank you for your order"? Print da tela final.
11. Volte pro carrinho vazio, adicione 1 produto, vá pro checkout de novo.
12. **TC07**: preencha nome e CEP, deixe sobrenome vazio, clique "Continue". Qual mensagem de erro aparece?

## Bloco 3 — Usuários "especiais" (TC08 a TC11 + hipóteses de bug) — ~12 min
13. Logout. Login com `problem_user` / `secret_sauce`.
14. **TC08**: olhe as 6 imagens de produtos na tela de inventário. Elas são diferentes entre si (cada produto com sua própria foto) ou repetidas/erradas? Print comparando.
15. **TC09**: use o dropdown "Name (A to Z)" no canto superior direito da lista de produtos, mude para "Price (low to high)". Os preços realmente ficaram em ordem crescente? Anote os 6 preços na ordem que apareceram.
16. Enquanto estiver logado como `problem_user`, tente adicionar um produto ao carrinho e ir pro checkout — tente digitar algo no campo de sobrenome. O texto digitado aparece corretamente no campo?
17. Logout. Login com `performance_glitch_user` / `secret_sauce`.
18. **TC10**: cronometre (celular ou timer) o tempo entre clicar "Login" e a tela de produtos carregar de fato. Quantos segundos levou, comparado ao login "normal" do bloco 1?
19. Logout. Login com `error_user` / `secret_sauce`.
20. **TC11**: adicione 2 produtos ao carrinho, vá ao carrinho, clique "Remove" em um deles. O item saiu da lista? O contador do carrinho atualizou?
21. Ainda como `error_user`, tente marcar/desmarcar itens ou clicar em outros botões da tela — algo trava, não responde, ou dá erro no console (F12 → aba Console)?
22. Logout. Login com `visual_user` / `secret_sauce`.
23. Compare visualmente essa tela de produtos com a do `standard_user` (print lado a lado): algo desalinhado, tamanho de imagem diferente, botão fora do lugar?

## Bloco 4 — Fechar (extra, se der tempo)
24. Logout de novo, com qualquer usuário. Depois de deslogar, clique no botão "Voltar" do navegador. Você consegue ver a tela de produtos de novo mesmo já tendo deslogado? (isso testa se a aplicação protege página autenticada contra cache do navegador)

## Depois de terminar
- Volte no `README.md` e substitua cada `[A CONFIRMAR]` pelo que você realmente viu.
- Para cada comportamento inesperado real que você confirmou, adicione uma entrada na seção "2. Problemas encontrados" usando o modelo que já está lá.
- Responda a pergunta final: qual foi o cenário mais interessante e por quê (baseado no que você mesmo achou mais chamativo).
