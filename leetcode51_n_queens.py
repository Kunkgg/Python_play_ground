class Solution:
    def solveNQueens(self, n):

        def is_vaild(record, i, j):
            for k in range(i):
                if (record[k] == j) or (abs(k - i) == abs(record[k] - j)):
                    return False
            return True

        def convert(record):
            return ['.' * col + 'Q' + '.' * (n - col - 1) for col in record]

        def process(i, record, n):
            if i == n:
                ans.append(record[:])
                return 1
            res = 0
            for j in range(n):
                if is_vaild(record, i, j):
                    record[i] = j
                    res += process(i + 1, record, n)
            return res

        record = [-1] * n
        ans = []

        process(0, record, n)

        detail_ans = []
        for record in ans:
            detail_ans.append(convert(record))

        return detail_ans



if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))

