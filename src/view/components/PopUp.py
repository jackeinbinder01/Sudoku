from tkinter import messagebox


class PopUp:
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        messagebox.showinfo(title=self.title, message=self.message)
