from messaging.message_provider import MessageProvider
import smtplib, ssl

class EmailProvider(MessageProvider):
# maciej.forys.dev@gmail.com
    def send(self, message:str, email_to: str, email_from: str, password: str):
        port = 465

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email_from, password)
            server.sendmail(email_from, email_to, message)