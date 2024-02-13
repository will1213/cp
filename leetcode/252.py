class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key= lambda x: x[0])
        prev = None
        for i in intervals:
            if prev and (i[0] < prev):
                return False
            prev = i[1]
        return True