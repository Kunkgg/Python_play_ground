from typing import List


class Solution:
    @staticmethod
    def increase(s):
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if (ord(c) + 1 > ord('9')):
                c = '0'
                s = list(s)
                s[i] = c
                s = ''.join(s)
            else:
                c = chr(ord(c) + 1)
                s = list(s)
                s[i] = c
                s = ''.join(s)
                break
        return s

    def printNumbers(self, n: int) -> List[int]:
        s = "0" * n
        res = []
        count = 0
        while (count < pow(10, n) - 1):
            s = Solution.increase(s)
            res.append(int(s))
            count += 1
        return res


def main():
    solution = Solution()
    print(solution.printNumbers(1))


if __name__ == "__main__":
    main()
