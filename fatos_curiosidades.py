from bs4 import BeautifulSoup
from asyncio import ensure_future, gather, get_event_loop
from aiohttp import ClientSession
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import *

# Aqui eu uni todos os 4 arquivos do propgrama em um só para criar o excutavel linux e windows

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


async def buscar(session, url):
    async with session.get(url) as response:
        return await response.text()

async def buscar_com_agent(session, url, agent=0):
    async with session.get(url, headers=agent) as response:
        return await response.text()

async def run():
    tasks = []
    contador_agent = 0
    headers = ""
    async with ClientSession() as session:
        for url in url_lista:
            if contador_agent < 3:
                if url == url_lista[contador_agent]:
                    headers = headers_lista[contador_agent]
                    task = ensure_future(buscar_com_agent(session, url, headers))
            if contador_agent == 3:
                del(headers)
            contador_agent += 1
            task = ensure_future(buscar(session, url))
            tasks.append(task)
        responses = await gather(*tasks)
        return responses

loop = get_event_loop()
future = ensure_future(run())
requisicao = loop.run_until_complete(future)
registra_requisicao = requisicao



def email(login, senha, destino, texto_principal):
    # definindo componentes pra dar start no servidor escolhido(gmail)
    host = "smtp.gmail.com"
    port = "587"
    login = login
    senha = senha
    destino = destino
    texto_principal = texto_principal
    # dando start no servidor, pesquisar caso não seja (gmail) o host
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login, senha)

    #texto a enviar
    #texto_principal = texto_principal
    #assunto = assunto

    # montando email
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = destino
    email_msg['Subject'] = "Fatos e curiosidades"
    email_msg.attach(MIMEText(texto_principal, "plain"))
    #no lugar de plain pode ser html, o texto vai com tags

    # enviar email
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    # desligar servidor
    server.quit()



janela = Tk()

janela.title("Primeiro Programa do Jefferson")
janela["bg"] = "light blue"
janela.geometry("600x500")
bem_vindo = Label(janela, text="Bem vindo ao curiosidades", height=2, bg="white")#.place(relx=0.5, y=0.1)
bem_vindo.pack(side=TOP, fill=X)
introducao = Label(janela, text="""Dez fatos que com certeza vão te surpreender, escolha uma!""", height=3, bg="white")#.place(relx=01, y=0)
introducao.pack(side=TOP, fill=X)

def janela_email(texto_envia):
    win_width, win_height = 700, 700
    janela3 = Tk()
    janela3.title("Primeiro Programa do Jefferson")
    janela3["bg"] = "light blue"
    janela3.geometry('{}x{}'.format(win_width, win_height))
    def login_senha():
        login_envia = str(login_dig.get())
        senha_envia = str(senha_dig.get())
        destino_envia = str(destino_dig.get())
        email(login_envia, senha_envia, destino_envia, texto_envia)
    login_ent = Label(janela3, wraplength=win_width, text="Login conta google: ", font="Arial 12", bg="light blue").place(relx=0.1, rely=0.1)
    senha_ent = Label(janela3, wraplength=win_width, text="Senha: ", font="Arial 12", bg="light blue").place(relx=0.1, rely=0.3)
    destino_ent = Label(janela3, wraplength=win_width, text="Enviar para: ", font="Arial 12", bg="light blue").place(relx=0.1, rely=0.5)
    login_dig = Entry(janela3)
    login_dig.place(relx=0.4, rely=0.1, relwidth = 0.4, relheight=0.04)
    senha_dig = Entry(janela3, show="*")
    senha_dig.place(relx=0.4, rely=0.3, relwidth = 0.4, relheight=0.04)
    destino_dig = Entry(janela3)
    destino_dig.place(relx=0.4, rely=0.5, relwidth = 0.4, relheight=0.04)
    login_envia = str(login_dig.get())
    senha_envia = str(senha_dig.get())
    destino_envia = str(destino_dig.get())
    confirma = Button(janela3, wraplength=win_width, text="confirma", font="Arial 12", command=lambda: login_senha()).place(relx=0.1, rely=0.6)
    informe = Label(janela3, wraplength=win_width, text="!!! Apenas gmail, para a conta que enviará é necessário  em: gerenciar sua conta google > seguranca > ativar o acesso de App menos seguro !!!", font="Arial 12", bg="light blue").place(relx=0.01, rely=0.8)
    informe_link = Label(janela3, wraplength=win_width, text="Link para ativar acesso do App: https://myaccount.google.com/security?gar=1", font="Arial 12", bg="light blue").place(relx=0.1, rely=0.9)

def fatos(fato):
    win_width, win_height = 1500, 1200
    janela2 = Tk()
    janela2.title("Primeiro Programa do Jefferson")
    janela2["bg"] = "white"
    janela2.geometry('{}x{}'.format(win_width, win_height))
    if fato == registra_requisicao[0]:
        texto1 = cidade(registra_requisicao[0])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[1]:
        texto1 = gatos(registra_requisicao[1])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[2]:
        texto1 = mel(registra_requisicao[2])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[3]:
        texto1 = presidente(registra_requisicao[3])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[4]:
        texto1 = baby_shark(registra_requisicao[4])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[5]:
        texto1 = bilionario(registra_requisicao[5])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[6]:
        texto1 = herois(registra_requisicao[6])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[7]:
        texto1 = imperio_romano(registra_requisicao[7])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[8]:
        texto1 = exterior(registra_requisicao[8])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()
    if fato == registra_requisicao[9]:
        texto1 = santos_dumont(registra_requisicao[9])
        mensagem = Label(janela2, pady=20, wraplength=win_width, text=texto1, font="Arial 12", bg="white").pack()
        envia_email1 = Button(janela2, text="Enviar esse texto por e-mail", height=2, width=20, command=lambda: janela_email(texto1)).pack()

botao1 = Button(janela, text="A cidade que nunca anoitece", height=2, width=30, command=lambda: fatos(registra_requisicao[0])).place(relx=0.02, rely=0.20)
botao2 = Button(janela, text="O animal que não sente sabor doce", height=2, width=30, command=lambda: fatos(registra_requisicao[1])).place(relx=0.53, rely=0.20)
botao3 = Button(janela, text="Um alimento que não estraga", height=2, width=30, command=lambda: fatos(registra_requisicao[2])).place(relx=0.02, rely=0.36)
botao4 = Button(janela, text="O primeiro presidente brasileiro", height=2, width=30, command=lambda: fatos(registra_requisicao[3])).place(relx=0.53, rely=0.36)
botao5 = Button(janela, text="O video mais assistido no YouTube", height=2, width=30, command=lambda: fatos(registra_requisicao[4])).place(relx=0.02, rely=0.52)
botao6 = Button(janela, text="O bilionário que doou sua fortuna", height=2, width=30, command=lambda: fatos(registra_requisicao[5])).place(relx=0.53, rely=0.52)
botao7 = Button(janela, text="10 heróis da vida real", height=2, width=30, command=lambda: fatos(registra_requisicao[6])).place(relx=0.02, rely=0.68)
botao8 = Button(janela, text="A duração do maior imperio antigo", height=2, width=30, command=lambda: fatos(registra_requisicao[7])).place(relx=0.53, rely=0.68)
botao9 = Button(janela, text="País com mais brasileiros no exterior", height=2, width=30, command=lambda: fatos(registra_requisicao[8])).place(relx=0.02, rely=0.84)
botao10 = Button(janela, text="Outra inovação de Santos Dumont", height=2, width=30, command=lambda: fatos(registra_requisicao[9])).place(relx=0.53, rely=0.84)

janela.mainloop()
