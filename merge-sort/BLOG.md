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
Time complexity: O(n * log(n))

Each broken down subpart of the initial list that’s sorted using the merge sort algorithm takes linear time to merge with another subpart.

## Algorithm
1. Divide the list into two equal halves


## Visualization


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




## Pseudo Code
    ALGORITHM Mergesort(arr)
        DECLARE n <-- arr.length
        if n < 2
        return
        /
        if n > 1
        DECLARE mid <-- n/2
        DECLARE left <-- arr of size mid
        DECLARE right <-- arr of size n-mid

        for i <- 0 to mid - 1
            left[i] <- arr[i]
        for i <- mid to n - 1
            right[i - mid] <- arr[i]

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
                k <-- k + 1
            else
                arr[k] <-- right[j]
                j <-- j + 1
                k <-- k + 1

        if i = left.length
        set remaining entries in arr to remaining values in right
        else
        set remaining entries in arr to remaining values in left