#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#示例:
#
#输入："23"
#输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#说明:
#尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        import itertools

        num_char_dict = {
                "2":["a", "b", "c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m","n","o"],
                "7":["p","q","r", "s"],
                "8":["t","u","v"],
                "9":["w","x","y","z"]
                }

        digits_list = []
        for item in digits:
            digits_list.append(num_char_dict[item])

        res_list = []
        if len(digits_list):
            for element in itertools.product(*digits_list):
                res_list.append("".join(element))

        return res_list

