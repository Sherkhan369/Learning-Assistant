# main.py

import sys
from gui import run_gui
from gui import run_cli
from scheduler import run_scheduler

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'cli':
            run_cli()
        elif sys.argv[1] == 'scheduler':
            run_scheduler()
        else:
            print("wrong argument 'cli' or'scheduler' use")
    else:
        run_gui()

if __name__ == "__main__":
    main()
