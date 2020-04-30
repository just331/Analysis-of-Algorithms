# Justin Rodriguez
# 4/25/30
# CS 5381
# Project 3


class Graph:
    def __init__(self, nodes):
        self.N = nodes
        self.graph = []

    def addNode(self, u, v, w):
        self.graph.append([u, v, w])

    def printSol(self, dist):
        print("Node Distance from Source Node")
        for i in range(self.N):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, source):
        dist = [float("Inf")] * self.N
        dist[source] = 0

        for _ in range(self.N - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.printSol(dist)


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

    g2 = Graph(19)
    g2.addNode(0, 2, 150)
    g2.addNode(0, 4, 30)
    g2.addNode(0, 5, 80)
    g2.addNode(0, 6, 40)
    g2.addNode(1, 2, 200)
    g2.addNode(1, 3, 300)
    g2.addNode(2, 3, 250)
    g2.addNode(3, 4, 100)
    g2.addNode(3, 7, 120)
    g2.addNode(3, 4, 100)
    g2.addNode(4, 6, 80)
    g2.addNode(4, 7, 300)
    g2.addNode(4, 11, 200)
    g2.addNode(5, 6, 30)
    g2.addNode(5, 9, 100)
    g2.addNode(6, 8, 30)
    g2.addNode(7, 11, 150)
    g2.addNode(7, 14, 100)
    g2.addNode(7, 15, 150)
    g2.addNode(7, 16, 160)
    g2.addNode(8, 9, 200)
    g2.addNode(8, 10, 90)
    g2.addNode(8, 11, 100)
    g2.addNode(9, 10, 50)
    g2.addNode(9, 13, 100)
    g2.addNode(10, 11, 180)
    g2.addNode(10, 12, 80)
    g2.addNode(3, 4, 100)
    g2.addNode(11, 12, 100)
    g2.addNode(11, 14, 50)
    g2.addNode(12, 13, 50)
    g2.addNode(12, 14, 100)
    g2.addNode(12, 15, 110)
    g2.addNode(13, 17, 200)
    g2.addNode(14, 15, 50)
    g2.addNode(15, 16, 30)
    g2.addNode(15, 17, 20)
    g2.addNode(16, 17, 40)
    g2.addNode(17, 18, 350)

    print("~" * 100)
    print("Dijakstra's Algorithm on graph:")
    g.dijkstra(graph, 0)
    print("\n")
    print("~" * 100)
    print("\n")
    print("~" * 100)
    print("Bellman-Ford Algorithm on graph:")
    g2.BellmanFord(0)
    print("\n")
    print("~" * 100)


if __name__ == '__main__':
    main()
