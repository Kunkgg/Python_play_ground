import heapq

class Solution:
    def lastStoneWeight(self, stones):
        if not stones:
            return 0
        stones_heap = [-1 * stone for stone in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            stone1 = -1 * heapq.heappop(stones_heap)
            stone2 = -1 * heapq.heappop(stones_heap)
            if stone1 != stone2:
                heapq.heappush(stones_heap, stone1 - stone2)
        if not stones_heap:
            return 0
        else:
            return stones_heap[0]


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    solution = Solution()
    print(solution.lastStoneWeight(stones))
