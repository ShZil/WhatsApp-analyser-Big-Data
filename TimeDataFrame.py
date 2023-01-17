# Time DF --------------------------------------------------------------------------------------------------------------
import datetime

import pandas as pd
from timeit import default_timer as timer
from Data import Data

from NormalDataFrame import NormalDataFrame
import util

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
            if len(date.split('/')) > len(date.split('.')):
                month = date.split('/')[1]
                day = date.split('/')[0]
                year = date.split('/')[2]
            else:
                month = date.split('.')[0]
                day = date.split('.')[1]
                year = date.split('.')[2]
            weekday = datetime.datetime(year=int(year), month=int(month), day=int(day)).date().weekday()
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

