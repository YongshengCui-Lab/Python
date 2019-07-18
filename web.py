import requests

res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')

page = res.text

with open('article.txt','a+',encoding = 'utf-8') as f:
    code = f.write(page)