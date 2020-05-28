import requests
import bs4

response = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
print(response.json())

# ajax와 달리 response 변수에 바로 딕셔너리가 저장되어 있지 않음
# ajax 처럼 사용하려면 response.json() 함수를 실행시켜야 얻을 수 있음.

result = response.json()
print(result)

data = result['RealtimeCityAir']['row'] #js 랑 같음
print(data)

for datum in data:
    print(datum['MSRSTE_NM'], datum['IDEX_MVL'])




