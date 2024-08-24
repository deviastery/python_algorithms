# алгоритм Левита
import collections

import sys
from PyQt5.QtWidgets import *
import networkx as nx
import matplotlib.pyplot as plt

def read_matrix(name):
    matrix = []
    file = open("graph_files/"+name+".txt", "r", encoding="utf-8")
    for lines in file:
        row = lines.split()
        matrix.append(row)
    file.close()
    return matrix

def filling_graph_from_matrices(graph, incidenceMatrix, adjacencyMatrix):
    for j in range(len(incidenceMatrix[0])): # j - столбец / ребро
        start_index = -1
        end_index = -1
        
        for i in range(len(incidenceMatrix)): # i = строка / вершина
            if incidenceMatrix[i][j] == "1":
                start_index = i

            if incidenceMatrix[i][j] == "-1":
                end_index = i

            if not start_index == -1 and not end_index == -1:
                break
            
        graph.add_edge(start_index, end_index, int(adjacencyMatrix[start_index][end_index]))


def levit(gr, start, end):
    # вершины, расстояние до которых и сосдей которых посчитали
    m0 = []

    # вершины, расстояние до соседей которых надо рассчитать
    m1 = collections.deque()
    
    # вершины, до которых мы ещё не знаем, как добраться
    m2 = [x for x in range(gr.V)]
    m1.append(m2.pop(start))
    # массив расстояний до вершины
    dist = [float('inf') for _ in range(gr.V)]
    dist[start] = 0

    # родительские вершины
    pred = [-1 for _ in range(gr.V)]
    pred[start] = None

    while m1: 
        current = m1.popleft()
        for u, v, w in gr.graph:
            if u == current:
                # мы не находили путь к этой вершине раньше
                if v in m2:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    m2.remove(v)
                    m1.append(v)
                    
                # мы уже знаем какой-то путь к ней, но не от неё
                elif v in m1:
                    # нашли более короткий путь
                    if dist[v] >= dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                
                # мы уже посчитали путь от вершины v к её соседям
                elif v in m0:
                    # нашли более короткий путь до вершины v
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        m0.remove(v)
                        # отправили вершину на перерасчёт всех путей к её соседям
                        m1.appendleft(v)

        # расчёт путей до соседей окончен
        m0.append(current)
    
    if dist[end] == float('inf'):
        return

     # Сбор вершин кратчайшего пути
    path_vertices = []
    current_vertex = end
    while current_vertex is not None:
        path_vertices.append(current_vertex)
        current_vertex = pred[current_vertex]

    path_vertices.reverse()

    res = [
            dist[end],
            path_vertices
        ]
    
    return res

class Graph:
    def __init__(self, vertices:int) -> None:
        self.V = vertices
        self.graph = []

    def add_edge(self, u:int, v:int, w:int) -> None:
        self.graph.append([u, v, w])


adjacencyMatrix = read_matrix('adjacency_matrix')
incidenceMatrix = read_matrix('incidence_matrix')

graph = Graph(len(adjacencyMatrix))

        
filling_graph_from_matrices(graph, incidenceMatrix, adjacencyMatrix)

class GraphVisualizationApp(QWidget):
    def __init__(self, graph):
        super().__init__()
        self.graph = graph
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Графический интерфейс для визуализации графа')
        self.setGeometry(550, 250, 800, 600)

        label0 = QLabel(f'Допустимые значения от 0 до {len(adjacencyMatrix)-1}', self)
        label0.move(280, 160)

        label1 = QLabel('Введите первую вершину:', self)
        label1.move(220, 200)
        self.vertex1_input = QLineEdit(self)
        self.vertex1_input.move(380, 198)

        label2 = QLabel('Введите вторую вершину:', self)
        label2.move(220, 240)
        self.vertex2_input = QLineEdit(self)
        self.vertex2_input.move(380, 238)

        button = QPushButton('Найти кратчайшее расстояние', self)
        button.move(285, 280)
        button.clicked.connect(self.find_shortest_distance)

        self.show()

    def find_shortest_distance(self):
        vertex1 = int(self.vertex1_input.text())
        vertex2 = int(self.vertex2_input.text())

        isOk = 0

        try:
            [shortest_distance, list_vertices] = levit(self.graph, vertex1, vertex2)
            isOk = 1
        except TypeError:
            pass 

        self.hide()

        G = nx.DiGraph(directed=True)
        
        for i in range(len(adjacencyMatrix)) :
            G.add_node(i)

        for i in graph.graph:
            G.add_edge(i[0], i[1] )
      

        if isOk:
            distance_label = f"Кратчайшее расстояние от {vertex1} до {vertex2} равно {shortest_distance}"
        else:
            distance_label = "Нет пути"
        plt.text(0.5, -0.1, distance_label, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12)

        # установить макет узлов
        pos = nx.circular_layout(G)

        if isOk:
            edges = []

            # создаем массив активных ребер
            for i in range(len(list_vertices) - 1):
                edge = (list_vertices[i], list_vertices[i + 1])
                edges.append(edge)


            # установка цвета активных ребер
            edge_colors = ['gray' for _ in G.edges()] 
            edges_to_green = edges  
            for edge in edges_to_green:
                edge_index = list(G.edges()).index(edge)
                edge_colors[edge_index] = 'green' 
        else:
            edge_colors='gray'

        # отрисовка графа
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='orange', font_size=10, font_weight='bold', width=2, edge_cmap=plt.cm.Blues, arrowsize=20, edge_color=edge_colors)

        # отрисовка надписей ребер

        edjes = {}

        for i in range(len(graph.graph)):
            edjes[graph.graph[i][0], graph.graph[i][1]] = f'№{i}; w: {graph.graph[i][2]}'

        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=edjes,
            font_color='red'
        )

        plt.show()

app = QApplication(sys.argv)
ex = GraphVisualizationApp(graph)

sys.stdout.reconfigure(encoding='utf-8')

print('_____________________________________________________________')
print('|                       |                   |                |',)
print('|     Критерий          |  Алгоритм Левита  |    Пояснение   |',)
print('______________________________________________________________')
print('|                       |                   |                |')
print('|  Временная сложность  |     O(V*E)        |  V - вершины   |')
print('|                       |                   |  E - ребра     |')
print('_____________________________________________________________')

sys.exit(app.exec_())



