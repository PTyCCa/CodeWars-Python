def sum_of_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: (-x[0], x[1]), reverse=True)
    start = sorted_intervals[0][0]
    end = sorted_intervals[0][1]
    sum = end - start
    
    for i in sorted_intervals[1:]:
        if i[0] < end and i[1] > end:
            sum += i[1] - end
            end = i[1]
        if i[0] > end:
            sum += i[1] - i[0]
            end = i[1]
    
    return sum


def sum_of_intervals_2(intervals):
    result = set()
    for start, stop in intervals:
        for x in range(start, stop):
            result.add(x)
            
    return len(result)

def sum_of_intervals_3(intervals):
    return len(set([i for a,b in intervals for i in range(a,b)]))