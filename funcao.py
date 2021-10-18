from bs4 import BeautifulSoup

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
# funções que fazem as raspagens apartir do recebimento do get.text do arquivo requisicao, são usados no arquivo interface

def cidade(soup):
    tags_cidade = BeautifulSoup(soup, "html5lib")
    titulo_cidade = tags_cidade.find_all("div", attrs = {"class": "article__header__headline"})[0]
    texto_cidade = tags_cidade.find_all("div", attrs = {"id": "content-wrapper"})[0]
    filtra_texto = texto_cidade.find_all("p")
    saida = titulo_cidade.text.strip() + "\n" + filtra_texto[0].text.strip() + "\n" + filtra_texto[1].text.strip() + "\n" + "Fonte: "  + "\n" + url_lista[0]
    return saida

def gatos(soup):
    tags_gatos = BeautifulSoup(soup, "html5lib")
    texto_gatos = tags_gatos.find_all("h1", attrs = {"class": "single__headerTitle"})
    texto_gatos2 = tags_gatos.find_all("div", attrs = {"class": "single__content"})
    saida = [h1.text for h1 in texto_gatos][0] + "\n" + [p.text for p in texto_gatos2][0] + "\n" + "Fonte: "  + "\n" + url_lista[1]
    return saida

def mel(soup):
    tags_mel = BeautifulSoup(soup, "html5lib")
    texto_mel = tags_mel.find_all("span", attrs = {"style": "font-weight: 400;"})
    titulo_mel = tags_mel.find_all("h1", attrs = {"class": "entry-title"})[0]
    texto_saida1 = ""
    texto_saida2 = ""
    for i in range(len(texto_mel) - 4):
        if i < 1:
            texto_saida1 = [span.text for span in texto_mel][i]
        if i == 2:
            texto_saida2 = [span.text for span in texto_mel][1] + "Centro de Mel e Polinização" + [span.text for span in texto_mel][2]
    saida = titulo_mel.text + "\n" + texto_saida1 + "\n" + texto_saida2 + "\n" + "Fonte: "  + "\n" + url_lista[0]
    return saida

def presidente(soup):
    tags_presidente = BeautifulSoup(soup, "html5lib")
    titulo = tags_presidente.find_all("h1", attrs = {"class": "heading"})
    historia = tags_presidente.find_all("div", attrs = {"class" : "story"})
    historia2 = tags_presidente.find_all("p", attrs = {"style" : "text-align: justify;"})
    saida = [h1.text for h1 in titulo][0] + "\n" + [div.p.text for div in historia][0] + "\n" + historia2[0].text +  "\n" + historia2[1].text + "\n" + historia2[2].text + "\n" + historia2[3].text + "\n" + historia2[4].text + "\n" + "Fonte: "  + "\n" + url_lista[0]
    return saida

def baby_shark(soup):
    tags_baby = BeautifulSoup(soup, "html5lib")
    titulo_baby = tags_baby.find_all("i", attrs = {"class": "col-sm-22 col-md-22 col-lg-22 custom-title"})
    texto_baby = tags_baby.find_all("div", attrs = {"class": "image-content-pad"})
    saida = [title.text for title in titulo_baby][0] + "\n" + [p.text for p in texto_baby][0].strip()[78:1490] + "\n" + "Fonte: "  + "\n" + url_lista[4]
    return saida

def bilionario(soup):
    tags_doacao = BeautifulSoup(soup, "html5lib")
    titulo_doacao = tags_doacao.find_all("h1", attrs = {"class": "post__title"})
    texto_doacao = tags_doacao.find_all("div", attrs = {"class": "entry-content"})
    saida = titulo_doacao[0].text + "\n" + [p.text for p in texto_doacao][0].strip()[1046:2815] + "\n" + "Fonte: "  + "\n" + url_lista[5]
    return saida

def herois(soup):
    tags_heroi = BeautifulSoup(soup, "html5lib")
    titulo_heroi = tags_heroi.find_all("i", attrs = {"class": "custom-title"})
    texto_heroi = tags_heroi.find_all("div", attrs = {"class": "text"})[0]
    herois = tags_heroi.find_all("ul", attrs = {"class": "list-unstyled"})[0]
    herois = herois.find_all("p", attrs = {"class": "minor"})
    saida = []
    saida1 = ""
    for i in range(len(herois)):
        saida.append(f"Herói {i+1} \n {herois[i].text.strip()}, \n")
        saida1 = saida1 + saida[i]
    saida2 = titulo_heroi[0].text +"\n" + texto_heroi.text.strip()[:410] + "\n" + saida1 + "\n" + "Fonte: "  + "\n" + url_lista[6]
    return saida2

def imperio_romano(soup):
    tags_romano = BeautifulSoup(soup, "html5lib")
    texto_romano = tags_romano.find_all("div", attrs = {"id": "wrapper"})
    return [p.text for p in texto_romano][0].replace("\n", "").strip()[376:1519] + "\n" + "Fonte: "  + "\n" + url_lista[7]

def exterior(soup):
    tags_exterior = BeautifulSoup(soup, "html5lib")
    titulo_exterior = tags_exterior.find_all("h1", attrs = {"class": "entry-title"})
    texto_exterior = tags_exterior.find_all("div", attrs = {"class": "wprt-container"})
    saida = titulo_exterior[0].text + "\n" + texto_exterior[0].text[:3196]
    return saida  + "\n" + "Fonte: "  + "\n" + url_lista[8]

def santos_dumont(soup):
    tags_relogio = BeautifulSoup(soup, "html5lib")
    texto_relogio = tags_relogio.find_all("div", attrs = {"class": "board"})[1]
    return texto_relogio.text.strip() + "\n" + "Fonte: "  + "\n" + url_lista[9]
