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
                selected_cell = self.view.get_game_board().get_selected_cell()
                for each in self.view.game_board.get_game_cells():
                    each.use_auto_candidate()
                    each.unclick()
                    each.draw_cell()
                if selected_cell is not None:
                    selected_cell.on_click()
            if self.view.candidate_button.auto_candidate:
                self.view.normal_button.unclick()
                for each in self.view.game_board.get_game_cells():
                    each.use_auto_candidate(False)
                    each.draw_cell()

        print(f"[Controller] - {button.on_click()}")

    def handle_clock_event(self, button):
        print(f"[Controller] - {button.on_click()}")

    def handle_new_puzzle_event(self, button):
        next_difficulty = None
        for each in self.view.difficulty_buttons:
            if each.is_on:
                next_difficulty = each.text

        if next_difficulty is not None:
            print(f"[Controller] - {button.on_click()}")
            self.model.get_new_puzzle(next_difficulty)
            self.view.reset_display(self.model.get_puzzle().get_difficulty())
            self.display_puzzle()
        else:
            print(f"[Controller] - {button.on_click()}")
            self.model.get_new_puzzle()
            self.view.reset_display(self.model.get_puzzle().get_difficulty())
            self.display_puzzle()

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
                selected_cell = self.view.get_game_board().get_selected_cell()
                selected_cell.set_number(button.get_number())
                self.model.set_number_in_cell(button.get_number(), selected_cell.get_row(), selected_cell.get_col())

                self.view.game_board.get_selected_cell().draw_cell(s.HIGHLIGHT, s.BLACK)
            if self.view.candidate_button.is_on and self.view.get_game_board().get_selected_cell().number in ["", None]:
                self.view.game_board.get_selected_cell().add_candidate(button.get_number())
                self.view.game_board.get_selected_cell().draw_cell(s.HIGHLIGHT, s.BLACK)

        if self.model.is_solved():
            print(f"YOU SOLVED THE SUDOKU!")

    def handle_puzzle_button_event(self, button):
        print(f"[Controller] - {button.on_click()}")
        if button == self.view.reset_puzzle_button:
            self.view.reset_display(self.model.get_puzzle().get_difficulty())
            self.display_puzzle("initial_matrix")
        if button == self.view.reveal_cell_button:
            selected_cell = self.view.game_board.get_selected_cell()
            if selected_cell in ["", None]:
                return
            else:
                solved_matrix = self.model.get_puzzle().get_matrix("solved_matrix")
                selected_cell_answer = self.model.get_puzzle().get_value_at(selected_cell.get_row(), selected_cell.get_col(), solved_matrix)
                selected_cell.set_number(selected_cell_answer)
                self.model.get_puzzle().set_number_in_cell(selected_cell_answer, selected_cell.get_row(), selected_cell.get_col())
                self.display_puzzle()
        if button == self.view.give_up_button:
            self.model.solve_puzzle()
            self.display_puzzle()
            self.view.clock.pause()

    def populate_auto_candidates(self):
        for game_cell in self.view.game_board.get_game_cells():
            candidates = self.model.get_puzzle().get_candidates(game_cell.get_row(), game_cell.get_col())
            game_cell.set_auto_candidates(candidates)

    def display_puzzle(self, puzzle_state="matrix"):
        game_cells = self.view.game_board.get_game_cells()
        flattened_puzzle_matrix = self.model.get_puzzle().get_matrix(puzzle_state, flattened=True)

        for i in range(0, len(flattened_puzzle_matrix)):
            game_cells[i].set_number(flattened_puzzle_matrix[i])
            game_cells[i].draw_cell(s.GREY)
            if game_cells[i].get_number() == "":
                game_cells[i].set_editable()
                game_cells[i].set_given(False)
                game_cells[i].draw_cell()
                candidates = self.model.get_puzzle().get_candidates(game_cells[i].get_row(), game_cells[i].get_col())
                game_cells[i].set_auto_candidates(candidates)

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
