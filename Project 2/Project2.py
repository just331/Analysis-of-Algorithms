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
    print(len(courses))
    courses_dict = {i: courses[i] for i in range(0, len(courses))}
    for j in courses_dict:
        print(str(j)+ ": " + courses_dict[j] + "\n")
    keys = list(courses_dict.keys())
    print(keys)
    g = Graph(29)
    g.add(0, 3)
    g.add(0, 8)
    g.add(1, 4)
    g.add(1, 5)
    g.add(1, 9)
    g.add(2, 6)
    g.add(2, 17)
    g.add(3, 7)
    g.add(3, 12)
    g.add(4, 10)
    g.add(4, 16)
    g.add(5, 11)
    g.add(6, 17)
    g.add(7, 13)
    g.add(7, 18)
    g.add(7, 19)
    g.add(7, 22)
    g.add(8, 19)
    g.add(8, 24)
    g.add(9, 12)
    g.add(10, 20)
    g.add(12, 23)
    g.add(13, 22)
    g.add(14, None)
    g.add(15, None)
    g.add(16, 19)
    g.add(19, 26)
    g.add(19, 27)
    g.add(20, 22)
    g.add(21, None)
    g.add(22, 25)
    g.add(23, 26)
    g.add(25, 28)
    print("Following is a Topological Sort of the given graph")
  #  g.topologicalSort_DFS()


if __name__ == "__main__":
    main()
