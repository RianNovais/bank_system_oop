import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# The gmail class has the functionality to send emails using python via the gmail SMTP server, using smtplib, it has
# methods to send emails to the user when an account is created, be it "SavingAccount" or "CheckingAccount", an email is
#sent with a personalized message that comes from HTML and processed using string.Template , all sensitive information
# is brought from the .env file and loaded via load-dotenv.


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
