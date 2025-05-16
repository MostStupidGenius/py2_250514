# part1_crawling_with_selenium.py
# 웹 크롤링 with 셀레니움
# 셀레니움 라이브러리는 단순히 문자열만 주고 받는
# 리퀘스트, bs4 같은 방식을 넘어서, 직접 웹 브라우저를
# 코드를 이용하여 자동화할 수 있도록 만들어진 라이브러리이다.
# 눈으로 직접 조작되는 것을 보면서 코드를 작성, 실행할 수 있다.

# 실무에서 사용하는 라이브러리는 아니라고 하지만
# 대략적으로 웹 크롤링이 어떤 방식으로 이루어지는지
# 그 흐름을 파악하는 데 학습 목적이 있다.

# 셀레니움은 web driver를 이용하여 크롬 브라우저를 띄우는 방식으로
# 활용된다.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome WebDriver 초기화
driver = webdriver.Chrome()
driver.get("https://news.google.com/")
input("Enter to exit")