class Solution(object):
    def gcdOfStrings(self, str1, str2):
        min_len = min(len(str1), len(str2))

        def divisor(i):

            # GCD must divide both strings 
            if len(str1) % i != 0:
                return False
            if len(str2) % i != 0:
                return False
            
            fact1 = len(str1) // i
            fact2 = len(str2) // i

            if (str1[:i] * fact1 == str1) and (str1[:i] * fact2 == str2):
                return True
            else:
                return False

        for i in range(min_len, 0, -1):
            if divisor(i) == True:
                return str1[:i]
                print("H")
        return ""