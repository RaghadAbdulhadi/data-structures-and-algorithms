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

## Big O Notation
### Time Complexity
Best Case: O(n)
Worst Case: O(n^2)
### Space Complexity
O(1)
## Algorithm
- A function that takes in an list of numbers and returns them in a sorted order
- Check if the list is empty -> raise exception
- Check if the input is an list -> raise exception
- Loop over the elements of the list by index
    - Assign the pr
## Pseudo Code
    InsertionSort(int[] arr)
        FOR i = 1 to arr.length
            int j <-- i - 1
            int temp <-- arr[i]
            WHILE j >= 0 AND temp < arr[j]
            arr[j + 1] <-- arr[j]
            j <-- j - 1
            arr[j + 1] <-- temp

## Python Implementation
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

## Running the code

    if __name__ == "__main__":
    lst = [5,12,7,5,5,7]
    lst_1 = [20,18,12,8,5,-2]
    lst_2 = [2,3,5,7,13,11]
    print(insertion_sort(lst))
    print(insertion_sort(lst_1))
    print(insertion_sort(lst_2))

**INPUT**

LIST1 = [5, 12, 7, 5, 5, 7]

LIST2 = [20, 18, 12, 8, 5, -2]

LIST3 = [2, 3, 5, 7, 13, 11]

**OUTPUT**

LIST1 = [5, 5, 5, 7, 7, 12]

LIST2 = [-2, 5, 8, 12, 18, 20]

LIST2 = [2, 3, 5, 7, 11, 13]