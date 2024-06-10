import collections
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        cards = {}
        cards = collections.Counter(hand)

        heap = list(cards.keys())
        heapq.heapify(heap)
        while len(heap) != 0:
            for i in range(heap[0], heap[0] + groupSize):
                if i not in cards.keys():
                    return False
                else:
                    cards[i] -= 1
                    if cards[i] == 0:
                        if i != heap[0]:
                            return False
                        heapq.heappop(heap)
        return True