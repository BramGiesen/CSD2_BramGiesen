#!/usr/bin/env python
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()


    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.quit = tk.Button(self, text='Quit', command=self.quit)
        bottonValue = tk.Button(self, text='print', command=print("text"))
        # self.bottonValue.grid(row=1, column=1,
        #     sticky=tk.N+tk.S+tk.E+tk.W)
        self.quit.grid(row=0, column=0,
            sticky=tk.N+tk.S+tk.E+tk.W)

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(1000, 500))
app = Application()
app.master.title('IRREGULAR BEAT GENERATOR')
app.mainloop()
root.mainloop()
