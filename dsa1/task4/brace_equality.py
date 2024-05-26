from task4 import Stack
import unittest


def brace_equal(input_string: str) -> bool:
    """Check if the braces and quotes in the input string are balanced."""
    if len(input_string) == 0 or len(input_string) % 2 != 0:
        return False

    stack: Stack = Stack()
    equality: dict[str, str] = {"(": ")", "\"": "\""}
    stack.push(input_string[0])

    for i in range(1, len(input_string)):
        current_char: str = input_string[i]
        if stack.peek() not in equality.keys():
            return False
        if equality[stack.peek()] == current_char:
            stack.pop()
        else:
            stack.push(current_char)

    return stack.len() == 0


class TestBraceEqual(unittest.TestCase):

    def test_(self):
        self.assertEqual(brace_equal(""), False)
        self.assertEqual(brace_equal("()"), True)
        self.assertEqual(brace_equal("())"), False)
        self.assertEqual(brace_equal("(())"), True)
        self.assertEqual(brace_equal("(()))"), False)
        self.assertEqual(brace_equal("(()((())()))"), True)
        self.assertEqual(brace_equal('"(()()(()")'), False)
        self.assertEqual(brace_equal("))(("), False)
        self.assertEqual(brace_equal("((())"), False)
        self.assertEqual(brace_equal("(()))"), False)
        self.assertEqual(brace_equal("\"()\""), True)
        self.assertEqual(brace_equal('"(()()"'), False)


if __name__ == "__main__":
    print(None)
    unittest.main()
