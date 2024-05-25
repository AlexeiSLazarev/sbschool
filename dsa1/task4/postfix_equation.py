from task4 import Stack, Node
import unittest
from typing import List


def precedence(operator: str) -> int:
    """Returns the precedence of the given operator."""
    if operator == '^':
        return 3
    elif operator in ('/', '*'):
        return 2
    elif operator in ('+', '-'):
        return 1
    else:
        return -1


def associativity(operator: str) -> str:
    """Returns the associativity of the given operator."""
    if operator == '^':
        return 'R'
    return 'L'


def infix_to_postfix(expression: str) -> Stack:
    """Converts an infix expression to postfix notation using a stack."""
    result: List[str] = []
    stack: List[str] = []

    for char in expression:
        if char.isalnum():  # If the character is an operand (digit or letter), add it to the result.
            result.append(char)
        elif char == '(':  # If the character is an '(', push it to the stack.
            stack.append(char)
        elif char == ')':  # If the character is a ')', pop from the stack until '(' is found.
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Remove the '(' from the stack.
        else:  # An operator is encountered
            while (stack and precedence(char) < precedence(stack[-1])) or \
                    (stack and precedence(char) == precedence(stack[-1]) and associativity(char) == 'L'):
                result.append(stack.pop())
            stack.append(char)

    while stack:  # Pop all remaining operators from the stack.
        result.append(stack.pop())

    res_stack = Stack()
    result.reverse()
    for item in result:
        res_stack.push(item)

    return res_stack


def evaluate_postfix_eq(stack: Stack) -> int:
    """Evaluates a postfix expression using a stack."""
    evaluation_stack = Stack()
    for _ in range(stack.len()):
        current_val = stack.pop()
        if current_val.isdigit():
            evaluation_stack.push(current_val)
        elif current_val in {'*', '+'}:
            a = evaluation_stack.pop()
            b = evaluation_stack.pop()
            res = eval(f"{b}{current_val}{a}")
            evaluation_stack.push(res)
    return int(evaluation_stack.pop())


def process_expr(expression: str) -> int:
    """Processes an infix expression, converts it to postfix, and evaluates it."""
    if '=' in expression:
        expression = expression.split('=')[0]
    postfix_stack = infix_to_postfix(expression)
    return evaluate_postfix_eq(postfix_stack)


class TestPostfixExpr(unittest.TestCase):
    def test_postfix_expr(self):
        self.assertEqual(process_expr("1+2"), 3)
        self.assertEqual(process_expr("(1+2)*3"), 9)
        self.assertEqual(process_expr("(1+2)*3=+5*6"), 9)
        self.assertEqual(process_expr("(1+2)*3+5*6"), 39)


if __name__ == "__main__":
    expression = "(1+2)*3=+5*6"
    result = process_expr(expression)
    print("Result:", result)
