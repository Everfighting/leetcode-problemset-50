#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#示例 1：
#
#输入: "babad"
#输出: "bab"
#注意: "aba" 也是一个有效答案。
#示例 2：
#
#输入: "cbbd"
#输出: "bb"

class Solution(object):
    
    def check(self, sub):
        return True if sub[::-1] == sub else False               
       
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        
        step = n
        while step >= 1:
            i = 0
            while i <= n-step:
                if self.check(s[i:i+step]):
                    return s[i:i+step]
                else:
                    i += 1
            step -= 1
            
        return ''
