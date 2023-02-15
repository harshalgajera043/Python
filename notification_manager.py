import smtplib

from_mail = "hgajera307@gmail.com"
to_mail = "hgajera345@gmail.com"
password = "ouxlxxvjvrmxvxhq"


class NotificationManager():

    def __init__(self):
        super().__init__()

    def send_sms(self, message):
        message1 = smtplib.SMTP("smtp.gmail.com", 587)
        message1.starttls()
        message1.login(user=from_mail, password=password)
        message1.sendmail(from_addr=from_mail, to_addrs=to_mail, msg=message)

