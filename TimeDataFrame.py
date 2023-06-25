# Time DF --------------------------------------------------------------------------------------------------------------
import datetime

import pandas as pd
from timeit import default_timer as timer
from Data import Data

from NormalDataFrame import NormalDataFrame
import util
from abc import ABC, abstractmethod

class DateFormat(ABC):
    # Is the string in the correct format?
    @abstractmethod
    def __contains__(self, string):
        pass

    # Parse this string to a unified format of (DD, MM, YYYY)
    @abstractmethod
    def __getitem__(self, string) -> tuple[int, int, int]:
        pass

class SlashesDMYFormat(DateFormat):
    def __contains__(self, string):
        return len(string.split('/')) == 3
    
    def __getitem__(self, string) -> tuple[int, int, int]:
        return tuple(string.split('/'))

class DotsDMYFormat(DateFormat):
    def __contains__(self, string):
        return len(string.split('.')) == 3

    def __getitem__(self, string) -> tuple[int, int, int]:
        return tuple(string.split('.'))

class DotsMDYFormat(DateFormat):
    def __contains__(self, string):
        return len(string.split('.')) == 3

    def __getitem__(self, string) -> tuple[int, int, int]:
        return string.split('.')[1], string.split('.')[0], string.split('.')[2]


class TimeDataFrame(Data):
    def __init__(self, df: NormalDataFrame, run: bool) -> None:
        if not run:
            util.Time.append(0)
            return None
        temp = timer()
        minutes = []
        hours = []
        days = []
        months = []
        years = []
        weekdays = []
        # 0 = monday, 6 = sunday.
        months_since = []
        # months since idk 2000 or something (combine year and month ez).
        daily_ids = []
        # an ID for every day, like the months_since.
        date_formats = [SlashesDMYFormat(), DotsDMYFormat(), DotsMDYFormat()]
        # formats to parse the dates.
        restart = True
        while restart:
            restart = False
            for i in list(df.index):
                date, time, author, text = df.row(i)
                # if len(time) > 5 or len(time.split(':')) < 2 or len(date.split('/')) < 3:
                    # hour = 0
                    # minute = 0
                    # day = 0
                    # month = 0
                    # year = 0
                    # weekday = 0
                    # month_id = 0
                    #     day_id = 0
                # else:
                hour = time.split(':')[0]
                minute = time.split(':')[1]
                
                try:
                    day, month, year = date_formats[0][date]
                    weekday = datetime.datetime(year=int(year), month=int(month), day=int(day)).date().weekday()
                except (ValueError, IndexError):
                    date_formats.pop(0)
                    restart = True
                    continue
                month_id = int(year) * 12 + int(month)
                day_id = month_id * 31 + int(day)

                hours.append(int(hour))
                minutes.append(int(minute))
                days.append(int(day))
                months.append(int(month))
                years.append(int(year))
                weekdays.append(weekday)
                months_since.append(month_id)
                daily_ids.append(day_id)
                print(" TDF -", i, "     ", end='\r')

        util.Time.append(timer() - temp)
        super().__init__(pd.DataFrame(list(zip(minutes, hours, days, months, years, weekdays, months_since, daily_ids)),
                            columns=['minute', 'hour', 'day', 'month', 'year', 'weekday', 'monthly-index', 'day-id']))

    def get_months(self):
        return list(set(self.df['monthly-index']))


def filter_indexes(index_list, df):
    index_list = list(index_list)
    minutes = []
    hours = []
    days = []
    months = []
    years = []
    weekdays = []
    # 0 = monday, 6 = sunday.
    months_since = []
    # months since idk 2000 or something (combine year and month ez).
    daily_ids = []
    # an ID for every day, like the months_since.
    for i in index_list:
        minute, hour, day, month, year, weekday, monthly_index, day_id = df.row(i)

        hours.append(int(hour))
        minutes.append(int(minute))
        days.append(int(day))
        months.append(int(month))
        years.append(int(year))
        weekdays.append(weekday)
        months_since.append(monthly_index)
        daily_ids.append(day_id)

    return pd.DataFrame(list(zip(index_list, minutes, hours, days, months, years, weekdays, months_since, daily_ids)),
                        columns=['index', 'minute', 'hour', 'day', 'month', 'year', 'weekday', 'monthly-index', 'day-id'])

# OPTIMIZE ???

