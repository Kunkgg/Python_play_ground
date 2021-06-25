# -*- coding: utf-8 -*-
import unittest


def insert_sort(alist):
    if not alist:
        return
    for i in range(1, len(alist)):
        value = alist[i]
        j = i - 1
        while j >= 0:
            if alist[j] > value:
                alist[j + 1] = alist[j]
            else:
                break
            j -= 1
        alist[j + 1] = value

    return alist


class TestInertSort(unittest.TestCase):
    def test_insert_sort(self):
        alist1 = [2, 10, 5, 3]
        alist2 = [0, 10, 4, 7, 10, 8]
        self.assertEqual(insert_sort(alist1), [2, 3, 5, 10])
        self.assertEqual(insert_sort(alist2), [0, 4, 7, 8, 10, 10])


if __name__ == "__main__":
    unittest.main()
