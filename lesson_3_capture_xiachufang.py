# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
# 解析数据
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
# 查找最小父级标签
list_foods = bs_foods.find_all('div',class_='info pure-u')# 只有最小父级标签，才能形成列表。
# 打印最小父级标签
# print(list_foods)
#
# t = list_foods[0].find('a')
# print(t.text[17:])
# url='http://www.xiachufang.com'+t['href']
# print(url)

# 做题的过程中，需要先找到最小的单元，然后都取出来后，再写循环
#text针对这个标签里的，所有文字都可以取出来。而属性必须取当前标签下，如父标签不能取子标签的属性值
for i in list_foods:
    tag_a=i.find('a')
    name = tag_a.text[17:-13]
    URL = 'http://www.xiachufang.com'+tag_a['href']
    tag_p = list_foods[0].find('p',class_='ing ellipsis')
    ingredients = tag_p.text[1:-1]
    print('菜的名称：'+name+'\r\n'+'详细的做菜步骤：'+URL+'\r\n菜的主要成分:'+ingredients)
