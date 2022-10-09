import sys
from tkinter import Tk
from MyFrame import MyFrame 
 
def main():
    root = Tk()
    root.geometry("400x400")
    root.resizable(0,0)
    app = MyFrame(root)   #creates a frame of 300x300 pixels
    root.mainloop()   
 
if __name__ == "__main__":
    sys.exit(int(main() or 0)) 