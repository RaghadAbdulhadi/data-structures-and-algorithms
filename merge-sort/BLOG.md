# Merge Sort
- Merge sort works by splitting the input list into two halves, repeating the process on those halves, and finally merging the two sorted halves together. The algorithm first moves from top to bottom, dividing the list into smaller and smaller parts until only the separate elements remain.
- The merge sort algorithm adopts the divide-and-conquer algorithm paradigm to sort elements within a list efficiently.

## What Are Divide And Conquer Algorithms?
- The initial problem is divided into associated subproblems where a solution can be applied recursively to each subproblem. The final solution to the larger problem is a combination of the solutions to the subproblems.

**There are three main components of the divide-and-conquer approach to algorithm design:**
1. Divide: continuously break down the larger problem into smaller parts.
2. Conquer: solve each of the smaller parts by utilising a function that’s called recursively.
3. Combine: merge all solutions for all smaller parts into a single unified solution, which becomes the solution to the starting problem.

## How Merge Sort Works
Merge sort operation follows the basis of dividing the list into halves and continuously dividing the new halves down to their individual component. Then there is a comparison between individual components, which are merged to form the final sorted list.

## Merge Sort Performance
*Time complexity:* O(n * log(n))

Each broken down subpart of the initial list that’s sorted using the merge sort algorithm takes linear time to merge with another subpart.

*Space Complexity: *O(n)

Merge sort has space complexity of O(n) because to sort the unsorted list, the recursive function will be splitting and creating subarrays but the sum of sizes of all the subarray will be n.


## Visualization

## Algorithm
1. Divide the list into two equal halves 

## Pseudo Code
    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length

        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr[0...mid]
        DECLARE right <-- arr[mid...n]
        // sort the left side
        Mergesort(left)
        // sort the right side
        Mergesort(right)
        // merge the sorted left and right sides together
        Merge(left, right, arr)

    ALGORITHM Merge(left, right, arr)
        DECLARE i <-- 0
        DECLARE j <-- 0
        DECLARE k <-- 0

        while i < left.length && j < right.length
            if left[i] <= right[j]
                arr[k] <-- left[i]
                i <-- i + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1

            k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left

## Python Implementation
```python
def merge_sort(lst):
    if type(lst) == str:
        raise MyException("The input should be a list of numbers")
    if len(lst) == 0:
        raise MyException("List is empty, the input should be a list of numbers")
    list_length = len(lst)
    # Base Case
    if list_length < 2:
        return
    else:
        mid_point = list_length // 2
        left_sublist = lst[:mid_point]
        # print(left_sublist)
        right_sublist = lst[mid_point:]
        # print(right_sublist)

        # Recursive call to divide the left subpart of the list to reach 1 element
        merge_sort(left_sublist)
        # Recursive call to divide the right subpart of the list to reach 1 element
        merge_sort(right_sublist)
        merge(left_sublist, right_sublist, lst)
    return lst

def merge(left_sublist, right_sublist, lst):
    i = 0
    j = 0
    k = 0
    while i < len(left_sublist) and j < len(right_sublist):
        if left_sublist[i] <= right_sublist[j]:
            lst[k] = left_sublist[i]
            i = i + 1
            k = k + 1
        else:
            lst[k] = right_sublist[j]
            j = j + 1
            k = k + 1
    while i < len(left_sublist):
        lst[k] = left_sublist[i]
        i = i + 1
        k = k + 1
    while j < len(right_sublist):
        lst[k] = right_sublist[j]
        j = j + 1
        k = k + 1
```
## Trace and Test