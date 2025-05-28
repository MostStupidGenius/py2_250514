# part4_import_sort.py
# 지금까지 작성한 기본 정렬 알고리즘 3개
# 고급 정렬 알고리즘 3개를 import하여
# 그 정렬 시간을 직접 측정해보자.

# 다른 폴더에 존재하는 파일 임포트하기
# 기본 알고리즘 파일은 day03폴더에 있다.
import os
import sys
# 작업 폴더 경로 추출
file_path = os.path.abspath(__file__)
parent_folder = os.path.dirname(file_path) # day05 폴더 경로
root_folder = os.path.dirname(parent_folder) # workspace 폴더 경로

# 작업 폴더를 시스템에 환경 변수로 등록
sys.path.append(root_folder)
# 이제 day01, day02 등 하위 폴더에 접근이 가능하다.
from day03.part4_sort_select import selection_sort
from day03.part5_sort_bubble import bubble_sort
from day03.part6_sort_insertion import insertion_sort

from day05.part1_sort_quick import quick_sort
from day05.part2_sort_merge import merge_sort
from day05.part3_sort_heap import heap_sort

import random # 난수 생성
import time # 시간 측정

# 테스트용 난수(random) 리스트 생성 함수
def generate_random_list(size: int, min_val: int=0, max_val:int=10000):
    """ # docstring
    테스트용 난수 리스트를 생성하는 함수
    - size : 생성될 리스트의 난수 개수를 정한다.
    - min_val : 난수의 최소값 설정(기본값 0)
    - max_val : 난수의 최대값 설정(기본값 10000)
    """
    # random의 randint를 이용하여 정수형 난수 리스트를 생성
    result = [random.randint(min_val, max_val) for _ in range(size)]
    # 난수 리스트 반환
    return result

# 실행 시간 측정 함수
# 실행 시간을 측정할 함수와 정렬할 데이터를 전달
def measure_time(sort_func, data: list):
    # 반환값은 실행에 걸린 시간(초 단위)

    # 원본 데이터를 복제하여 복제본으로 정렬 시행
    copied = data.copy() # shallow copy 얕은 복사
    # 얕은 복사란, 데이터만 복사해가는 것을 가리킨다.
    # 깊은 복사란, 객체, 대상에 접근할 수 있는 권한을 부여하는 것을 가리킨다
    # -> 주소값으로의 접근
    # 원본을 직접 조작하는 것이 아니라 그 값을 그대로 가져온 복제본을
    # 다루는 것이므로 원본 데이터를 보존할 수 있다.
    # 시작시간 측정
    start_time = time.perf_counter()
    sort_func(copied) # 정렬 시행
    # 종료시간 측정
    end_time = time.perf_counter()

    # 종료시간 - 시작시간(초 단위) 반환
    return end_time - start_time

# 선택한 알고리즘 함수와 데이터, 해당 함수를 실행할 횟수를 전달하여
# 정렬을 하는 데 걸리는 평균 소요 시간을 반환하는 함수
def avg_time(sort_func, times:int=10, size: int=100) -> float:
    # 각 반복마다 소요된 시간을 저장할 리스트 생성
    time_list: list = []

    # times 횟수만큼 반복
    for _ in range(times):
        # 매 반복마다 같은 사이즈의 새로운 난수 리스트를 data에 저장
        data = generate_random_list(size, 1, 1000)
        # data를 해당 정렬 함수에 전달하여 정렬 시간 측정
        # 측정 시간을 time_list에 추가
        time_list.append(measure_time(sort_func, data))
    
    # time_list의 평균값을 반환
    return sum(time_list) / len(time_list)

if __name__ == "__main__":
    selectrion_time = avg_time(selection_sort, times=50, size=5000)
    print(f"선택정렬 완료 {selectrion_time:.3f}")
    bubble_time     = avg_time(bubble_sort, times=50, size=5000)
    print(f"버블정렬 완료 {bubble_time:.3f}")
    insertion_time  = avg_time(insertion_sort, times=50, size=5000)
    print(f"삽입정렬 완료 {insertion_time:.3f}")
    quick_time      = avg_time(quick_sort, times=100, size=10000)
    print(f"퀵정렬 완료 {quick_time:.3f}")
    merge_time      = avg_time(merge_sort, times=100, size=10000)
    print(f"병합정렬 완료 {e:.3f}")
    heap_time       = avg_time(heap_sort, times=100, size=10000)
    print(f"힙 정렬 완료 {heap_time:.3f}")