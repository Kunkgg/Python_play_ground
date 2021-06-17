# -*- utf-8


def bin_search(target, sorted_list):
    if not is_sorted(sorted_list):
        raise ValueError("Input is not a sorted list")

    start = 0
    end = len(sorted_list)

    while start < end:
        mid = (end - start) // 2 + start
        if target < sorted_list[mid]:
            end = mid
        elif target > sorted_list[mid]:
            start = mid + 1
        else:
            return mid
    return -1


def is_sorted(alist):
    return sorted(alist) == alist


if __name__ == "__main__":
    sorted_list1 = list(range(10))
    target1 = 5
    sorted_list2 = list(range(100, 110))
    target2 = 5
    sorted_list3 = [1, 7, 9, 10]
    target3 = 7
    sorted_list4 = [2, 7, 11, 20, 25]
    target4 = 25
    sorted_list5 = [2, 7, 11, 20, 25]
    target5 = 12

    print(
        f"sorted_list1: {sorted_list1}, target: {target1}, result: {bin_search(target1, sorted_list1)}"
    )
    print(
        f"sorted_list2: {sorted_list2}, target: {target2}, result: {bin_search(target2, sorted_list2)}"
    )
    print(
        f"sorted_list3: {sorted_list3}, target: {target3}, result: {bin_search(target3, sorted_list3)}"
    )
    print(
        f"sorted_list4: {sorted_list4}, target: {target4}, result: {bin_search(target4, sorted_list4)}"
    )
    print(
        f"sorted_list5: {sorted_list5}, target: {target5}, result: {bin_search(target5, sorted_list5)}"
    )
