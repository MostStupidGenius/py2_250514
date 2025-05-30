# part1_tkinter.py
# GUI 프로그램을 만들기 위한 기본 내장 라이브러리로
# GUI 프로그래밍에 있어서 기초적인 개념을 배우는 데 적합한
# 간단한 라이브러리이다.
# 작은 프로젝트나 짧은 시간 안에 개발해야 하는 경우 주로 사용되며
# 기본에 충실하기 때문에 복잡한 동작이나 세련된 디자인엔 약한 면모를 보인다.
# 하지만 설치가 필요없기 때문에 개발시간을 크게 단축할 수 있다.
import tkinter as tk
from tkinter import messagebox

# 메인 윈도우 생성
# 모든 GUI 프로그램은 윈도우 객체를 기본으로 삼고
# 이것에서 파생된 다른 자식창들이 존재할 수도 있다.
# 메인 윈도우가 종료되는 순간 프로그램도 종료된다.
root = tk.Tk()
# 윈도우의 상단 제목을 변경
root.title("나의 첫 프로그램")

# 윈도우의 시작시 크기 설정
# geometry("가로길이x세로길이")
width = 600
height = 200
root.geometry(f"{width}x{height}") # "300x200"

# 위젯(widget)
# 위젯이란, 창 내부에 배치되어 사용자와 상호작용하는 개체들을 가리킨다.
# 단순히 내용을 보여주는 목적일 수도 있고 입력을 받거나 클릭 등의 이벤트와
# 상호작용하여 그 입력되거나 선택된 값을 변수로 받아서
# 내부적인 처리에 사용될 수 있다.

# 1. 라벨(label) 위젯
# 라벨 위젯은 사용자와의 상호작용은 없지만 텍스트나 이미지를 보여주는
# 용도로 사용된다.
label = tk.Label(
    root, # 해당 위젯이 들어갈 부모, 공간을 설정하는 부분
    text="라벨1의 텍스트" # 해당 라벨의 내용을 적는 부분
)
# 위젯이 창에 나오려면 패킹과 같은 렌더링 과정을 거쳐야 한다.
# pady는 위아래로 공간을 만들어 위젯 내부와 콘텐츠 사이에 빈 공간을
# 만드는 매개변수다.
label.pack(
    pady=5,
    padx=10
)

# 엔트리(Entry) 위젯
# 짧은 텍스트 입력을 받기 위한 input box로, 사용자로부터
# 타자를 통해 값을 직접 입력받는 용도로 쓰인다.
entry = tk.Entry(
    root,
    width=20
)
entry.pack(pady=5)

# 버튼(button) 위젯
# 사용자로부터의 마우스 클릭 이벤트와 직접적으로 상호작용하는
# 대표적인 위젯이다.
# 해당 버튼을 클릭했을 때 동작할 메서드, 함수를 지정할 수 있다.
# -> binding이라고 부른다.

# 버튼을 클릭했을 때 실행할 동작 정의
def btn_click():
    name = entry.get() # 엔트리의 텍스트를 str로 가져오는 동작
    # 엔트리에 입력된 문자가 있다면
    if name:
        messagebox.showinfo("인사", f"안녕하세요. {name}님. 환영합니다.")
    else:
        messagebox.showwarning("경고", "입력된 이름이 없습니다.")

# 버튼(button) 위젯 생성
button = tk.Button(
    root,
    text="이름입력",
    command=btn_click # ★버튼을 눌렀을 때 동작할 함수 이름을 전달한다.
    # 함수를 사용()하는 것이 아니라 함수, 메서드의 이름만 전달하는 것이다.
)
button.pack()

# 체크박스(checkbox)
# 체크박스란, 여러 선택지를 주고 중복으로 체크를 할 수 있는
# 위젯이다.
# 체크를 하면 True, 체크가 풀려있으면 False를 나타내며
# 체크한 체크박스의 값을 추출할 수 있다.
check_var = tk.BooleanVar() # 체크박스의 값을 담을 tk의 특별한 객체
checkbox = tk.Checkbutton(
    root,
    text="메시지박스 on/off",
    variable=check_var # 체크박스의 체크여부를 어떤 변수에 전달할지를 정하는 부분
)
checkbox.pack(pady=5)



if __name__ == "__main__":
    root.mainloop()