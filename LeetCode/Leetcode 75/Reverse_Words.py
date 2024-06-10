class Solution(object):
    def reverseWords(self, s):
        s_list = s.split()
        start = 0
        end = len(s_list)
        while start < end:
            temp = s_list[start]
            s_list[start] = s_list[end - 1]
            s_list[end - 1] = temp
            start += 1
            end -= 1
        return " ".join(s_list)
            