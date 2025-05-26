# part6_sort_insertion.py
# 삽입 정렬
# 정렬이 된 부분과 정렬되지 않은 부분으로 나뉘어
# 정렬된 부분의 값을 순서대로 비교하여 현재 삽입하려는 값을
# 정렬된 부분 중 적절한 위치까지 이동하는 방식으로 동작한다.

def insertion_sort(arr: list):
    # 삽입 정렬
    n = len(arr)
    # 반복문
    for i in range(1, n): # 0번째 요소는 이미 정렬된 부분으로 취급
        # 현재 삽입하려는 숫자
        key = arr[i]
        # 현재 숫자의 이전 위치
        j = i - 1
        # 정렬된 부분에서 현재 숫자보다 큰 숫자들을
        # 오른쪽으로 이동
        # j가 0보다 크거나 같고
        # j번째 요소가 정렬하려는 값보다 클 때 동작
        while j >= 0 and key < arr[j]:
            # j번째 요소의 값을 j+1번째 요소 값으로 설정
            arr[j+1] = arr[j]
            j -= 1 # 검사하는 순서값을 1 줄인다.
        # 위의 반복문이 끝났다는 것은
        # 삽입하려는 값이 적절한 위치에 도달했다는 의미이므로
        # 값을 변경해준다.
        arr[j+1] = key
        # print(arr)
    # 정렬된 리스트를 반환
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted = insertion_sort(arr)
    print("삽입 정렬 결과: ", sorted)