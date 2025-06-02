# 필요한 라이브러리 임포트
import sys
from PyQt5.QtWidgets import *  # PyQt5의 모든 위젯 임포트
from PyQt5.QtCore import Qt    # Qt 코어 기능 임포트

# TodoList 클래스 정의 - QMainWindow를 상속받음
class TodoList(QMainWindow):
    def __init__(self):
        super().__init__()     # 부모 클래스 초기화
        self.initUI()          # UI 초기화 메서드 호출
        
    def initUI(self):
        # 중앙 위젯 생성 및 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 수직 레이아웃 생성
        layout = QVBoxLayout(central_widget)
        
        # 입력 부분을 위한 수평 레이아웃 생성
        input_layout = QHBoxLayout()
        
        # 할 일 입력을 위한 텍스트 입력창 생성
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText('할 일을 입력하세요')  # 플레이스홀더 텍스트 설정
        
        # 추가 버튼 생성 및 클릭 이벤트 연결
        add_button = QPushButton('추가')
        add_button.clicked.connect(self.add_task)  # 버튼 클릭 시 add_task 메서드 실행
        
        # 입력창과 추가 버튼을 수평 레이아웃에 추가
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_button)
        
        # 할 일 목록을 표시할 리스트 위젯 생성
        self.task_list = QListWidget()
        
        # 삭제 버튼 생성 및 클릭 이벤트 연결
        delete_button = QPushButton('체크된 항목 삭제')
        delete_button.clicked.connect(self.delete_task)  # 버튼 클릭 시 delete_task 메서드 실행
        
        # 모든 요소를 메인 레이아웃에 추가
        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)
        layout.addWidget(delete_button)
        
        # 메인 윈도우 설정
        self.setWindowTitle('Todo List')           # 창 제목 설정
        self.setGeometry(300, 300, 400, 500)      # 창 위치와 크기 설정 (x, y, width, height)
        
    def add_task(self):
        # 입력창에서 텍스트 가져오기
        task = self.task_input.text()
        if task:  # 텍스트가 비어있지 않은 경우
            # 새로운 할 일 항목 생성
            item = QListWidgetItem(task)
            # 체크박스 기능 추가
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)  # 초기 상태는 체크 해제
            # 리스트에 항목 추가
            self.task_list.addItem(item)
            # 입력창 비우기
            self.task_input.clear()
            
    def delete_task(self):
        # 삭제할 항목들을 저장할 리스트
        items_to_remove = []
        # 모든 항목을 순회하면서 체크된 항목 찾기
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                items_to_remove.append(item)
        
        # 체크된 항목들 삭제
        for item in items_to_remove:
            self.task_list.takeItem(self.task_list.row(item))

# 메인 실행 부분
if __name__ == '__main__':
    app = QApplication(sys.argv)      # QApplication 인스턴스 생성
    todo_list = TodoList()           # TodoList 인스턴스 생성
    todo_list.show()                 # 윈도우 표시
    sys.exit(app.exec_())            # 이벤트 루프 시작