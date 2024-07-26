#!/usr/bin/python3

import urllib.request
import datetime

weekday = str(datetime.datetime.today().weekday());
filename = ".dump//epr"+weekday+".zip";
urllib.request.urlretrieve("https://www.electronpribor.ru/epr.zip", filename);
