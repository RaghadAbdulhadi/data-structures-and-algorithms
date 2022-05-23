
class Hashtable():
    def __init__(self, size= 100):
        # initialize the size of the list
        self.size = size
        self.table = [None]*size

    def hash(self, key):
        """
        A method that takes in a key and returns the index of the key in the collection of that key
            Arguments: key
            Returns: Index in the collection for that key
        """
        sum_of_ascii = 0
        for charc in key:
            charc_ascii = ord(charc)
            sum_of_ascii += charc_ascii
        hashed_key = (sum_of_ascii) % self.size

        return hashed_key

    def set(self, key, value):
    # def __setitem__(self, key, value):
        """
        A method that takes in a key and a value, it hashes the key, and sets the key and value pair in the table, handles collisions as needed.
            Arguments: key, value
            Returns: Nothing
        """
        # get the hashed key from the hash method
        hashed_key = self.hash(key)
        # check if the bucket is empty at the hashed_key index, add the key/value pair
        if not self.table[hashed_key]:
            self.table[hashed_key] = [[key, value]]
        # if the bucket is not empty, append the key/value pair
        else:
            self.table[hashed_key].append([key, value])

    def get(self, key):
    # def __getitem__(self, key):
        """
        A method that returns the value associated with a specific key that is passed to the method as an argument.
            Arguments: key
            Returns: Value associated with that key in the table
        """
        # call the get hash method and send the key to it
        hashed_key = self.hash(key)
        # lookup the index of the value from the table
        # return the value stored in that index
        return self.table[hashed_key][0][1]

    def __delitem__(self, key):
        """                
        A method that deleted an key and value from the table
            Arguments: key
            Returns: Nothing
        """
        # call the get hash method and send the key to it
        hashed_key = self.hash(key)
        # Set this particular key's value to be none
        self.table[hashed_key] = None


    def contains(self, key):
        """
        A method that takes in a key and checks if it is in the table or not.
            Arguments: key
            Returns: Boolean, indicating if the key exists in the table already.
        """
        hashed_key = self.hash(key)
        if self.table[hashed_key] == None:
            return False
        return True
        
    def keys(self):
        """
        A method that returns a collection of keys
            Arguments: None
            Returns: Collection of keys
        """
        keys_collection = []
        for idx, value in enumerate(self.table):
            if self.table[idx] != None:
                if len(self.table[idx]) == 1:
                    keys_collection.append(self.table[idx][0][0])
                else:
                    keys_collection.append(self.table[idx][0][0])
                    keys_collection.append(self.table[idx][1][0])  
        return keys_collection
def repeated_word(string):
    pass

if __name__ == "__main__":
    t = Hashtable(size=20)
    # print(t.hash('march 6'))

    # get and set methods
    t.set('march 6', 300)
    t.set('april 6', 300)
    t.set('march 6', 300)
    t.set('march 4', 600)
    t.set('march 5', 1000)
    # print(t.get('march 5'))
    print(t.table)

    # # __setitem__ and __getitem__
    # t['march 5'] = 130
    # t['march 6'] = 800
    # t['march 6'] = 500
    # t['march 7'] = 1000
    # t['march 7'] = 1000
    # del t['march 5']

    # contains and keys collection
    # print(t.contains('march 5'))
    # print(t.contains('march 6'))
    print(t.keys())
    # print(t.table)