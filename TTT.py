import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic Tac Toe')
        self.frame = tk.Frame(self.master, padx=10, pady=10)
        self.frame.pack()

        # Create a list to represent the game board
        self.board = [' '] * 9

        # Create a list of button objects to represent the game board
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.frame, text='', width=6, height=3, font=('Arial', 20), command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Create a new game button
        new_game_button = tk.Button(self.master, text='New Game', font=('Arial', 16), command=self.new_game)
        new_game_button.pack(pady=10)

        self.current_player = 'X'
        self.game_over = False

    def make_move(self, position):
        if self.board[position] == ' ' and not self.game_over:
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)

            # Check for a win
            if self.check_win(self.current_player):
                messagebox.showinfo('Game Over', f'Player {self.current_player} wins!')
                self.game_over = True
            # Check for a tie
            elif self.check_tie():
                messagebox.showinfo('Game Over', 'Tie game!')
                self.game_over = True
            else:
                # Switch players
                if self.current_player == 'X':
                    self.current_player = 'O'
                else:
                    self.current_player = 'X'

    def check_win(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False

    def check_tie(self):
        return ' ' not in self.board

    def new_game(self):
        self.board = [' '] * 9
        for button in self.buttons:
            button.config(text='')
        self.current_player = 'X'
        self.game_over = False

if __name__ == '__main__':
    root = tk.Tk()
    tictactoe = TicTacToe(root)
    root.mainloop()
