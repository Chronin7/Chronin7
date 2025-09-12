import curses

def get_single_char():
	screen = curses.initscr()
	curses.noecho()
	curses.cbreak()
	char = screen.getch()
	curses.endwin()
	return chr(char)

print("Press any key:")
key = get_single_char()
print(f"You pressed: {key}")