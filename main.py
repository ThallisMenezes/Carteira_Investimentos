import yfinance as yf
import time
import json
import os

carteira = {}
extrato = {}

class Carteira:
# Atributos(caracteristicas/estado)
    def __init__(self, nome):
        self.nome = nome

# Métodos(funções/ações)
    def adicionarAtivo(self):
        while True:
            try:
                ticker = input("Digite o ticker do ativo: ")
            except:
                print("Ticker não pode ser vazio.")
                continue
            try:
                quantidade = int(input("Digite a quantidade: "))
            except:
                print("Erro!\nDigite novamente.")
                continue
            try:
                precoMedio = float(input("Digite o preço médio: "))
            except:
                print("Erro!\nDigite novamente.")
                continue
            try:
                data = input(f"Insira a data(dia/mês/ano): ")
            except:
                print("Erro!\nDigite novamente.")
                continue
            valorAplicado = (quantidade * precoMedio)
            if ticker in carteira and extrato:
                print("Ativo já existe!")
                continue
            else:
# Criando a chave
                carteira[f"{ticker}"] = {}
                extrato[f"{data}"] = {}
# inserindo os valores
                carteira[f"{ticker}"]["Quantidade"] = quantidade
                carteira[f"{ticker}"]["Preço-Médio"] = f"{precoMedio:,.2f}"
                carteira[f"{ticker}"]["Valor Aplicado"] = f"{valorAplicado:,.2f}"
                extrato[f"{data}"]["Compra"] = f"Ticker: {ticker}, Quantidade: {quantidade}, Preço-Médio: {precoMedio:,.2f}, Valor Aplicado: {valorAplicado:,.2f}"
                print("Salvo!")
                break

    def removerAtivo(self):
        while True:
            try:
                removerCarteira = input("Digite o ticker do ativo: ")
                removerExtrato = input("Digite a data: ")
            except:
                print("Digite novamente!")
                continue
            if (removerExtrato not in carteira) and (removerExtrato not in extrato):
                print("Digite corretamente o ticker e a data!")
                continue
            else:
                carteira.pop(removerCarteira)
                extrato.pop(removerExtrato)
                break

    def aplicar(self):
        while True:
            try:
                ticker = input("Digite o ticker do ativo: ")
            except:
                print("Digite novamente.")
                continue
            if ticker in carteira:
                pass
            else:
                print("Ativo não adicionado!")
                break
            quantidadeAplicacao = int(input("Digite a quantidade: "))
            quantidade = carteira[f"{ticker}"]["Quantidade"]
            quantidadeFinal = quantidade + quantidadeAplicacao
            carteira[f"{ticker}"]["Quantidade"] = quantidadeFinal

            precoMedioAplicacao = float(input("Digite o preço médio: "))

            data = input(f"Insira a data(dia/mês/ano): ")

            saldoAplicado = (quantidadeAplicacao * precoMedioAplicacao)
            valorAplicado = float(carteira[f"{ticker}"]["Valor Aplicado"].replace(',', '').replace('R$', '').strip())
            saldoFinal = float(saldoAplicado) + float(valorAplicado)
            carteira[f"{ticker}"]["Valor Aplicado"] = saldoFinal

            precoMedioFinal = carteira[f"{ticker}"]["Valor Aplicado"] / carteira[f"{ticker}"]["Quantidade"]
            carteira[f"{ticker}"]["Preço-Médio"] = (f"{precoMedioFinal:,.2f}")

            extrato[f"{data}"] = {}
            extrato[f"{data}"]["Compra"] = f"Ticker: {ticker}, Quantidade: {quantidadeAplicacao}, Preço-Médio: {precoMedioAplicacao:,.2f}, Valor Aplicado: {saldoAplicado:,.2f}"
            print("Salvo!")
            break

    def resgatar(self):
        while True:
            try:
                ticker = input("Digite o ticker do ativo: ")
            except:
                print("Digite novamente.")
                continue
            if ticker in carteira:
                pass
            else:
                print("Ativo não adicionado!")
                break
            try:
                quantidadeResgate = int(input("Digite a quantidade: "))
            except:
                print("Digite novamente.")
                continue
            quantidade = carteira[f"{ticker}"]["Quantidade"]
            quantidadeFinal = quantidade - quantidadeResgate
            try:
                precoMedioResgate = float(input("Digite o preço médio: "))
            except:
                print("Digite novamente.")
                continue
            try:
                data = input(f"Insira a data(dia/mês/ano): ")
            except:
                print("Digite novamente.")
                continue
            valorResgate = (quantidadeResgate * precoMedioResgate)

            if valorResgate > 0:
                lucro = float(valorResgate) - float(carteira[f"{ticker}"]["Preço-Médio"]) * quantidadeResgate
                lucroPercent = lucro * 100 / float(carteira[f"{ticker}"]["Valor Aplicado"])
                carteira[f"{ticker}"]["Lucro"] = (f"{lucro:,.2f}")
                carteira[f"{ticker}"]["Lucro%"] = (f"{lucroPercent:,.2f}%")
            else:
                prejuizo = float(valorResgate) - float(carteira[f"{ticker}"]["Preço-Médio"]) * quantidadeResgate
                prejuizoPercent = prejuizo * 100 / float(carteira[f"{ticker}"]["Valor Aplicado"])
                carteira[f"{ticker}"]["Prejuízo"] = (f"{prejuizo:,.2f}")
                carteira[f"{ticker}"]["Prejuízo%"] = (f"{prejuizoPercent:,.2f}%")

            carteira[f"{ticker}"]["Quantidade"] = (f"{quantidadeFinal}")
            preco_medio = carteira[f"{ticker}"]["Preço-Médio"]
            novoValor = float(preco_medio) * float(quantidadeFinal)
            carteira[f"{ticker}"]["Valor Aplicado"] = (f"{novoValor:,.2f}")
            extrato[f"{data}"] = {}
            extrato[f"{data}"]["Venda"] = f"Ticker: {ticker}, Quantidade: {quantidadeResgate}, Preço-Médio: {precoMedioResgate:,.2f}, Valor Resgatado: {valorResgate:,.2f}"
            break

    def listarAtivos(self):
        for chave, valor in carteira.items():
            print(f"{chave} - {valor}")

            ativo = yf.Ticker(f"{chave}.SA")
            dados = ativo.history(period='1mo')
            cotacao = dados['Close'].iloc[-1]
            print(f"{chave} - Preço atual: {cotacao:,.2f}")
            valorAplicado = float(carteira[chave]["Valor Aplicado"].replace(',', '').replace('R$', '').strip())
            quantidade = int(carteira[chave]["Quantidade"])
            posicaoAtual = float(cotacao * quantidade)
            print(f"Posição atual: R${posicaoAtual:,.2f}")
            resultado = float(posicaoAtual - valorAplicado)
            print(f"Resultado em aberto: R${resultado:,.2f}")
            rentabilidade = resultado * 100 / valorAplicado
            print(f"Rentabilidade%: {rentabilidade:,.2f}%")
            time.sleep(2)

    def salvar_CarteiraJson(self):
        with open("Carteira.JSON", "w", encoding="utf-8") as arquivoWrite:
            json.dump(carteira, arquivoWrite, ensure_ascii=False, indent=4)

    def carregar_CarteiraJson(self):
        if os.path.exists("Carteira.JSON"):
            try:
                with open("Carteira.JSON", "r", encoding="utf-8") as arquivoRead:
                    dados_Carteira = json.load(arquivoRead)
                    carteira.update(dados_Carteira)
            except:
                print("Erro!")
        else:
            print("Arquivo não existe!")

    def salvar_ExtratoJson(self):
        with open("Extrato.JSON", "w", encoding="utf-8") as extratoWrite:
            json.dump(extrato, extratoWrite, ensure_ascii=False, indent=4)

    def carregar_ExtratoJson(self):
        if os.path.exists("Extrato.JSON"):
            try:
                with open("Extrato.JSON", "r", encoding="utf-8") as extratoRead:
                    dados_Extrato = json.load(extratoRead)
                    extrato.update(dados_Extrato)
            except:
                print("Erro!")
        else:
            print("Arquivo não existe!")


    def menu(self):
        while True:
            try:
                opcoes = int(input("1. Adicionar um ativo.\n2. Remover um ativo.\n3. Nova aplicação.\n4. Novo resgate\n5. Exibir carteira\n6. Sair\nDigite uma opção: "))
            except ValueError:
                print("Opção inválida! Digite novamente.")
                continue

            if opcoes == 1:
                self.adicionarAtivo()
            elif opcoes == 2:
                self.removerAtivo()
            elif opcoes == 3:
                self.aplicar()
            elif opcoes == 4:
                self.resgatar()
            elif opcoes == 5:
                self.listarAtivos()
            elif opcoes == 6:
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida! Tente novamente.")

#Instânciando a classe Carteira
novaCarteira = Carteira("Valor")

#Fluxo do programa
novaCarteira.carregar_CarteiraJson()
novaCarteira.carregar_ExtratoJson()
novaCarteira.menu()
novaCarteira.salvar_CarteiraJson()
novaCarteira.salvar_ExtratoJson()