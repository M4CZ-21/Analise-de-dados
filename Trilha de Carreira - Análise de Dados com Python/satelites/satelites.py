import os
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    carregar()
    sns.set_theme(style="whitegrid")
    qt_satelites()
    plt.show()

    # Exibe gráficos de relação de bandas utilizadas e operadoras comerciais separadamente (satélites estrageiros e brasileiros)
    for tipo in "Brasileiro Estrangeiro".split():
        qt_operadoras(tipo)
        qt_bandas(tipo)
        plt.show()

# Carrega os dados do arquivo .csv (que contém a relação de satélites operando comercialmente) em um DataFrame
def carregar():
    pasta_atual = os.path.dirname(os.path.realpath(__file__))
    arquivo = pasta_atual + "\\satelites_operando_comercialmente.csv"
    global tabela
    tabela = pd.read_csv(arquivo, sep=';')
    tabela.drop(columns=["Satélite em operação", "Posição orbital", "Posição Orbital Decimal"], inplace=True)

# Cria um gráfico que exibe quantos satélites são estrangeiros e quantos são brasileiros
def qt_satelites():
    plt.figure(num=1, figsize=(5, 5))
    sns.countplot(data=tabela, x="Tipo de Direito")

# Cria um gráfico que exibe quantos satélites pertencem a cada operadora comercial
def qt_operadoras(tipo):
    plt.figure(num=2, figsize=(10, 5), layout='tight')
    ax = sns.countplot(data=tabela[tabela["Tipo de Direito"] == tipo], y="Operadora comercial")
    ax.axes.set_title(f"Para satélites {tipo.lower()}s", fontsize=14)
    ax.set_xlabel("Quantidade", fontsize=14)

# Cria um gráfico que exibe quantos satélites utilizam cada banda
def qt_bandas(tipo):
    plt.figure(num=3, figsize=(8, 5), layout='tight')
    ax = sns.countplot(data=tabela[tabela["Tipo de Direito"] == tipo], y="Bandas do satélite")
    ax.axes.set_title(f"Para satélites {tipo.lower()}s", fontsize=14)
    ax.set_xlabel("Quantidade", fontsize=14)

if __name__ == "__main__":
    main()