# -*- coding: utf-8 -*-
import unittest


# def bubble_sort(alist: list) -> list:
#     temp = alist[:]
#     for i in range(len(temp) - 1):
#         for j in range(len(temp) - 1 - i):
#             if temp[j] > temp[j + 1]:
#                 temp[j], temp[j + 1] = temp[j + 1], temp[j]
# 
#     return temp

def bubble_sort(nums):
	for i in range(len(nums) - 1):
		end = len(nums) - 1 - i
		for j in range(end):
			if nums[j] > nums[j + 1]:
				nums[j], nums[j + 1] = nums[j + 1], nums[j]
	return nums

def bubble_sort_improve_with_sorted_flag(alist: list) -> list:
    temp = alist[:]
    is_sorted = True
    for i in range(len(temp) - 1):
        for j in range(len(temp) - 1 - i):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                is_sorted = False
        if is_sorted:
            break

    return temp

def select_sort(nums):
	for i in range(len(nums) - 1):
		min_num_idx = i
		for j in range(i, len(nums)):
			if nums[j] < nums[min_num_idx]:
				min_num_idx = j
		nums[i], nums[min_num_idx] = nums[min_num_idx], nums[i]
	return nums

class TestBubbleSort(unittest.TestCase):
    def test_dubble_sort(self):
        alist = [2, 3, 5, 10, 7]
        sorted_list = sorted(alist)
        self.assertEqual(bubble_sort(alist), sorted_list)

    def test_dubble_sort_improve_with_sorted_flag(self):
        alist = [2, 3, 5, 10, 7]
        sorted_list = sorted(alist)
        self.assertEqual(bubble_sort_improve_with_sorted_flag(alist),
                         sorted_list)

    def test_select_sort(self):
        alist = [2, 3, 5, 10, 7]
        sorted_list = sorted(alist)
        self.assertEqual(select_sort(alist), sorted_list)


if __name__ == "__main__":
    unittest.main()
