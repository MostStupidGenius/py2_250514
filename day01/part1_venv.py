# part1_venv.py
# print("Hello Python")

# 파일 입출력 살짝 연습하기
def write_file(file_name, content):
    # file = open(file_name, 'w')
    # file.write(content)
    # file.close()
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    write_file('test2.txt', 'hello world')

