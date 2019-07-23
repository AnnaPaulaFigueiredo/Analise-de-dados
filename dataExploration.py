import plotly as py
import plotly.graph_objs as go
import statistics as st

def main():

    # lendo arquivo dataExploratin
    arq = open('data-exploration-test.csv', 'r')

    time = []
    stock = []
    currency = []

    linha = arq.readline()
    linha = arq.readline()

    while linha:
        # alterando a , para .
        linha = linha.replace(",", ".")

        # separando a linha pelo delimitador ;
        linha = linha.split(";")

        # atribuindo os valores do txt em seus respectivos atributos
        time.append(int(linha[0]))
        stock.append(float(linha[1]))
        currency.append(float(linha[2]))

        linha = arq.readline()

# Box Plot
    # Informações do gráfico
    layout = go.Layout(title='BoxPlot do Valor da Ação e Moeda', yaxis={'title': 'Valor'})

    # criando box da Ação
    box_stock = go.Box(y=stock, name="Stock")

    # criando box da Moeda
    box_currency = go.Box(y=currency, name="Currency")

    # selecionando os dados para o gráfico
    data = [box_stock, box_currency]

    # configurando o gráfico
    fig = go.Figure(data=data, layout=layout)

    # plotando
    py.offline.plot(fig, filename="BoxPlotStockCurrency.html", auto_open=False)

# Scatterplot
    # Informações do gráfico
    layout = go.Layout(title='ScatterPlot dos Valores da Ação e Moeda', yaxis={'title': 'Valor'})

    # linha da Ação
    scr_stock = go.Scatter(x=time, y=stock, mode="lines", name="Sotock")

    # linha Moeda
    scr_currency = go.Scatter(x=time, y=currency, mode="lines", name="Currency")

    # selecionando os dados para o gráfico
    data = [scr_stock, scr_currency]

    # configurando o gráfico
    fig = go.Figure(data=data, layout=layout)

    # plotando
    py.offline.plot(fig, filename="ScatterPlotStockCurrency.html", auto_open=False)

# BoxPlot com intervalo de tempo
# Intervalo Stock
    # Informações do gráfico
    layout = go.Layout(title='Valor da Ação por Intervalo de Tempo', yaxis={'title': 'Valor'}, xaxis={'title': 'Tempo'})

    # definindo o intervalo
    bs1 = go.Box(y=stock[0:999], name="0~999")
    bs2 = go.Box(y=stock[1000:1999], name="1000~1999")
    bs3 = go.Box(y=stock[2000:2999], name="2000~2999")
    bs4 = go.Box(y=stock[3000:3999], name="3000~3999")
    bs5 = go.Box(y=stock[4000:4999], name="4000~4999")
    bs6 = go.Box(y=stock[5000:5999], name="5000~5999")
    bs7 = go.Box(y=stock[6000:6999], name="6000~6999")
    bs8 = go.Box(y=stock[7000:7999], name="7000~7999")
    bs9 = go.Box(y=stock[8000:8999], name="8000~8999")
    bs10 = go.Box(y=stock[9000:10001], name="9000~10001")

    # selecionando os dados
    data = [bs1, bs2, bs3, bs4, bs5, bs6, bs7, bs8, bs9, bs10]

    # configurando gráfico
    fig = go.Figure(data=data, layout=layout)

    # plotando
    py.offline.plot(fig, filename="BoxPlotStockIntervaloDeTempo.html", auto_open=False)

# Intervalo Currency
    # Informações do gráfico
    layout = go.Layout(title='Valor da Moeda por Intervalo de Tempo', yaxis={'title': 'Valor'}, xaxis={'title': 'Tempo'})

    # definindo o intervalo
    bc1 = go.Box(y=currency[0:999], name="0~999")
    bc2 = go.Box(y=currency[1000:1999], name="1000~1999")
    bc3 = go.Box(y=currency[2000:2999], name="2000~2999")
    bc4 = go.Box(y=currency[3000:3999], name="3000~3999")
    bc5 = go.Box(y=currency[4000:4999], name="4000~4999")
    bc6 = go.Box(y=currency[5000:5999], name="5000~5999")
    bc7 = go.Box(y=currency[6000:6999], name="6000~6999")
    bc8 = go.Box(y=currency[7000:7999], name="7000~7999")
    bc9 = go.Box(y=currency[8000:8999], name="8000~8999")
    bc10 = go.Box(y=currency[9000:10001], name="9000~10001")

    # selecionando os dados
    data = [bc1, bc2, bc3, bc4, bc5, bc6, bc7, bc8, bc9, bc10]

    # configurando gráfico
    fig = go.Figure(data=data, layout=layout)

    # plotando
    py.offline.plot(fig, filename="BoxPlotCurrencyIntervaloDeTempo.html", auto_open=False)

# Criando arquivo do relatório
    relatorio = open("\nRelatorio.txt", 'w')

# Quantidade de instâncias
    relatorio.write("\nQuantidade de Instâncias: " + str(len(time)))

# Calculando média geral
    relatorio.write("\n\nMedia Geral Ação: " + str(sum(stock)/len(stock)))
    relatorio.write("\nMedia Geral Moeda: " + str(sum(currency)/len(currency)))

# Calculando Variancia e Desvio Padrão
    relatorio.write("\n\nVariancia da Ação: " + str(st.variance(stock)))
    relatorio.write("\nDesvio Padrão da Ação: " + str(st.pstdev(stock)))

    relatorio.write("\n\nVariancia da Moeda: " + str(st.variance(currency)))
    relatorio.write("\nDesvio Padrão da Moeda: " + str(st.pstdev(currency)))

if __name__ == '__main__':
    main()
