# Justin Rodriguez
# CS 5381 Analysis of Algorithms
# Project 1
from _ast import operator
def inversioncount(arr):
    count = 0
    n = len(arr)
    arr = [k[1] for k in arr]
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]> arr[j]:
                count += 1
        return  count

def combineRank(arr1, arr2, arr3, arr4, arr5):
    combarr = []
    for i in range(0, len(arr1)):
        combarr.append(
            arr1[i] + arr2[i] + arr3[i] + arr4[i] + arr5[i])  # Combines the ranks of each web page from every source

    page = []  # create list that contains the combined rank list as well as the corresponding page
    for x in range(10000):
        page.append("Page {}".format(x))
    combarr = list(zip(page, combarr))
    combarr.sort(key=lambda k: k[1])  # Sort the combined rank list
    return combarr


def formatlist(l1, l2):
    page = []
    for x in range(10000):
        page.append("Page {}".format(x))

    l1 = list(zip(page, l1))

    dic = {v: j for j, v in enumerate(l2)}
    return sorted(l1, key=lambda p: dic[p[0]])


# Need to do merge sort on arrays with inversion count
# Sort

# " " quick sort " "

# " " algorithm of choice " "

def main():
    s1 = [line.strip() for line in open("data/source1.txt", "r")]
    s1 = [int(i) for i in s1]
    s2 = [line.strip() for line in open("data/source2.txt", "r")]
    s2 = [int(i) for i in s2]
    s3 = [line.strip() for line in open("data/source3.txt", "r")]
    s3 = [int(i) for i in s3]
    s4 = [line.strip() for line in open("data/source4.txt", "r")]
    s4 = [int(i) for i in s4]
    s5 = [line.strip() for line in open("data/source5.txt", "r")]
    s5 = [int(i) for i in s5]

    cr = combineRank(s1, s2, s3, s4, s5)
    print("The combined rank of each web page is: ", cr)

    crp = [i[0] for i in cr]

    c1 = formatlist(s1, crp)
    print(c1)
    print("Number of inversion in Source 1 are: ", inversioncount(c1))
    c2 = formatlist(s2, crp)
    c3 = formatlist(s3, crp)
    c4 = formatlist(s4, crp)
    c5 = formatlist(s5, crp)

    # create list that contains the combined rank list as well as the corresponding page
    # c1 = list(zip(page, s1))


main()
