# Words DF -------------------------------------------------------------------------------------------------------------
import pandas as pd
from timeit import default_timer as timer
from Data import Data

from MessageTypeDataFrame import MessageTypeDataFrame
from NormalDataFrame import NormalDataFrame
import util

class WordsDataFrame(Data):
    def __init__(self, ndf: NormalDataFrame, mtdf: MessageTypeDataFrame, run: bool) -> None:
        if not run:
            util.Time.append(0)
            return None
        temp = timer()
        df = ndf.df.drop(mtdf.df['ind'])
        words = []
        rarities = []

        for i in list(df.index):
            date, time, author, text = ndf.row(i)
            if util.is_nan(text):
                continue
            for word in text.split():
                if word not in words:
                    words.append(word)
                    rarities.append(0)
            for word in text.split():
                rarities[words.index(word)] += text.count(word)

        util.Time.append(timer() - temp)
        super().__init__(pd.DataFrame(list(zip(words, rarities)), columns=['word', 'rarity']))
        self.df.sort_values(by="rarity", ascending=False, inplace=True)
    

    def count(self, word: str) -> int:
        selected = self.df[self.df['word'] == word]
        if selected.empty:
            return 0
        return selected.iloc[0]["rarity"]
