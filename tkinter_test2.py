import ttk
from Tkinter import * 
import Tkinter as tk 
from Tkinter import Tk, Text, BOTH, W, N, E, S
from ttk import Frame, Button, Label, Style

from tkFileDialog import askdirectory

class configuration():
    def __init__(self):
        self._tf_height = 2
        self._tf_width = 50

config = configuration()

class ExampleTextFrame(Frame):
    def __init__(self, parent, name, notebookFrame):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.notebookFrame = notebookFrame
        self.initUI(name)
    def initUI(self, name):
        if name != '+':
            text = Text(self)
            text.focus()
            text.insert(END, "Sample Text 1\n") 
            text.pack()
        if name == '+':
           self.bind('<FocusIn>', self.gen_new)
    def gen_new(self, event):
        t = self.notebookFrame.gen_tab('test')
        count = self.parent.index('end')
        self.parent.select(count-1)
        self.parent.forget(count-2)
        self.notebookFrame.gen_tab('+')

class ExampleNotebookFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.area = ttk.Notebook(self.parent)
        self.area.grid(
            row=1, 
            column=0, 
            columnspan=2, 
            rowspan=4, 
            padx=5, 
            sticky=E+W+S+N
            )
        self.gen_default_tabs()
    def gen_default_tabs(self):
        self.gen_tab('SQL')
        self.gen_tab('Python')
        self.gen_tab('+')
    def show_tabs(self):
        a = ""
    def show_next_tab(self, pos):
        a = ""
    def show_previous(self, pos):
        a = ""
    def gen_tab(self, name):
        f = ExampleTextFrame(self.area, name, self)
        return self.area.add(f, text=name)
        
class ExampleSideFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent  
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Test Everthing")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl = Label(self, text="Placeholder")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        ExampleNotebookFrame(self)

        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)
        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)
    
        obtn = Button(self, text="OK", command = self.testprint)
        obtn.grid(row=5, column=3)        
    def testprint(self):
        print('okokoko')          

def main():
    root = Tk()
    root.geometry("550x400+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
