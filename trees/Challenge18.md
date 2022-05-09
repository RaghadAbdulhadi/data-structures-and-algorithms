# Challenge Summary
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
**Approach:**

Argument -> k_ary_tree
Returns -> new fizz_buzz_tree

- Traverse the k_ary_tree
- Check each node if:
    - If the value is divisible by 3, replace the value with “Fizz”
    - If the value is divisible by 5, replace the value with “Buzz”
    - If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    - If the value is not divisible by 3 or 5, simply turn the number into a String
- Return a new tree with the fizz buzz values
## Solution
<!-- Show how to run your code, and examples of it in action -->