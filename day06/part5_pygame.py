# pip install pygame

import pygame
import random
import time

class SortingVisualizer:
    def __init__(self, width=800, height=600, array_size=50):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("정렬 알고리즘 시각화")
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        
        self.array_size = array_size
        self.array = [random.randint(10, self.HEIGHT - 10) 
                     for _ in range(self.array_size)]
        
        self.running = True
        self.sorting_started = False

    def draw_array(self, red_indices=[], green_indices=[]):
        self.screen.fill(self.WHITE)
        bar_width = self.WIDTH // len(self.array)
        for i, height in enumerate(self.array):
            if i in red_indices:
                color = self.RED
            elif i in green_indices:
                color = self.GREEN
            else:
                color = self.BLACK
            pygame.draw.rect(
                self.screen,
                color,
                (i * bar_width, self.HEIGHT - height, bar_width - 1, height)
            )
        pygame.display.flip()
        time.sleep(0.05)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.draw_array([j, j + 1])
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array([j, j + 1])

    def quick_sort(self, start, end):
        if start >= end:
            return

        pivot = self.array[end]
        i = start - 1

        for j in range(start, end):
            self.draw_array([end], [i + 1, j])
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.draw_array([end], [i, j])

        self.array[i + 1], self.array[end] = self.array[end], self.array[i + 1]
        pivot_pos = i + 1

        self.quick_sort(start, pivot_pos - 1)
        self.quick_sort(pivot_pos + 1, end)

    def merge_sort(self, start, end):
        if end <= start:
            return

        mid = (start + end) // 2
        self.merge_sort(start, mid)
        self.merge_sort(mid + 1, end)

        merged = []
        left = start
        right = mid + 1

        while left <= mid and right <= end:
            self.draw_array([left, right])
            if self.array[left] <= self.array[right]:
                merged.append(self.array[left])
                left += 1
            else:
                merged.append(self.array[right])
                right += 1

        while left <= mid:
            self.draw_array([left])
            merged.append(self.array[left])
            left += 1

        while right <= end:
            self.draw_array([right])
            merged.append(self.array[right])
            right += 1

        for i, sorted_val in enumerate(merged):
            self.array[start + i] = sorted_val
            self.draw_array([], [start + i])

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if not self.sorting_started:
                    self.sorting_started = True
                    if event.key == pygame.K_1:
                        self.bubble_sort()
                    elif event.key == pygame.K_2:
                        self.quick_sort(0, len(self.array) - 1)
                    elif event.key == pygame.K_3:
                        self.merge_sort(0, len(self.array) - 1)

    def run(self):
        while self.running:
            self.handle_events()
            if not self.sorting_started:
                self.draw_array()
        pygame.quit()

if __name__ == "__main__":
    visualizer = SortingVisualizer()
    print("1: 버블 정렬")
    print("2: 퀵 정렬")
    print("3: 병합 정렬")
    visualizer.run()