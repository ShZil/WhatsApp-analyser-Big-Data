# Filtering ------------------------------------------------------------------------------------------------------------
from math import floor
from import_handler import ImportDefence
with ImportDefence():
    import matplotlib.patches as mpatches
    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    from bidi.algorithm import get_display as bidir

import Alphabets
import AlphabetsDataFrame
import MessageTypeDataFrame
import color
import IOCDataFrame
import NormalDataFrame
import TimeDataFrame
import util


def start(name, ndf, tdf, mtdf, idf, adf):
    while input(f"{color.GREEN}Do a filter? {color.END}").lower() in ["yes", "y", "yeah", "yep", "yup", "yea", "ye", "true"]:
        print(f"{color.END}Applying filter to chat with {color.UNDERLINE}{name}{color.END}{color.GREEN}.")
        print("Information sets (Available variables):")
        data = Message.attributes(ndf, tdf, mtdf, idf, adf)
        for att, info in data.items():
            sep = ': '
            data = ''
            if isinstance(info, list):
                data = f"could be {', '.join(info)}."  # check this (`type` attribute)
            elif isinstance(info, tuple):
                data = f"from {info[0]} to {info[1]}"
            elif isinstance(info, str):
                data = f"{info}"
            else:
                sep = ''
            print(f"    {color.GREEN}{color.UNDERLINE}{att}{color.END}{color.GREEN}{sep}{color.END}{color.CYAN}{data}")

        print(f"{color.GREEN}Type your filter (python condition syntax).{color.WHITE}")
        display = input()
        print("\n")
        count = 0
        index = 0
        try:
            for i in range(ndf.shape[0]):
                index += 1
                date, time, author, text = ndf.row(i)
                
                progress_width = 30
                progress = int(progress_width * index / ndf.shape[0])
                left = int(progress_width - progress)
                print(f"{color.END}[{'-' * progress}{' ' * left}]", end='\r')

                if condition_met(display, i, ndf, tdf, mtdf, idf, adf):
                    print(f"{i} {color.CYAN}{date}{color.END}, {color.DARKCYAN}{time}{color.END} - {color.GREEN}{color.BOLD}{bidir(author)}{color.END}: {bidir(text)}{color.END}")
                    count += 1
            print(f"____________________________________________________________")  # Change to continuous lines (special charater)
            print(f"{color.BOLD}{count} message(s) passed the filter.{color.END} ({percent(count, int(ndf.shape[0]))}%)")
        except KeyboardInterrupt:
            print(f"____________________________________________________________")
            print(f"{color.BOLD}(^C) pressed. Skipping.{color.END}")
            print(f"{color.BOLD}{count} message(s) passed the filter.{color.END} ({percent(count, index)}%)")
            print(f"{color.BOLD}{index} message(s) checked; {int(ndf.shape[0]) - index} message(s) are left unchecked.{color.END}")
        # Add longest/shortest message that passed? Or some other (custom) criteria for sorting (max/min)?


def percent(count: int, length: int) -> float:
    return floor(10000 * count / length) / 100


def condition_met(display, i, ndf, tdf, mtdf, idf, adf):
    # Add 'next' or 'prev' messages so I can do like "next.type = media" for all messages one-before a media.
    # Add ranges for 'after' or 'before'?
    # Maybe even print all the messages to a text file and open it once the filter finishes? (Optional for the user)
    # Ask the user whether they want the messages or just the count and statistics
    # Add more statistics! (Shortest, longest, most alphabets, etc.)
    # Custom graph from the filtered messages?
    message = Message(i, ndf.row(i), tdf.row(i), MessageTypeDataFrame.message_at(mtdf.df, i), idf.row(i), adf.row(i))
    return evaluate(display, message)


class Message:
    def __init__(self, index, ndf_row, tdf_row, mtdf_row, idf_row, adf_row):
        self.index = index
        self.date, self.time, self.author, self.text = ndf_row
        self.time = self.time.split(':')[0].zfill(2) + ':' + self.time.split(':')[1].zfill(2)
        self.minute, self.hour, self.day, self.month, self.year, self.weekday, self.monthly_index, self.day_id = tdf_row
        self.ind, self.type, self.mtauthor, self.arg = mtdf_row
        self.ioc = idf_row[0]
        self.length, self.english, self.hebrew, self.punctuation, self.math, self.emojis, self.whitespace = adf_row
    

    def to_dict(self):
        return {
            "index": int(self.index),
            "date": self.date,
            "time": self.time,
            "author": self.author,
            "text": self.text,
            "minute": int(self.minute),
            "hour": int(self.hour),
            "day": int(self.day),
            "month": int(self.month),
            "year": int(self.year),
            "weekday": int(self.weekday),
            "monthly_index": int(self.monthly_index),
            "day_id": int(self.day_id),
            "ind": int(self.ind),
            "type": self.type,
            "mtauthor": self.mtauthor,
            "arg": self.arg,
            "ioc": float(self.ioc),
            "length": int(self.length),
            "english": int(self.english),
            "hebrew": int(self.hebrew),
            "punctuation": int(self.punctuation),
            "math": int(self.math),
            "emojis": int(self.emojis),
            "whitespace": int(self.whitespace)
        }
    
    @staticmethod
    def attributes(ndf, tdf, mtdf, idf, adf):
        return {
            "index": (0, ndf.shape[0] - 1),
            "date": "DD/MM/YYYY",
            "time": "HH:mm",
            "author": None,
            "text": None,
            "minute": (0, 59),
            "hour": (0, 23),
            "day": (1, 31),
            "month": (1, 12),
            "year": "YYYY",
            "weekday": ("0 = Monday", "6 = Sunday"),
            "monthly_index": "YYYY*12 + MM",
            "day_id": "YYYY*12*31 + MM*31 + DD",
            "ind": "MTDF's index (identical to `index`).",
            "type": list(reversed(["nan", "whatsapp-info", 'group-created', 'participant-join', 'title-change', 'description-change', 'settings-change', 'icon-change', 'admin', 'participant-leave', 'block', 'unblock', "deleted", "media", "text"])),
            "mtauthor": "MTDF's author (maybe identical to `author`, might contain other information; depends on `type`).",
            "arg": "MTDF's additional information.",
            "ioc": (0.0, 1.0),
            "length": "The length (character count) of the message.",
            "english": "How many letters are A-Z / a-z?",
            "hebrew": "How many letters are ת-א?",
            "punctuation": "How many letters are punctuation symbols? (like + . , :)",
            "math": "How many letters are digits 0-9?",
            "emojis": "How many emojis? (i.e. not any other category)",
            "whitespace": "How many letters are \" \"?"
        }


def evaluate(display, message):
    try:
        value = eval(display, {}, message.to_dict())
    except (SyntaxError, NameError, TypeError, ZeroDivisionError, KeyError):
        # print(display, message.to_dict())
        return False
    return value is True
