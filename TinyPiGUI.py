import tkinter as tk
import Main as le
from Main import CutOneLineTokens


class TinyPiGUI:
    def __init__(self):
        self.currLineNum = 0.0

        #Window
        self.root = tk.Tk()
        self.root.geometry("1000x750")
        self.root.resizable(False, False)
        self.root.title("TinyPi")

        #Header
        self.label = tk.Label(self.root, text="Lexical Analyzer for TinyPi", font=("Arial", 18), bg='green')
        self.label.pack(padx=20, pady=20)

        #Grid Layout
        self.framehi = tk.Frame(self.root)
        self.framehi.columnconfigure(0, weight=2)
        self.framehi.columnconfigure(1, weight=1)
        self.framehi.columnconfigure(2, weight=2)
        self.framehi.rowconfigure(0, weight=1)
        self.framehi.rowconfigure(1, weight=2)
        self.framehi.rowconfigure(2, weight=1)
        self.framehi.rowconfigure(3, weight=1)

        #Left and right headers
        self.headerL = tk.Label(self.framehi, text="Source Code Input:", font=("Arial", 18))
        self.headerL.grid(row=0, column=0, sticky=tk.W)

        self.headerR = tk.Label(self.framehi, text="Lexical Analyzed Result:", font=("Arial", 18))
        self.headerR.grid(row=0, column=2, sticky=tk.W)

        #Counter
        self.counter = tk.Label(self.framehi, text="Current Line: " + str(self.currLineNum)[0], font=("Arial", 18))
        self.counter.grid(row=2, column=0, sticky=tk.W)

        #Button event
        def nextLineButtonClick(event=None):
            self.textboxR.delete(1.0, tk.END)
            currLine = self.textboxL.get(self.currLineNum, str(self.currLineNum) + " lineend")
            hi = le.CutOneLineTokens(currLine)
            self.currLineNum = self.currLineNum + 1.0 #increment line by one
            self.counter.config(text="Current Line: " + str(self.currLineNum)[0])
            self.textboxR.insert(tk.END, str(hi) + "\n")

        #Textboxes
        self.textboxL = tk.Text(self.framehi, font=('Arial', 16))
        #textboxL.bind("<Return>",nextLineButtonClick())
        self.textboxL.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.textboxR = tk.Text(self.framehi, font=('Arial', 16))
        self.textboxR.grid(row=1, column=2, sticky=tk.W+tk.E)
        self.textboxR.bind("<Return>",nextLineButtonClick())


        #Buttons
        self.button1 = tk.Button(self.framehi, text="Next Line!", command=nextLineButtonClick)
        self.button1.grid(row=3, column=0, sticky=tk.W+tk.E)

        button2 = tk.Button(self.framehi, text="Exit", command=self.root.destroy)
        button2.grid(row=3, column=2, sticky=tk.W+tk.E)

        self.framehi.pack()

        self.root.mainloop()

#Main loop / run GUI
TinyPiGUI()