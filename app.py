import requests
from lxml import html
import re
import json
import csv

res = requests.get('https://www.bnn.in.th/th/p/lenovo-notebook-legion5-15arh05-82b50045ta-black-a-195042346855_zge05r',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'})

tree = html.fromstring(html=res.text)

main_info = tree.xpath("//div[@id='__layout']/div/main/section")[0]
name = main_info.xpath(".//section[1]/div[2]/div[1]/h1/text()")[0].strip()
description = main_info.xpath(".//section[1]/div[2]/div[1]/div[2]/text()")[0]
price = main_info.xpath(".//section[1]/div[2]/div[3]/div[1]/div/div[1]/text()")[0].strip()
display = main_info.xpath(".//section[2]/div/div/table/tbody/tr[1]/td[2]/text()")[0].strip()

re_name = re.sub(r'^โน๊ตบุ๊ค\s+', '', name)
re_price = re.sub(r'[^\d]', '', price)

notebook_spec = {
    'name':re_name,
    'description':description,
    'price':re_price,
    'display':display
}

def write_to_json(filename, data):
    f = open(filename,'w')
    f.write(json.dumps(data))
    f.close
    
def write_to_csv(filename, data):
    headers = ['name','description','price','display']
    with open(filename,'w') as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerow(data)

write_to_json('Notebook_spec.json',notebook_spec)
write_to_csv('Notebook_spec.csv',notebook_spec)


print(notebook_spec)

  