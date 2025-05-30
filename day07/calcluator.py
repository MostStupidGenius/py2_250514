# calcluator.py
# tkinter 라이브러리를 이용한 간단한 계산기 만들기
# tkinter로 만들 GUI 프로그램을 클래스화 하고
# 체계적으로 코드를 작성해 프로그램의 흐름을 알아보도록 하자.
import tkinter as tk
from tkinter import messagebox as msgbox

class Calculator():
    def __init__(self):
        # 1. tk.Tk()를 self.root에 담기
        self.root = tk.Tk()
        # 2. root의 타이틀, 크기 등 설정
        self.root.title("계산기")
        
        # 시작시 창크기를 담을 변수 선언
        self.width = 300
        self.height = 200
        self.root.geometry(f"{self.width}x{self.height}")

        # 계산결과를 담을 변수 선언
        self.result = 0 # 초기값 0
        # 피연산할 문자형 숫자를 담을 리스트 선언
        self.nums: list[str] = []
        # 연산자를 담을 변수
        self.oper: str = None
        # 마지막으로 입력한 값이 숫자인지여부
        self.is_last_oper_num = False
        
        # 프레임 및 위젯 생성 실행
        self.set_ui()

        # 프로그램 메인루프 실행
        self.root.mainloop()

    
    def set_ui(self):
        # 3. 위젯의 배치를 실행 + 레이아웃
        # 메인 창에서 그룹을 만들 상단 프레임
        self.top_frame = tk.Frame(self.root, borderwidth=5)
        # self.mid_frame = tk.Frame(self.root, borderwidth=3)
        # self.bottom_frame = tk.Frame(self.root, borderwidth=3)

        # 각각의 프레임 안에 위젯을 배치
        # 라벨 위젯 - 계산결과를 보여줄 라벨 위젯
        self.display = tk.Label(self.top_frame, text=self.result)
        self.display.grid(row=0, column=0)
        # .pack(pady=5, padx=5)

        # 계산기 버튼 생성
        self.create_buttons()


        self.top_frame.pack()
        # self.mid_frame.pack()
        # self.bottom_frame.pack()
    
    # 계산기의 버튼을 생성하는 메서드
    def create_buttons(self):
        # 버튼에 표시될 텍스트를 리스트로 정의
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # 시작행(display가 0행이므로 1부터 시작)
        row = 1
        # 시작열
        col = 0

        # 버튼 텍스트 리스트를 순회하며 버튼 생성
        for btn_text in button_texts:
            # 버튼 위젯 생성
            # lambda함수를 이용한 각 버튼별 고유한 함수 생성 및 연결(binding)
            btn = tk.Button(
                self.top_frame,
                text=btn_text,
                width=5,
                height=2,
                command=lambda x=btn_text: self.button_click(x)
            )

            # 버튼을 그리드에 배치
            # 그리드: 행 번호와 열 번호를 입력하여
            # master(부모창)에 배치하는 방식이다.
            btn.grid(
                row=row,
                column=col,
                padx=2,
                pady=2
            )
            col += 1 # 열 번호 증가

            # 4열까지 배치했으면 다음 행으로 이동
            if col > 3:
                col = 0
                row += 1
    
    # 기존 결과값(self.result)에 문자열 연산자와 피연산자 숫자값을 전달받아서
    # 연산하는 함수
    def button_click(self, value: str):
        # 입력된 value 값에 따라 다른 동작을 수행하는 메서드

        # 입력된 문자열이 숫자인지 연산자인지 구분하여
        # 숫자라면 이전 숫자와 합쳐서 하나의 문자열로 만들어야 한다.
        # -> 숫자를 하나씩 입력받기 때문에 각각 연산을 해버리면
        # 계산 결과에 문제가 발생한다.
        
        if value.isdigit():
            # 피연산할 숫자값을 담은 리스트 nums에 문자열 추가
            self.nums.append(value)
            
            # 직전에 입력한 값이 연산자면 display 라벨을 비워준다.
            if not self.is_last_oper_num: self.display["text"] = "0"
            display_text = "" if int(self.display["text"]) == 0 else str(self.display["text"])
            self.display["text"] = "".join([display_text, str(value)])
            self.result = int(self.display["text"])
            self.is_last_oper_num = True
        else:
            # self.nums에 담긴 문자형 숫자들을 피연산으로 전달
            int_num = Calculator.convert_nums(self.nums)
            # 문자형 숫자를 담은 리스트를 비워준다.
            self.nums: list[str] = []
            self.calculate(value, int_num)
            self.is_last_oper_num = False

    # 문자열 리스트를 전달받아서 하나의 문자열로 결합후
    # 숫자로 변환하는 함수
    def convert_nums(nums: list[str]):
        expressions = "".join(nums)
        return int(expressions)

    def calculate(self, oper: str, value: int):
        # 입력된 값에 따라 동작을 다르게 수행
        # match-case문으로 value의 값이 특정 값일 때
        # 특정 동작을 수행하도록 설정
        # self.oper가 설정되지 않은 경우
        if not self.oper:
            self.result = value
            self.oper = oper
            return
        match oper:
            case '=':
                self.result = self.calculate(self.oper, value)
                self.display.config(text=self.result) # 연산결과 보여주기
            case '+':
                self.display["text"] = str(self.result + int(value))
            case '-':
                self.display["text"] = str(self.result - int(value))
            case '*':
                self.display["text"] = str(self.result * int(value))
            case '/':
                self.display["text"] = str(self.result / int(value))
            case _:
                msgbox.showinfo("정보", "알 수 없는 결과입니다.")
if __name__ == "__main__":
    obj = Calculator()
