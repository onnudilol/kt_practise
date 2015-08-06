import time
from datetime import datetime

jobs = {'Job A': ['05/08/2015 00:00', '05/08/2015 06:00'],
        'Job B': ['05/08/2015 01:00', '05/08/2015 04:00'],
        'Job C': ['05/08/2015 03:00', '05/08/2015 05:00'],
        'Job D': ['05/08/2015 03:00', '05/08/2015 08:00'],
        'Job E': ['05/08/2015 04:00', '05/08/2015 07:00'],
        'Job F': ['05/08/2015 05:00', '05/08/2015 09:00'],
        'Job G': ['05/08/2015 06:00', '05/08/2015 10:00'],
        'Job H': ['05/08/2015 08:00', '05/08/2015 11:00']}


class Request:

    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.utc_start_time = int(time.mktime(datetime.strptime(start_time, '%d/%m/%Y %H:%M').timetuple()))
        self.utc_end_time = int(time.mktime(datetime.strptime(end_time, '%d/%m/%Y %H:%M').timetuple()))

    def __repr__(self):
        return str(self.name)


def interval_scheduling(schedule):

    """
    Greedy algorithm to schedule intervals from data in the format of 'name of slot' : 'requested time slot' with
    times in the format of %d/%m/%Y %H:%M
    """

    requests = list()
    sorted_schedule = list()

    for key in schedule:
        i = Request(key, schedule[key][0], schedule[key][1])
        requests.append(i)

    requests.sort(key=lambda x: x.utc_end_time)

    earliest_end = requests[0].utc_end_time

    sorted_schedule.append(requests.pop(0))

    for h in requests:
        if earliest_end <= h.utc_start_time:
            earliest_end = h.utc_end_time
            sorted_schedule.append(h)
            requests.remove(h)

    return sorted_schedule
