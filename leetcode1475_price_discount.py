from collections import deque

class Solution:
    def finalPrices(self, prices):
        pays = [-1] * len(prices)

        i = 0
        stack = deque()
        while i < len(prices):
            if not stack or stack[-1][1] < prices[i]:
                stack.append((i, prices[i]))
            elif stack[-1][1] >= prices[i]:
                while stack and stack[-1][1] >= prices[i]:
                    item = stack.pop()
                    pays[item[0]] = item[1] - prices[i]
                stack.append((i, prices[i]))
            i += 1
        while stack:
            item = stack.pop()
            pays[item[0]] = item[1]
        return pays

if __name__ == '__main__':
    prices = [8, 4, 6, 2, 3]
    solution = Solution()
    print(solution.finalPrices(prices))

