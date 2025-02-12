# from collections import defaultdict
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_counts = Counter("balloon")
        text_counts = Counter(text)
        
        # print(balloon_counts)
       
        return min(text_counts[char] // balloon_counts[char] for char in balloon_counts)
        


        # word = "balloon"
        # n = 1

        # counts = defaultdict(int)
        # word_counts = defaultdict(int)

        # for letter in text:
        #     if letter in word:
        #         counts[letter] += 1
        
        # for char in word:
        #     word_counts[char] += 1

        # for key , value in counts.items():
        #     for word_key, word_value in word_counts.items():
        #         if (key == word_key) and (value == word_value):
        #             return n
        #         elif (key == word_key) and value != word_value:
        #             n += 1
        #             if value == (word_value * n):
        #                 return n
        #             else:
        #                 return 0
              
                

             