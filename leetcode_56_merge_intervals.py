from typing import List
from collections import deque


class Solution:
    def merge(self, intervals:List[List[int]]) -> List[List[int]]:
        result = []
        stack = deque()
        for interval in reversed(sort_intervals(intervals)):
            stack.append(interval)

        while len(stack) > 0:
            first = stack.pop()
            if len(stack) > 0 and is_overlayered(first, stack[-1]):
                second = stack.pop()
                stack.append(merge_intervals(first, second))
            else:
                result.append(first)

        return result


def sort_intervals(intervals):
    return list(sorted(intervals, key=lambda x:x[0]))


def is_overlayered(interval1, interval2):
    return not (
        (interval1[0] < interval2[0] and interval1[1] < interval2[0])
        or (interval2[0] < interval1[0] and interval2[1] < interval1[0])
    )

def merge_intervals(interval1, interval2):
    return [
        min(interval1[0], interval2[0]),
        max(interval1[1], interval2[1])
    ]

def main():
    intervals1 = [[1,3], [2,6], [8,10], [15,18]]
    intervals2 = [[1,4],[4,5]]
    solution = Solution()
    print(solution.merge(intervals1))
    print(solution.merge(intervals2))


if __name__ == '__main__':
    main()
