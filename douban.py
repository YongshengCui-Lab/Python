import requests
import bs4

for num in range(10):
    url = 'https://movie.douban.com/top250?start='+ str(num*25) + '&filter='
    res = requests.get(url)
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    
    movies = soup.find('ol',class_ ='grid_view')
    
    for movie in movies.find_all('li'):
        number = movie.find('em', class_ = "").text
        #序列号
        name = movie.find('span', class_ = 'title').text
        #电影名
        rank = movie.find('span', class_ = 'rating_num').text
        #电影评分
        #recom = movie.find('span', class_ = 'inq').text
        #推荐语
        link = movie.find('div',class_ = 'hd').find('a')
        #链接
        if movie.find('span',class_="inq") != None:
            recom = movie.find('span',class_="inq").text #推荐语
            print('序列号：' + number)
            print('电影名：' + name)
            print('评分：' + rank)
            print('推荐语：' + recom)
            print('链接：' + link['href'])
            print('_______________')
        else:
            print('序列号：' + number)
            print('电影名：' + name)
            print('评分：' + rank)
            print('链接：' + link['href'])
            print('_______________')