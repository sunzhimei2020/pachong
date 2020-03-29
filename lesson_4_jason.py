#
# from bs4 import BeautifulSoup
#
# bs = BeautifulSoup('<p><a>惟有痴情难学佛</a>独无媚骨不如人</p>','html.parser')
# tag = bs.find('p')
# print(tag.text)
#
#
# list_all =[]
# list_a=[1,2,3]
# list_b=[4,5,6]
# list_all.append(list_a)
# list_all.append(list_b)
# print(list_all)
# print(list_all[0][0])


# import requests
# from bs4 import  BeautifulSoup
#
# # 请求html，得到response 以下第一个请求来自doc，但是里边没有我们想要的数据
# res_music = requests.get('https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6')
# # res_music.content
# # 打印它
# print(res_music.content)

#
# import  requests
# from bs4 import BeautifulSoup
# res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=67985810462556236&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# # print(res_music.text)  #这个值是一个字典
# json_music = res_music.json()
# # print(res_music.json())
#
# list_music = json_music['data']['song']['list']
# # list_music是一个列表，music是它里面的元素
# for music in list_music:
#     # 以name为键，查找歌曲名
#     print(music['name'])
#     # 查找专辑名
#     print('所属专辑：' + music['album']['name'])
#     # 查找播放时长
#     print('播放时长：' + str(music['interval']) + '秒')
#     # 查找播放链接
#     print('播放链接：https://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')
#
# 回归Jason 用法

# 引用requests库
# import requests
# # 调用get方法，下载这个字典
# res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# # # 使用json()方法，将response对象，转为列表/字典
# json_music = res_music.json()
# #
# # print(json_music)
#
# list_music = json_music['data']['song']['list']
# # print(type(list_music))
# # print(list_music)
#
# #将歌曲名、所属专辑、播放时长，以及播放链接自己给提取出来
#
# for  everyname in list_music:
#     song_name = everyname['name']
#     album     =everyname['album']['name']
#     interval = everyname['interval']
#     url = everyname['url']
#     print(song_name,album,interval,url)
#

# 引入json模块
# import json
# # 创建一个列表a
# a = [1,2,3,4]
# # 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b
# b = json.dumps(a)
# # 打印b
# print(b)
# # 打印b的数据类型
# print(type(b))
# # 使用loads()函数，将json格式的字符串b转为列表，赋值给c
# c = json.loads(b)
# # 打印c
# print(c)
# # 打印c的数据类型
# print(type(c))
#


a = {'name':'吴枫'}
# 定义一张列表
b = [1,2,3,4]
# 定义一个json
c = {
        "forchange":
        [
            { "name":"吴枫" , "gender":"male"},
            { "name":"酱酱" , "gender":"female"},
            { "name":"延君" , "gender":"male"},
        ]
    }

# print(c['forchange'][0]['name'])

for i in range(len(c['forchange'])):
    print(c['forchange'][i]['name'])  #吴枫,酱酱,延君


for j in c['forchange']:
    print(j['name'])   #吴枫,酱酱,延君