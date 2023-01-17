# Index of Coincidence DF ----------------------------------------------------------------------------------------------

import pandas as pd
from timeit import default_timer as timer
from Data import Data

from NormalDataFrame import NormalDataFrame
import TimeDataFrame
import util

class IOCDataFrame(Data):
    def __init__(self, df: NormalDataFrame, run: bool):
        if not run:
            util.Time.append(0)
            return None
        temp = timer()
        iocs = []
        for i in list(df.index):
            date, time, author, text = df.row(i)
            if util.is_nan(text):
                iocs.append(0)
            else:
                iocs.append(util.ioc(text))

        util.Time.append(timer() - temp)
        super().__init__(pd.DataFrame(list(zip(iocs)), columns=['ioc']))


def per_month(this, time_df):
    merged = pd.merge(this, time_df, left_index=True, right_index=True)
    merged = merged[['ioc', 'monthly-index']]
    merged = merged.groupby("monthly-index").mean()
    merged['month'] = merged.index
    return merged


def avg(idf):
    return sum(idf['ioc']) / len(idf)
