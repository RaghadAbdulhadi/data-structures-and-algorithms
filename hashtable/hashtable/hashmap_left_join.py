# from hashtable import Hashtable

class MyExceptionTwo(Exception):
    pass

def left_join(left_table, right_table):
    """
    A function that LEFT JOINs two hashmaps into a single data structure.
        Arguments: two hash maps
            The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
            The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
        Returns: returns all the strings in the left table, and if there is a matches in the left table, if not, returns None
    """
    joined_strings = []
    left_table_keys = left_table.keys()
    for key in left_table_keys:
        hashed_key = left_table.hash(key)
        if right_table.contains(key):
            joined_strings.append([key, left_table.table[hashed_key][0][1], right_table.table[hashed_key][0][1]])
        else:
            joined_strings.append([key, left_table.table[hashed_key][0][1],None])
    if len(joined_strings) == 0:
        raise MyExceptionTwo("Left table has no strings to be appended and compared with the right table")
    return joined_strings



if __name__ == '__main__':
    from hashtable import Hashtable
    left_table = Hashtable()
    # left_table.set("diligent", "employed")
    # left_table.set("fond", "enamored")
    # left_table.set("guide", "usher")
    # left_table.set("outfit", "garb")
    # left_table.set("wrath", "anger")

    right_table = Hashtable()
    right_table.set("diligent", "idle")
    right_table.set("fond", "averse")
    right_table.set("guide", "follow")
    right_table.set("flow", "jam")
    right_table.set("wrath", "delight")

    # print(left_table.table)
    # print(right_table.table)
    print(left_join(left_table, right_table))


