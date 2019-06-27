#实现 strStr() 函数。
#给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
#示例 1:
#输入: haystack = "hello", needle = "ll"
#输出: 2
#示例 2:
#
#输入: haystack = "aaaaa", needle = "bba"
#输出: -1
#说明:
#
#当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


#方法一：暴力求解
class Solution:
    # 传入位置i, 依次比较i+n2-1的位置，所有都一样了，判断为True
    def helper(i):
        haystack_p = i
        needle_q = 0
        while needle_q < n2:
            if haystack[haystack_p] !=  needle[needle_q]:
                return False
            else:
                haystack_p += 1
                needle_q += 1
            return True

    def strStr(self, haystack: str, needle: str) -> int:
        # 长度为0，直接返回为0
        if not needle : return 0

        # needle长度大于haystack长度，直接返回为0
        n1 = len(haystack)
        n2 = len(needle)
        if n1 < n2:return -1

        # 逐个调用判断函数
        for i in range(n1 - n2 + 1):
            if helper(i):
                return i
        return -1


#方法二：利用index包
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

