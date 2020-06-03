
a = 2
print(a+3)

first_name = 'kiyul'
last_name = 'kim'
print(first_name + last_name)
a_list = ['사과','배','딸기']
a_list.append('귤')
print(a_list)

b_list = ['김기준','김기열','김기호']

a_dict = {'name':'bob','age':24}
a_dict['height'] = 178
print('a_dict')
print(a_dict)
a_dict['fruits']=a_list
print(a_dict['fruits'][2])


def sum(a,b):
    return a+b

result = sum(2,3)
print(result)

# 아래는 함수

def is_adult(age,sex):
    if (age > 20 and sex =='남'):
        print('남자 성인입니다')
    elif (age >20 and sex =='여') :
        print ('여자 성인입니다')
    else :
        print('청소년입니다')

is_adult(25,'남')

# 아래는 조건문

fruits=['사과','배','밤','귤'] 

for fruit in fruits : 
    print(fruit)

fruits=['사과','배','밤','귤','배','배','배','귤'] 

def count_fruit(name) :
    count=0
    for fruit in fruits :
        if (fruit == name):
            count += 1
        return count

result = count_fruit('배')
print(result)
