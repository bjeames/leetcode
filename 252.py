"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)

        curr_meeting = 0
        next_meeting = 1
        while next_meeting < len(intervals):
            if intervals[curr_meeting].end > intervals[next_meeting].start:
                return False
            curr_meeting+=1
            next_meeting+=1
        
        return True
        
