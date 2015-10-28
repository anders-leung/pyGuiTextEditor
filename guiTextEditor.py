import tkinter as tk
from tkinter.filedialog import *


class TextEditor(tk.Tk):

    def __init__(self, parent):
        self.fileName = None
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()

    def initUI(self):
        self.parent.title("My Python Text Editor")
        self.parent.minsize(width=400, height=500)
        self.parent.maxsize(width=400, height=500)

        self.text = Text(self.parent, width=400, height=600, undo=True,
                         autoseparators=True)
        self.text.pack()

        menubar = Menu(self)
        filemenu = Menu(menubar)
        filemenu.add_command(label="New", command=self.newFile)
        filemenu.add_command(label="Open", command=self.openFile)
        filemenu.add_command(label="Save", command=self.saveFile)
        filemenu.add_command(label="Save As...", command=self.saveAs)
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        self.parent.bind("<Control-q>", self.close)
        self.parent.bind("<Control-n>", self.newFile)
        self.parent.bind("<Control-o>", self.openFile)
        self.parent.bind("<Control-s>", self.saveFile)
        self.parent.bind("<Control-Alt-s>", self.saveAs)

        self.parent.config(menu=menubar)


    def newFile(self, event=None):
        global fileName
        fileName = "Untitled"
        self.text.delete(0.0, END)

    def saveFile(self, event=None):
        global fileName
        t = self.text.get(0.0, END)
        f = open(fileName, "w")
        f.write(t)
        f.close()
        self.saveMessage()

    def saveAs(self, event=None):
        f = asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except Exception as e:
            showerror(title="Oops!", message="Unable to open file!\\nError: %s" % (e))

    def openFile(self, event=None, inputFilename=None):
        global fileName
        if inputFilename:
            fileName = inputFilename
            t = open(inputFilename, mode="r").read()
            self.text.delete(0.0, END)
            self.text.insert(0.0, t)
        else:
            f = askopenfilename()
            if f == "":
                return
            fileName = f
            t = open(f, "r").read()
            self.text.delete(0.0, END)
            self.text.insert(0.0, t)

    def close(self, event=None):
        self.parent.destroy()

    def saveMessage(self):
        tk.messagebox.showinfo("Saving...", "Saved!")


def main():
    root = Tk()
    app = TextEditor(root)
    print("hello")
    app.openFile(None, "testing.txt")
    app.mainloop()
    

if __name__ == "__main__":
    main()
