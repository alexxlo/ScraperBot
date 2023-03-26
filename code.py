# -*- coding: utf-8 -*-

import requests
import datetime
import pytz
import numpy as np
import pandas as pd
import csv
import os
import time
from htmldate import find_date

token = 'your token'
chat_id = 'your chat it'

"""中央新聞社"""

good_list = []

URL = 'chosen link'

today = datetime.datetime.now()
year = str(today.year)
month = str(today.month)
day = str(today.day)

if len(month) == 1 and len(day) == 1:
    date = year + '0' + month + '0' + day
elif len(month) == 2 and len(day) == 1:
    date = year + month + '0' + day
elif len(month) == 1 and len(day) == 2:
    date = year + '0' + month + day
elif len(month) == 2 and len(day) == 2:
    date = year + month + day

URL = URL + date
URL = str(URL)
news_code = '0000'
code_list = []

range_limit = 180

beijing_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H:%M:%S")[0:2]

for i in range(1, range_limit):
    start_code = int(news_code)
    code_to_link = start_code + i
    
    if len(str(code_to_link)) == 1:
      code_to_link = str(code_to_link)
      final_code = '000' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 2:
      code_to_link = str(code_to_link)
      final_code = '00' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 3:
      code_to_link = str(code_to_link)
      final_code = '0' + code_to_link
      code_list.append(final_code)

for post in code_list:
    end = '.aspx'
    def_URL = URL + post + end
    #print(def_URL)
    if requests.get(def_URL).status_code == 200:
      #print(requests.get(str(def_URL)).status_code)
      good_list.append(def_URL)

rows = good_list.copy() 

dir = 'export dir'

if (len(os.listdir('export dir')) - 1) == 0:
  for text in good_list:
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

elif (len(os.listdir('export dir')) - 1) == 1:
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
  
  latest_links = pd.read_csv(f'export dir/{file_name}.csv')
  latest_links = latest_links['Links'].tolist()
  send_links = set(good_list) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

else:
  
  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  name_list = []
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
      name_list.append(int(file_name))
    
  latest = max(name_list)
  latest = str(latest)
    
  latest_links = pd.read_csv(f'export dir/{latest}.csv')
  latest_links = latest_links['Links'].tolist()
    
  send_links = set(rows) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  df.to_csv(f'export dir/{unique_time_format}.csv')

"""中央新聞社"""

good_list = []

URL = 'chosen link'

today = datetime.datetime.now()
year = str(today.year)
month = str(today.month)
day = str(today.day)

if len(month) == 1 and len(day) == 1:
    date = year + '0' + month + '0' + day
elif len(month) == 2 and len(day) == 1:
    date = year + month + '0' + day
elif len(month) == 1 and len(day) == 2:
    date = year + '0' + month + day
elif len(month) == 2 and len(day) == 2:
    date = year + month + day

URL = URL + date
URL = str(URL)
news_code = '0000'
code_list = []

range_limit = 0

beijing_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H:%M:%S")[0:2]

if int(beijing_time) <= 10:
  range_limit += 70
elif 10 < int(beijing_time) <= 13:
  range_limit += 150
elif 13 < int(beijing_time) <= 16:
  range_limit += 200
elif 16 < int(beijing_time) <= 19:
  range_limit += 300
elif 19 < int(beijing_time) <= 23:
  range_limit += 400


for i in range(1, range_limit):
    start_code = int(news_code)
    code_to_link = start_code + i
    
    if len(str(code_to_link)) == 1:
      code_to_link = str(code_to_link)
      final_code = '000' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 2:
      code_to_link = str(code_to_link)
      final_code = '00' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 3:
      code_to_link = str(code_to_link)
      final_code = '0' + code_to_link
      code_list.append(final_code)

for post in code_list:
    end = '.aspx'
    def_URL = URL + post + end
    #print(def_URL)
    if requests.get(def_URL).status_code == 200:
      #print(requests.get(str(def_URL)).status_code)
      good_list.append(def_URL)

rows = good_list.copy() 

dir = 'export dir'

if (len(os.listdir('export dir')) - 1) == 0:
  for text in good_list:
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

elif (len(os.listdir('export dir')) - 1) == 1:
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
  
  latest_links = pd.read_csv(f'export dir/{file_name}.csv')
  latest_links = latest_links['Links'].tolist()
  send_links = set(good_list) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

else:
  
  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  name_list = []
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
      name_list.append(int(file_name))
    
  latest = max(name_list)
  latest = str(latest)
    
  latest_links = pd.read_csv(f'export dir/{latest}.csv')
  latest_links = latest_links['Links'].tolist()
    
  send_links = set(rows) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  df.to_csv(f'export dir/{unique_time_format}.csv')

"""FocusTaiwan"""

good_list = []
good_list_1 = []

URL = 'first chosen url/'
URL_s = 'second chosen url/'

today = datetime.datetime.now()
year = str(today.year)
month = str(today.month)
day = str(today.day)

if len(month) == 1 and len(day) == 1:
    date = year + '0' + month + '0' + day
elif len(month) == 2 and len(day) == 1:
    date = year + month + '0' + day
elif len(month) == 1 and len(day) == 2:
    date = year + '0' + month + day
elif len(month) == 2 and len(day) == 2:
    date = year + month + day

URL = URL + date
URL = str(URL)

URL_s = URL_s + date
URL_s = str(URL_s)

news_code = '0000'
code_list = []

range_limit = 17

beijing_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H:%M:%S")[0:2]

for i in range(1, range_limit):
    start_code = int(news_code)
    code_to_link = start_code + i
    
    if len(str(code_to_link)) == 1:
      code_to_link = str(code_to_link)
      final_code = '000' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 2:
      code_to_link = str(code_to_link)
      final_code = '00' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 3:
      code_to_link = str(code_to_link)
      final_code = '0' + code_to_link
      code_list.append(final_code)

for post in code_list:
    def_URL = URL + post
    if requests.get(def_URL).status_code == 200:
      good_list.append(def_URL)

for post in code_list:
    def_URL_s = URL_s + post
    if requests.get(def_URL_s).status_code == 200:
      good_list_1.append(def_URL_s)

good_list = good_list + good_list_1

rows = good_list.copy() 

dir = 'export dir'

if (len(os.listdir('export dirs')) - 1) == 0:
  for text in good_list:
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

elif (len(os.listdir('export dir')) - 1) == 1:
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
  
  latest_links = pd.read_csv(f'export dir/{file_name}.csv')
  latest_links = latest_links['Links'].tolist()
  send_links = set(good_list) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

else:
  
  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  name_list = []
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
      name_list.append(int(file_name))
    
  latest = max(name_list)
  latest = str(latest)
    
  latest_links = pd.read_csv(f'export dir/{latest}.csv')
  latest_links = latest_links['Links'].tolist()
    
  send_links = set(rows) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  df.to_csv(f'export dir/{unique_time_format}.csv')

"""##FocusTaiwan(中央英文版)


"""

good_list = []
good_list_1 = []

URL = 'chosen url'
URL_s = 'secondo chosen link'

today = datetime.datetime.now()
year = str(today.year)
month = str(today.month)
day = str(today.day)

if len(month) == 1 and len(day) == 1:
    date = year + '0' + month + '0' + day
elif len(month) == 2 and len(day) == 1:
    date = year + month + '0' + day
elif len(month) == 1 and len(day) == 2:
    date = year + '0' + month + day
elif len(month) == 2 and len(day) == 2:
    date = year + month + day

URL = URL + date
URL = str(URL)

URL_s = URL_s + date
URL_s = str(URL_s)

news_code = '0000'
code_list = []

range_limit = 0

beijing_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H:%M:%S")[0:2]

if int(beijing_time) <= 10:
  range_limit += 30
elif 10 < int(beijing_time) <= 13:
  range_limit += 40
elif 13 < int(beijing_time) <= 16:
  range_limit += 50
elif 16 < int(beijing_time) <= 19:
  range_limit += 50
elif 19 < int(beijing_time) <= 23:
  range_limit += 60


for i in range(1, range_limit):
    start_code = int(news_code)
    code_to_link = start_code + i
    
    if len(str(code_to_link)) == 1:
      code_to_link = str(code_to_link)
      final_code = '000' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 2:
      code_to_link = str(code_to_link)
      final_code = '00' + code_to_link
      code_list.append(final_code)
    
    elif len(str(code_to_link)) == 3:
      code_to_link = str(code_to_link)
      final_code = '0' + code_to_link
      code_list.append(final_code)

if len(str(month)) == 1:
  month = '0' + str(month)
else:
  month = str(month)

if len(str(day)) == 1:
  day = '0' + str(day)
else:
  day = str(day)

date_okay = str(year) + '-' + day + '-' + month

for post in code_list:
    def_URL = URL + post
    if find_date(def_URL) == date_okay:
    #if requests.get(def_URL).status_code == 200:
      good_list.append(def_URL)

for post in code_list:
    def_URL_s = URL_s + post
    if find_date(def_URL_s) == date_okay:
    #if requests.get(def_URL_s).status_code == 200:
      good_list_1.append(def_URL_s)

good_list = good_list + good_list_1

rows = good_list.copy() 

dir = 'export dir'

if (len(os.listdir('export dir')) - 1) == 0:
  for text in good_list:
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

elif (len(os.listdir('export dir')) - 1) == 1:
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
  
  latest_links = pd.read_csv(f'export dir/{file_name}.csv')
  latest_links = latest_links['Links'].tolist()
  send_links = set(good_list) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

else:
  
  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  name_list = []
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
      name_list.append(int(file_name))
    
  latest = max(name_list)
  latest = str(latest)
    
  latest_links = pd.read_csv(f'export dir/{latest}.csv')
  latest_links = latest_links['Links'].tolist()
    
  send_links = set(rows) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  df.to_csv(f'export dir/{unique_time_format}.csv')

"""Taipei Times"""

good_list = []

URL = 'chosen url'

today = datetime.datetime.now()
year = str(today.year)
month = str(today.month)
day = str(today.day)

if len(month) == 1 and len(day) == 1:
    date = year + '/' + '0' + month + '/' + '0' + day + '/'
elif len(month) == 2 and len(day) == 1:
    date = year + '/' + month + '/' + '0' + day + '/'
elif len(month) == 1 and len(day) == 2:
    date = year + '/' + '0' + month + '/' + day + '/'
elif len(month) == 2 and len(day) == 2:
    date = year +'/' + month + '/' + day + '/'

URL = URL + date
URL = str(URL)

news_code = '2003783'
code_list = []

range_limit = 0

beijing_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H:%M:%S")[0:2]

if int(beijing_time) <= 10:
  range_limit += 30
elif 10 < int(beijing_time) <= 13:
  range_limit += 60
elif 13 < int(beijing_time) <= 16:
  range_limit += 100
elif 16 < int(beijing_time) <= 19:
  range_limit += 150
elif 19 < int(beijing_time) <= 23:
  range_limit += 150


for i in range(1, range_limit):
  if len(str(i)) == 1:
    code_to_link = str(i)
    final_code = '00' + code_to_link
    code_list.append(final_code)
    
  elif len(str(i)) == 2:
    code_to_link = str(i)
    final_code = '0' + code_to_link
    code_list.append(final_code)
    
  elif len(str(i)) == 3:
    code_to_link = str(i)
    final_code = code_to_link
    code_list.append(final_code)

if len(str(month)) == 1:
  month = '0' + str(month)
else:
  month = str(month)

if len(str(day)) == 1:
  day = '0' + str(day)
else:
  day = str(day)

date_okay = str(year) + '-' + day + '-' + month

for post in code_list:
    def_URL = URL + news_code + post
    if find_date(def_URL) == date_okay:
    #if requests.get(def_URL).status_code == 200:
        good_list.append(def_URL)

rows = good_list.copy() 

dir = 'export dir'

if (len(os.listdir('export dir')) - 1) == 0:
  for text in good_list:
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

elif (len(os.listdir('export dir')) - 1) == 1:
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
  
  latest_links = pd.read_csv(f'export dir/{file_name}.csv')
  latest_links = latest_links['Links'].tolist()
  send_links = set(good_list) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

else:
  
  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  name_list = []
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
      name_list.append(int(file_name))
    
  latest = max(name_list)
  latest = str(latest)
    
  latest_links = pd.read_csv(f'export dir/{latest}.csv')
  latest_links = latest_links['Links'].tolist()
    
  send_links = set(rows) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  df.to_csv(f'export dir/{unique_time_format}.csv')

"""中華日報"""

AGG = 'final numbers in latest news article url'

#AGG = str(input())

good_list = []

URL = 'chosen link'

news_code = AGG
code_list = []

range_limit = 0

beijing_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime("%H:%M:%S")[0:2]

if int(beijing_time) <= 10:
  range_limit += 80
elif 10 < int(beijing_time) <= 13:
  range_limit += 120
elif 13 < int(beijing_time) <= 16:
  range_limit += 160
elif 16 < int(beijing_time) <= 19:
  range_limit += 240
elif 19 < int(beijing_time) <= 23:
  range_limit += 330

i = 0
while i != range_limit:
  news_code_int = int(news_code)
  news_code_int = news_code_int + i
  news_code_str = str(news_code_int)
  code_list.append(news_code_str)

  i += 1  

for post in code_list:
    def_URL = URL + post
    if requests.get(def_URL).status_code == 200:
        good_list.append(def_URL)

rows = good_list.copy() 

dir = 'export dir'

if (len(os.listdir('export dir')) - 1) == 0:
  for text in good_list:
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

elif (len(os.listdir('export dir')) - 1) == 1:
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
  
  latest_links = pd.read_csv(f'export dir/{file_name}.csv')
  latest_links = latest_links['Links'].tolist()
  send_links = set(good_list) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)

  df.to_csv(f'export dir/{unique_time_format}.csv')

else:
  
  unique_time = int(round(time.time() * 1000))
  unique_time_format = str(unique_time)
  
  dic = {'Links': rows}  
  
  df = pd.DataFrame(dic) 

  name_list = []
  for file in os.listdir(dir):
    if file.endswith(".csv"):
      file_name = os.path.splitext(os.path.split(file)[1])[0]
      name_list.append(int(file_name))
    
  latest = max(name_list)
  latest = str(latest)
    
  latest_links = pd.read_csv(f'export dir/{latest}.csv')
  latest_links = latest_links['Links'].tolist()
    
  send_links = set(rows) - set(latest_links)
  send_links = list(send_links)

  if len(good_list) == len(send_links):
    text = 'no news for now'
    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  else:
    for text in send_links:
      requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  
  df.to_csv(f'export dirh/{unique_time_format}.csv')
