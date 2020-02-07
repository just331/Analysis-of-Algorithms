# Justin Rodriguez
# CS 5381 Analysis of Algorithms
# Project 1

# Need to get combined rank of each of each web page
def combineRank(arr1, arr2, arr3, arr4, arr5):
    combarr = []
    for i in range(0, len(arr1)):
        combarr.append(arr1[i] + arr2[i] + arr3[i] + arr4[i] + arr5[i])
    return print("Combined Rank of sources is: " + str(combarr))


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
    combineRank(s1, s2, s3, s4, s5)


main()
