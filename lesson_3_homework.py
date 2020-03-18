import requests
from bs4 import BeautifulSoup

def search(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

        res = requests.get(url, headers=headers)#这里不加headers会提示 返回状态码是418.所以要加headers
        bs = BeautifulSoup(res.text, 'html.parser')

        contents = bs.find_all('div', class_='item')
        # print(contents)
        #
        for i in contents:
            tit = i.find('span', class_='title')
            moviename = tit.text
            xh = i.find('em')
            xuhao = xh.text
            ur = i.find('a')
            url = ur['href']
            pingfen = i.find('span', class_='rating_num')
            rating_num = pingfen.text
            tj = i.find('span', class_='inq')
            if( hasattr(tj,'text')):# 判断tj有没有这个属性text,如果没有，就显示没有推荐语。
                tuijianyu = tj.text
            else:
                tuijianyu = "no 推荐语"
            print(" 序号：" + xuhao + ' 电影名：' + moviename + "    超链接： " + url + "  用户评分： " + rating_num + " 推荐语: " + tuijianyu)



# 这次试用的方法是 最小父标签(item)。找到列表中的第一个值，提取出所需要的值，然后进行循环，所有的List


for i in range(0,226,25):
    url = 'http://movie.douban.com/top250?start='+str(i)+'&filter='
    print(url)
    search(url)# 把一个url的处理逻辑搞成一个方法。然后传给他url地址即可。
