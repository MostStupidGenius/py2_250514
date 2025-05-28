# part4_visual.py
# pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt

def visualize_binary_tree():
    # 이진 트리 시각화 예시
    G = nx.Graph()
    G.add_edges_from([(1,2), (1,3), (2,4), (2,5)])
    nx.draw(G, with_labels=True)
    plt.show()

# pip install graphviz
# dot 언어와 그 프로그램을 통해 그래프 시각화를 시행한다.
# dot 프로그램이 없으면 실행할 수 없다.
from graphviz import Digraph

def visualize_graphviz():
    # 방향성 그래프 시각화 예시
    dot = Digraph()
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.render('graph', view=True)

if __name__ == "__main__":
    # visualize_binary_tree()
    
    pass