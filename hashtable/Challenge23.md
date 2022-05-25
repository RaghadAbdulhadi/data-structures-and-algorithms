# Challenge Summary
Create a function that finds the first word to occur more than once in a string
    Arguments: string
    Return: string
## Whiteboard Process
[repeated-words](https://www.figma.com/file/eOdsXMv3gKhbgXhvnp8W8V/Repeated-Words?node-id=0%3A1)
## Approach & Efficiency
### Approach
- Create a function that takes in a string and returns the first repeated word
- If passed argument is not string or if no repeated words raise an exception
- Remove al the symbols or charcters from the string
    (Replacing the actual charcter or symbol by nothing)
- Transfer all the upper case letters to lower 
- Split the string into a list, each word will represent an element in the list
- Intialaize a hashtable using the hashtable class
- Hash the words to be placed in the hashtable in the correct position
- The words will be placed as key/value pairs 
- The values will be the words 
- The keys will be depending on the repetion of the words 
- The first time the key will be more than 1 and the value is equal to the word 
- Return the value 

### Efficiency
**Big O**
Time Complexity: O(n)
Space Complexity: O(n)

## Solution

```python
if __name__ == "__main__":
    print(repeated_word("Once upon a time, there was a brave princess who"))
    print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
    print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
    print(repeated_word("Raghad, raghad"))
    print(repeated_word("hello"))
    print(repeated_word(""))
    print(repeated_word(0))
```
[solution](image.jpg)
