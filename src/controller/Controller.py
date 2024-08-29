'''
Sudoku controller
'''


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
                for each in self.view.game_board.get_game_cells():
                    each.use_auto_candidate(False)
                    each.draw_cell()

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
        print(f"[Controller] - {button.on_click()}")
        new_difficulty = None
        for each in self.view.difficulty_buttons:
            if each.is_on:
                new_difficulty = each.text

        if new_difficulty is not None:
            self.model.get_new_puzzle(new_difficulty)
            self.view.reset_display(self.model.get_puzzle().get_difficulty())
            self.display_puzzle()
        else:
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
            if self.view.normal_button.is_on or button.get_number() == 0:
                # This code is copied below
                selected_cell = self.view.get_game_board().get_selected_cell()
                selected_cell.set_number(button.get_number())
                self.model.set_number_in_cell(button.get_number(), selected_cell.get_row(), selected_cell.get_col())
                self.model.get_puzzle().find_invalid_affected_cells()

                for cell in self.view.game_board.get_game_cells():
                    cell.set_invalid_affected(False)

                for row_col in self.model.get_puzzle().get_invalid_affected_cells():
                    invalid_affected_cell = self.view.game_board.get_cell_at(row_col[0], row_col[1])
                    invalid_affected_cell.set_invalid_affected()

                self.view.game_board.get_selected_cell().draw_cell()
                if self.view.candidate_button.auto_candidate:
                    self.refresh_auto_candidates()

                    for each in self.view.game_board.get_game_cells():
                        each.use_auto_candidate(True)
                        each.draw_cell()

            if self.view.candidate_button.is_on and self.view.get_game_board().get_selected_cell().number in ["", None]:
                self.view.game_board.get_selected_cell().add_candidate(button.get_number())
                self.view.game_board.get_selected_cell().draw_cell()

        if self.model.is_solved():
            self.view.clock.pause()
            self.view.show_winner_popup(f"You completed the {self.model.get_puzzle().get_difficulty().lower()} Sudoku in {self.view.clock.get_time(True)}!")

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

    def refresh_auto_candidates(self):
        game_cells = self.view.game_board.get_game_cells()
        flattened_puzzle_matrix = self.model.get_puzzle().get_matrix(flattened=True)

        for i in range(0, len(flattened_puzzle_matrix)):
            candidates = self.model.get_puzzle().get_candidates(game_cells[i].get_row(), game_cells[i].get_col())
            game_cells[i].set_auto_candidates(candidates)
            game_cells[i].draw_cell()

    def display_puzzle(self, puzzle_state="matrix"):
        game_cells = self.view.game_board.get_game_cells()
        flattened_puzzle_matrix = self.model.get_puzzle().get_matrix(puzzle_state, flattened=True)

        for i in range(0, len(flattened_puzzle_matrix)):
            game_cells[i].set_number(flattened_puzzle_matrix[i])
            game_cells[i].draw_cell()
            if game_cells[i].get_number() == "":
                game_cells[i].set_editable()
                game_cells[i].set_given(False)
                game_cells[i].draw_cell()
                candidates = self.model.get_puzzle().get_candidates(game_cells[i].get_row(), game_cells[i].get_col())
                game_cells[i].set_auto_candidates(candidates)

    def print_puzzle(self):
        puzzle = self.model.get_puzzle()
        puzzle.pretty_print()