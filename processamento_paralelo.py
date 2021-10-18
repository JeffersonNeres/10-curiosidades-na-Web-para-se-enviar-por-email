from multiprocessing import Pool
from requests import get
from time import time
from funcao import *

# foi pedido um processamento paralelo com as mesmas requisições do projeto principal

url_lista = [
            "https://www.terra.com.br/vida-e-estilo/turismo/internacional/conheca-regiao-do-mundo-que-fica-ate-tres-meses-sem-ver-o-sol,516a392625237310VgnCLD100000bbcceb0aRCRD.html",
            "https://sciam.com.br/estranho-porem-verdade-gatos-nao-sentem-o-sabor-doce/",
            "https://www.melsantabarbara.com.br/o-mel-nao-tem-data-de-validade-mito-ou-verdade/",
            "https://www.marechaldeodoro.al.gov.br/a-cidade/conheca-o-marechal-deodoro-da-fonseca/",
            "https://www.uol.com.br/tilt/noticias/redacao/2020/11/02/baby-shark-e-o-video-mais-assistido-do-youtube.htm",
            "https://forbes.com.br/videos/2021/01/conheca-o-bilionario-que-doou-mais-de-us-8-bilhoes-e-e-inspiracao-de-bill-gates/",
            "https://www.bol.uol.com.br/listas/nem-todo-heroi-usa-capa-dez-historias-que-inspiram.htm",
            "https://www.todamateria.com.br/imperio-romano/",
            "https://www.eurodicas.com.br/cidades-com-mais-brasileiros-no-exterior/",
            "https://www.lebrave.com.br/loja/noticia.php?loja=748613&id=1"
            ]

headers_lista = [
                {"User-Agent" : "Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"},
                {"User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.61 Mobile/15E148 Safari/604.1"},
                {"User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.61 Mobile/15E148 Safari/604.1"}
                ]

# a função a baixo tem esses ifs porque cada site tem sue cminho de raspagem e uns precisam de User-Agent para raspagem
def scraper(url):
    if url == url_lista[0]:
        res = get(url, headers=headers_lista[0])
        print(cidade(res.text))
    if url == url_lista[1]:
        res = get(url, headers=headers_lista[1])
        print(gatos(res.text))
    if url == url_lista[2]:
        res = get(url, headers=headers_lista[2])
        print(mel(res.text))
    if url == url_lista[3]:
        res = get(url)
        print(presidente(res.text))
    if url == url_lista[4]:
        res = get(url)
        print(baby_shark(res.text))
    if url == url_lista[5]:
        res = get(url)
        print(bilionario(res.text))
    if url == url_lista[6]:
        res = get(url)
        print(herois(res.text))
    if url == url_lista[7]:
        res = get(url)
        print(imperio_romano(res.text))
    if url == url_lista[8]:
        res = get(url)
        print(exterior(res.text))
    if url == url_lista[9]:
        res = get(url)
        print(santos_dumont(res.text))

p= Pool(10)
p.map(scraper, url_lista)
p.terminate()
p.join()
