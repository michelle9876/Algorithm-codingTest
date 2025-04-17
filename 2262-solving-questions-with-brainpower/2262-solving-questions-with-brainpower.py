class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = {}
        n = len(questions)

        # i => index
        def dp(i):
            # base case
            if i >= n :
                return 0
            
            if i in memo :
                return memo[i]
            
            points, brainpower = questions[i]

        # solve question - index
            # point = questions[i][0]
            # next_point = questions[i+brainpower+1][0]
            # brainpower = questions[i][1]
            
            # solveQ = point + next_point
            next_index = i + brainpower + 1
            solveQ = points + dp(next_index)

        # skip question - index
            # skipQ = questions[i+1][0]
            skipQ = dp(i + 1)

            memo[i] = max(solveQ, skipQ)
            return memo[i]

        return dp(0)
            