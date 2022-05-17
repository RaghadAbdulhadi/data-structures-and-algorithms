class MyException(Exception):
    pass

def insertion_sort(lst):
    """
    A function that takes in a list of numbers and sorts them inplace using the insertion sort algorithm
        Arguments: list
        Returns: sorted list
    """
    if type(lst) == str:
        raise MyException("The input should be a list of numbers")

    if len(lst) == 0:
        raise MyException("List is empty, the input should be a list of numbers")

    for index in range(1, len(lst)):
        current_index = index - 1
        current_value = lst[index]
        while current_index >= 0 and current_value < lst[current_index]:
            lst[current_index + 1] = lst[current_index]
            current_index = current_index - 1
        lst[current_index + 1] = current_value
    
    return lst


if __name__ == "__main__":

    lst = [5,12,7,5,5,7]
    lst_1 = [20,18,12,8,5,-2]
    lst_2 = [2,3,5,7,13,11]
    lst_3 = []
    lst_4 = "not a list"


    print(insertion_sort(lst))
    print(insertion_sort(lst_1))
    print(insertion_sort(lst_2))
    print(insertion_sort(lst_3))
    print(insertion_sort(lst_4))

