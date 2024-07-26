import urllib.request
import datetime
import smtplib
import os.path
import requests
import sys

weekday = str(datetime.datetime.today().weekday()+1);
src_filename = "https://www.electronpribor.ru/epr.zip";
dst_filename = "E:\\Shares\\Electronpribor\\Общая\\Сайт\\Dump\\epr"+weekday+".zip";


from_mail = "info@1ep.ru"
to_mail = "psa@1ep.ru, mas@1ep.ru"

request = requests.head(src_filename, allow_redirects=True)
if request.status_code == 200:
   urllib.request.urlretrieve(src_filename, dst_filename);
else:
    SUBJECT = "Backup DB site fail!"
    text =  "Source file https://www.electronpribor.ru/epr.zip not found"
    BODY = "\r\n".join((
    "From: %s" % from_mail,
    "To: %s" % to_mail,
    "Subject: %s" % SUBJECT ,
    "",
    text
    ))
    server = smtplib.SMTP("10.1.4.211", "587")
    server.sendmail(from_mail, ["psa@1ep.ru", "mas@1ep.ru", "ta77@ro.ru"], BODY)
    server.quit()
    sys.exit(1)

if os.path.isfile(dst_filename):
   SUBJECT = "Backup DB site success"
   text = "Backup DB site success! - " + "erp"+weekday+".zip"
else:
   SUBJECT = "Backup DB site fail!"
   text = "Backup DB site fail!"

BODY = "\r\n".join((
"From: %s" % from_mail,
"To: %s" % to_mail,
"Subject: %s" % SUBJECT ,
"",
text
))
server = smtplib.SMTP("10.1.4.211", "587")
server.sendmail(from_mail, ["psa@1ep.ru", "mas@1ep.ru", "ta77@ro.ru"], BODY)
server.quit()
