class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map = {}

        # for s in strs:
        #     sort = "".join(sorted(s))
        #     map.setdefault(sort,[]).append(s)
        # return list(map.values())

        
        check = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c)- ord("a")] += 1

            check[tuple(count)].append(string)
        return list(check.values())