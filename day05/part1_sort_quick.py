# part1_sort_quick.py

# 퀵 정렬
# 퀵 정렬은 전체 데이터 중 하나를 골라서 이를 피벗(pivot)이라고
# 명명한다.
# 이 피벗을 기준으로 작은 값은 왼쪽으로, 큰 값은 오른쪽 정렬하여
# 이를 재귀적으로 반복한다.
# 더이상 좌우로 나눌 수 있는 값이 없을 때까지 반복한다.
# 반복을 멈추면 피벗을 포함한 모든 데이터를 정렬한 상태로 반환
# 이를 병합하여 최종 정렬데이터를 만들어낸다.
def quick_sort(data: list) -> list:
    # 전달된 데이터의 길이를 확인한다.
    length = len(data)
    if length <= 1: return data # 기본케이스
    # 길이가 1이면 재귀를 멈추고 값을 되돌려준다.

    # 피벗(pivot) 선택하기
    # 순서상 가운데에 있는 값을 선택한다.
    pivot = data[length // 2]

    # 피벗을 기준으로 리스트를 세 부분으로 분할한다.
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    # 분할된 리스트를 재귀적으로 정렬하고 병합
    # 리스트 자료구조는 덧셈연산을 하면 연산 순서에 따라
    # 하나의 리스트로 병합된다.
    result: list = quick_sort(left) + middle + quick_sort(right)
    return result

if __name__ == "__main__":
    # 예시 데이터 준비
    data = [3, 6, 8, 9, 1, 2, 1]
    # 퀵 정렬 진행
    sorted = quick_sort(data)
    # 정렬된 데이터 확인
    print(sorted) # 1, 1, 2, 3, 6, 8