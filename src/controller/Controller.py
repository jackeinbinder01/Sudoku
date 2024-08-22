'''
Sudoku controller
'''


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def go(self):
        self.view.display()



