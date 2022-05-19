# Hash Table

## What is a Hash Table
- key value pair 

    id: name
    3: raghad
    users = [raghad, gheed, jood]
    Instead of grabbing the elemnts by index, the ids are calculated and used
    users[618] = jood
    key -> 618 -> goes through actual processing to get the memory location 

- Lookup Table, Lookup data by using the key
- Fast in inserts, retrievals
- Constant time operation in the best case 

## How to use a Hash Table
    data = {}
    data[key=3] = "raghad"
    {3:"raghad"}
    print(data[3]) -> "raghad"

![example](./images/illustration.PNG)

**To resolve collisions**
Linear probing

Linked-list
![example](./images/collisions.PNG)

## Big O

- Lookup by key O(1)
- Insert/Delete O(1)

## Creating a Hash 

- A hash table is created from an array
- Create an array with an appropriate size (usually= 1024)
- Turn key into numeric value

    key = "Cat"
    value = "Josie"
    - Add all ASCII values togather
        Cat = 67 + 97 + 116 = 280
    - Multiply it by a prime number such as 599
        280 * 599 = 69648
    - Use modulo to get the remainder of the result, when divided by the total size of the array.    
        69648 % 1024 = 16
    - Insert into the array at that index.
        key gets placed in index of 16

## How the key/values are stored in the array

- Each index of the array can hold many types of values
- Each Index of the array contain “buckets”
    - Each of these “buckets” holds one key/value pair combination
    - When there is no entry in a specific bucket, the buckets (each index of the array) all start none
    - Each index in the array is called a “bucket” because it can store multiple key/value pairs.
- The hash table starts each bucket empty and overwrites their value once a key generates a hashCode that corresponds with an index

## Collisions
- A collision occurs when more than one key hashes to the same index in an array
- A “perfect hash” will never have any collisions. 
- A worst possible hash is one that hashes every single key to the same exact index of an array.

**Collisions are solved by changing the initial state of the buckets.**
- Instead of starting them all as null we can initialize a LinkedList in each one
    - If two keys resolve to the same index in the array then their key/value pairs can be stored as a node in a linked list


**Ratio between the number of items stored and the size of the list:**
The load factor tells us something about how full the hash table is:

    Load Factor = Total number of items stored / Size of the list

## Internal Methods

#### Add()
1. Send the key to the GetHash method.
2. Once you determine the index of where it should be placed, go to that index
3. Check if something exists at that index already, if it doesn’t, add it with the key/value pair.
4. If something does exist, add the new key/value pair to the data structure within that bucket.

#### Find()
The Find takes in a key, gets the Hash, and goes to the index location specified. Once at the index location is found in the array, it is then the responsibility of the algorithm the iterate through the bucket and see if the key exists and return the value.

#### Contains()
The Contains method will accept a key, and return a boolean if that key exists inside the hashtable. The best way to do this is to have the contains call the GetHash and check the hashtable if the key exists in the table given the index returned.

#### GetHash()
The GetHash will accept a key as a string, conduct the hash, and then return the index of the array where the key/value should be placed.