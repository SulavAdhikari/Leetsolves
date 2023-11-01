class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        result = collections.defaultdict(list)

        for string in strs:
            c = [0] * 26

            for index in string:
                c[ord(index) - ord("a")] += 1
                
            result[tuple(c)].append(string)

        return result.values()