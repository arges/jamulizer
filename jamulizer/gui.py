"""tkinter gui"""

from tkinter import Frame, Label

class Application(Frame):
    """ tkinter main application frame """

    def create_label(self, name):
        label = Label(self)
        label["text"] = name + ": "
        label["font"] = ("Courier", 72, "bold")
        label["fg"] = "#ffffff"
        label["bg"] = "#000000"
        label.pack({"side": "top", "fill": "x", "anchor": "w", "expand": True})
        return label

    def create_widgets(self):
        self.chords = self.create_label("Chords")
        self.key = self.create_label("Key")
        self.notes = self.create_label("Notes")
        self.bass = self.create_label("Bass")

    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()
        self.pack()
        master.title("jamulizer")
        master["bg"] = "#000000"

    def set_label(self, chord, key, notes, bass):
        self.chords["text"] = " Chord: {0: <20}".format(str(chord))
        self.key["text"] = " Key:   {0: <20}".format(str(key))
        self.notes["text"] = " Notes: {0: <20}".format(str(",".join(notes)))
        self.bass["text"] = " Bass:  {0: <20}".format(str(bass))
