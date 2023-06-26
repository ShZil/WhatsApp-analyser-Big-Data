# Util ----------------------------------------------------------------------------------------------------------
from math import sqrt

import pandas as pd

import Alphabets
import BlocksDataFrame
import IOCDataFrame
import os

import MessageTypeDataFrame
import NormalDataFrame
import TimeDataFrame
import color
from bidi.algorithm import get_display as bidir


CHAT_PATH = 'raw'


class Time:
    times = []
    # [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]] // count = 3

    @staticmethod
    def append(t):
        Time.times.append(t)

    @staticmethod
    def get():
        n = 10
        return [tuple(Time.times[i:i + n]) for i in range(0, len(Time.times), n)]


def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def is_nan(num):
    return num != num


def two_digits(num):
    return str(num).zfill(2)


def get_paths(names):
    return [f"WhatsApp Chat with {name}.txt" for name in names]


def get_names(paths):
    return [path[len(CHAT_PATH + "/WhatsApp Chat with "):path.find(".txt")] for path in paths]


def remove_unwanted_chars(string):
    return string.strip('\n \"').replace("\u200e", "").replace("\u202b", "").replace("\u202c", "")


def character_name(char):
    return "Space" if char == " " else char


def stringify_weekday(n):
    return (["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])[n]


def stringify_month(month_id):
    return f"{two_digits(month_id % 12 + 1)}/{two_digits(month_id // 12)}"  # TODO: refactor


def fix_rtl(strings):
    return [
        string[::-1]
        .replace(')', '(')
        .replace('(', ')')
        if Alphabets.count_hebrew(string) > 0
        else string
        for string in strings
    ]


def ioc(string):
    # Returns the square root of the Index Of Coincidence of a string.
    # ioc = sum(count * (count-1)) where count is every character's appearance count.
    # Divided by length * (length-1)
    if len(string) < 2:
        return 0
    thick = {string.count(char) for char in set(string)}
    ioc = sum([x * (x - 1) for x in thick])
    return sqrt(ioc / (pow(len(string), 2) - len(string)))


def percentages(start, end, jump):
    return list(frange(start / 100, end / 100, jump / 100)), [str(x) + '%' for x in range(start, end + 1, jump)]


def frange(x, y, jump):
    while x <= y:
        yield x
        x += jump


def find_avgs(ndf, idf, bdf, tdf):
    ioc_avg = list(IOCDataFrame.per_month(idf, tdf)['ioc'])
    block_avg = list(BlocksDataFrame.per_month(bdf, tdf)['avg-char-count'])
    return ioc_avg, block_avg


def pride():
    return ['Red', 'Orange', 'Yellow', 'Green', 'Turquoise', 'Blue', 'Violet']


def date(st):
    for char in st:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/', ':', ',', ' ', '.', '[', ']']:
            return False
    return st.count('/') == 2 or st.count('.') == 2


def get_files(extend):
    all_files = os.listdir(path="./" + CHAT_PATH)
    all_txt = list(filter(lambda x: x.endswith(extend), all_files))
    paths = [CHAT_PATH + '/' +
    file for file in all_txt]
    return paths, get_names(paths)


def warn_user(render_names, names):
    if len(set(render_names) - set(names)) == 0 or set(render_names) == {"*"}:
        return
    print("Not all render requests are present in the folder. Missing:")
    print(', '.join(set(render_names) - set(names)))


def progress(value, array, shape):
    index = array.index(value)
    length = len(array)
    return (len(max(array, key=len)) - len(value) + 2) * " " + shape[0] + (index+1)*shape[1] + shape[2] * (length-index-1) + shape[3]


# Filters / Group-By -------------------------------------------------------------------------------------------------

def filter_author(df, allowed_author):
    return df[df.author == allowed_author]


def select_month(df, time_df, allowed_month_id):
    t = time_df.df[time_df.df['monthly-index'] == allowed_month_id]
    n = df[df.index.isin(list(t.index))]
    return n, t


def parse_settings():
    with open("settings.txt", 'r', encoding="utf8") as f:
        lines = f.readlines()
    d = {
        "render_names": [],
        "generate_names": [],
        "joins_names": [],
        "titles_names": [],
        "filter_names": [],
        "render_final": False,
        "optimize": False,
        "colored": True,
        "save_metadata": False
    }
    for line in lines:
        key, value = line.strip("\n").split(":", 1)
        value = value.strip(' ')
        if type(d[key]) == bool:
            d[key] = value.lower() == "true" or value == "1"
        else:
            d[key] = [x.strip(' "') for x in value.strip('[]').split(",")]
            d[key] = [] if d[key][0] == "" else d[key]
    return d


# Pseudo DataFrames
def participant_queue(ndf, mtdf):
    queue = []
    for inc in range(len(list(mtdf.df['ind']))):
        ind, mtype, mtauthor, arg = mtdf.row(inc)
        date, time, author, message = ndf.row(ind)
        if mtype == "participant-join":
            queue.append(date + ', ' + time + ':\n    ' + color.GREEN +
                         '\n    '.join(join_message(message)) + color.END)
        if mtype == "participant-leave":
            queue.append(date + ', ' + time + ':\n    ' + color.RED +
                         '\n    '.join(leave_message(message)) + color.END)
    return '\n'.join(queue)


def leave_message(text):
    return [text[:text.find(" left")], "left"]


def join_message(text):
    if "joined using this group\'s invite link" in text:
        return [text[:text.find(" joined using this group\'s invite link")], "joined using an invite link"]
    elif "was added" in text:
        if "and" in text[:text.find(" was added")]:
            return [text[:text.find(" was added")].replace("and", ","), "were added"]
        else:
            return [text[:text.find(" was added")], "was added"]
    elif "added" in text:
        if "and" in text[text.find("added ") + len("added "):]:
            return [text[text.find("added ") + len("added "):].replace("and", ","),
                    "were added by " + text[:text.find(" added")]]
        else:
            return [text[text.find("added ") + len("added "):], "was added by", text[:text.find(" added")]]
    else:
        return ["Error", "Here"]


def titles_queue(ndf, mtdf, colored):
    queue = []
    for inc in range(len(list(mtdf.df['ind']))):
        ind, mtype, mtauthor, arg = mtdf.row(inc)
        date, time, author, message = ndf.row(ind)
        if mtype == "title-change":
            queue.append(date + ', ' + time + ':    ' + (color.YELLOW if colored else '') +
                         '\n'.join(title_message(message, colored)) + (color.END if colored else ''))
    return '\n'.join(queue)


def title_message(text, colored):
    return [(color.YELLOW if colored else '') + remove_unwanted_chars(text[:text.find(" changed the subject from ")]) + (color.END if colored else '') + ' changed the title.',
            (color.YELLOW if colored else '') + remove_unwanted_chars(text[text.find(" changed the subject from ") + len(" changed the subject from "):text.find(" to ")]) + (color.END if colored else ''),
            ' → ',
            (color.YELLOW if colored else '') + remove_unwanted_chars(text[text.find(" to ") + len(" to "):])]


def title_sequence(ndf, mtdf, colored):
    queue = []
    for inc in range(len(list(mtdf.df['ind']))):
        ind, mtype, mtauthor, arg = mtdf.row(inc)
        date, time, author, message = ndf.row(ind)
        if mtype == "title-change":
            if message.find(" to ") == -1:
                continue
            if len(queue) == 0:
                queue.append('\n'.join(title_message(message, colored)[1:2]))
            else:
                queue.append('\n'.join(title_message(message, colored)[3:]))
    return '\n'.join(queue)


def titles_list(ndf, mtdf, colored, to_print=False):
    yellow, end = color.YELLOW, color.END
    if not colored:
        yellow = end = ""
    queue = []
    for inc in range(len(list(mtdf.df['ind']))):
        ind, mtype, mtauthor, arg = mtdf.row(inc)
        date, time, author, message = ndf.row(ind)
        if mtype == "title-change":
            if message.find(" to ") == -1:
                continue
            else:
                queue.append(message[message.find("from ") + len("from "):message.find(" to ")].strip(' ').strip('\"'))
                queue.append(message[message.find(" to ")+len(" to "):].strip(' ').strip('\"'))
        elif mtype == "group-created":
            queue.append(message[message.find("created group")+len("created group"):].strip(' ').strip('\"'))
    return ''.join([yellow + e + end + '\n' for e in non_repeating_list(queue, ndf.get_authors(), colored, to_print)])


def non_repeating_list(list0, authors, colored, to_print=False):
    # This function returns a list where no item is equal to the next, but there can be duplicates, just not immediately
    # [1, 1, 2, 1, 3, 3, 3, 3, 4, 2, 2] -> [1, 2, 1, 3, 4, 2]
    underline, end, yellow = color.UNDERLINE, color.END, color.YELLOW
    if not colored:
        underline = end = yellow = ""
    if "WhatsApp" in authors:
        authors.remove("WhatsApp")
    authors.sort()
    if not list0:
        if len(authors) == 1:
            return ["Private WhatsApp Chat of " + underline +
                    authors[0] + end + yellow]
        else:
            return ["WhatsApp Chat between " + ' and '.join([underline + (bidir(author) if to_print else author) + end + yellow for author in authors])]
    if colored: print("Titles:")
    to_return = [list0[0]]
    for element in list0:
        if element != to_return[len(to_return) - 1]:
            to_return.append(element)
    return to_return


def common_names(ndf, wdf):
    print("Most commonly used participants' names:")
    authors = ndf.get_authors()
    try:
        authors.remove("WhatsApp")
    except ValueError:
        pass
    names = []
    for author in authors:
        names.extend(author.split(' '))
    names = list(set(names))
    values = [wdf.count(name) for name in names]
    for name, value in sorted(zip(names, values), key=lambda tup: tup[1], reverse=True)[:20]:
        if value > 0:
            print(f"    {name}: {value}")
    print()
