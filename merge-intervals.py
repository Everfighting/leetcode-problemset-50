#给出一个区间的集合，请合并所有重叠的区间。
#示例 1:
#
#输入: [[1,3],[2,6],[8,10],[15,18]]
#输出: [[1,6],[8,10],[15,18]]
#解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#示例 2:
#
#输入: [[1,4],[4,5]]
#输出: [[1,5]]
#解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        # 先把区间进行排序
        for interval in sorted(intervals, key= lambda x:x[0]):
            # 如果interval的开始位置在现有区间后，则直接叠加
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            # 如果interval的结束位置比区间最后一段的开始大，则取两者的最大值进行更新
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
