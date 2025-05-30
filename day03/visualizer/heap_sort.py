class HeapSort:
    def __init__(self, tuttle):
        self.bars = tuttle.bars
        self.tuttle = tuttle

    def sort(self):
        n = len(self.bars)
        # 힙을 구성
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # 하나씩 요소를 추출
        for i in range(n-1, 0, -1):
            self.bars[i], self.bars[0] = self.bars[0], self.bars[i]  # 현재 루트와 마지막 요소 교환
            self.heapify(i, 0)  # 힙을 재구성

    def heapify(self, n, i):
        largest = i  # 루트
        left = 2 * i + 1  # 왼쪽 자식
        right = 2 * i + 2  # 오른쪽 자식

        # 현재 비교 중인 막대기의 색상 변경
        self.bars[i].color("yellow")  # 현재 막대기 색상 변경
        self.bars[left].color("yellow")  # 최소 막대기 색상 변경
        self.bars[right].color("yellow")  # 최소 막대기 색상 변경

        # 왼쪽 자식이 루트보다 큰 경우
        if left < n and self.bars[left].size > self.bars[largest].size:
            largest = left
            self.tuttle.restore_colors(i, left)

        # 오른쪽 자식이 현재 가장 큰 값보다 큰 경우
        if right < n and self.bars[right].size > self.bars[largest].size:
            largest = right
            self.tuttle.restore_colors(i, right)

        # 가장 큰 값이 루트가 아닌 경우
        if largest != i:
            self.bars[i], self.bars[largest] = self.bars[largest], self.bars[i]  # 교환
            self.tuttle.restore_colors(i, largest)

            self.heapify(n, largest)  # 재귀적으로 힙을 구성 