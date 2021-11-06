# def merge_sort(nums):
#     nums_cp = nums[:]
#     _merge_sort(nums_cp, 0, len(nums) - 1)
#     return nums_cp
# 
# 
# def _merge_sort(nums, start, end):
#     if start >= end:
#         return
#     mid = (start + end) // 2
#     _merge_sort(nums, start, mid)
#     _merge_sort(nums, mid + 1, end)
#     _merge(nums, start, end, mid)
# 
# 
# def _merge(nums, start, end, mid):
#     i = start
#     j = mid + 1
#     tmp = []
#     while i <= mid and j <= end:
#         if nums[i] <= nums[j]:
#             tmp.append(nums[i])
#             i += 1
#         else:
#             tmp.append(nums[j])
#             j += 1
# 
#     while i <= mid:
#         tmp.append(nums[i])
#         i += 1
#     while j <= end:
#         tmp.append(nums[j])
#         j += 1
# 
#     for i in range(start, end + 1):
#         nums[i] = tmp[i - start]

def merge_sort(nums):
    def process(nums, left, right):
        if left == right:
            return
        mid = left + ((right - left) >> 1)
        process(nums, left, mid)
        process(nums, mid + 1, right)
        merge(nums, left, mid, right)
        return nums
    
    def merge(nums, left, mid, right):
        if left == right:
            return
        helper = []
        p1 = left
        p2 = mid + 1
        while (p1 <= mid and p2 <= right):
            if nums[p1] <= nums[p2]:
                helper.append(nums[p1])
                p1 += 1
            else:
                helper.append(nums[p2])
                p2 += 1
        while (p1 <= mid):
            helper.append(nums[p1])
            p1 += 1
        while (p2 <= mid):
            helper.append(nums[p2])
            p2 += 1

        for idx, num in enumerate(helper):
            nums[left + idx] = num
    
    return process(nums, 0, len(nums) - 1)

def main():
    nums = [10, 7, 5, 6, 1, 3]
    print(nums)
    print(merge_sort(nums))


if __name__ == "__main__":
    main()
