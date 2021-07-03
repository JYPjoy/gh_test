"""
    # LeetCode 937.Reorder Data in Log files
    # https://leetcode.com/problems/reorder-data-in-log-files/
    # Algo: String
"""


import collections
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = [""]
strs3 = ["a"]

def groupAnagrams(strs):
    anagrams = collections.defaultdict(list) #list형태의 dict이 생성됨

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
       #print(sorted(word), anagrams.keys(), anagrams.values())
    return list(anagrams.values())
print(groupAnagrams(strs1))


# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = collections.defaultdict(list)
# for k, v in s:
#     d[k].append(v)
#
# print(d)#defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
# print(sorted(d.items()))#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# print(list(d.values())) #[[1, 3], [2, 4], [1]]
