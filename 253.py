"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for item in intervals:
            start.append(item.start)
            end.append(item.end)
        start.sort()
        end.sort()
        global_max = 0
        counter = 0
        sp = 0
        ep = 0
        while sp < len(end):
            if start[sp] < end[ep]:
                counter +=1
                sp +=1
                global_max = max(counter, global_max)
            else:
                counter -=1
                ep+=1
        return global_max


        