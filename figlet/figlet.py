import sys
from pyfiglet import Figlet
f = Figlet(font='slant')
g = Figlet()



# Default Prompt
for i in sys.argv:
    if len(sys.argv) == 1:
        text = input("Input: ")
        print("output:",g.renderText(text))

    elif len(sys.argv) != 3:
        sys.exit("Invalid usage")


# Scan for Command Line Argument
for i in sys.argv:
    if len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--f':
            f = Figlet(font=sys.argv[2])
            text = input("Input: ")
            print ("output:",f.renderText(text))
            sys.exit()

        else:
            sys.exit("Invalid usage")


print(f"SysArgv1 = {sys.argv[1]}")



