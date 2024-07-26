#!/usr/bin/env python3

import urllib.request
import datetime
import smtplib
import os.path

weekday = str(datetime.datetime.today().weekday());
srs_filename = "https://www.electronpribor.ru/epr.zip";
dst_filename = "./dump/epr"+weekday+".zip";
urllib.request.urlretrieve(srs_filename, dst_filename);

TO = "mailta@ya.ru"
FROM = "info@hostping.ru"

if os.path.isfile(dst_filename):
    SUBJECT = "Backup DB Success"
    text = "Backup DB Success!"
else:
    SUBJECT = "Backup DB FAIL"
    text = "Backup DB FAIL!"

BODY = "\r\n".join((
"From: %s" % FROM,
"To: %s" % TO,
"Subject: %s" % SUBJECT ,
"",
text
))
server = smtplib.SMTP("10.1.137.157", "588")
server.sendmail(FROM, [TO], BODY)
server.quit()
