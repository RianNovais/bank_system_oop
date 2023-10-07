import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Gmail():

    def send_mail_new_account_saving(self, name, email):
        PATH_MESSAGE_EMAIL = Path().absolute() / 'emailMessage' / 'msgEmail.html'

        with open(PATH_MESSAGE_EMAIL, 'r', encoding='UTF-8') as message:
            bodyMessage = message.read()
            template = string.Template(bodyMessage)
            bodyMessage = template.substitute(nome = name, typeAccount = 'Saving Account' )

        mime_multipart = MIMEMultipart()
        mime_multipart['from'] = os.getenv('EMAIL_SENDER')
        mime_multipart['to'] = email
        mime_multipart['subject'] = f'New account created!!'

        mime_text = MIMEText(bodyMessage, 'html', 'utf-8')

        mime_multipart.attach(mime_text)

        with smtplib.SMTP(os.getenv('SMTP_SERVER'),os.getenv('SMTP_PORT')) as server:
            server.ehlo()
            server.starttls()
            server.login(os.getenv('EMAIL_SENDER'), os.getenv('PASSWORD_EMAIL'))
            server.send_message(mime_multipart)

            print('email sent to user confirming account creation')

    def send_mail_new_account_checking(self, name, email):
        PATH_MESSAGE_EMAIL = Path().absolute() / 'emailMessage' / 'msgEmail.html'

        with open(PATH_MESSAGE_EMAIL, 'r', encoding='UTF-8') as message:
            bodyMessage = message.read()
            template = string.Template(bodyMessage)
            bodyMessage = template.substitute(nome=name, typeAccount='Checking Account')

        mime_multipart = MIMEMultipart()
        mime_multipart['from'] = os.getenv('EMAIL_SENDER')
        mime_multipart['to'] = email
        mime_multipart['subject'] = f'New account created!!'

        mime_text = MIMEText(bodyMessage, 'html', 'utf-8')

        mime_multipart.attach(mime_text)

        with smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:
            server.ehlo()
            server.starttls()
            server.login(os.getenv('EMAIL_SENDER'), os.getenv('PASSWORD_EMAIL'))
            server.send_message(mime_multipart)

            print('email sent to user confirming account creation')
