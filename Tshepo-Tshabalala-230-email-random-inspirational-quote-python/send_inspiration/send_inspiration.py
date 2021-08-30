import sib_api_v3_sdk
from sib_api_v3_sdk import (
    TransactionalEmailsApi,
    ApiClient,
    SendSmtpEmailTo,
    SendSmtpEmail,
    SendSmtpEmailSender,
    Configuration,
    configuration,
)
import os, sys
from random import randint

ROOT_EMAIL = os.getenv("SMTP_LOGIN")
API_KEY = os.getenv("SMTP_API_KEY")


def select_quote():
    file = open("quotes.txt")
    email_content = file.readlines()
    file_length = len(email_content)
    random_num = randint(0, file_length - 1)
    file.close()
    return email_content[random_num]


def configure_api_key():
    configuration = Configuration()
    configuration.api_key["api-key"] = API_KEY
    api_instance = TransactionalEmailsApi(ApiClient(configuration))
    return api_instance


def send_email():
    if len(sys.argv) > 1 :
        email = sys.argv[1]
    else:
        email = ''
    api_instance = configure_api_key()
    email_content = select_quote()
    email_sender = SendSmtpEmailSender(name="Inspirational Quote", email=ROOT_EMAIL)
    recipient = SendSmtpEmailTo(email=email)
    send_smtp_email = SendSmtpEmail(
        sender=email_sender,
        to=[recipient],
        html_content=email_content,
        subject="This is a test subject 3",
    )
    api_response = api_instance.send_transac_email(send_smtp_email)
    return api_response


def main():
    email_content = select_quote()
    print(send_email())


if __name__ == "__main__":
    main()
