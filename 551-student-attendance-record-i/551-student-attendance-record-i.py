class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') <= 1 and 'LLL' not in s:
            return True
        else:
            return False