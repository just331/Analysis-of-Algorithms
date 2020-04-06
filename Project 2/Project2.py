# Justin Rodriguez
# 3/31/20
# CS 5381
# Project 2

from collections import defaultdict as d


class Graph:
    def __init__(self, vert):
        self.graph = d(list)
        self.V = vert

    def add(self, u, v):
        self.graph[u].append(v)

    def explore(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.explore(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort_DFS(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.explore(i, visited, stack)

        print(stack)


def main():
    courses = ["CS 1411: Programming Principles I", "MATH 1451: Calculus I",
               "ENGL 1301: Essentials of College Rhetoric", "CS 1412: Programming Principles II",
               "MATH 1452: Calculus II", " PHYS 1408: Principles of Physics I", "ENGL 1302: Advanced College Rhetoric",
               "CS 2413 - Data Structures", "CS 1382 - Discrete Computational Structures",
               "ECE 2372: Modern Digital System Design", "MATH 2450: Calculus III",
               "PHYS 2401: Principles of Physics II",
               "CS 2350: Computer Organization and Assembly Language Programming",
               "CS 2365: Object-Oriented Programming", "ENGR 2392: Engineering Ethics and Its Impact on Society",
               "POLS 1301: American Government", "MATH 2360: Linear Algebra",
               "ENGL 2311: Introduction to Technical Writing", "CS 3361: Concepts of Programming Languages",
               "CS 3364: Design and Analysis of Algorithms",
               "MATH 3342: Mathematical Statistics for Engineers and Scientists",
               "POLS 2306: Texas Politics and Topics", "CS 3365: Software Engineering I",
               "CS 3375: Computer Architecture", "CS 3383: Theory of Automata", "CS 4365: Software Engineering II",
               "CS 4352: Operating Systems",
               "CS 4354: Concepts of Database Systems", "CS 4366: Senior Capstone Project"]
    courses_dict = {i: courses[i] for i in range(0, len(courses))}
    for j in courses_dict:
        print(str(j) + ": " + courses_dict[j] + "\n")
    keys = list(courses_dict.keys())
    g = Graph(29)
    g2 = Graph(3)
    g3 = Graph(6)
    g.add(0, 2)  # CS 1411 --> CS 1382
    g.add(0, 3)  # CS 1411 --> CS 1412
    g.add(1, 4)  # MATH 1451 --> MATH 1452
    g.add(1, 5)  # MATH 1451 --> PHYS 1408
    g.add(1, 8)  # MATH 1451 --> ECE 2372
    g.add(2, 16)  # CS 1382 --> CS 3364
    g.add(2, 17)  # CS 1382 --> CS 3383
    g.add(3, 6)  # CS 1412 --> CS 2413
    g.add(3, 11)  # CS 1411 --> CS 2350
    g.add(4, 7)  # MATH 1452 --> MATH 2450
    g.add(4, 12)  # MATH 1452 --> MATH 2360
    g.add(5, 9)  # PHYS 1408 --> PHYS 2401
    g.add(6, 10)  # CS 2413 --> CS 2365
    g.add(6, 13)  # CS 2413 --> CS 3361
    g.add(6, 15)  # CS 2413 --> CS 3365
    g.add(6, 16)  # CS 2413 --> CS 3364
    g.add(7, 14)  # MATH 2450 --> MATH 3342
    g.add(8, 11)  # ECE 2372 --> CS 2350
    g.add(10, 15)  # CS 2365 --> CS 3365
    g.add(11, 18)  # CS 2350 --> CS 3375
    g.add(12, 16)  # MATH 2360 --> CS 3364
    g.add(15, 21)  # CS 3365 --> CS CS 4365
    g.add(14, 15)  # MATH 3342 --> CS 3365
    g.add(16, 19)  # CS 3364 --> CS 4354
    g.add(16, 20)  # CS 3364 --> CS 4352
    g.add(18, 20)  # CS 3375 --> CS 4352
    g.add(21, 22)  # CS 4365 --> CS 4366
    g.add(23, 24)  # ENGL 1301 --> ENGL 1302
    g.add(23, 25)  # ENGL 1301 --> ENGL 2311
    g.add(24, 25)  # ENGL 1302 --> ENGL 2311

    ####################### TEST GRAPHS ##########################
    g2.add(0, 1)
    g2.add(0, 2)
    g2.add(1, 2)

    g3.add(5, 2)
    g3.add(5, 0)
    g3.add(4, 0)
    g3.add(4, 1)
    g3.add(2, 3)
    g3.add(3, 1)
    ####################### TEST GRAPHS ##########################
    print("The Topological Sort for the given graph is: ")
    g.topologicalSort_DFS()
    g2.topologicalSort_DFS()
    g3.topologicalSort_DFS()


if __name__ == "__main__":
    main()
