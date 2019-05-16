#编写一个函数来查找字符串数组中的最长公共前缀。
#
#如果不存在公共前缀，返回空字符串 ""。
#
#示例 1:
#
#输入: ["flower","flow","flight"]
#输出: "fl"
#示例 2:
#
#输入: ["dog","racecar","car"]
#输出: ""
#解释: 输入不存在公共前缀。
#说明:
#
#所有输入只包含小写字母 a-z 。


# 思路1
# 将所有字符串堆叠起来，对应的每个位置去重
# 在去重长度大于1之前的长度就是最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i,x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

# 思路2
# 取一个单词s 和后面的单词比较，看s与每个单词相同的最长前缀是多少，遍历所有单词
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res


