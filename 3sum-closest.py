#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
#与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 思路：使用15题三数相加的原理，判断三数之和与target的差值，更新差值
        nums.sort()
        res = 0
        min_diff = float('inf')         # 存储三数之和与target差值的绝对值
        n = len(nums)
        for i in range(n):
            left = i+1
            right = n-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                add = nums[i]+nums[left]+nums[right]        # 三数之和
                diff = add-target                           # 三数之和与target的差值
                # 如果当前差值的绝对值小于存储的值，更新最小差值，同时更新结果
                if abs(diff) < min_diff:   
                    min_diff = min(abs(diff), min_diff)
                    res = add
                if diff == 0:           # 差值为0，直接返回
                    return add
                elif diff < 0:          # 差值小于0，left指针向更大的值方向移动
                    left += 1
                else:
                    right -= 1
        return res
