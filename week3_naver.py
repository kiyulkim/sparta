import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta #새로운 데이터베이스 추가
# dbsparta 라는 이름의 데이터베이스가 있으면 가져오고 없으면 추가 

# mongoDB 추가하기
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# mongDB 가져오기
# users = list(db.users.find())
users = list(db.users.find({'age' : 21}))

for user in users:
    print(user['name'])

# 특정한 오브젝트 하나만 찾아보기
user = db.users.find_one({'name':'bobby'},{'_id':False})

#크롤링 하고 싶은 사이트 URL
target_url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303'

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')


# $('#cards-box') jquery 를 이용해 특정 html 태그의 정보를 가져옴
# .class, #cards-box, div > h1-> CSS 선택자(설렉터)
# soup 변수는 jquery 와 비슷하게 특정 html 태그의 정보를 가져올 수 있도록 준비된 상태
# bs4 프로그램 (BeautifulSoup)이 requests로 받아온 html 을 분석해 놓음 --> soup
# soup 역시 CSS 선택자를 이용해 정보를 가져올 수 있다. 

#선택자 정보 - #old_content > table > tbody > tr > td.title > div > a

#$('#old_content > table > tbody > tr')
# select() 여러 개를 가져온다 (for 문에서 사용가능)
movies = soup.select('#old_content > table > tbody > tr')




for movie in movies:
#여러 개의 tr 태그를 순서대로 순회
    #select_one 하나를 찾을 때 쓴다(없으면 None 값을 리턴)
    #만약 여러개가 있다면.. 가장 첫 번째를 리턴(이렇게는 사용하지 않음)
    a_tag = movie.select_one('td.title > div > a')
    b_tag = movie.select_one('td.point')


    # if a_tag is not None # 만약 있다면 
    if a_tag is not None: # 만약 있다면
        rank = movie.select_one('td.ac > img ')['alt']
        text = a_tag.text # 태그의 값을 가져옴 <a><값></a>
        point = b_tag.text 
        print(int(rank), text, point)

        document = {
            'rank' : int(rank),
            'title' : text,
            'point' : point,
        }
        db.users.insert_one(document)

# 숫자를 문자열로 str()
# 문자열을 숫자로 int(), 숫자가 아닌 문자는 에러