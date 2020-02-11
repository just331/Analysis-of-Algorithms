# Justin Rodriguez
# CS 5381 Analysis of Algorithms
# Project 1
from _ast import operator


def inversioncount(arr):
    count = 0
    n = len(arr)
    arr = [k[1] for k in arr]
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count


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
def mergeSort(arr):
    n = len(arr)
    temp_arr = [0] * n  # Temp list created to count inversions
    return _mergeSort(arr, temp_arr, 0, n - 1)


def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(arr, temp_arr, left, mid)  # get the inversion count for the left subarray
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)  # get the inversion count for the right subarray
        inv_count += merge(arr, temp_arr, left, mid, right)  # get the inversion count once two subarrays are combined
    return inv_count


# Merge left and right subarrays into single sorted-array
def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:  # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


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
    a1 = [1, 20, 6, 4, 5]
    cr = combineRank(s1, s2, s3, s4, s5)
    print("The combined rank of each web page is: ", cr)

    crp = [i[0] for i in cr]

    c1 = formatlist(s1, crp)
    print("Formatted list: ", c1)
    out = [item[1] for item in c1]
    print("Work: ", out)
    #  print("Number of inversion in Source 1 are: ", inversioncount(c1))
    print("Merge sort Num of inversions: ", mergeSort(out))
    c2 = formatlist(s2, crp)
    c3 = formatlist(s3, crp)
    c4 = formatlist(s4, crp)
    c5 = formatlist(s5, crp)

    # create list that contains the combined rank list as well as the corresponding page
    # c1 = list(zip(page, s1))


main()
