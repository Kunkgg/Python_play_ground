def merge_sort(nums):
    nums_cp = nums[:]
    _merge_sort(nums_cp, 0, len(nums) - 1)
    return nums_cp


def _merge_sort(nums, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    _merge_sort(nums, start, mid)
    _merge_sort(nums, mid + 1, end)
    _merge(nums, start, end, mid)


def _merge(nums, start, end, mid):
    i = start
    j = mid + 1
    tmp = []
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1

    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= end:
        tmp.append(nums[j])
        j += 1

    for i in range(start, end + 1):
        nums[i] = tmp[i - start]


def main():
    nums = [10, 7, 5, 6, 1, 3]
    print(merge_sort(nums))
    print(nums)


if __name__ == "__main__":
    main()
