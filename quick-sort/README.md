# Challenge Summary
QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. 
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

## Whiteboard Process
![WhiteBoard](https://www.figma.com/file/9zRbsOieou2GvCOSj6wfDu/Quick-Sort?node-id=0%3A1)

## Approach & Efficiency
### Approach
- Select any element in the list and call it pivot
- Partitioning the list
(Partition is a proccess where we select the pivot and rearrange the list)
- Rearrange the list, in which all the elemnts less than the pivot are at the left and all the elements greater than the pivot are at the right of it
- There will be two sublists, reassign the pivot for each sublist
- Rearrange the two sublists, in which all the elemnts less than the pivot are at the left and all the elements greater than the pivot are at the right of it
- When we have only one element in the sublist 
    - Stop the recursive call 
### Efficiency
*Time complexity:*

O(nlogn) -> Average case running time
O(n^2) -> Worst case running time

*Space Complexity:* 

In-place 
O(1)

## Solution

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