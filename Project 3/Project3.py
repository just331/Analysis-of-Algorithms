# Justin Rodriguez
# 4/25/30
# CS 5381
# Project 3

from collections import defaultdict as d


class GraphADT:

    def minDistance(self, dist, queue):
        minimum = float("Inf")
        index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                index = i
        return index

    def printPath(self, root, j):
        if root[j] == -1:
            print(j, end=" "),
            return
        self.printPath(root, root[j])
        print(j, end=" "),

    def solution(self, dist, root):
        source = 0
        print("Vertex \t\tDistance from Source\t\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d  \t\t\t\t\t" % (source, i, dist[i]), end=" "),
            self.printPath(root, i)

    def dijkstra(self, graph, source):
        row = len(graph)
        col = len(graph[0])

        dist = [float("Inf")] * row

        parent = [-1] * row

        dist[source] = 0

        queue = []
        for i in range(row):
            queue.append(i)
        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        self.solution(dist, parent)


def main():
    g = GraphADT()
    graph = [[0, 0, 150, 0, 30, 80, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 200, 0, 0, 300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [150, 200, 0, 250, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 250, 0, 100, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [30, 0, 0, 100, 0, 0, 80, 300, 0, 0, 0, 200, 0, 0, 0, 0, 0, 0, 0],
             [80, 300, 0, 0, 0, 0, 30, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [40, 0, 0, 0, 80, 30, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 120, 300, 0, 0, 0, 0, 0, 0, 150, 0, 0, 100, 150, 160, 0, 0],
             [0, 0, 0, 0, 0, 0, 30, 0, 0, 200, 90, 100, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 100, 0, 0, 200, 0, 50, 0, 0, 100, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 90, 50, 0, 180, 80, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 200, 0, 0, 150, 100, 0, 180, 0, 100, 0, 50, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 100, 0, 50, 100, 110, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 50, 0, 0, 0, 0, 200, 0],
             [0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 50, 100, 0, 0, 50, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 150, 0, 0, 0, 0, 110, 0, 50, 0, 30, 20, 0],
             [0, 0, 0, 0, 0, 0, 0, 160, 0, 0, 0, 0, 0, 0, 0, 30, 0, 40, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 20, 40, 0, 350],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 350, 0]]

    graph1 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
              [4, 0, 8, 0, 0, 0, 0, 11, 0],
              [0, 8, 0, 7, 0, 4, 0, 0, 2],
              [0, 0, 7, 0, 9, 14, 0, 0, 0],
              [0, 0, 0, 9, 0, 10, 0, 0, 0],
              [0, 0, 4, 14, 10, 0, 2, 0, 0],
              [0, 0, 0, 0, 0, 2, 0, 1, 6],
              [8, 11, 0, 0, 0, 0, 1, 0, 7],
              [0, 0, 2, 0, 0, 0, 6, 7, 0]
              ]

    g.dijkstra(graph, 0)


if __name__ == '__main__':
    main()
