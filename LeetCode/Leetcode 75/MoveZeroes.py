class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        i = 0
        while(i < len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
                # print(nums)
            else:
                i += 1

        print(count)

        while (count != 0):
            nums.append(0)
            count -= 1


        return nums
    

test = Solution()
print(test.moveZeroes([0, 1, 0, 3, 12]))
print(test.moveZeroes([0, 0, 1]))

