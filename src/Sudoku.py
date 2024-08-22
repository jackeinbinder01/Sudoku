from src.model.Model import Model
from src.view.View import View
from src.controller.Controller import Controller

'''
Main driver for the Sudoku app
'''


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.go()


if __name__ == '__main__':
    main()
