class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prevArrival, prevTime, waitTime, cumulativeWaitTime = 0,0,0,0
        for arrrival, time in customers:
            waitTime = max(waitTime + prevArrival + prevTime - arrrival, 0)
            cumulativeWaitTime += waitTime + time
            prevArrival, prevTime = arrrival, time
        return cumulativeWaitTime/len(customers)