import tkinter as tk
from tkinter import messagebox 
import random

word=["java","python","kotlin","hangman"]

def get_word():
    return random.choice(word)

class hangman:
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Hangman Game")
        self.word = get_word()
        self.guesses = set()
        self.max_attempts = 6
        self.remaining_attempts = self.max_attempts
        self.word_display = ['_' for _ in self.word]

        self.canvas = tk.Canvas(self.root,width= 300, height= 300)
        self.canvas.pack(pady=10)

        self.word_label = tk.Label(self.root,text=" ".join(self.word_display))
        self.word_label.pack(pady=10)

        self.attempt_label = tk.Label(self.root,text= f"Remaining attempts: {self.remaining_attempts}")
        self.attempt_label.pack(pady=10)

        self.letter_entry = tk.Entry(self.root)
        self.letter_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root,text="Guess",command=self.guess_letter)
        self.guess_button.pack(pady=10)

        self.reset_button = tk.Button(self.root,text="Reset",command=self.reset_game)
        self.reset_button.pack(pady=10)

    def guess_letter(self):
        letter = self.letter_entry.get().lower()
        self.letter_entry.delete(0,tk.END)

        if len(letter) != 1 and not letter.isalpha():
            messagebox.showerror("Invalid letter","please enter the valid single letter")
            return
        
        if letter in self.guesses:
            messagebox.showerror("Already guessed")
            return
        self.guesses.add(letter)
        if letter in self.word:
            for i,char in enumerate(self.word):
                if char == letter:
                    self.word_display[i] = letter
        else:
            self.remaining_attempts -= 1
            self.draw_hangman()

        self.update_display()
        self.check_game_status()

    def update_display(self):
        self.word_label.config(text=' '.join(self.word_display))
        self.attempt_label.config(text= f"Remaining attempts: {self.remaining_attempts}")

    def check_game_status(self):
        if '_' not in self.word_display:
            messagebox.showerror("Hangman","Congratulations! You won!")
            self.reset_game()

        elif self.remaining_attempts <= 0:
            messagebox.showerror("Hangman",f"You Lose! the word was '{self.word}' ")

    def draw_hangman(self):
        if self.remaining_attempts == 5:
            self.canvas.create_oval(130,100,170,140,width=2)#Head

        elif self.remaining_attempts == 4:
            self.canvas.create_line(150,140,150,200,width=2)#body

        elif self.remaining_attempts == 3:
            self.canvas.create_line(150,160,130,180,width=2)
            self.canvas.create_line(150,160,170,180,width=2)

        elif self.remaining_attempts == 2:
            self.canvas.create_line(150,200,130,240,width=2)
            self.canvas.create_line(150,200,170,240,width=2)

        elif self.remaining_attempts == 1:
            self.canvas.create_line(150,50,150,100,width=2)

        elif self.remaining_attempts == 0:
            self.canvas.create_line(150,200,130,240,width=2)
            self.canvas.create_line(150,200,130,240,width=2)
            self.canvas.create_line(150,200,130,240,width=2)

    def reset_game(self):
        self.word = get_word()
        self.guesses.clear()
        self.word__display = ['_' for _ in self.word]
        self.remaining_attempts = self.max_attempts
        self.canvas.delete("all")
        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    game = hangman(root)
    root.mainloop()







