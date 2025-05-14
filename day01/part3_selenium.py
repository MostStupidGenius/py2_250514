# part3_selenium.py
# 웹 크롤링
# 웹페이지의 구조를 파악하여 그 구조 안에서 원하는 데이터를 추출하는 것을
# 가리킨다. -> 데이터 수집
# 웹 크롤링을 하려면 세 가지 준비가 필요한데
# 1. 웹페이지 문서를 파이썬에서 읽기 쉬운 객체로 바꿔주는
# beautifulsoup
# 2. 웹페이지를 요청하여 그 내용을 받아오는
# requests
# 3. 브라우저를 파이썬 코드로 조작할 수 있게 해주는 라이브러리
# selenium
from bs4 import BeautifulSoup as bs
import requests
import selenium

# url을 함수의 인수로 전달하여 해당 페이지의 모든 html 텍스트를 읽어온다.
def request_url(url: str):
    # requests.get(url) # 전달된 url의 응답 문자열을 반환
    response = requests.get(url)
    # html 코드의 내용을 쉽게 읽기 위해
    # bs의 parser를 사용한다.
    soup = bs(response.text, 'html.parser')

    # 스프 형태로 만들어진 html 문서 내용은
    # 객체처럼 메서드, 변수 등으로 이루어져 있다.
    divs = soup.find_all('div')
    for div in divs:
        result = div.get('class')
        print(result if result else 'None')

if __name__ == "__main__":
    # url = 'https://code.visualstudio.com/docs/?dv=winzip'
    url = 'https://www.naver.com/'
    request_url(url)
