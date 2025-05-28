# part2_dfs_pratice.py
# dfs를 구현한 코드를 import 하여 여러 그래프에 적용하여
# 그 성질을 학습해보자.
from part1_dfs import (
    dfs_iterative as iter, 
    dfs_recursive as recur,
)

if __name__ == "__main__":
    data = {
        'A' : ['C', 'D'],
        'B' : ['D'],
        'C' : ['A', 'F'],
        'D' : ['A', 'B', 'E', 'G'],
        'E' : ['D', 'H', 'J'],
        'F' : ['C', 'G', 'I'],
        'G' : ['D', 'F', 'H'],
        'H' : ['E', 'G'],
        'I' : ['F', 'J'],
        'J' : ['E', 'I']
    }
    # iter(data, 'A') # A D G H E J I F C B
    # recur(data, 'A') # A C F G D B E H J I
    recur(data, 'F') # F C A D B E H G J I
