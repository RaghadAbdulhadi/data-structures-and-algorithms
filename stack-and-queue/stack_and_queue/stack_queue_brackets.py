# from stack_and_queue.stack import Stack

class BracketValidation:
    def __init__(self):
        pass
    
    @staticmethod
    def is_match(opening_bracket, closing_bracket):
        """
        A function used to check if the popped element from the stack is an oppening for the closing bracket
            Arguments: opening bracket, closing bracket
            Returns: boolean
        """
        if opening_bracket == "(" and closing_bracket == ")":
            return True
        elif opening_bracket == "{" and closing_bracket == "}":
            return True
        elif opening_bracket == "[" and closing_bracket == "]":
            return True
        else:
            return False
    @staticmethod
    def validate_brackets(string):
        """
        A function that represents whether or not the brackets in the string are balanced
            Arguments: string
            Retrun: boolean
        """
        opening_bracket_container = Stack()
        index_string = 0
        while index_string < len(string):
            bracket = string[index_string]
            if bracket == "(" or bracket == "{" or bracket == "[":
                opening_bracket_container.push(bracket)
            elif bracket == ")" or bracket == "}" or bracket == "]":
                if opening_bracket_container.is_empty():
                    return False
                else:
                    pop_oppening = opening_bracket_container.pop()
                    if not BracketValidation.is_match(pop_oppening, bracket):
                        return False
            index_string += 1
        if opening_bracket_container.is_empty():
            return True
        else:
            return False

if __name__ == '__main__':
    from stack import Stack
    print(BracketValidation.validate_brackets("{}"))
    print(BracketValidation.validate_brackets("{}(){}"))
    print(BracketValidation.validate_brackets("()[[Extra Characters]]"))
    print(BracketValidation.validate_brackets("(){}[[]]"))
    print(BracketValidation.validate_brackets("{}{Code}[Fellows](())"))
    print(BracketValidation.validate_brackets("[({}]"))
    print(BracketValidation.validate_brackets("(]("))
    print(BracketValidation.validate_brackets("{(})"))
    # Edge Case:
    print(BracketValidation.validate_brackets("(("))
    print(BracketValidation.validate_brackets("]]"))