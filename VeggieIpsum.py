import sublime
import sublime_plugin
import random
import re

class VeggieIpsumCommand(sublime_plugin.TextCommand):

    def run(self, edit, qty=10):

        selections = self.view.sel()
        for selection in selections:

            # always start with Veggie ipsum for first output
            para = "Veggies es bonus vobis "

            # words from veggieipsum.com
            words = "proinde vos postulo essum magis kohlrabi welsh onion daikon amaranth tatsoi tomatillo melon azuki bean garlic gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette tatsoi pea sprouts fava bean collard greens dandelion okra wakame tomato. Dandelion cucumber earthnut pea peanut soko zucchini".split()

            # get preceding numbers (possibly with decimal separation) if available
            lastchars = self.view.substr(sublime.Region(selection.begin()-20, selection.end()))
            last = re.search("(|(\d+)(\.\d+)?)$", lastchars).group(0)

            m = str(last).split(".")

            if re.search("\d", last) and (
                (len(m) > 1 and (int(m[0]) * int(m[1])) < 1000)
                or (len(m) == 1 and int(m[0]) < 1000)
            ):
                selection = sublime.Region(selection.begin() - len(str(last)), selection.end())
            else:
                # if they wasked for too much lorem, just give 'em one - for their own safety!
                last = 1
            # could give error instead - but who wants to think that much about lorem?
            # else:
            #     print("[ERROR] too much lorem ipsum - try a smaller number")

            m = str(last).split(".")
            paras = int(m[0])

            if len(m) > 1:
                qty = int(m[1])

            for i in list(range(0, paras)):
                from random import choice
                para += choice(words).capitalize() + " "
                for x in list(range(random.randint(int(qty - qty/3)-2, int(qty + qty/3)-2))):
                    para += choice(words) + " "
                para += choice(words) + "."
                if i != paras and paras > 1:
                    para += "\n\n"

            # erase region
            self.view.erase(edit, selection)

            last = self.view.substr(sublime.Region(selection.begin()-1, selection.end()))
            if last == ".":
                para = " " + para

            # insert para before current cursor position
            self.view.insert(edit, selection.begin(), para)

            self.view.end_edit(edit)

