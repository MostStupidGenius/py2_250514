# part2_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl as pyxl

class WebCrawler():
    def __init__(self):
        # Chrome WebDriver 초기화
        self.driver = webdriver.Chrome()
        self.driver.get("https://news.google.com/")
    
    def click_element(self, selector: str):
        # 선택한 요소를 클릭하는 기능
        # driver.fine_elements(선택방식, 특정 값)
        # 해당 조건을 만족하는 여러 요소를 가져올 수 있다.
        # find_elements이므로 여러 요소가 들어있는 것을 반환한다.
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        # 찾은 요소를 담을 변수 선언
        target = None

        for e in elements:
            if e.text == "과학/기술":
                target = e
                break
        # 요소를 클릭한다.
        target.click()
        input("Enter to next")
    
    def extract_elements(self, selector: str):
        # 전달된 셀렉터(선택자)의 조건을 만족하는 요소들을 반환
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return elements
    
    def print_titles(self, elements):
        # 출력할 파일명 설정
        file_name = 'web.txt'

        # 출력할 파일의 초기화 담당
        with open(file_name, 'w') as f:
            f.write("")
            # 기사 제목을 뽑아서
            for e in elements:
                # print(e.text)
                # 추출한 기사 제목이 비어 있으면
                # 다음 기사 제목 가져오기
                if not e.text.strip(): continue\
                # url 들고 오기. href 속성에 담긴 값은 링크를 가리킨다.
                url = e.get_attribute('href')
                with open(file_name, 'a', encoding='utf-8') as f:
                    # txt 파일로 출력
                    f.write(e.text + "," + url + "\n") # 기사 제목 뒤에 줄바꿈 추가
    
    def make_excel(self, elements, file_name: str):
        # excel 파일로 기사 제목과 그 링크 내보내기를 진행하려고 한다.
        # 엑셀을 파이썬에서 다루려면 openpyxl 라이브러리가 필요하다.
        # pip install openpyxl
        # import openpyxl을 해주어야 한다.
        # 엑셀 파일 생성
        # 엑셀은 기본적으로 workBook으로 이루어져 있다.
        # 이러한 워크북 안에 sheet가 들어 있는 구조를 가진다.
        wb = pyxl.Workbook()

        # 워크북을 활성화
        sheet = wb.active

        # 시트의 셀에 접근하려면 딕셔너리처럼 대괄호[] 안에 셀주소를 입력해주어야 한다.
        sheet['A1'] = '기사 제목'
        sheet['B1'] = '링크'
        
        # 엑셀의 행 번호를 증가시킬 인덱스 변수 선언
        i = 2 # 1행은 제목 행이기 때문에 건너뛴다.
        for e in elements:
            if not e.text.strip(): continue
            sheet[f'A{i}'] = e.text # 기사 제목
            sheet[f"B{i}"] = e.get_attribute('href') # 기사 링크
            i += 1 # 인덱스 값 증가 -> 다음 줄로 이동하여 입력
        print(f"총 {i-1}개 링크 추출 완료")
        # 정해진 파일 이름으로 저장
        wb.save(file_name)

if __name__ == "__main__":
    crawler = WebCrawler()
    input("Enter to next")
    # 과학/기술 태그 클릭
    crawler.click_element('#gb > div.gb_a.gb_qd > div > c-wiz > div.VCnfNe > div:nth-child(9) > a')
    # 특정 클래스를 가진 요소들 리스트를 가져와서
    elements = crawler.extract_elements('a.gPFEn')
    # 기사 제목과 링크를 txt 파일로 추출하는 기능
    # crawler.print_titles(elements)

    crawler.make_excel(elements, 'title and links.xlsx')
    input("Enter to continue 3")
    