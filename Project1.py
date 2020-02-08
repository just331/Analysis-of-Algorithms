# Justin Rodriguez
# CS 5381 Analysis of Algorithms
# Project 1


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


# Need to do merge sort on arrays with inversion count
# Sort

# " " quick sort " "

# " " algorithm of choice " "

def main():
    s1 = [line.strip() for line in open("source1.txt", "r")]
    s1 = [int(i) for i in s1]
    s2 = [line.strip() for line in open("source2.txt", "r")]
    s2 = [int(i) for i in s2]
    s3 = [line.strip() for line in open("source3.txt", "r")]
    s3 = [int(i) for i in s3]
    s4 = [line.strip() for line in open("source4.txt", "r")]
    s4 = [int(i) for i in s4]
    s5 = [line.strip() for line in open("source5.txt", "r")]
    s5 = [int(i) for i in s5]
    print("The combined rank of each web page is: ", combineRank(s1, s2, s3, s4, s5))

    page = []
    for x in range(10000):
        page.append("Page {}".format(x))
    # create list that contains the combined rank list as well as the corresponding page
    c1 = list(zip(page, s1))
    c2 = list(zip(page, s2))
    c3 = list(zip(page, s3))
    c4 = list(zip(page, s4))
    c5 = list(zip(page, s5))


main()
