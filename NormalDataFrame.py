# Regular DF -----------------------------------------------------------------------------------------------------------
import pandas as pd
from timeit import default_timer as timer
from Data import Data

import util

class NormalDataFrame(Data):
    def __init__(self, messages: list):
        temp = timer()
        texts = []
        dates = []
        times = []
        authors = []
        for index in range(len(messages)):
            # FORMAT: "mm/dd/yy, HH:MM - [Author]: [message]"
            message = messages[index]
            date = message[:message.find(',')]
            time = message[message.find(', ') + 2:message.find(' - ')]
            author = util.remove_unwanted_chars(message[message.find(' - ') + 3:util.find_2nd(message, ':')])
            text = util.remove_unwanted_chars(message[util.find_2nd(message, ':') + 1:])
            if util.find_2nd(message, ':') == -1:
                author = "WhatsApp"
                text = util.remove_unwanted_chars(message[message.find(' - ') + 3:])
            elif "created group" in author or "changed the" in author:
                text = author
                author = "WhatsApp"
            texts.append(text)
            times.append(time)
            dates.append(date)
            authors.append(author)
            print(" NDF -", index, "      ", end='\r')

        util.Time.append(timer() - temp)
        super().__init__(pd.DataFrame(list(zip(dates, times, authors, texts)),
                                    columns=['date', 'time', 'author', 'message']))


    def get_authors(self):
        return list(set([self.row(i)[2] for i in range(len(self))]))


def avg(nd):
    try:
        return sum([len(string) for string in nd['message']]) / len(nd)
    except ZeroDivisionError:
        return 0
