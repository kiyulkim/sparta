print('hello')
name = 'bob' #111
# let 없고 ; 없고, 주석은 #
num = 12
is_number = True #js 에서는 true(대소문자 주의)

a_list=[] #  빈리스트
a_list.append(1) #js 에서는 push
a_list[0] #호출은 동일
print(a_list) # console.log

a_dict = {}
a_dict = {'name': 'bob', 'age': 21}
a_dict['height'] = 178 #새로추가
print(a_dict['name']) # 값 가져오기 동일함

print(a_dict)

people =[{'name':'bob','age':20},{'name':'carry','age':25}]
print(people[0]['name'])


# function make_card(image){ 
#     console.log(image);
# }

def make_card(image):
    #파이썬은 들여쓰기를 강제한다. 단 {}를 쓰지 않는다.
    # : 얘가 들여쓰기를 명령한다. 
    print(image)

make_card('hello')


#조건문
def oddeven(num):
    if num % 2 == 0: #if 다음에 ( ) 없음 : 들여쓰기로 구분
        return True
    else:
        return False

print(oddeven(10))



#반복문
fruits = ['사과', '배', '감', '귤']

# for (let i=0;i<fruit.length;i++){
#     console.log(fruits[i]);
# }

for fruit in fruits: # fruits 에서 하나씩 꺼내다가 fuit에 저장해서 쓴다.


fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0 #사과 개수 저장하는 변수
for fruit in fruits:
    if fruit =='사과' :
        count +=1



people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]


#모든 사람의 이름과 나이를 출력해보자
def get_age(myname):
    # my name에 들어온 이름의 나이를 출력하는 함수
    for person in people :
        if person == myname:
            return person['age']
    else :
        return '해당하는 이름이 없습니다'

print(get)

get_age('bob') 