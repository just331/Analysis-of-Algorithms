# Justin Rodriguez
# 3/31/20
# CS 5381
# Project 2

from collections import defaultdict as d


class GraphADT:
    def __init__(self, node):
        self.graph = d(list)
        self.N = node

    def add(self, source, dest):
        self.graph[source].append(dest)

    def explore(self, node, visited, stack):
        visited[node] = True

        for i in self.graph[node]:
            if not visited[i]:
                self.explore(i, visited, stack)

        stack.insert(0, node)

    def topologicalSort_DFS(self):
        visited = [False] * self.N
        stack = []
        for i in range(self.N):
            if not visited[i]:
                self.explore(i, visited, stack)

        return stack


def returnOutput(l1, d1):  # Returns the topological sort in terms of course names
    ssort = [str(i) for i in l1]
    print("Topological Sort by course name:")
    new_order = sorted(d1.items(), key=lambda pair: ssort.index(pair[0]))
    val_new_order = [x[1] for x in new_order]
    print(val_new_order)


def main():
    courses = {"0": "CS 1411: Programming Principles I",  # 0
               "1": "MATH 1451: Calculus I",  # 1
               "2": "CS 1382 - Discrete Computational Structures",  # 2
               "3": "CS 1412: Programming Principles II",  # 3
               "4": "MATH 1452: Calculus II",  # 4
               "5": "PHYS 1408: Principles of Physics I",  # 5
               "6": "PHYS 2401: Principles of Physics II",  # 6
               "7": "CS 2413 - Data Structures",  # 7
               "8": "MATH 2450: Calculus III",  # 8
               "9": "ECE 2372: Modern Digital System Design",  # 9
               "10": "CS 2350: Computer Organization and Assembly Language Programming",  # 10
               "11": "CS 2365: Object-Oriented Programming",  # 11
               "12": "MATH 2360: Linear Algebra",  # 12
               "13": "CS 3361: Concepts of Programming Languages",  # 13
               "14": "MATH 3342: Mathematical Statistics for Engineers and Scientists",  # 14
               "15": "CS 3364: Design and Analysis of Algorithms",  # 15
               "16": "CS 3365: Software Engineering I",  # 16
               "17": "CS 3375: Computer Architecture",  # 17
               "18": "CS 3383: Theory of Automata",  # 18
               "19": "CS 4352: Operating Systems",  # 19
               "20": "CS 4354: Concepts of Database Systems",  # 20
               "21": "CS 4365: Software Engineering II",  # 21
               "22": "CS 4366: Senior Capstone Project",  # 22
               "23": "ENGL 1301: Essentials of College Rhetoric",  # 23
               "24": "ENGL 1302: Advanced College Rhetoric",  # 24
               "25": "ENGL 2311: Introduction to Technical Writing",  # 25
               "26": "ENGR 2392: Engineering Ethics and Its Impact on Society",  # 26
               "27": "POLS 1301: American Government",  # 27
               "28": "POLS 2306: Texas Politics and Topics"}  # 28
    g = GraphADT(29)
    g3 = GraphADT(6)
    g.add(0, 2)  # CS 1411 --> CS 1382
    g.add(0, 3)  # CS 1411 --> CS 1412
    g.add(1, 4)  # MATH 1451 --> MATH 1452
    g.add(1, 5)  # MATH 1451 --> PHYS 1408
    g.add(1, 9)  # MATH 1451 --> ECE 2372
    g.add(2, 15)  # CS 1382 --> CS 3364
    g.add(2, 18)  # CS 1382 --> CS 3383
    g.add(3, 7)  # CS 1412 --> CS 2413
    g.add(3, 10)  # CS 1412 --> CS 2350
    g.add(4, 8)  # MATH 1452 --> MATH 2450
    g.add(4, 12)  # MATH 1452 --> MATH 2360
    g.add(5, 6)  # PHYS 1408 --> PHYS 2401
    g.add(7, 11)  # CS 2413 --> CS 2365
    g.add(7, 13)  # CS 2413 --> CS 3361
    g.add(7, 15)  # CS 2413 --> CS 3364
    g.add(7, 16)  # CS 2413 --> CS 3365
    g.add(8, 14)  # MATH 2450 --> MATH 3342
    g.add(9, 10)  # ECE 2372 --> CS 2350
    g.add(10, 17)  # CS 2350 --> CS 3375
    g.add(11, 16)  # CS 2365 --> CS 3365
    g.add(12, 15)  # MATH 2360 --> CS 3364
    g.add(14, 16)  # MATH 3342 --> CS 3365
    g.add(15, 19)  # CS 3364 --> CS 4352
    g.add(15, 20)  # CS 3364 --> CS 4354
    g.add(16, 21)  # CS 3365 --> CS CS 4365
    g.add(17, 19)  # CS 3375 --> CS 4352
    g.add(21, 22)  # CS 4365 --> CS 4366
    g.add(23, 24)  # ENGL 1301 --> ENGL 1302
    g.add(23, 25)  # ENGL 1301 --> ENGL 2311
    g.add(24, 25)  # ENGL 1302 --> ENGL 2311

    ####################### TEST GRAPH ##########################
    g3.add(5, 2)
    g3.add(5, 0)
    g3.add(4, 0)
    g3.add(4, 1)
    g3.add(2, 3)
    g3.add(3, 1)
    ####################### TEST GRAPH ##########################

    print("The Topological Sort for the given graph by code: ")
    sort = g.topologicalSort_DFS()
    print(sort)
    print("\n")
    returnOutput(sort, courses)

    test2 = g3.topologicalSort_DFS()
    print("\nTEST OUTPUT: ")
    print(test2)


if __name__ == "__main__":
    main()
