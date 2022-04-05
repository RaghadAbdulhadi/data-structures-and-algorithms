# Challenge Summary
Create a function that represents whether or not the brackets in the string are balanced
    Arguments: string
    Retrun: boolean
## Whiteboard Process
[validateabrackets](./images/bracketvalidatioWB.PNG)


## Approach & Efficiency
1. Create a function to check if the opening and the closing match for each kind of brackets which takes2 arguments. opening bracket and closing bracket
2. Create a function to validate brackets it takes a string as an argument
3. Instaniate a stack to push the opening brackets to it
4. Assign the index of each element in the string as variable and instantiate it with zero
5. Iterate until the index is larger than the length of the string
6. If the bracket is equal to “{“ or “[“ or “(“
7. Push the bracket to the stack
8. If the bracket is equal to “}“ or “]“ or “)“
9. Check if stack is empty return false
10. If not empty assign a varaible to be the popped elemnt from the stack
11. Check the matching of the opening and closing brackets using the match function
12. When index is greater than length of string, exit the loop and check if the stack is empty, if not return false

**Big O:**

Space Complexity: O(n) -> Depends on the string argument length

Time Complexity: O(n) -> iterating iver the string argument length
## Solution
[Solution#2](./images/Solution%232.PNG)