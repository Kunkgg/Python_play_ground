from typing import List
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        if not array:
            return False
        row = col = 0
        max_row = len(array) - 1
        max_col = len(array[0]) - 1

        while row <= max_row and col <= max_col:
            cur = array[row][col]
            if cur == target:
                return True
            elif col < max_col and cur < target:
                if  target < array[row][col + 1]:
                    row +=1
                else:
                    col += 1

        while row <= max_row and col <= max_col:
            cur = array[row][col]
            if cur == target:
                return True
            elif row < max_row and cur < target:
                if  target < array[row + 1][col]:
                    col +=1
                else:
                    row += 1

        return False


def main():
    array = [
        [1,2,8,9],
        [2,4,9,12],
        [4,7,10,13],
        [6,8,11,15]
    ]

    target = 7
    solution = Solution()
    print(solution.Find(target, array))


if __name__ == "__main__":
    main()


