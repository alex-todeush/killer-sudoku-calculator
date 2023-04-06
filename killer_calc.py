"""
This program can be used as a tool for generating and selecting combinations
of numbers for solving Killer Sudoku puzzles or similar games.
"""

import tkinter as tk
import customtkinter as ctk
import itertools
from PIL import Image,ImageTk

buttons = []
results = []
ARIAL_12 = ("Arial", 12)
ARIAL_14 = ("Arial", 14)

def calculate():
    """Generate buttons for all possible combinations"""
    global buttons
    global results
    cage_sum = int(sum_entry.get())
    num_cells = int(num_cells_entry.get())

    if cage_sum < 1 or cage_sum > 45:
        error_label.configure(text="The cage sum must be between 1 and 45.")
        return
    if num_cells < 1 or num_cells > 9:
        error_label.configure(text="The number of cells must be between 1 and 9.")
        return

    for button in buttons:
        button.destroy()
    buttons = []
    error_label.configure(text="")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_combinations = list(itertools.combinations(nums, num_cells))

    # Calculate the sum of each combination and add it to the list if it matches the cage sum
    results = []
    for combination in all_combinations:
        if sum(combination) == cage_sum:
            results.append(combination)
    # Display the results as clickable buttons
    if len(results) == 0:
        error_label.configure(text="There are no possible combinations.")
        result_frame.configure(bg="white")
    else:
        for i, combination in enumerate(results):
            if len(combination) == 1:
                button_text = '(' + str(combination[0]) + ')'
            else:
                button_text = str(combination)
            button = tk.Button(result_frame, text=button_text, font=ARIAL_12, bg="#abdbe3", command=lambda x=combination, index=i: toggle_button(x, index),)
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col, padx=5, pady=5)
            buttons.append(button)

        error_label.pack()

def toggle_button(combination, button_index):
    """Toggle combination appearance when clicked"""
    button = buttons[button_index]
    if button["relief"] == "raised":
        button.configure(relief="sunken", bg="#6b898e")
        print(f"{combination} selected")
    else:
        button.configure(relief="raised", bg="#abdbe3")
        print(f"{combination} unselected")

def check_exclusions():
    """Check all combinations and see if any of the number in them are excluded,
        if so, toggle them off.
    """
    for i, combination in enumerate(results):
        found = 0
        button = buttons[i]
        for number in combination:
            if number in number_pad.exclusions:
                found = 1
        if found == 0:
            button.configure(relief="raised", bg="#abdbe3")
        else:
            button.configure(relief="sunken", bg="#6b898e")

class NumberPad:
    """Exclusion number pad"""
    def __init__(self, master):
        self.master = master
        self.numbers = []
        self.exclusions = []
        for i in range(9):
            pad_button = tk.Button(grid_frame, text=str(i+1), width=4, height=2, relief="raised")
            pad_button.configure(bg="#abdbe3", font=ARIAL_12, command=lambda button=pad_button, num=i+1: self.toggle(button, num))
            pad_button.grid(row=i//3, column=i%3)
            self.numbers.append(pad_button)

    def toggle(self, button, num):
        """Toggle number pad keys and check for changes to possible combinations"""
        if button['relief'] == 'raised':
            button.configure(relief='sunken', bg="#6b898e")
            self.exclusions.append(num)
            print(f"{num} excluded")
        else:
            button.configure(relief='raised', bg="#abdbe3")
            self.exclusions.remove(num)
            print(f"{num} included")
        check_exclusions()

    def reset_exclusions(self):
        """Turn off all exclusions"""
        for button in self.numbers:
            button.configure(relief='raised', bg="#abdbe3")
            self.exclusions = []
            check_exclusions()

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

window = ctk.CTk()
window.title("Killer Sudoku Combination Calculator")
window.geometry("600x450")

title_label = ctk.CTkLabel(window, text="Enter the cage sum and the number of cells in the cage:", font=ARIAL_14)
title_label.pack(pady=10)

input_frame = ctk.CTkFrame(window)
input_frame.pack(pady=10)

sum_input_label = ctk.CTkLabel(input_frame, text="Cage Sum (1-45):", font=ARIAL_12, justify="center")
sum_input_label.grid(row=0, column=0, padx=5, pady=5)

sum_entry = ctk.CTkEntry(input_frame, font=ARIAL_14, justify="center")
sum_entry.grid(row=0, column=1, padx=5, pady=5)

num_cell_label = ctk.CTkLabel(input_frame, text="Number of Cells (1-9):", font=ARIAL_12, justify="center")
num_cell_label.grid(row=1, column=0, padx=5, pady=5)

num_cells_entry = ctk.CTkEntry(input_frame, font=ARIAL_14, justify="center")
num_cells_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = ctk.CTkButton(window, text="Calculate Combinations", font=ARIAL_12, command=calculate)
calculate_button.pack(pady=10)

error_label = ctk.CTkLabel(window, text="", font=ARIAL_12)
error_label.pack(pady=10)

dual_pane_frame = ctk.CTkFrame(window)
dual_pane_frame.pack()

grid_frame = ctk.CTkFrame(dual_pane_frame)
grid_frame.pack(side="left")
number_pad = NumberPad(dual_pane_frame)

image = Image.open('assets/reset.jpg')
image = image.resize((45,45), Image.ANTIALIAS)
img = ctk.CTkImage(image, size=(45,45))

reset_button = ctk.CTkButton(dual_pane_frame, text="", image=img, font=ARIAL_12, command=number_pad.reset_exclusions, height=50)
reset_button.pack(pady=10, side="left")

result_frame = ctk.CTkFrame(dual_pane_frame)
result_frame.pack(pady=10, side="left")

dual_pane_frame.grid_rowconfigure(0, minsize=max(grid_frame.winfo_reqheight(), result_frame.winfo_reqheight()))

window.mainloop()
