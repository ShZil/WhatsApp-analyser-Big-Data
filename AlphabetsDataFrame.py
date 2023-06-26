# Alphabets DF ---------------------------------------------------------------------------------------------------------
import pandas as pd
from timeit import default_timer as timer

import Alphabets
from Data import Data
import NormalDataFrame
import TimeDataFrame
import util

class AlphabetsDataFrame(Data):
    def __init__(self, ndf: NormalDataFrame.NormalDataFrame, run: bool):
        if not run:
            util.Time.append(0)
            return None
        temp = timer()
        lengths = []
        englishes = []
        hebrews = []
        emojis = []
        punctuation = []
        spaces = []
        maths = []
        for i in list(ndf.index):
            date, time, author, text = ndf.row(i)
            if util.is_nan(text):
                length = english = hebrew = emoji = pun = math = space = 0
            else:
                length = len(text)
                english = Alphabets.count_letters(text)
                hebrew = Alphabets.count_hebrew(text)
                pun = Alphabets.count_punctuation(text)
                space = Alphabets.count_spaces(text)
                math = Alphabets.count_math(text)
                emoji = length - english - hebrew - pun - math - space
            englishes.append(english)
            hebrews.append(hebrew)
            lengths.append(length)
            punctuation.append(pun)
            maths.append(math)
            spaces.append(space)
            emojis.append(emoji)

        util.Time.append(timer() - temp)
        super().__init__(pd.DataFrame(list(zip(lengths, englishes, hebrews, punctuation, maths, emojis, spaces)),
                        columns=['length', 'english-letters', 'hebrew-letters', 'punctuation', 'math', 'emojis',
                                 'whitespace']))


def per_month(this, time_df):
    if hasattr(this, 'df'):
        df = this.df
    else:
        df = this
    merged = pd.merge(df, time_df, left_index=True, right_index=True)
    merged = merged[['length', 'english-letters', 'hebrew-letters', 'punctuation', 'math', 'emojis', 'whitespace', 'monthly-index']]
    merged = merged.groupby("monthly-index").mean()
    merged['month'] = merged.index
    return merged
