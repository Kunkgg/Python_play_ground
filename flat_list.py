import unittest


def flat_list(alist, res=[]):
    for e in alist:
        if isinstance(e, list):
            flat_list(e, res)
        else:
            res.append(e)
    return res


def main():
    alist = [1, [2, 3, [4]], 5]
    res = []
    res = flat_list(alist, res)
    print(res)


class TestFlatList(unittest.TestCase):
    def test_flat_list(self):
        alist = [1, [2, 3, [4]], 5]
        res = []
        res = flat_list(alist, res)
        self.assertEqual(res, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
