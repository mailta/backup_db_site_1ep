#!/usr/bin/python3

import urllib.request
import datetime
import smtplib

weekday = str(datetime.datetime.today().weekday());
srs_filename = "https://www.electronpribor.ru/epr.zip";
dst_filename = "./dump/epr"+weekday+".zip";
urllib.request.urlretrieve(srs_filename, dst_filename);

#send post messages
#smtp_server = "smtp.gmail.com"
#port = 587
#server = smtplib.SMTP(smtp_server, port)
#server.starttls()

#email = "your_email@gmail.com"
#password = "your_password"
#server.login(email, password)
#from_email = email
#to_email = "recipient_email@example.com"
#subject = "Тестовое сообщение"
#message = "Привет, это тестовое сообщение, отправленное с помощью Python и SMTP."
#server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{message}")

#server.quit()
