# Hashtables
## Challenge
Implement a Hashtable Class with the following methods:
- set

    Arguments: key, value

    Returns: nothing

    This method should hash the key, and set the key and value pair in the table, handling collisions as needed.

    Should a given key already exist, replace its value from the value argument given to this method.
- get

    Arguments: key

    Returns: Value associated with that key in the table
- hash

    Arguments: key

    Returns: Index in the collection for that key
- contains

    Arguments: key

    Returns: Boolean, indicating if the key exists in the table already.
- keys

    Returns: Collection of keys

## Approach & Efficiency
#### Approach
- Intialize the class with two attributes: 
    - size, initialize it with any number of items
    - table, create an list with an appropriate size (usually= 1024)
- Create a hash method that takes in a key and returns the index of the key in the collection of that key
    - Turn key into numeric value
        - Add all ASCII values togather
        - Multiply it by a prime number such as 599
        - Use modulo to get the remainder of the result, when divided by the total size of the array.    
        - Insert into the array at that index.
- Create a set method that takes in a key and a value, it hashes the key, and sets the key and value pair in the table, handles collisions as needed.
    - get the hashed key from the hash method
    - check if the bucket is empty at the hashed_key index, add the key/value pair
    - if the bucket is not empty, append the key/value pair
- Create a get method that returns the value associated with a specific key that is passed to the method as an argument.
    - get the hashed key from the hash method
    - lookup the index of the value from the table
    - return the value stored in that index
- Create a delete method that deletes specific key/value pairs from the table
    - get the hashed key from the hash method
    - Set this particular key's value to be none
- Create a contains method that checks if a key exists in the table
    - get the hashed key from the hash method
    - If the index of the key is None return False, else return True
- Create a keys method that returns a list of all the keys in the table
    - loop over the list's of the table and append each element's key to a variable
    - if the length of the list inside the table is not equal to one, then there is collision and append both keys to the list's variable
#### Efficiency
**Best Case Time Complexity**

- Lookup by key O(1)
- Insert/Delete O(1)

**Worst Case Time Complexity**

*When collisions occur:*
- A collision occurs when more than one key hashes to the same index in an array
- A “perfect hash” will never have any collisions. 
- A worst possible hash is one that hashes every single key to the same exact index of an array.

- Lookup by key O(n)
- Insert/Delete O(1)



**Space Complexity**

Depends on the number of items that are stored in the table

O(n)
## API

#### hash method
    A function that takes in a key and returns the index of the key in the collection of that key
        Arguments: key
        Returns: Index in the collection for that key
#### set method
    A function that takes in a key and a value, it hashes the key, and sets the key and value pair in the table, handles collisions as needed.
        Arguments: key, value
        Returns: Nothing

#### get method
    A function that returns the value associated with a specific key that is passed to the function as an argument.
        Arguments: key
        Returns: Value associated with that key in the table

#### delete method
    A function that deleted an key and value from the table
        Arguments: key
        Returns: Nothing

#### contains method
    A function that takes in a key and checks if it is in the table or not.
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
#### keys method
    A function that returns a collection of keys
        Arguments: None
        Returns: Collection of keys