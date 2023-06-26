import os

import pandas as pd
from timeit import default_timer as timer

import util


def to_messages(path):
    time = timer()
    with open(path, 'r', encoding="utf8") as f:
        lines = f.readlines()
    messages = []
    i = -1
    for line in lines:
        line = line.replace('\u200E', '')
        if util.date(line[0:12]):
            i += 1
            # first line in message
            try:
                if '[' in line and ']' in line and line.index(']') < line.index(':', line.index(':', line.index(':') + 1) + 1):
                    line = line.replace('[', '')
                    line = line[0:util.find_2nd(line, ':')] + line[util.find_2nd(line, ':')+3:]
                    line = line.replace(']', ' -')
            except (ValueError, IndexError):
                pass
            messages.append(line)
        elif i == -1:
            print("Invalid file!")
            return None
        else:
            messages[i] += line
    util.Time.append(timer() - time)
    return messages


def get_dfs(name):
    try:
        return (pd.read_csv(f'saved/{name}/chat_messages.csv', header=0, index_col='index'),
                pd.read_csv(f'saved/{name}/chat_time.csv', header=0, index_col='index'),
                pd.read_csv(f'saved/{name}/chat_characters.csv', header=0, index_col='char'),
                pd.read_csv(f'saved/{name}/chat_message_types.csv', header=0, index_col='index'),
                pd.read_csv(f'saved/{name}/chat_words.csv', header=0, index_col='index'),
                pd.read_csv(f'saved/{name}/chat_ioc.csv', header=0, index_col='index'),
                pd.read_csv(f'saved/{name}/chat_blocks.csv', header=0, index_col='index'))
    except FileNotFoundError:
        print(f"`saved/{name}/chat_....csv` were not found. Try to generate the Database again.")
        return (None,) * 7


def get_df(name):
    try:
        return pd.read_csv(f'saved/{name}/chat.csv', header=0)
    except FileNotFoundError:
        print(f"`saved/{name}/chat.csv` not found. Try to generate the Database again.")
        return None


# File Saving ----------------------------------------------------------------------------------------------------------

def save_df(df, name):
    folder(name)
    df.index.name = 'index'
    df.to_csv(f'saved/{name}/chat.csv', encoding="utf-8")


def save_dfs(mdf, tdf, cdf, mtdf, wdf, idf, bdf, name):
    folder(name)
    mdf.index.name = 'index'
    tdf.index.name = 'index'
    if cdf is not None:
        cdf.index.name = 'char'
    mtdf.index.name = 'index'
    if wdf is not None:
        wdf.index.name = 'index'
    idf.index.name = 'index'
    bdf.index.name = 'index'
    mdf.to_csv(f'saved/{name}/chat_messages.csv', encoding="utf-8")
    tdf.to_csv(f'saved/{name}/chat_time.csv', encoding="utf-8")
    if cdf is not None:
        cdf.to_csv(f'saved/{name}/chat_characters.csv', encoding="utf-8")
    mtdf.to_csv(f'saved/{name}/chat_message_types.csv', encoding="utf-8")
    if wdf is not None:
        wdf.to_csv(f'saved/{name}/chat_words.csv', encoding="utf-8")
    idf.to_csv(f'saved/{name}/chat_ioc.csv', encoding="utf-8")
    bdf.to_csv(f'saved/{name}/chat_blocks.csv', encoding="utf-8")


def folder(name):
    if not os.path.exists(f"saved/{name}"):
        os.makedirs(f"saved/{name}")


def save(string, foldr, name):
    folder(foldr)
    df = pd.DataFrame(string.split('\n'), columns=[name])
    df.to_csv(f'saved/{foldr}/chat_{name}.csv', encoding="utf-8")
