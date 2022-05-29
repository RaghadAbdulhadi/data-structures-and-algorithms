# Hashmap LEFT JOIN

Hashmap LEFT JOIN Combines the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
If no values exist in the right hashmap, then some flavor of NONE should be appended to the result row.

## Challenge
A function that LEFT JOINs two hashmaps into a single data structure.

    Arguments: two hash maps
        The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
        The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    Returns: returns all the strings in the left table, and if there is a matches in the left table, if not, returns None

## Approach & Efficiency

### Approach
- Create a function that takes in two hashmaps and is used to join two hashmaps into a single data structure
- If the left hashtable is empty raise an exception that there is no values in the left table to be compared with the right tree
- Instantiate an empty list to append the values to it
- Instantiate a variable and call the keys method to return all the keys in the left table
- Loop over the keys and check if they are in the right table using the contains method in the HashTable class
- If the key is pressent in the right table
- Append the key and the value in the left table, with the value from the right table
- Append the key and the value in the left table, with None that repressents there is no value in the right table
- Return the varaible that instatiated an empty list
### Efficiency
Time Complexity: O(n)

Space Complexity: O(n)
## WhiteBoard 
Check the link please:
[WhiteBoard](https://www.figma.com/file/jd3Kee25BFvYX2BgpFOmxo/Left-Join?node-id=0%3A1)

![WhiteBoard](https://www.figma.com/file/jd3Kee25BFvYX2BgpFOmxo/Left-Join?node-id=0%3A1)

## Solution

```python
if __name__ == '__main__':
    left_table = Hashtable()
    left_table.set("diligent", "employed")
    left_table.set("fond", "enamored")
    left_table.set("guide", "usher")
    left_table.set("outfit", "garb")
    left_table.set("wrath", "anger")

    right_table = Hashtable()
    right_table.set("diligent", "idle")
    right_table.set("fond", "averse")
    right_table.set("guide", "follow")
    right_table.set("flow", "jam")
    right_table.set("wrath", "delight")

    # print(left_table.table)
    # print(right_table.table)
    print(left_join(left_table, right_table))
```

-> Output:

[['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['outfit', 'garb', None]]