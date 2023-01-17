import util
import color

cset = color.PURPLE
cnames = color.BLUE
crender = color.CYAN
cgenerate = color.DARKCYAN


def prints(names, ignored, render_names, generate_names, joins_names, titles_names):
    print(cnames + color.UNDERLINE + f"Chats" + color.END + cnames + ": " + (', '.join(names)) + color.END)
    print(cnames + color.UNDERLINE + f"Ignored" + color.END + cnames + ": " + (', '.join(ignored)) + color.END)
    print(crender + color.UNDERLINE + f"Will Render" + color.END + crender + ": " +
          (color.BOLD + "All" if render_names == ["*"] else
           color.BOLD + "None" if render_names == [] else ', '.join(render_names)) + color.END)
    print(cgenerate + color.UNDERLINE + f"Will Generate" + color.END + cgenerate + ": " +
          (color.BOLD + "All" if generate_names == ["*"] else
           color.BOLD + "None" if generate_names == [] else ', '.join(generate_names)) + color.END)
    print(crender + color.UNDERLINE + f"Joins queue" + color.END + crender + ": " +
          (color.BOLD + "All" if joins_names == ["*"] else
           color.BOLD + "None" if joins_names == [] else ', '.join(joins_names)) + color.END)
    print(cgenerate + color.UNDERLINE + f"Title list" + color.END + cgenerate + ": " +
          (color.BOLD + "All" if titles_names == ["*"] else
           color.BOLD + "None" if titles_names == [] else ', '.join(titles_names)) + color.END)

    util.warn_user(render_names, names)


def print_settings(settings):
    print(color.ize((cset, color.BOLD), "Starting with settings:"))
    print("    " + color.ize((cset, color.UNDERLINE), "render mutual graph(s)"), end="")
    print(color.ize(cset, ": " + str(settings["render_final"])))
    print("    " + color.ize((cset, color.UNDERLINE), "optimize"), end="")
    print(color.ize(cset, " (don't generate time-consuming data): " + str(settings["optimize"])))
    print("    " + cset + color.UNDERLINE + f"use ANSI coloring" + color.END +
          cset + f": " + str(settings["colored"]))
    print("    " + cset + color.UNDERLINE + f"save metadata" + color.END +
          cset + f" (i.e. title history): " + str(settings["save_metadata"]))


def uncolor():
    global cset
    global cnames
    global crender
    global cgenerate
    cset = ''
    cnames = ''
    crender = ''
    cgenerate = ''
