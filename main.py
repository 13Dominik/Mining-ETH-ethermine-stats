from src import *
from GUI import *


def main():
    root = Tk()
    e = GUI(root)
    e.pack(fill=BOTH, expand=YES)
    root.mainloop()


if __name__ == '__main__':
    main()
