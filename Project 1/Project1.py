# Justin Rodriguez
# CS 5381 Analysis of Algorithms
# Project 1
import time


# Function to get time it takes for function to complete its task
# Taken from: https://stackoverflow.com/questions/5478351/python-time-measure-function
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))

        return ret

    return wrap


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


# Function that takes one list and sorts according to order of another list (Combined Rank)
def formatlist(l1, l2):
    page = []
    for x in range(10000):  # Create list of 10000 with corresponding page number
        page.append("Page {}".format(x))

    l1 = list(zip(page, l1))  # Give current list corresponding page number
    # Sort the given list based on order of combined ranked list
    dic = {v: j for j, v in enumerate(l2)}
    return sorted(l1, key=lambda p: dic[p[0]])


def inversioncount(arr):  # Standard way to count inversion based on algorithm given during lecture
    count = 0
    n = len(arr)  # Used for loop management
    arr = [k[1] for k in arr]  # Get rid of page number elements within list
    for i in range(n):  # iterate through list
        for j in range(i + 1, n):  # Get ith next position
            if arr[i] > arr[j]:  # If the ith element is greater than its next, increment inversion count
                count += 1
    return count


# Modified Merge sort to count number of inversions
def mergeInversion(arr):
    if len(arr) == 1:  # If array is size 1 or less there will be no inversions. Return array and 0
        return arr, 0
    else:  # If not of len 1 or less, array needs to be sorted
        left = arr[:len(arr) // 2]  # Create left subarray that consists of elements to left of mid
        right = arr[len(arr) // 2:]  # Create right subarray that consists of elements to right of mid

        left, left_inv = mergeInversion(left)  # Recursively call func to further decompose org array into single item
        right, right_inv = mergeInversion(right)  # Recursively call func to further decompose array into single item
        sortedlist = []  # Create temp array to store sorted list from original array
        inversion_count = left_inv + right_inv  # final inversion count will be the sum of left/right inversion count

        i = 0  # var to index left subarray
        j = 0  # var to index right subarray

    while i < len(left) and j < len(right):  # Traverse both left and right subarrays
        if left[i] <= right[j]:  # No inversion will occur proceed to sort and check
            sortedlist.append(left[i])  # add current element to left subarray
            i += 1
        else:  # By definition (i > j) an inversion has occurred
            sortedlist.append(right[j])  # save element j to right subarray
            j += 1
            inversion_count += (len(left) - i)  # increment inversion count
    # combine left and right subarrays into sorted array
    sortedlist += left[i:]
    sortedlist += right[j:]

    return sortedlist, inversion_count


# Helper function for quickSortInversion that divides a given array into two subarrays
def quickSortDivide(arr):
    less = []  # Create empty array for left subarray
    greater = []  # Create empty array for right subarray
    pivot = arr[-1]  # Let the pivot be the last element in the array
    inversion_count = greater_inv_count = 0  # Set inversion count and right subarray count to 0

    for i in arr:  # Traverse array
        if i <= pivot:  # If current is less than pivot append to less subarray
            less.append(i)
            inversion_count += greater_inv_count  # Increase inversion count by what right subarray's is currently
        else:  # if current is greater than pivot append to greater subarray
            greater.append(i)
            greater_inv_count += 1  # Increase inversion count by 1
    return inversion_count, less, greater


# Modified quick sort to count inversions during sort from source files
def quickSortInversion(arr):
    if len(arr) <= 1:  # If array size less is less than 2 we won't have an inversion
        return 0
    inversion_count, less, greater = quickSortDivide(arr)  # divide the array into 2 subarrays and get their inversions
    less.pop()
    return inversion_count + quickSortInversion(less) + quickSortInversion(greater)  # combine inversions


# Modified Bubble Sort Inversion count
@timing
def bubbleSortInverion(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):  # Traverse through array
        for j in range(0, n - i - 1):  # Look at current elements' previous
            if arr[j] > arr[j + 1]:  # When current element is greater than next's, inversion has occurred
                inv_count += 1
                arr[j], arr[j+1] = arr[j + 1], arr[j]   # Swap elements S.T inversion no longer occurs
    return arr, inv_count  # Return sorted array and inversion count


# Function to determine quality of sources based on number of inversions (equation from lecture)
def sourceQuality(source_inv):
    quality = 1 / (1 + source_inv)  # Equation to calculate quality of a source given # of inversions
    return quality * 100


def callAlgorithms(arr, n):
    s = quickSortInversion(arr)
    q = sourceQuality(s)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Mergesort Inversion Count for Source {}: ".format(n), mergeInversion(arr)[1])
    print("Quicksort Inversion Count for Source {}: ".format(n), quickSortInversion(arr))
    print("Bubble Sort Inversion Count for Source {}: ".format(n), bubbleSortInverion(arr)[1])
    print("Quality of source is: {}%".format(q))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def main():
    d1 = [line.strip() for line in open("project 1/data/source1.txt", "r")]  # Read in the data file and save to d1
    s1 = [int(i) for i in d1]  # Turn data from file into list of ints and save to s1
    d2 = [line.strip() for line in open("project 1/data/source2.txt", "r")]  # Read in the data file and save to d2
    s2 = [int(i) for i in d2]  # Turn data from file into list of ints and save to s2
    d3 = [line.strip() for line in open("project 1/data/source3.txt", "r")]  # Read in the data file and save to d3
    s3 = [int(i) for i in d3]  # Turn data from file into list of ints and save to s3
    d4 = [line.strip() for line in open("project 1/data/source4.txt", "r")]  # Read in the data file and save to d4
    s4 = [int(i) for i in d4]  # Turn data from file into list of ints and save to s4
    d5 = [line.strip() for line in open("project 1/data/source5.txt", "r")]  # Read in the data file and save to d5
    s5 = [int(i) for i in d5]  # Turn data from file into list of ints and save to s5
    cr = combineRank(s1, s2, s3, s4, s5)  # Get the combined rank of every page from each source and save to cr
    crp = [i[0] for i in cr]  # Used to format sources to be list of tuples [(page #, rank)]
    print("The combined rank of each web page sorted is: ", cr)
    print("Source 1 Original: ", s1)
    print("Source 1 Formatted (Page #, Ranking): ", formatlist(s1, crp))

    new_s1 = [item[1] for item in formatlist(s1, crp)]
    callAlgorithms(new_s1, 1)

    new_s2 = [item[1] for item in formatlist(s2, crp)]
    callAlgorithms(new_s2, 2)

    new_s3 = [item[1] for item in formatlist(s3, crp)]
    callAlgorithms(new_s3, 3)

    new_s4 = [item[1] for item in formatlist(s4, crp)]
    callAlgorithms(new_s4, 4)

    new_s5 = [item[1] for item in formatlist(s5, crp)]
    callAlgorithms(new_s5, 5)

    a1 = [1, 2, 6, 3, 5]
    callAlgorithms(a1, 0)


main()
