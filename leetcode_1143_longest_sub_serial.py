import re

def sub_serials(s):
    res = set()

    def _sub_serials(s):
        if s:
            res.add(s)
        if len(s) == 1:
            return
        else:
            for i in range(len(s)):
                s_list = list(s)
                s_list.pop(i)
                _sub_serials(''.join(s_list))
    _sub_serials(s)
    return res

# def sub_serials(s):
#     if s:
#         print(s)
#     if len(s) == 1:
#         return 
#     else:
#         for i in range(len(s)):
#             s_list = list(s)
#             s_list.pop(i)
#             sub_serials(''.join(s_list))

def test_sub_serials():
    s = 'abcd'
    sub_serials(s)

def is_sub_serial(s, sub_s):
    if not s or not sub_s:
        return True
    i = 0
    j = 0
    s_list = list(s)
    sub_s_list = list(sub_s)
    while i < len(s) and j < len(sub_s):
        if s_list[i] == sub_s_list[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(sub_s):
        return True
    else:
        return False

def _test_is_sub_serial(s, s_sub):
    print(f"{s}, {s_sub} : {is_sub_serial(s, s_sub)}")

def test_is_sub_serial():
    s1 = 'abcde'
    s_sub1 = 'afce'
    s2 = 'abcde'
    s_sub2 = 'ace'
    s3 = 'abcde'
    s_sub3 = 'aed'
    test_is_sub_serial(s1, s_sub1)
    test_is_sub_serial(s2, s_sub2)
    test_is_sub_serial(s3, s_sub3)

def clean_strs(text1, text2):
    cleaned_text1 = re.sub(fr"[^{''.join(set(list(text2)))}]", "", text1)
    cleaned_text2 = re.sub(fr"[^{''.join(set(list(text1)))}]", "", text2)
    return cleaned_text1, cleaned_text2

def test_solution(text1, text2):
    solution = Solution()
    print(f"{text1}")
    print(f"{text2}")
    print(solution.longestCommonSubSequence(text1, text2))
    print()

def main():
    text1 = "abcde"
    text2 = "ace"

    test_solution(text1, text2)

    text1 = "abc"
    text2 = "abc"

    test_solution(text1, text2)

    text1 = "abc"
    text2 = "def"

    test_solution(text1, text2)
    # test_is_sub_serial()
    # test_sub_serials()
    # s = 'abcd'
    # print(len(sub_serials(s)))


class Solution:
    def longestCommonSubSequence(self, text1: str, text2: str) -> int:
        cleaned_text1, cleaned_text2 = clean_strs(text1, text2)
        if len(cleaned_text1) > len(cleaned_text2):
            s = cleaned_text1
            s_sub = cleaned_text2
        else:
            s = cleaned_text2
            s_sub = cleaned_text1
        s_sub_set = sub_serials(s_sub)
        longest = 0
        for s_sub in s_sub_set:
            if is_sub_serial(s, s_sub) and len(s_sub) > longest:
                longest = len(s_sub)
        return longest


                
if __name__ == "__main__":
    main()
