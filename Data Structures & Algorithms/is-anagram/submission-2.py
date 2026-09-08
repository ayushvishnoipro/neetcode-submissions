class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch,0)+1
        
        for ch in t:
            if ch in cnt:
                cnt[ch] = cnt.get(ch,0)-1
        return all(cnt[ch] == 0 for ch in s)