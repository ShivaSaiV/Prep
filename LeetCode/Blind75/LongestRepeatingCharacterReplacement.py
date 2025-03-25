class Solution:
    def characterReplacement(self, s, k):
        if s is None:
            return 0
        
        left = 0
        maxLength = 0
        counts = [0] * 26
        
        for right in range(len(s)):
            # Update the counts array (frequency of each char)
            counts[ord(s[right]) - ord("A")] += 1
            while (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - ord("A")] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength

        