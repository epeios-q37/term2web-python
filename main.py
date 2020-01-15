# For 'Repl.it'.

import os,sys

if ('HOME' in os.environ) and (os.environ['HOME'] == '/home/runner'):
  os.environ["ATK"] = "REPLit"

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
    for id in range(0,demosAmount):
        print(chr(id + ord('a')) + ": " + demos[id]) 
        
    lastChar = chr(demosAmount + ord('a') - 1)
        
    demoId = input("Select one of above demos ('a' or 'b') : ").lower()
   
    try:
        demo = demos[ord(demoId) - ord('a')] + "." + "py"
        
        # Below line is needed by 'Repl.it'.
        sys.argv[0]=demos[ord(demoId) - ord('a')] + "/"

        if True:  # Simplifies debugging when set to False
            try:
                __import__(demo)
            except ImportError:
                print("'" + demo + "' not found!")
            else:
                success = True
        else:
            __import__(demo)
    except Exception:
        pass