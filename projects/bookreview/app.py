from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분, 나랑 통신할 수 있는(앱스토어를 받는것과 ㄷ동일)
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    #ajax 에서 가져온 데이터 변수 저장
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    # mongodb에 저장할 데이터 (오브젝트/도큐먼트)
    review = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive,
    }

    # dbsparta 데이터 베이스의 reviews 콜렉션에 review 도큐먼트 저장
    db.reviews.insert_one(review)


    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 작성되었다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)