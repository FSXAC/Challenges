class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        total = 0
        history = []
        for op in ops:
            end = len(history) - 1
            if op == '+' and end >= 0:    # add two previous valid scores
                score = history[end]
                if (end > 0):
                    score += history[end - 1]
                total += score
                history.append(score)
            elif op == 'D' and end >= 0:  # add the double of last score
                score = history[end] * 2
                total += score
                history.append(score)
            elif op == 'C' and end >= 0:  # Minus the last score AND devalidate last valid score
                total -= history[end]
                history.pop(end)
            else:                         # integer
                score = int(op)
                total += score
                history.append(score)
        
        return total