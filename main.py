# For 'Repl.it'.

import os
import sys

try:
    input = raw_input
except NameError:
    pass

success = False

demos = (
    "Basic",
    "WithCSS",
)

demosAmount = len(demos)


while not success:
    for id in range(0, demosAmount):
        print(chr(id + ord('a')) + ": " + demos[id])

    lastChar = chr(demosAmount + ord('a') - 1)

    demoId = input("Select one of above demos ('a' or 'b') : ").lower()

    try:
        demo = demos[ord(demoId) - ord('a')] + "." + "py"
    except:
        pass
    else:
        if True:  # Simplifies debugging when set to False
            try:
                __import__(demo)
            except ImportError:
                print("'" + demo + "' not found!")
            except IndexError:
                pass
            else:
                success = True
        else:
            __import__(demo)
