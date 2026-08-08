class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #is profit > 0
        starter = None
        max_p = 0
        for x in range(len(prices)):
            if starter is None:
                starter = prices[x]
            elif prices[x] < starter:
                starter = prices[x]
            
            max_v = max(starter, prices[x])
            lower_v = min(starter, prices[x])

            current_p = max_v - lower_v

            if current_p > max_p:
                max_p = current_p
            
        return max_p
            
            