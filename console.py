import curses

stdscr = curses.initscr()

def print_char(x, y, char):
    stdscr.addch(y, x, char)
    
print_char(10,10, "here is the console")