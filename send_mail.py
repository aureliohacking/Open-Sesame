import smtplib
import ssl
import socket
import certifi
import os

os.environ['SSL_CERT_FILE'] = certifi.where()


def send_ip(correo, password, ip):

    context = ssl.create_default_context()
    # Certificados de CA de confianza del correo.
    # Así no envía a bandeja de spam.

    message = """\
    Subject: IP Definitivas U

    URL: {0}:8000""".format(ip)
    

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(correo, password)
        server.sendmail(correo, 'Ingresa el correo', message)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    
    return IP



def send():

    correo = 'Ingresa el correo'
    password = 'Ingresa la contraseña'
    ip = get_ip()

    send_ip(correo, password, ip)

