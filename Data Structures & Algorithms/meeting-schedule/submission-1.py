"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
    
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start) # Sort by the start time. 

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start: # If the first meeting's end time is greater than the next meeting's start time
                return False # Then we cannot attend all meetings. 

                #ie the first meeting ends at minute 10 when meeting 2 starts at minute 8.
                # Therefore there is a conflict -> Return False. 

        return True 
