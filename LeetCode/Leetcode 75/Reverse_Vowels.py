class Solution(object):
    def reverseVowels(self, s):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        start = 0
        end = len(s) - 1
        s_list = list(s)
        while (start < end):
            if s[start] in vowels:
                if s_list[end] in vowels:
                    temp = s_list[start]
                    s_list[start] = s_list[end]
                    s_list[end] = temp
                    start += 1
                    end -= 1
                else:
                    end -= 1

            if s_list[start] not in vowels:
                start += 1
        return "".join(s_list)
            