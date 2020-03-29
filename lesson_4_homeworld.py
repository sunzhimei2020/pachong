import requests
from bs4 import BeautifulSoup

# def listc(url):
#     res = requests.get(url)
#     content = res.json()
#     beauticomment = content['comment']['commentlist']
#     for i in beauticomment:
#         print(i['rootcommentcontent'])
#         print('-----------------------------------')
#
#     # print(content['comment']['commentlist'])
#
# for t in range(1,6):
#     url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum='+str(t)+'&pagesize=15&lasthotcommentid=song_102065756_1255296135_1577461106&domain=qq.com&ct=24&cv=10101010'
#     print(url)
#     listc(url)


def listcomment(url):
    res = requests.get(url)
    content = res.json()
    beauticomment = content['comment']['commentlist']
    for i in beauticomment:
        print(i['rootcommentcontent'])
        print('-----------------------------------')


for pagenumber in range(1,6):
    url= 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=8&needmusiccrit=0&pagenum='+str(pagenumber)+'&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'
    print(url)
    listcomment(url)
