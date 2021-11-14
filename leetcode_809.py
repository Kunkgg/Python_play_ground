class Solution:
    def expressivewords(self, s, words):
        count = 0
        for word in words:
            if is_stretchy(s, word):
                count += 1
        return count

def is_stretchy(s, word):
    s_count = count_str(s)
    word_count = count_str(word)
    if [c[0] for c in s_count] != [c[0] for c in word_count]:
        return False
    i = 0
    while i < len(s_count):
        if (s_count[i][1] == 2 and word_count[i][1] != 2) or s_count[i][1] < word_count[i][1]:
            return False
        i += 1
    return True

def count_str(s):
    if not s:
        return []
    if len(s) == 1:
        return [[s, 1]]
    i = 0
    j = 1
    res = []
    cur_count = 1
    while j < len(s):
        if s[j] == s[i]:
            cur_count += 1
        else:
            cur_chara = [s[i], cur_count]
            res.append(cur_chara)
            i = j
            cur_count = 1
        j += 1
    res.append([s[i], cur_count])
    return res


if __name__ == "__main__":
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    solution = Solution()
    print(solution.expressivewords(s, words))
