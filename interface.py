from tkinter import *
from requisicao import *
from funcao import *
from envia_email import *

# rquivo que abre a janela de interação com usuario, as funções e raspagem do arquivo funcao, são usados nos botões(Button)

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
