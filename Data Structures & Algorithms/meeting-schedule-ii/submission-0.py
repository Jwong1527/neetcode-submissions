"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        start_times = sorted([i.start for i in intervals])

        end_times = sorted([i.end for i in intervals])

        s_pointer, e_pointer = 0, 0

        current_meetings, total_rooms = 0, 0 


        while s_pointer < len(intervals):

            if start_times[s_pointer] < end_times[e_pointer]:

                current_meetings += 1
                s_pointer += 1

            else:

                current_meetings -= 1
                e_pointer += 1

            total_rooms = max(total_rooms, current_meetings)
        
        return total_rooms 



        