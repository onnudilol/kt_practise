import time
from datetime import datetime, timedelta
import re


jobs = {'Job A': ['01:00:00', '05/08/2015 02:00'],
        'Job B': ['02:00:00', '05/08/2015 04:00'],
        'Job C': ['03:00:00', '05/08/2015 06:00']}


class Jobs:

    def __init__(self, name, length, deadline):
        self.name = name

        self.length = length
        self.h, self.m, self.s = re.split(':', self.length)
        self.length_seconds = int(timedelta(hours=int(self.h), minutes=int(self.m),
                                            seconds=int(self.s)).total_seconds())

        self.deadline = int(time.mktime(datetime.strptime(deadline, '%d/%m/%Y %H:%M').timetuple()))
        self.start_time = 0
        self.end_time = 0
        self.lateness = 0

    def __repr__(self):
        return str(self.name)

    def human_readable(self):
        # todo: convert utc timestamps to human readable format

        pass


def min_lateness(jobs, start_time):

    """
    Function that uses a greedy algorithm to schedule requests to minimise lateness.
    Takes input in the form of a set of jobs with running lengths of 'HH:MM:SS' and deadlines of '%d/%m/%Y %H:%M' and
    an initial starting time of '%d/%m/%Y %H:%M'.
    """

    finish_time = int(time.mktime(datetime.strptime(start_time, '%d/%m/%Y %H:%M').timetuple()))
    requests = list()
    sorted_schedule = list()

    for j in jobs:
        i = Jobs(j, jobs[j][0], jobs[j][1])
        requests.append(i)

    requests.sort(key=lambda x: x.deadline)

    for r in requests:

        r.start_time = finish_time
        r.end_time = r.start_time + r.length_seconds
        r.lateness = r.end_time - r.deadline
        finish_time = r.end_time
        sorted_schedule.append(r)

    return sorted_schedule
