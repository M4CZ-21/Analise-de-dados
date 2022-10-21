import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    dados_brutos = raspar_dados()
    tabela = extrair_tabela(dados_brutos)
    exportar_tabela(tabela)

# Obtém dados da internet, utilizando raspagem web (web scraping)
def raspar_dados():
    texto_string = requests.get('https://globoesporte.globo.com/').text
    bsp_texto = BeautifulSoup(texto_string, 'html.parser')
    dados_brutos = bsp_texto.find_all('div', attrs={'class':'feed-post-body'})
    return dados_brutos

# Analisa e extrai informações dos dados obtidos, organizando-os em um DataFrame
def extrair_tabela(lista_noticias):
    tabela = []
    for noticia in lista_noticias:
        manchete = noticia.find("a", attrs={"class": "feed-post-link"}).get_text().strip().replace("\n", '')
        link = noticia.find("a", attrs={"class": "feed-post-link"}, href=True)
        descricao = noticia.find("div", attrs={"class": "feed-post-body-resumo"})
        secao = noticia.find("span", attrs={"class": "feed-post-metadata-section"})
        hora_extracao = datetime.now().strftime('%H:%M, %d/%m/%Y')
        time_delta = noticia.find("span", attrs={"class": "feed-post-datetime"}).get_text().strip()
        tabela.append((
            manchete if manchete else None,
            descricao.get_text().strip().replace("\n", '') if descricao else None,
            link["href"] if link else None,
            secao.get_text().strip() if secao else None,
            hora_extracao,
            time_delta if time_delta else None
        ))
    return tabela

# Cria uma tabela, com os dados obtidos, na mesma pasta deste arquivo .py
def exportar_tabela(tabela):
    dataframe = pd.DataFrame(tabela, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
    pasta_atual = os.path.dirname(os.path.realpath(__file__))
    dataframe.to_excel(pasta_atual + "\\tabela.xlsx")

if __name__ == "__main__":
    main()