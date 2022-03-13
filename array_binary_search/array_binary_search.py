import math

def binary_search(list, key):

    # Sort the array
    for number in range(len(list)):
        for next_number in range(number + 1, len(list)):
            if list[next_number] < list[number]:
                list[number], list[next_number] = list[next_number], list[number]


    start_index = 0
    end_index = len(list) - 1
    
    # Keep looping when start_index is less than or equal to end_index
    while start_index <= end_index:

        # mid_index each time a part is ignored
        mid_index = math.floor((start_index + end_index) // 2)

        # If the element is smaller than key, Ignore elements at the right
        if list[mid_index] > key:  
            end_index = mid_index - 1
        
        # If the element is greater than key, Ignore elements at the left
        elif list[mid_index] < key:
            start_index = mid_index + 1
        
        # If the element is equal to the key, return the index
        else:
            return mid_index

    # If start_index is greater than end_index
    return -1

print(binary_search([4, 5, 10, 16, 23], 5))


