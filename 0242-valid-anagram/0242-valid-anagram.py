class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {} 
        for i in range(len(s)):
            
            if dict_s.get(s[i]):
                dict_s[s[i]] = dict_s[s[i]] + 1
            else:
                dict_s[s[i]] = 1
            
            if dict_t.get(t[i]):
                dict_t[t[i]] = dict_t[t[i]] + 1
            else:
                dict_t[t[i]] = 1 

        if dict_s == dict_t:
            return True
        return False
