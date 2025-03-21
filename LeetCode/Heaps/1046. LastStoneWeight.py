# https://leetcode.com/problems/last-stone-weight/description/
# Difficulty: Easy

'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
'''
import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        n = len(stones)
        if n == 1:
            return 1
        if n == 0:
            return 0
        for i in range(n):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            print(stones)
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if -x == -y:
                continue
            if x != y:
                heapq.heappush(stones, -1 * (-y - (-x)))

            print(stones)
        if stones:
            return -stones[0]
        else:
            return 0
        


test = Solution()
print(test.lastStoneWeight([2,7,4,1,8,1]))
print(test.lastStoneWeight([3,7,2]))
        
        