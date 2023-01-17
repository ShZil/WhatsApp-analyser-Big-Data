# Character DF ---------------------------------------------------------------------------------------------------------
import pandas as pd
from timeit import default_timer as timer

import Alphabets
from Data import Data
from NormalDataFrame import NormalDataFrame
import util

class CharacterDataFrame(Data):
    def __init__(self, df: NormalDataFrame, run: bool):
        if not run:
            util.Time.append(0)
            return None
        temp = timer()
        all = True
        if all:
            chars = []
            rarities = []

            for i in list(df.index):
                date, time, author, text = df.row(i)
                if util.is_nan(text):
                    continue
                for c in text:
                    if c not in chars:
                        chars.append(c)
                        rarities.append(0)
                for letter in text:
                    rarities[chars.index(letter)] += text.count(letter)
            util.Time.append(timer() - temp)
            super().__init__(pd.DataFrame(list(zip(chars, rarities)), columns=['letter', 'rarity']).sort_values(by="rarity", ascending=False))
            return
        else:
            chars = Alphabets.characters()
            rarities = []
            for _ in chars:
                rarities.append(0)
            for i in range(len(df)):
                date, time, author, text = df.row(i)
                if util.is_nan(text):
                    continue
                for letter in chars:
                    rarities[chars.index(letter)] += text.count(letter)

        util.Time.append(timer() - temp)
        super().__init__(pd.DataFrame(list(zip(chars, rarities)), columns=['letter', 'rarity']))
