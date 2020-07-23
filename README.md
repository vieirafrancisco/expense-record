# Expense Record
Aplicação para registrar gastos (principalmente fixos) de cartões de créditos do usuário

# Ideia
O usuário pode adicionar cartões de créditos (não dados do cartão, somente um identificador) e associar os cartões com serviços. Cada serviço terá um valor fixo e uma data de cobrança.  
No final de cada mês (data de fechamento de fatura), o usuário será notificado para a data do pagamento da fatura e deverá informar o valor total dessa fatura para que o sistema consiga dividir os gastos fixos (serviços) com relação aos gastos situacionais.  
Também será notificado ao usuário toda vez que a data de pagamento de um serviço chegar (essa opção poderá ser desabilitada caso o usuário deseje).  

# Ferramentas
- Flask (API)
- React Native (Mobile)

# Estrutura
````
.
├── doc     # Documentação e diagramas
├── api     # Aplicação em flask
└── app     # Aplicação em react native
````