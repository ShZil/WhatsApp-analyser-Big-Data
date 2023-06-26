from Alphabets import count_hebrew
from import_handler import ImportDefence
with ImportDefence():
    import matplotlib.pyplot as plt
    import pandas as pd
    from bidi.algorithm import get_display as bidir

from AlphabetsDataFrame import AlphabetsDataFrame
from BlocksDataFrame import BlocksDataFrame
from CharacterDataFrame import CharacterDataFrame
from IOCDataFrame import IOCDataFrame
from MessageTypeDataFrame import MessageTypeDataFrame
from TimeDataFrame import TimeDataFrame
from NormalDataFrame import NormalDataFrame
from WordsDataFrame import WordsDataFrame

import start
import util
import warnings
import color
import render
import files
import filterer


# TODO: Reply time for messages, reply patterns (phrase matching).
# Consider word distribution per author (across chats), not one chat.
# Then clean the code,
# And to github you shall upload
# Length in months of chat
# Most common letters by alphabet (e.g. most common emojis)
# Whom do I mostly talk to? - Comparison of talking hours (00-24), weekdays (1-7), months (0-inf)
# Conversations - separate by time intervals, select Conversations and calculate average length
# Percentage of Media and Voice messages
# frequency of given selected word or character graph.
# Probability of rare phrases raises if previous message includes some rare phrase (conditional probability)
# Most common names (collision between participants' names and most common words. Note that a participant's name might include spaces)
# graph of message count per day
# Split alphabets render by user
# Time estimate for generation, assuming linear growth O(n)


# Main -----------------------------------------------------------------------------------------------------------------

def main():
    warnings.filterwarnings("ignore")
    paths, names = util.get_files('.txt')
    settings = util.parse_settings()
    colored = settings["colored"]
    render_names = settings["render_names"]
    generate_names = settings["generate_names"]
    joins_names = settings["joins_names"]
    titles_names = settings["titles_names"]
    filter_names = settings["filter_names"]
    optimize = settings["optimize"]
    save_metadata = settings["save_metadata"]
    render_final = settings["render_final"]
    if not colored:
        color.uncolor()
        start.uncolor()
    relations = []
    counts = []

    start.print_settings(settings)
    start.prints(names, util.get_files('.txt.ignore')[1], render_names, generate_names, joins_names, titles_names)

    for path, name in zip(paths, names):
        if name in generate_names or generate_names == ["*"]:
            print("Generating chat with " + color.UNDERLINE + name + color.END + ". " +
                  color.RED + util.progress(name, names, "[- ]") + color.END + color.GREEN)
            util.Time.append(name)
            print("[         ]", end="      \r")
            messages = files.to_messages(path)
            print("[█        ]", end="      \r")
            ndf = NormalDataFrame(messages)
            files.save_df(ndf.df, name)
            print("[██       ]", end="      \r")
            adf = AlphabetsDataFrame(ndf, True)
            print("[███      ]", end="      \r")
            bdf = BlocksDataFrame(ndf, True)
            print("[████     ]", end="      \r")
            cdf = CharacterDataFrame(ndf, not optimize) if not optimize else None
            print("[█████    ]", end="      \r")
            idf = IOCDataFrame(ndf, True)
            print("[██████   ]", end="      \r")
            mtdf = MessageTypeDataFrame(ndf, True)
            print("[███████  ]", end="      \r")
            tdf = TimeDataFrame(ndf, True)
            print("[████████ ]", end="      \r")
            wdf = WordsDataFrame(ndf, mtdf, not optimize) if not optimize else None
            print("[█████████]" + color.END)
        else:
            print(color.END + "Loading chat with " + color.UNDERLINE + name + color.END + ". " +
                  color.RED + util.progress(name, names, "[- ]") + color.END + color.GREEN)
            ndf = files.get_df(name)
            adf, tdf, cdf, mtdf, wdf, idf, bdf = files.get_dfs(name)
            if ndf is None or tdf is None:
                continue

        relations.append(util.find_avgs(ndf, idf, bdf, tdf))
        counts.append(len(ndf))

        if name in joins_names or joins_names == ["*"]:
            if colored:
                print(color.END)
            print(util.participant_queue(ndf, mtdf))
            print("Participants:")
            for author in ndf.get_authors():
                print('    ' + bidir(author))
            if not optimize:
                util.common_names(ndf, wdf)
        if name in titles_names or titles_names == ["*"]:
            if colored:
                print(color.END)
            print(util.titles_list(ndf, mtdf, colored, to_print=True))
            if save_metadata:
                files.save(util.titles_list(ndf, mtdf, False), name, "titles")
        files.save_dfs(adf, tdf, cdf, mtdf, wdf, idf, bdf, name)
        if name in render_names or render_names == ["*"]:
            n = names if render_names == ["*"] else render_names
            render.renders(name, n, ndf, adf, tdf, cdf, mtdf, wdf, idf, bdf)
        if name in filter_names or filter_names == ["*"]:
            filterer.start(name, ndf, tdf, mtdf, idf, adf)

    if render_final:
        render.render_relations(names, relations)
    if generate_names:
        times = pd.DataFrame(util.Time.get(), columns=['Name', 'Messages', 'NDF', 'ADF', 'BDF', 'CDF', 'IDF', 'MTDF', 'TDF', 'WDF'])
        lengths = pd.DataFrame(zip(names, counts, [len(open(path, 'r', encoding='utf-8').readlines()) for path in paths]), columns=['Name', 'Count', 'Rows'])
        fig, (ax1, ax2) = plt.subplots(2, 1)
        render.display_lengths(lengths, ax1)
        render.display_times(times, ax2)
        print("\nTime it took to generate each DataFrame (s):")
        print(times)


if __name__ == '__main__':
    main()
