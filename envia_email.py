import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# sera usada para enivair o testo escolhido por email, no arquivo interface janela3

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
