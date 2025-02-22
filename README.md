# Descrição do Funcionamento do Código

## Descrição do Programa
Este programa simula uma **carteira de investimentos** onde o usuário pode adicionar, remover, aplicar e resgatar ativos (ações). Ele utiliza a biblioteca `yfinance` para obter cotações de ações e salva os dados em arquivos JSON para persistência.

## Importações
- **`yfinance`**: Para obter cotações de ações.
- **`time`**: Para adicionar pausas entre as execuções.
- **`json`**: Para salvar e carregar dados em arquivos JSON.
- **`os`**: Para verificar a existência de arquivos.

## Menu
O programa oferece um menu interativo com as seguintes opções:
1. **Adicionar um ativo**
2. **Remover um ativo**
3. **Nova aplicação**
4. **Novo resgate**
5. **Exibir carteira**
6. **Sair**

## Funções
- **adicionarAtivo**: Permite adicionar um ativo à carteira com informações como ticker, quantidade, preço médio e data.
- **removerAtivo**: Remove um ativo da carteira.
- **aplicar**: Realiza uma nova compra (aplicação) em um ativo existente.
- **resgatar**: Vende uma quantidade de ações, calculando lucro ou prejuízo.
- **listarAtivos**: Exibe todos os ativos na carteira com informações como preço atual e rentabilidade.
- **salvar_CarteiraJson**: Salva os dados da carteira em um arquivo JSON.
- **carregar_CarteiraJson**: Carrega os dados da carteira a partir de um arquivo JSON.
- **salvar_ExtratoJson**: Salva o extrato das transações em um arquivo JSON.
- **carregar_ExtratoJson**: Carrega o extrato das transações a partir de um arquivo JSON.

## Conclusão
O programa permite o gerenciamento simples de uma carteira de investimentos, com a capacidade de salvar e carregar os dados, e realizar transações como compras, vendas e consultas de ativos.
