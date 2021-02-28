class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        if ruleKey == 'type':
            for i in items:
                if i[0] == ruleValue:
                    ans += 1
        if ruleKey == 'color':
            for i in items:
                if i[1] == ruleValue:
                    ans += 1
        if ruleKey == 'name':
            for i in items:
                if i[2] == ruleValue:
                    ans += 1
        return ans