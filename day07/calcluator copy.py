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
        self.width = 400  # 창 크기 증가
        self.height = 500
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

        # 디스플레이 영역 개선
        self.display = tk.Label(
            self.top_frame,
            text=self.result,
            font=('Arial', 24),
            width=20,
            anchor='e',
            relief='sunken',
            padx=10,
            pady=10
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky='ew', padx=5, pady=5)
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
            'C', '←', '±', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', '='
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
        
        # Clear 버튼 처리
        if value == 'C':
            self.clear_calculator()
            return
            
        # Backspace 버튼 처리
        if value == '←':
            self.handle_backspace()
            return
            
        # +/- 버튼 처리
        if value == '±':
            self.toggle_sign()
            return
        
        if value.isdigit():
            # 피연산할 숫자값을 담은 리스트 nums에 문자열 추가
            self.nums.append(value)
            
            # 직전에 입력한 값이 연산자면 display 라벨을 비워준다.
            if not self.is_last_oper_num: 
                self.display["text"] = "0"
                self.nums = [value]  # 새로운 숫자 시작
            
            display_text = "" if self.display["text"] == "0" else self.display["text"]
            self.display["text"] = display_text + str(value)
            self.result = int(self.display["text"])
            self.is_last_oper_num = True
        else:
            # 현재 display에 있는 값을 숫자로 변환
            current_value = int(self.display["text"])
            # 문자형 숫자를 담은 리스트를 비워준다.
            self.nums = []
            self.calculate(value, current_value)
            self.is_last_oper_num = False

    # 문자열 리스트를 전달받아서 하나의 문자열로 결합후
    # 숫자로 변환하는 함수
    @staticmethod
    def convert_nums(nums: list[str]) -> int:
        if not nums:
            return 0
        return int("".join(nums))

    def clear_calculator(self):
        """계산기 초기화"""
        self.result = 0
        self.nums = []
        self.oper = None
        self.is_last_oper_num = False
        self.display["text"] = "0"
        
    def handle_backspace(self):
        """마지막 입력 숫자 삭제"""
        if self.is_last_oper_num and self.display["text"] != "0":
            current_text = self.display["text"]
            if len(current_text) > 1:
                self.display["text"] = current_text[:-1]
                self.result = int(self.display["text"])
            else:
                self.display["text"] = "0"
                self.result = 0
                
    def toggle_sign(self):
        """현재 숫자의 부호 변경"""
        if self.is_last_oper_num and self.display["text"] != "0":
            current_text = self.display["text"]
            if current_text.startswith('-'):
                self.display["text"] = current_text[1:]
            else:
                self.display["text"] = '-' + current_text
            self.result = int(self.display["text"])
            
    def calculate(self, oper: str, value: int):
        # 입력된 값에 따라 동작을 다르게 수행
        if not self.oper:
            self.result = value
            self.oper = oper
            return
            
        try:
            match oper:
                case '=':
                    # 이전 연산자로 계산 수행
                    match self.oper:
                        case '+':
                            self.result += value
                        case '-':
                            self.result -= value
                        case '*':
                            self.result *= value
                        case '/':
                            if value == 0:
                                msgbox.showerror("에러", "0으로 나눌 수 없습니다.")
                                self.clear_calculator()
                                return
                            self.result //= value
                    self.display.config(text=str(self.result))
                    self.oper = None  # 연산 완료 후 연산자 초기화
                case '+':
                    self.result += value
                    self.display["text"] = str(self.result)
                    self.oper = oper
                case '-':
                    self.result -= value
                    self.display["text"] = str(self.result)
                    self.oper = oper
                case '*':
                    self.result *= value
                    self.display["text"] = str(self.result)
                    self.oper = oper
                case '/':
                    if value == 0:
                        msgbox.showerror("에러", "0으로 나눌 수 없습니다.")
                        self.clear_calculator()
                        return
                    self.result //= value
                    self.display["text"] = str(self.result)
                    self.oper = oper
                case _:
                    msgbox.showinfo("정보", "알 수 없는 연산입니다.")
        except Exception as e:
            msgbox.showerror("에러", f"계산 중 오류가 발생했습니다: {str(e)}")
            self.clear_calculator()

if __name__ == "__main__":
    obj = Calculator()
