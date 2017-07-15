"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        rooms = []
        
        intervals.sort(key=lambda x:x.start)
        
        for i in intervals:
            if len(rooms) == 0:
                heapq.heappush(rooms, i.end)
            else:
                if i.start >= rooms[0]:
                    heapq.heapreplace(rooms, i.end)
                else:
                    heapq.heappush(rooms, i.end)
                 
        return len(rooms)