# n kids with candies
# candies : int array
# candies[i] : represents numb of candies i th kid has
# extraCandies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        greatestCandy = max(candies)
        ans = []
        for candy in candies:
            new_candy_count = (candy+ extraCandies)
            if new_candy_count >= greatestCandy:
                ans.append(True)
            else: 
                ans.append(False)
        return ans
         



        