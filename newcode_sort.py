import sys
import operator

def merge_sort(datas, asc):
    def process(datas, left, right):
        if left == right:
            return
        mid = left + ((right - left) >> 1)
        process(datas, left, mid)
        process(datas, mid + 1, right)
        merge(datas, left, right, mid, asc)
    
    def merge(datas, left, right, mid, asc):
        helper = []
        p1 = left
        p2 = mid + 1
        cmp = operator.le if asc else operator.ge
        key = lambda x : operator.getitem(x, 1)
        
        while p1 <= mid and p2 <= right:
            if cmp(key(datas[p1]), key(datas[p2])):
                helper.append(datas[p1])
                p1 += 1
            else:
                helper.append(datas[p2])
                p2 += 1
        while p1 <= mid:
            helper.append(datas[p1])
            p1 += 1
        while p2 <= right:
            helper.append(datas[p2])
            p2 += 1

        for idx, data in enumerate(helper):
            datas[left + idx] = data
    
    process(datas, 0, len(datas) - 1)
    return datas

def print_result(datas):
    for data in datas:
        print(" ".join([str(e) for e in data]))

# while True:
#     line_no = 0
#     datas = []
#     for line in sys.stdin:
#         if line_no == 0:
#             length = int(line.strip())
#         elif line_no == 1:
#             asc = int(line.strip())
#         elif line_no < length + 2:
#             name, score = line.strip().split()
#             datas.append((name, int(score)))
#         if line_no == length + 1:
#             print_result(merge_sort(datas, asc))
#             break
#         line_no += 1
# 


def main():
    # datas = [
    #     ("fang", 90),
    #     ("yang", 50),
    #     ("ning", 70),
    # ]
    # print_result(merge_sort(datas, asc=0))

    datas2 = [
        ("qhsq", 15),
        ("ozslg", 79),
        ("ncttmtsphb", 71),
        ("a", 39),
        ("eeiuyzsj", 34),
        ("nmlrokx", 21),
        ("pjizylo", 90),
        ("ec", 45),
        ("f", 12),
        ("sh", 31),
        ("fm", 25),
        ("ptprphubqk", 29),
        ("wxdiwv", 0),
        ("uhlcpjtxad", 60),
        ("w", 20),
        ("zwktbpun", 70),
        ("efzfkf", 69),
        ("v", 31),
        ("rsnrgtl", 73),
        ("lhdo", 76),
        ("wt", 56),
        ("mcdwd", 14),
        ("ydrnoyd", 37),
        ("gmlfds", 76),
        ("zx", 1),
        ("dqx", 98),
        ("gz", 90),
        ("kvbzrwrrjj", 13),
    ]

    print_result(merge_sort(datas2, asc=0))

if __name__ == "__main__":
    main()
