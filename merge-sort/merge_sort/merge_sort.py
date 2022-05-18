class MyException(Exception):
    pass

def merge_sort(lst):
    """
    A function that is used to split the list to smaller sublists intil the list reaches one element
        Arguments: List
        Returns: sorted list
    """
    if type(lst) == str:
        raise MyException("The input should be a list of numbers")
    if len(lst) == 0:
        raise MyException("List is empty, the input should be a list of numbers")
    list_length = len(lst)
    # Base Case
    if list_length < 2:
        return
    # Recursive Call
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
        # Function call to merge all the sublists and adjust there values
        merge(left_sublist, right_sublist, lst)
    return lst

def merge(left_sublist, right_sublist, lst):
    """
    A function that is used to merge all the sublists and adjust the elements in the original list based on the sorted sublists
        Arguments: left sublist, right sublist, original list
        Returns: None
    """
    # index in the left sublists
    i = 0
    # index in the right sublists
    j = 0
    # index in the original list
    k = 0

    # Loop over the elements in both the left and right sublists 
    while i < len(left_sublist) and j < len(right_sublist):
        # Compare the element from the left and the right sublists
        # If the element in the left sublist is smaller than the element in the right sublist reassign the element in the original list to be the element in the left sublist

        if left_sublist[i] <= right_sublist[j]:
            lst[k] = left_sublist[i]
            i = i + 1
            k = k + 1

        # Compare the element from the left and the right sublists
        # If the element in the right sublist is smaller than the element in the left sublist reassign the element in the original list to be the element in the right sublist
        elif right_sublist[i] <= left_sublist[j]:
            lst[k] = right_sublist[j]
            j = j + 1
            k = k + 1

    # 
    while i < len(left_sublist):
        lst[k] = left_sublist[i]
        i = i + 1
        k = k + 1
    # 
    while j < len(right_sublist):
        lst[k] = right_sublist[j]
        j = j + 1
        k = k + 1

if __name__ == "__main__":
    lst = [16,8,4,1]
    print(merge_sort(lst))