from Tkinter import Tk, Label, Button


#class MyFirstGUI:
def __init__(self, master):
    self.master = master
    master.title("")

    self.label = Label(master, text="Web Pages in Python")
    self.label.pack()


    quote = """At present, only GIF and PPM/PGM
    formats are supported, but an interface
    exists to allow additional image file
    formats to be added easily."""

    self.L1 = Label(master, text = quote)
    self.L1.pack()

    self.text = Text(master)
    self.text.insert(END, "Hello.....")
    self.text.pack()

    self.button = Button(master, text="Go to some other page")#, command = recursive.n)
    self.button.pack()

    self.buttonClose = Button(master, text="Go to a random page")# , command = recursive.n)
    self.buttonClose.pack()

    self.close_button = Button(master, text="Close", command=master.quit)
    self.close_button.pack()



root = Tk()
#my_gui = MyFirstGUI(root)
root.mainloop()
