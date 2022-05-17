# Insertion Sort
- Insertion sort algorithm builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position.
- Insertion sort algorithm is very slow on large lists, it's a stable, in-place algorithm, that works really well for nearly-sorted or small lists.
- Insertion Sort doesn't need to know the entire list in advance before sorting. The algorithm can receive one element at a time. Which is great if we want to add more elements to be sorted - the algorithm only inserts that element in it's proper place without "re-doing" the whole sort.

## How Insertion Sort Works
1. An list is partitioned into a "sorted" sublist and an "unsorted" sublist.
    - The sorted sublist contains only the first element of our original list.
2. The first element in the unsorted list is evaluated so that we can insert it into its proper place in the sorted sublist.
3. The insertion is done by moving all elements larger than the new element one position to the right.
4. Continue doing this until our entire list is sorted.

## 



## Algorithm
- A function that takes in an list of numbers and returns them in a sorted order
- Check if the list is empty -> raise exception
- Check if the input is a list -> raise exception
- Loop over the elements of the list by index from 1 till the length of the list
    - Assign a current_index variable to be the index of the first element in the list
    - Assign a next_value variable to be the value of the second element in the list
    - While the index of the current element is greater than or equal to zero and the next value is smaller than the current value
        - Reassign the element at current_index + 1 index to be the element at current_index
        - Reassign the current_index to be current_index - 1
        (Move the current element one unit to the right and reassign the current element's index one unit backward)
    - Reassign the element at current_index + 1 to be next_value
    - Return list argument sorted
## Big O Notation
### Time Complexity
Best Case: O(n)

Worst Case: O(n^2)
### Space Complexity
O(1)
## Pseudo Code
    InsertionSort(lst)
        FOR index = 1 to lst.length
            current_index <-- index - 1
            next_value <-- lst[index]
            WHILE current_index >= 0 AND next_value < lst[current_index]
            lst[current_index + 1] <-- lst[current_index]
            lst[current_index + 1] <-- next_value

## Python Implementation
```python
def insertion_sort(lst):
    """
    A function that takes in a list of numbers and sorts them inplace using the insertion sort algorithm
        Arguments: list
        Returns: sorted list
    """
    for index in range(1, len(lst)):
        previous_index = index - 1
        current = lst[index]

        while previous_index >= 0 and current < lst[previous_index]:
            lst[previous_index + 1] = lst[previous_index]
            previous_index = previous_index - 1
        lst[previous_index + 1] = current
    return lst
```

## Running the code
```python
if __name__ == "__main__":
    lst = [5,12,7,5,5,7]
    lst_1 = [20,18,12,8,5,-2]
    lst_2 = [2,3,5,7,13,11]
    print(insertion_sort(lst))
    print(insertion_sort(lst_1))
    print(insertion_sort(lst_2))
```

**INPUT**
```python
LIST1 = [5, 12, 7, 5, 5, 7]

LIST2 = [20, 18, 12, 8, 5, -2]

LIST3 = [2, 3, 5, 7, 13, 11]
```
**OUTPUT**
```python

LIST1 = [5, 5, 5, 7, 7, 12]

LIST2 = [-2, 5, 8, 12, 18, 20]

LIST2 = [2, 3, 5, 7, 11, 13]
```
## Tests
```python
# [2,3,5,7,13,11]
    # current_index = 1 - 1 = 0
    # next_value = lst[1] = 3
    # current_index(0) >= 0 and next_value(3) < lst[current_index](2)
    # FALSE
    # lst[1] = 3
    # [2,3,5,7,13,11]

    # current_index = 2 - 1 = 1
    # next_value = 5
    # current_index(1) >= 0 and next_value(5) < lst[current_index](3)
    # FALSE
    # lst[2] = 5
    # [2,3,5,7,13,11]

    # current_index = 4 - 1 = 2
    # next_value = 7
    # current_index(2) >= 0 and next_value(7) < lst[current_index](5)
    # FALSE
    # lst[3] = 7
    # [2,3,5,7,13,11]

    # current_index = 4 - 1 = 3
    # next_value = 13
    # current_index(3) >= 0 and next_value(13) < lst[current_index](7)
    # FALSE
    # lst[4] = 13
    # [2,3,5,7,13,11]

    # current_index = 5 - 1 = 4
    # next_value = 11
    # current_index(4) >= 0 and next_value(11) < lst[current_index](13)
    # TRUE
    # lst[5] = lst[4] - > 11 = 13
    # current_index = 3
    # lst[4] = 11
    # [2,3,5,7,11,13]
```