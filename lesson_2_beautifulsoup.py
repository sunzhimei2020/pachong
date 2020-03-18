import requests
from bs4 import BeautifulSoup
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# soup = BeautifulSoup(res.text,'html.parser')
# # # print(type(soup))
# # item1=soup.find('div')
# itemall=soup.find_all('div',class_='books') # 这里的class 必须带有_
# # itemall=soup.find_all('div', style='books') # 这里的class 必须带有_
# # print(item1)
# # print(itemall)
# for i in itemall:
#     # print("您的数据在这里",i)
#     #
#     kind = i.find('h2')
#     name = i.find(class_="title")
#     # name = i.find('href')
#     info = i.find(class_="info")
#     # print(kind,name,info)
#     # # print(type(kind),type(name),type(info))
#     print(kind.text,name.text,name['href'],info.text)
    # # print(type(i)) #这里的i 是一个<class 'bs4.element.Tag'> tag对象

# print(soup.str())
# print(soup)
# BeautifulSoup()

res = requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
content = res.text
bs = BeautifulSoup(content,'html.parser')
# print(type(bs))
# print(bs)
result =bs.find_all('div',id="comments")
print(type(result))
print(result)
