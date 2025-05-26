# part2_sort_merge.py
# 병합 정렬
# 퀵 정렬과 마찬가지로 분할정복 알고리즘을 사용하여 정렬한다.
# 동작 방식: 1. 전체 리스트를 반으로 나눈다.
# 2. 각 부분 리스트를 재귀적으로 정렬한다.
# 3. 정렬된 부분 리스트들을 병합하여 전체 리스트를 정렬한다.

# 재귀적으로 실행되는 병합 정렬 함수
def merge_sort(data: list)-> list:
    # 길이
    length = len(data)
    
    # 기본케이스: 리스트의 길이가 1 이하면 그대로 반환
    if length <= 1: return data

    # 리스트를 두 부분으로 나눔
    mid = length // 2
    left = merge_sort(data[:mid]) # 0번째부터 mid-1번째 요소까지
    right = merge_sort(data[mid:]) # mid번째부터 끝요소까지

    # 정렬된 부분 리스트를 병합 및 정렬 후 반환
    merged = merge(left, right)
    return merged

# 두 개의 리스트를 전달 받아서 정렬을 하는 함수
def merge(left: list, right: list)-> list:
    # 반환할 결과 리스트 생성
    result = []
    # 좌우 리스트의 인덱스를 관리할 변수 선언
    i, j = 0, 0

    # 두 리스트의 요소를 비교하며 작은 값을 result에 순서대로 추가
    # - 추가한 뒤 해당 리스트의 인덱스를 1씩 증가
    # - 인덱스의 크기가 해당 리스트의 길이와 같아지면 반복문 탈출
    while i < len(left) and j < len(right):
        # 왼쪽리스트의 i번째 요소와 오른쪽리스트의 j번째 요소를 비교
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] == right[j]:
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1
        else:
            result.append(right[j])
            j += 1
    
    # 반복문을 끝낸 뒤, 왼쪽, 오른쪽에 남은 요소들을
    # result의 뒤쪽에(큰값) 그대로 갖다 붙인다.
    result.extend(left[i:]) # 마지막으로 넣지 않은 요소부터 마지막 요소까지
    result.extend(right[j:]) # 혹시 에러가 날지도 모름

    # 병합된 결과 리스트를 반환
    return result


if __name__ == "__main__":
    import random

    # 예시 데이터 준비
    # data = [3, 6, 8, 9, 1, 2, 1]
    # 랜덤 데이터 만들기
    data = [random.randrange(1, 100, 1) for i in range(100)]
    print(data)
    # 퀵 정렬 진행
    sorted = merge_sort(data)
    # 정렬된 데이터 확인
    print(sorted) # 1, 1, 2, 3, 6, 8