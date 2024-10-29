import data
from math import sqrt
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1:data.Time,time2:data.Time)->data.Time:
    seconds_add = time1.second + time2.second
    minutes_add = time1.minute + time2.minute
    hours_add = time1.hour + time2.hour
    if seconds_add >= 60:
        minutes_add = minutes_add + 1
        seconds_add = 0
    if minutes_add >= 60:
        hours_add = hours_add + 1
        minutes_add = 0
    return data.Time(hours_add,minutes_add,seconds_add)
# Part 4
def is_descending(values:list[int])->bool:
    for i in range(len(values)):
        if values[i] > values[i+1]:
            return True
        else:
            return False

# Part 5
def largest_between(values:list[int],lowerbound:int,upperbound:int)->int:
    biggest = values[0]
    for value in values:
        if upperbound > value > lowerbound:
            if value > biggest:
                biggest = value
    return values.index(biggest)


# Part 6
def furthest_from_origin(values:list[data.Point]):
    furthest = 0
    index = 0
    if len(values) == 0:
        return None
    else:
        for value in values:
            distance = sqrt((value.x - 0) ** 2 + (value.y - 0) ** 2)
            if distance > furthest:
                furthest = distance
                index = values[value]
        return index


