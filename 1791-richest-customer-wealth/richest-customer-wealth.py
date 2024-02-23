class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])

        wealth = 0

        for i in range(m):
            summ = 0
            for j in range(n):
                summ += accounts[i][j]
            
            if summ > wealth:
                wealth = summ
                
        return wealth
            
        