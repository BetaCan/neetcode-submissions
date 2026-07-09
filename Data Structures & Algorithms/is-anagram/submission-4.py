class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        
        for i in range(len(s)):
            print(s[i])
            if s[i] in map:
                temp = map[s[i]]
                temp = temp+1
                map[s[i]] = temp
            else:
                map[s[i]] = 1

        map2 = {}

        for i in range(len(t)):
            print(t[i])
            if t[i] in map2:
                temp = map2[t[i]]
                temp = temp+1
                map2[t[i]] = temp
            else:
                map2[t[i]] = 1

        return map == map2
            
        