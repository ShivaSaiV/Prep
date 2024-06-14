class Solution(object):
    def countingSort(self, arr):
        max_val = max(arr)

        arr1 = [0] * (max_val + 1)
        for i in range(len(arr)):
            arr1[arr[i]] += 1
        print(arr1)

        countArray = []
        pre_sum = 0
        for i in range(len(arr1)):
            pre_sum += arr1[i]
            countArray.append(pre_sum)

        res = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            res[countArray[arr[i]] - 1] = arr[i]
            countArray[arr[i]] -= 1

        return res        
    

    def minIncrementForUnique(self, nums):
        sorted_nums = self.countingSort(nums)
        n = len(sorted_nums) - 1
        
        count = 0

        for i in range(n):
            if sorted_nums[i + 1] <= sorted_nums[i]:
                curr_count = 0
                count += sorted_nums[i] - sorted_nums[i + 1] + 1
                curr_count += sorted_nums[i] - sorted_nums[i + 1] + 1
                sorted_nums[i + 1] += curr_count

        return count

test = Solution()
print(test.minIncrementForUnique([1, 2, 2]))
print(test.minIncrementForUnique([3,2,1,2,1,7]))
