# part2_pickling.py
# 피클링이란, 파이썬의 변수, 함수, 객체 등을 바이너리 파일 형태로
# 만들어서 다른 개발자에게 그 파이썬 객체째로 전달하기 위한
# 기술을 가리킨다.
# 주의점1. 파이썬 버전이 다르면 서로 읽거나 쓰기가 불가능할 수 있다.
# 주의점2. 외부에서 피클링 파일을 받아올 경우, 바이러스나
# 악성코드가 포함되어 있을 수 있다. -> 보안에 취약하다.
# import pickle
# 위 코드를 통해서 피클 라이브러리를 임포트하여 사용할 수 있다.
# 피클 라이브러리는 기본 내장 라이브러리로 install이 필요없다.
import pickle

def write_pickle(file_name, content):
    # 해당 파일을 바이너리 모드로 열기 위해서는
    # mode 부분에 b가 들어가야 한다.
    with open(file_name, 'wb') as file:
        pickle.dump(content, file)
    return file_name

def read_pickle(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
        return data

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age

if __name__ == "__main__":

    # file_name = 'test3.pkl'
    # # write_pickle(file_name, {'name': '홍길동', 'age': 30})
    # unpickled_data = read_pickle(file_name)
    # print(unpickled_data) # {'name': '홍길동', 'age': 30}
    # print(type(unpickled_data)) # class dict

    # 클래스를 이용한 실습
    file_name_by_hong = "hong.pkl"
    hong = Person('홍길동', 30)
    write_pickle(file_name_by_hong, hong)
    data = read_pickle(file_name_by_hong)
    print(data)
    print(data.name)