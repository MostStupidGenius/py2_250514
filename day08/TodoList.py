# part1_pyqt5.py
# pyQt5는 c언어에서 만들어져 있던 프레임워크인
# Qt Framework를 파이썬에서 사용할 수 있도록 바인딩한
# 버전이다.
# tkinter에서처럼 애플리케이션과 상호작용할 수 있는 위젯으로
# 이루어진다.
# 이중 QWidget을 상속받아서 클래스를 작성하고 프로그램을 동작시킬 수 있다.

# pip install pyqt5

import sys # 프로그램 종료시 필요한 임포트
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QListWidget,
    QCheckBox
)

# 클래스 만들기 - QWidget 상속
class TodoList(QWidget):
    def __init__(self):
        # 상속받는 부모클래스에서 만들어둔 초기화코드 실행
        super().__init__()
        # 프로그램의 ui를 꾸미는 코드를 실행
        self.initUI()
    
    # 할일 리스트 프로그램 제작
    # 1. 할일 내용을 입력할 input 박스 필요
    # 2. 입력된 할일 리스트를 리스트업 할 리스트박스 필요
    # 3. 마우스 클릭으로 선택한 할일 요소를 '삭제' 버튼을 눌렀을 때 삭제
    def initUI(self):
        # 프로그램의 상단 표시되는 타이틀 내용 변경
        self.setWindowTitle("할일리스트 프로그램")
        # 프로그램 초기 위치 설정
        self.setGeometry(0, 0, 300, 200) # 0,0 위치에서 가로길이 300, 세로길이 200
        # 입력칸과 추가버튼을 생성하는 기능 호출
        self.initTopUI()
        # 리스트업을 할 리스트 박스를 생성하는 기능 호출
        self.initMidUI()
        # 삭제버튼이 들어갈 하단을 구성하는 기능을 호출
        self.initBottomUI()

        # 위에서 생성한 상단, 중단, 하단의 레이아웃을 하나의 레이아웃에 넣는다.
        # 세로로 상단, 중단, 하단 레이아웃을 배치
        self.wrapperLayout = QVBoxLayout() # 버티컬
        self.wrapperLayout.addLayout(self.topVerticalLayout)
        self.wrapperLayout.addLayout(self.midLayout)
        self.wrapperLayout.addLayout(self.bottomLayout)

        # 세 레이아웃을 모두 추가한 래퍼 레이아웃을 self에 세팅
        self.setLayout(self.wrapperLayout)

        self.show()
    
    def initTopUI(self):
        # 세로로 배치하는 레이아웃 생성
        # 입력칸, 추가버튼 아래로 다른 위젯을 추가
        self.topVerticalLayout = QVBoxLayout()

        # 가로로 배치하는 상단 레이아웃의 하위 레이아웃
        self.topVerHorizonLayout = QHBoxLayout()
        self.topVerticalLayout.addLayout(self.topVerHorizonLayout)

        # 할일 내용을 입력할 입력칸
        self.todoListInput = QLineEdit()
        # 상단 레이아웃에 입력칸 위젯을 추가
        self.topVerHorizonLayout.addWidget(self.todoListInput)

        # 할일을 목록에 추가하는 기능을 가진 버튼
        self.addButton = QPushButton(text="추가")
        # 추가 버튼을 클릭했을 때 동작할 기능 연결
        self.addButton.clicked.connect(self.addTask)
        # 추가 버튼을 상단 레이아웃에 추가
        self.topVerHorizonLayout.addWidget(self.addButton)

        # 상단 세로 레이아웃의 하단에 배치할 가로 레이아웃
        self.top2ndLayout = QHBoxLayout()
        self.topVerticalLayout.addLayout(self.top2ndLayout)

        # 체크 박스 위젯 생성
        self.rememberBox = QCheckBox(text="내용유지")
        self.rememberInput = self.rememberBox.isChecked()

        self.top2ndLayout.addWidget(self.rememberBox)

    def initMidUI(self):
        self.midLayout = QHBoxLayout()
        
        # 할일 목록 위젯 생성
        self.todoListBox = QListWidget() # 목록화 기능
        self.midLayout.addWidget(self.todoListBox)

    def initBottomUI(self):
        self.bottomLayout = QHBoxLayout()
        # 할일 삭제 버튼 위젯 생성
        self.deleteButton = QPushButton(text="삭제")
        # 삭제 버튼 동작 메서드 연결
        self.deleteButton\
            .clicked\
            .connect(self.deleteTask)
        
        # 삭제 버튼 추가
        self.bottomLayout.addWidget(self.deleteButton)

    # 추가 버튼을 눌렀을 때 동작할 기능
    def addTask(self):
        # 할일을 추가했을 때, input 박스가 지워질지 여부를 검사
        self.rememberInput = self.rememberBox.isChecked()

        # 추가할 할일 내용을 담을 변수
        task = self.todoListInput.text() # 할일을 입력한 박스에 작성된 텍스트
        if task.strip(): # 공백문자를 제거했을 때 비어있지 않으면 진입
            # 할일 목록을 보여주는 리스트
            self.todoListBox.addItem(task)
        if self.rememberInput is False: # 기억여부가 False이면
            self.todoListInput.clear() # 입력칸의 내용을 제거

    # 삭제 버튼을 눌렀을 때 동작할 기능
    def deleteTask(self):
        # 선택한 행이 없을 경우, 삭제하지 않음
        # 선택한 행을 가져와서 그 개수를 확인
        if self.todoListBox.selectedItems():
            if (currentRow := self.todoListBox.currentRow()) >= 0:
                self.todoListBox.takeItem(currentRow)

if __name__ == "__main__":
    qapp = QApplication(sys.argv) # 프로그램이 실행될 플랫폼
    ex = TodoList() # 실행하려는 프로그램
    # 프로그램이 종료되면 플랫폼, 어플리케이션을 종료해야 한다.
    sys.exit(qapp.exec_())
