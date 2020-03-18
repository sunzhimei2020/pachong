# import requests
# # print(dir(requests))
# # # print(requests.__author__)
#
# #获取状态码
# res = requests.get('http://www.baidu.com')
# print(res.status_code)
# #下载一个图片

# tupian = requests.get('https://www.baidu.com/img/bd_logo1.png?where=super')
# photo=tupian.content
# app = open('b.png','wb')
# app.write(photo)
# app.close()

#下载一偏小说

# res1= requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# novel = res1.text
# localfile = open('a.txt','a')
# localfile.write(novel)
# localfile.close()

#获取一段文本，然后存到本地文件

# res2 = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
# wenben = res2.text
# bendi = open('httpresponsestatus.txt','a+')
# bendi.write(wenben)
# bendi.close()
#
#
# tupian = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
# photo=tupian.content
# app = open('c.png','wb')
# app.write(photo)
# app.close()
#

# #lesson2
# import requests
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# print(res.status_code)
# if res.status_code==200:
#     l = res.text
#     localhtml = open('a.html','w')
#     localhtml.write(l)
#     localhtml.close()


#定义编码：

import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res.encoding='utf-8'
print(res.text)
