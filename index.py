import requests
from bs4 import BeautifulSoup
import pandas as pd

html = requests.get('https://www.tiobe.com/tiobe-index/')
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'lxml')

img_list = []; name_list = []; ranking_list = []
table = sp.find('table', id = 'top20')
table_trs = table.select('tbody > tr')
table_tds = table.find_all('td', 'td-top20')

for table_td in table_tds:
    if(table_td.find('img')):
        target = table_td.find('img')
        img_list.append('https://www.tiobe.com/tiobe-index/' + target['src'])
        
for table_tr in table_trs:
    index = 0
    for table_td in table_tr:
        if(index & 7 == 0):
            ranking_list.append(table_td.text)
        elif(index % 7 == 4):
            name_list.append(table_td.text)
        index += 1

output = pd.DataFrame([], columns = ['ranking', 'name', 'icon'])
output['ranking'] = ranking_list
output['name'] = name_list
output['icon'] = img_list
output = output.set_index('ranking')
print(output) # display(output)