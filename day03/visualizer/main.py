import tkinter as tk
from turtle import TurtleScreen, RawTurtle
import random
from tkinter import messagebox  # 메시지 박스를 사용하기 위해 추가
# from heap_sort import HeapSort  # 힙 정렬을 위한 클래스 임포트

# 프로그램을 만들면서 위치 수정을 쉽게 하기 위해서 기준 위치 등을 상수로 선언
BASE_X = -234
BASE_Y = -210
OFFSET_X = 2
CANVAS_WIDTH = 500  # 캔버스의 너비

# 여러 크기의 막대기를 그릴 막대기 클래스
class Bar(RawTurtle):
    def __init__(self, _canvas, _size, _bar_width, height_increase):
        super().__init__(_canvas)
        self.size = _size
        self.height_increase = height_increase
        self.penup()
        self.shape("square")
        self.turtlesize(1 + self.height_increase * _size, 0.4)  # 막대의 너비를 이전 상태로 설정하고 높이를 0.4로 설정
        self.set_color()

    def set_color(self):
        # 크기에 따라 색상 설정 (예: 크기가 클수록 빨간색, 작을수록 파란색)
        color_value = self.size / 39  # 0에서 1 사이의 값으로 변환
        self.color(color_value, 0, 1 - color_value)  # RGB 색상 설정 (0~1 범위)

    def set_position(self, position):
        # y좌표를 조정하여 막대의 높이 차이를 설정
        self.goto(BASE_X + (OFFSET_X + 10) * position, BASE_Y + (self.height_increase * 10) * self.size)  # 높이 차이를 설정

def quick_sort(arr):
    # 배열의 길이가 1 이하이면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) <= 1:
        return arr
    # 피벗을 배열의 중간 값으로 선택
    pivot = arr[len(arr) // 2]
    # 피벗보다 작은 값들로 이루어진 리스트
    left = [x for x in arr if x < pivot]
    # 피벗과 같은 값들로 이루어진 리스트
    middle = [x for x in arr if x == pivot]
    # 피벗보다 큰 값들로 이루어진 리스트
    right = [x for x in arr if x > pivot]
    # 재귀적으로 정렬하여 합친 결과 반환
    return quick_sort(left) + middle + quick_sort(right)

# 시각화 프로그램을 위한 클래스
class Visualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("정렬 알고리즘 시각화")
        self.canvas = tk.Canvas(self.root, width=CANVAS_WIDTH, height=500)
        self.canvas.pack()
        self.screen = TurtleScreen(self.canvas)
        self.bars = []
        self.shuffled = False  # 초기 상태를 False로 설정

        # 막대 개수를 입력할 수 있는 필드 추가
        self.num_bars_var = tk.IntVar(value=10)  # 기본값 설정
        tk.Label(self.root, text="막대 개수 (최대 40):").pack()
        tk.Entry(self.root, textvariable=self.num_bars_var).pack()

        # 높이 증가 값을 조정할 수 있는 슬라이더 추가
        self.height_increase_var = tk.DoubleVar(value=0.4)  # 기본값 설정
        tk.Label(self.root, text="막대 높이 증가 값:").pack()
        height_slider = tk.Scale(self.root, variable=self.height_increase_var, from_=0.1, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
        height_slider.pack()

        # 생성 버튼 추가
        self.create_bars_button = tk.Button(self.root, text="막대 생성", command=self.create_bars)
        self.create_bars_button.pack(pady=10)  # 버튼에 여백 추가

        # 정렬 알고리즘 선택을 위한 라디오 버튼 추가
        self.algorithm_var = tk.StringVar(value="bubble")  # 기본값 설정
        self.create_radio_buttons()

        # 섞기 버튼 추가
        self.create_shuffle_button()

        # 정렬 시작 버튼 추가
        self.create_sort_button()

    def create_bars(self):
        # 이전 막대 삭제
        for bar in self.bars:
            bar.hideturtle()  # 막대를 숨김
        self.bars.clear()  # 막대 리스트 초기화

        num_bars = self.num_bars_var.get()  # 입력된 막대 개수 가져오기

        # 막대 개수 제한 및 예외 처리
        if num_bars < 1 or num_bars > 40:
            messagebox.showwarning("경고", "막대 개수는 1에서 40 사이여야 합니다.")
            return

        bar_width = CANVAS_WIDTH / (num_bars + 1)  # 막대의 너비 계산
        height_increase = self.height_increase_var.get()  # 슬라이더에서 높이 증가 값 가져오기
        self.bars = [Bar(self.screen, i, bar_width, height_increase) for i in range(num_bars)]  # 리스트 컴프리헨션 사용
        for i, bar in enumerate(self.bars):
            bar.set_position(i)  # 정렬된 상태로 위치 설정

    def shuffle_bars(self):
        random.shuffle(self.bars)
        for i, bar in enumerate(self.bars):
            bar.set_position(i)

    def sort_bars(self):
        algorithm = self.algorithm_var.get()
        if algorithm == "bubble":
            self.bubble_sort()
        if algorithm == "insertion":
            self.insertion_sort()
        elif algorithm == "selection":
            self.selection_sort()
        elif algorithm == "quick":
            self.quick_sort()
        elif algorithm == "merge":
            self.merge_sort()
        elif algorithm == "heap":
            self.heap_sort()
        # 다른 정렬 알고리즘 추가 가능

    def bubble_sort(self):
        n = len(self.bars)
        for i in range(n):
            for j in range(0, n-i-1):
                # 현재 비교 중인 막대기의 색상 변경
                self.bars[j].color("yellow")  # 현재 막대기 색상 변경
                self.bars[j+1].color("yellow")  # 다음 막대기 색상 변경

                if self.bars[j].size > self.bars[j+1].size:
                    # 막대기 위치 교환
                    self.bars[j], self.bars[j+1] = self.bars[j+1], self.bars[j]
                    self.update_bar_positions()
                    self.root.update()  # 화면 업데이트
                    self.root.after(30)  # 지연 시간 (속도 증가)

                # 색상 복원
                self.restore_colors(j, j+1)  # 원래 색상으로 복원

    def selection_sort(self):
        n = len(self.bars)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                # 현재 비교 중인 막대기의 색상 변경
                self.bars[j].color("yellow")  # 현재 막대기 색상 변경
                self.bars[min_idx].color("yellow")  # 최소 막대기 색상 변경

                if self.bars[j].size < self.bars[min_idx].size:
                    min_idx = j

                # 색상 복원
                self.restore_colors(j, min_idx)  # 원래 색상으로 복원

            # 막대기 위치 교환
            self.bars[i], self.bars[min_idx] = self.bars[min_idx], self.bars[i]
            self.update()
            # self.update_bar_positions()
            # self.root.update()  # 화면 업데이트
            # self.root.after(30)  # 지연 시간 (속도 증가)

    def quick_sort(self):
        # 막대의 size 값만 추출하여 리스트로 만듦
        sizes = [bar.size for bar in self.bars]
        # quick_sort 함수로 정렬
        sorted_sizes = quick_sort(sizes)
        # 정렬된 순서에 맞게 self.bars 재배치
        size_to_bar = {bar.size: [] for bar in self.bars}
        for bar in self.bars:
            size_to_bar[bar.size].append(bar)
        new_bars = []
        for size in sorted_sizes:
            new_bars.append(size_to_bar[size].pop(0))
        self.bars = new_bars
        self.update()
        # 색상 복원
        for bar in self.bars:
            bar.set_color()
    
    def insertion_sort(self):
        n = len(self.bars)
        for i in range(1, n):
            key_bar = self.bars[i]
            j = i - 1
            # 현재 막대기 강조
            key_bar.color("yellow")
            self.update(50)
            while j >= 0 and self.bars[j].size > key_bar.size:
                self.bars[j + 1] = self.bars[j]
                self.update_bar_positions()
                self.root.update()
                self.root.after(30)
                j -= 1
            self.bars[j + 1] = key_bar
            self.update_bar_positions()
            self.root.update()
            self.root.after(30)
            # 색상 복원
            key_bar.set_color()
        for bar in self.bars:
            bar.set_color()
    def merge_sort(self):
        def merge_sort_recursive(bars):
            if len(bars) <= 1:
                return bars
            mid = len(bars) // 2
            left = merge_sort_recursive(bars[:mid])
            right = merge_sort_recursive(bars[mid:])
            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                # 시각화: 비교 중인 막대 색상 변경
                left[i].color("yellow")
                right[j].color("yellow")
                self.update(50)
                if left[i].size <= right[j].size:
                    merged.append(left[i])
                    left[i].set_color()
                    right[j].set_color()
                    i += 1
                else:
                    merged.append(right[j])
                    left[i].set_color()
                    right[j].set_color()
                    j += 1
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            # 병합된 막대 위치 갱신
            for idx, bar in enumerate(merged):
                bar.set_position(idx)
            self.root.update()
            self.root.after(50)
            return merged

        self.bars = merge_sort_recursive(self.bars)
        self.update()
        for bar in self.bars:
            bar.set_color()

    def heap_sort(self):
        n = len(self.bars)

        # Build max heap
        # Bottom-up heap construction
        for i in range(n // 2 - 1, -1, -1):
            largest = i
            while True:
                l = 2 * largest + 1
                r = 2 * largest + 2
                new_largest = largest

                if l < n and self.bars[l].size > self.bars[new_largest].size:
                    new_largest = l
                if r < n and self.bars[r].size > self.bars[new_largest].size:
                    new_largest = r

                if new_largest == largest:
                    break

                self.bars[largest], self.bars[new_largest] = self.bars[new_largest], self.bars[largest]
                self.update()
                largest = new_largest

        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            # Swap
            self.bars[0], self.bars[i] = self.bars[i], self.bars[0]
            self.update()
            self._heapify(i, 0)

        # 색상 복원
        for bar in self.bars:
            bar.set_color()

    def _heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.bars[l].size > self.bars[largest].size:
            largest = l
        if r < n and self.bars[r].size > self.bars[largest].size:
            largest = r

        if largest != i:
            # Swap
            self.bars[i], self.bars[largest] = self.bars[largest], self.bars[i]
            self.update()
            self._heapify(n, largest)

    def update(self, delay:int = 30):
        self.update_bar_positions()
        self.root.update()  # 화면 업데이트
        self.root.after(delay)  # 지연 시간 (속도 증가)

    def restore_colors(self, index1, index2):
        # 색상 복원
        self.bars[index1].set_color()  # 원래 색상으로 복원
        self.bars[index2].set_color()  # 원래 색상으로 복원

    def create_radio_buttons(self):
        tk.Label(self.root, text="정렬 알고리즘 선택:").pack()
        tk.Radiobutton(self.root, text="삽입 정렬", variable=self.algorithm_var, value="insertion").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="버블 정렬", variable=self.algorithm_var, value="bubble").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="선택 정렬", variable=self.algorithm_var, value="selection").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="퀵 정렬", variable=self.algorithm_var, value="quick").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="병합 정렬", variable=self.algorithm_var, value="merge").pack(anchor=tk.W)
        tk.Radiobutton(self.root, text="힙 정렬", variable=self.algorithm_var, value="heap").pack(anchor=tk.W)

    def create_shuffle_button(self):
        shuffle_button = tk.Button(self.root, text="막대 섞기", command=self.shuffle_bars)
        shuffle_button.pack(pady=10)  # 버튼에 여백 추가

    def create_sort_button(self):
        sort_button = tk.Button(self.root, text="정렬 시작", command=self.sort_bars)
        sort_button.pack(pady=10)  # 버튼에 여백 추가

    def update_bar_positions(self):
        for i, bar in enumerate(self.bars):
            bar.set_position(i)

    def run(self):
        self.root.mainloop()

# 프로그램 실행
if __name__ == "__main__":
    visualizer = Visualizer()
    visualizer.run()
