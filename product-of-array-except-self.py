#给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#示例:
#输入: [1,2,3,4]
#输出: [24,12,8,6]
#说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#进阶：
#你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

# 思路：从左往右乘一遍，放一个列表list1,从右往左乘一遍，放一个列表list2,最后对应位置左右乘积相乘。

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        for i in range(1,len(nums)):
            res[i]=res[i-1]*nums[i-1]
        right=1
        for i in range(len(nums))[::-1]:
            res[i]=res[i]*right
            right=nums[i]*right
        return res
