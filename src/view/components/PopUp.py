import tkinter as tk
from tkinter import messagebox


class PopUp:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(title=self.title, message=self.message)
        root.destroy()
