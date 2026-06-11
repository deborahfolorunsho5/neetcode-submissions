class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
# go through the array find the string 


        group = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in group:
                group[key] = []
            
            group[key].append(word)
        return list(group.values())