# Blocks DF ------------------------------------------------------------------------------------------------------------
import pandas as pd
from timeit import default_timer as timer
from Data import Data

from NormalDataFrame import NormalDataFrame
import TimeDataFrame
import util

class BlocksDataFrame(Data):
    def __init__(self, df: NormalDataFrame, run: bool):
        if not run:
            util.Time.append(0)
            return None
        temp = timer()
        starts = []
        lengths = []
        chars = []
        authors = []
        block_index = 0
        index = 0

        while index < len(df) - 1:
            date, time, author, text = df.row(index)
            a = author
            h = time.split(':')[0]
            starts.append(index)
            lengths.append(0)
            chars.append(0)
            authors.append(a)
            while author == a and h == time.split(':')[0] and index < len(df) - 1:
                index += 1
                lengths[block_index] += 1
                chars[block_index] += len(text)
                date, time, author, text = df.row(index)
            block_index += 1

        util.Time.append(timer() - temp)
        super().__init__(pd.DataFrame(list(zip(starts, lengths, chars, authors)), columns=['starting-index', 'length', 'chars', 'author']))


def avg_length(bdf):
    return sum(bdf.df['chars']) / len(bdf)


def per_month(this, time_df):
    indexes = []
    lengths = []
    charss = []
    counts = []
    index = -1
    for i in list(this.index):
        start, length, chars, author = this.row(i)
        monthly_index = time_df.row(i)[6]
        try:
            previous_monthly_index = time_df.row(i - 1)[6]
        except KeyError:
            previous_monthly_index = 0
        if previous_monthly_index < monthly_index or i == list(this.index)[0]:
            indexes.append(monthly_index)
            lengths.append(0)
            charss.append(0)
            counts.append(0)
            index += 1
        lengths[index] += length
        charss[index] += chars
        counts[index] += 1
    lengths = [i / j for i, j in zip(lengths, counts)]
    charss = [i / j for i, j in zip(charss, counts)]
    return pd.DataFrame(list(zip(indexes, charss, lengths)),
                        columns=['month', 'avg-char-count', 'avg-length'])


def avgs(bpmdf):
    return sum(bpmdf['avg-char-count']) / len(bpmdf)
