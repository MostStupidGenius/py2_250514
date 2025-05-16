# part3_regular_expression.py
# 정규 표현식
# 정규표현식이란, 대부분의 프로그래밍 언어가 지원하는 특별한 문법으로
# 문자열을 다루는 중요한 방법 중 하나이다.
# 특정 패턴을 가진 문자열을 찾거나, 대체하거나, 제거하는 등
# 단순히 정확히 일치하는 문자열뿐만 아니라 여러 조건을 부여하여
# 복잡한 패턴의 문자열을 검색, 변경, 제거 등을 수행할 수 있다.
# 혹은 그러한 패턴의 문자열인지 여부를 검사하는
# 유효성 검사에도 사용된다.

# 정규표현식을 사용하려면
# import re를 해주어야 하며
# 기본적으로 제공되는 라이브러리이기 때문에 따로 설치할 필요가 없다.
import re


def find_substring(text: str, r_pattern):
    # 전달된 text의 문자열 중 pattern에 부합하는
    # 문자열이 있는지 여부를 반환하는 함수

    # 전달된 r-string을 정규표현식으로 컴파일하여 패턴화
    pattern = re.compile(r_pattern)
    # 해당 패턴에 전달받은 문자열을 전달하여
    # 해당되는 부분 문자열을 추출한다.
    matches = pattern.findall(text)
    # 그러한 부분 문자열의 길이가 0보다 크면 발견한 것이므로
    # true를 반환한다.
    return len(matches) > 0

if __name__ == "__main__":
    result = find_substring("Hello, World", r"[h]")
    print(result)

