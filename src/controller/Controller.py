'''
Sudoku controller
'''
from src.model.Model import Model
from src.view.View import View
from src.resources.settings import settings as s


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        view.set_observer(self)

    def go(self):
        self.display_puzzle()
        #self.populate_auto_candidates()
        self.view.display()

    def process_events(self, event, button):
        match event.lower():
            case "difficulty_button_click":
                return self.handle_difficulty_button_event(button)
            case "mode_button_click":
                return self.handle_mode_button_event(button)
            case "clock_click":
                return self.handle_clock_event(button)
            case "new_puzzle_button_click":
                return self.handle_new_puzzle_event(button)
            case "number_button_click":
                return self.handle_number_button_event(button)
            case "puzzle_button_click":
                return self.handle_puzzle_button_event(button)
            case "cell_click":
                return self.handle_cell_event(button)
            case _:
                return "invalid button click"

    def handle_difficulty_button_event(self, button):
        [each.unclick() for each in self.view.difficulty_buttons if each.is_on and each != button]
        print(f"[Controller] - {button.on_click()}")
        [self.view.new_puzzle_button.arm_button() for each in self.view.difficulty_buttons if each.is_on]
        if not any([button.is_on for button in self.view.difficulty_buttons]):
            self.view.new_puzzle_button.disarm_button()

    def handle_mode_button_event(self, button):
        if button == self.view.normal_button:
            if self.view.candidate_button.is_on and not self.view.candidate_button.auto_candidate:
                self.view.candidate_button.unclick()
            if self.view.candidate_button.auto_candidate:
                self.view.candidate_button.on_click()
            if self.view.normal_button.is_on and not self.view.candidate_button.is_on:
                return
        if button == self.view.candidate_button:
            if self.view.normal_button.is_on and not self.view.candidate_button.auto_candidate:
                self.view.normal_button.unclick()
            if self.view.candidate_button.is_on:
                self.view.normal_button.click()
                for each in self.view.game_board.get_game_cells():
                    if each.get_number() == "":
                        each.draw_cell(auto_candidate=True)
            if self.view.candidate_button.auto_candidate:
                self.view.normal_button.unclick()
                for each in self.view.game_board.get_game_cells():
                    if each.get_number() == "":
                        each.draw_cell(auto_candidate=False)

        print(f"[Controller] - {button.on_click()}")

    def handle_clock_event(self, button):
        print(f"[Controller] - {button.on_click()}")

    def handle_new_puzzle_event(self, button):
        default_difficulty = "easy"
        next_difficulty = None
        for each in self.view.difficulty_buttons:
            if each.is_on:
                next_difficulty = each.text

        if next_difficulty is not None:
            print(f"[Controller] - {button.on_click()}")
            self.view.reset_display(next_difficulty)
        else:
            print(f"[Controller] - {button.on_click()}")
            self.view.reset_display(default_difficulty)

    def handle_cell_event(self, cell):
        [each.unclick() for each in self.view.game_board.get_game_cells() if each.is_on and each != cell]
        print(f"[Controller] - {cell.on_click()}")

    def handle_number_button_event(self, button):
        print(f"[Controller] - {button.on_click()}")
        if self.view.game_board.get_selected_cell() in ["", None]:
            return
        elif self.view.game_board.get_selected_cell() != "" and self.view.game_board.get_selected_cell().is_editable():
            print(self.view.game_board.get_selected_cell())
            if self.view.normal_button.is_on:
                self.view.game_board.get_selected_cell().set_number(button.get_number())
                self.view.game_board.get_selected_cell().draw_cell(s.HIGHLIGHT, s.BLACK)
            if self.view.candidate_button.is_on and self.view.get_game_board().get_selected_cell().number in ["", None]:
                self.view.game_board.get_selected_cell().add_candidate(button.get_number())
                self.view.game_board.get_selected_cell().draw_cell(s.HIGHLIGHT, s.BLACK)

    def handle_puzzle_button_event(self, button):
        print(f"[Controller] - {button.on_click()}")

    def populate_auto_candidates(self):
        for game_cell in self.view.game_board.get_game_cells():
            candidates = self.model.get_puzzle().get_candidates(game_cell.get_row(), game_cell.get_col())
            game_cell.set_auto_candidates(candidates)


    def display_puzzle(self):
        flattened_game_cells = self.view.game_board.get_game_cells()
        flattened_puzzle_matrix = self.model.get_puzzle().get_matrix(True)

        for i in range(0, len(flattened_puzzle_matrix)):
            flattened_game_cells[i].set_number(flattened_puzzle_matrix[i])
            flattened_game_cells[i].draw_cell(s.GREY)
            if flattened_game_cells[i].get_number() == "":
                flattened_game_cells[i].draw_cell()
                flattened_game_cells[i].set_editable()
                flattened_game_cells[i].set_hidden()
                candidates = self.model.get_puzzle().get_candidates(flattened_game_cells[i].get_row(), flattened_game_cells[i].get_col())
                flattened_game_cells[i].set_auto_candidates(candidates)

    def print_puzzle(self):
        puzzle = self.model.get_puzzle()
        puzzle.pretty_print()


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.go()




if __name__ == '__main__':
    main()
