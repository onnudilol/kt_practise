import time
from datetime import datetime
from collections import defaultdict

jobs = {'Job A': ['05/08/2015 09:00', '05/08/2015 10:30'],
        'Job B': ['05/08/2015 09:00', '05/08/2015 12:30'],
        'Job C': ['05/08/2015 09:00', '05/08/2015 10:30'],
        'Job D': ['05/08/2015 11:00', '05/08/2015 12:30'],
        'Job E': ['05/08/2015 11:00', '05/08/2015 14:00'],
        'Job F': ['05/08/2015 13:00', '05/08/2015 14:30'],
        'Job G': ['05/08/2015 13:00', '05/08/2015 14:30'],
        'Job H': ['05/08/2015 14:00', '05/08/2015 16:30'],
        'Job I': ['05/08/2015 15:00', '05/08/2015 16:30'],
        'Job J': ['05/08/2015 15:00', '05/08/2015 16:30']}


class Request:

    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.utc_start_time = int(time.mktime(datetime.strptime(start_time, '%d/%m/%Y %H:%M').timetuple()))
        self.utc_end_time = int(time.mktime(datetime.strptime(end_time, '%d/%m/%Y %H:%M').timetuple()))
        self.label = 0
        self.ignore = set()

    def __repr__(self):
        return str(self.name)


def interval_partitioning(schedule):

    """
    Greedy algorithm to partition intervals by assigning labels to requests
    sorted by the earliest start time to create sets of mutually compatible requests
    """

    requests = list()
    sorted_schedule = defaultdict(list)
    room_end_time = defaultdict(int)

    for key in schedule:
        i = Request(key, schedule[key][0], schedule[key][1])
        requests.append(i)

    requests.sort(key=lambda x: x.utc_start_time)
    sorted_schedule[requests[0].label] = [requests[0]]
    room_end_time[requests[0].label] = requests[0].utc_end_time
    del requests[0]

    while requests:
        r = requests.pop(0)

        if r.utc_start_time >= room_end_time[r.label]:
                sorted_schedule[r.label] += [r]
                room_end_time[r.label] = r.utc_end_time
        else:
            r.label += 1
            requests.insert(0, r)

    return sorted_schedule
