import unittest


def is_paired(c1, c2):
    if (c1, c2) in (("(", ")"), ("[", "]"), ("{", "}")):
        return True
    else:
        return False


def check_brackects(text):
    s = SimpleStack()
    for c in text:
        if c in "([{":
            s.push(c)
        if c in ")]}" and is_paired(s.get_top(), c):
            s.pop()
    return s.is_empty()


class SimpleStack:
    def __init__(self):
        self._container = []

    def push(self, element):
        self._container.append(element)

    def pop(self):
        return self._container.pop()

    def is_empty(self):
        return not self._container

    def get_top(self):
        return self._container[-1]


class TestCheckBrackects(unittest.TestCase):
    def test_check_brackects(self):
        str1 = "(a+b) * c"
        str2 = "{[(a+b) * c] + (e + d)}"
        str3 = "[a+b) * c"
        self.assertTrue(check_brackects(str1))
        self.assertTrue(check_brackects(str2))
        self.assertFalse(check_brackects(str3))


if __name__ == "__main__":
    unittest.main()
