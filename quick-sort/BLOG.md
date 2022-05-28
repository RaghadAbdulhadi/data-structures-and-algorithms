# Quick Sort
QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.
## How Quick Sort Works 
### There are many different versions of quickSort that pick pivot in different ways. 

1. Always pick the first element as a pivot
2. Always pick the last element as a pivot
3. Pick a random element as a pivot
4. Pick median as a pivot

**Quicksort is a sorting algorithm based on the divide and conquer approach where:**

1. An array is divided into subarrays by selecting a pivot element (element selected from the array).
2. While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
3. The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
4. At this point, elements are already sorted. Finally, elements are combined to form a sorted array.
### Partition Function

A function that is used to rearrange the array, and return the index of pivot
    Arguments: list, start index, end index
    Returns: Pivot Index

### Quick Sort Function

A function that is used to sort the elements of the list in place
    Arguments: List, start index, end index
    Returns: Sorted list

## Quick Sort Performance
*Time complexity:*

O(nlogn) -> Average case running time
O(n^2) -> Worst case running time

*Space Complexity: * 

In-place 
O(1)

## Algorithm
- Select any element in the list and call it pivot
- Partitioning the list
(Partition is a proccess where we select the pivot and rearrange the list)
- Rearrange the list, in which all the elemnts less than the pivot are at the left and all the elements greater than the pivot are at the right of it
- There will be two sublists, reassign the pivot for each sublist
- Rearrange the two sublists, in which all the elemnts less than the pivot are at the left and all the elements greater than the pivot are at the right of it
- When we have only one element in the sublist 
    - Stop the recursive call 
## Pseudo Code Partition
    Partition(Array, start, end)
    {
    pivot <- Array[end]
    pivotIndex <- start
    for i <- start to end -1
    {
        if Array[i] <= pivot 
        { 
            swap(Array[i], Array[pivotIndex])
            pivotIndex <- pivotIndex + 1
            }
    }
    swap(Array[pivotIndex], Array[end]
    return pivotIndex
    }
## Pseudo Code Quick Sort
    QuickSort(Array, start, end)
    { 
    # Base Case
    if(start < end)
            # Rearrange the array, and return the index of Pivot
            Partition(Array, start, end) -> PartitionIndex
        # Recursive Call
        # Sort the segments left and right of the Pivot
        QuickSort(Array, strat, PartitionIndex - 1)
        QuickSort(Array, PartitionIndex + 1, end)
    } 

## Python Implementation
```python
class MyException(Exception):
    pass

def partition(lst, start, end):
    """
    A function that is used to rearrange the array, and return the index of pivot
        Arguments: list, start index, end index
        Returns: Pivot Index
    """
    pivot = lst[end]
    pivot_index = start
    for i in range(start, end):
        if lst[i] <= pivot:
            lst[i], lst[pivot_index] = lst[pivot_index], lst[i]
            pivot_index += 1
    lst[pivot_index], lst[end] = lst[end], lst[pivot_index]
    return pivot_index

def quick_sort(lst, start, end):
    """
    A function that is used to sort the elements of the list in place
        Arguments: List, start index, end index
        Returns: Sorted list
    """
    if len(lst) == 0:
        raise MyException("List is empty")

    if start < end:
        pivot_index = partition(lst, start, end)
        quick_sort(lst, start, pivot_index - 1)
        quick_sort(lst, pivot_index + 1, end)
    return lst
```
## Visualization
![WhiteBoard](https://www.figma.com/file/dRHJD29hIZ0I9VNudUskgS/Partition?node-id=0%3A1)
![WhiteBoard](https://www.figma.com/file/56JyGTDNdw2ytqegcY8BfM/Quick-Sort-Test?node-id=0%3A1)
![WhiteBoard](https://www.figma.com/file/YPH52rlrDIoykx4LXedYhB/Quick-Sort-Visualization?node-id=0%3A1)


## Running the code

```python 
if __name__ == '__main__':
    print(quick_sort([5,12,7,5,5,7], 0, 5)) 
    # -> [5, 5, 5, 7, 7, 12]
    print(quick_sort([20,18,12,8,5,-2], 0, 5)) 
    # -> [-2, 5, 8, 12, 18, 20]
    print(quick_sort([8,4,23,42,16,15], 0, 5)) 
    # -> [4, 8, 15, 16, 23, 42]
    print(quick_sort([0,0,0,0,0,0], 0, 5)) 
    # -> [0, 0, 0, 0, 0, 0]
    print(quick_sort([], 0, 5)) 
    # -> "List is empty"
```

## Whiteboard Process
![Whiteboard Workflow](https://www.figma.com/file/9zRbsOieou2GvCOSj6wfDu/Quick-Sort?node-id=0%3A1)



