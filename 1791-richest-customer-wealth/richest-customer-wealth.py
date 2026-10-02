class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for customer in accounts:
            total = 0
            for money in customer:
                total = total +  money 
                richest = max(richest , total )
        return richest