def sum_of_intervals(intervals):
    if len(intervals) == 0:
        return 0
    else:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        total = 0
        for i in range(1,len(intervals)):
            if intervals[i][0] > end:
                total += end - start
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end,intervals[i][1])
        total += end - start
        return total