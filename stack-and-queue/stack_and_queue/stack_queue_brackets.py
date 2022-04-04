# from stack_and_queue.stack import Stack

class Brackets:
    def __init__(self):
        self.closing_bracket_container = Stack()
        self.opening_bracket_container = Stack()

    def validate_brackets(self,string):
        """
        A function that represents whether or not the brackets in the string are balanced
            Arguments: string
            Retrun: boolean
        """
        list_of_brackets = list(string)
        for bracket in list_of_brackets:
            if bracket == "{" or bracket == "[" or bracket == "(":
                self.opening_bracket_container.push(bracket)
            elif bracket == "}" or bracket == "]" or bracket == ")":
                self.closing_bracket_container.push(bracket)

            #     if self.opening_bracket_container.is_empty() or self.opening_bracket_container.top !=0:
            #         return False
            #     self.opening_bracket_container.pop()
            # elif self.opening_bracket_container.is_empty():
            #     return True



if __name__ == '__main__':
    from stack import Stack