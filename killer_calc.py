"""
This program can be used as a tool for generating and selecting combinations
of numbers for solving Killer Sudoku puzzles or similar games.
"""

import tkinter as tk
import itertools

buttons = []
ARIAL_12 = ("Arial", 12)
ARIAL_14 = ("Arial", 14)


def calculate():
    """Generate buttons for all possible combinations"""
    global buttons
    cage_sum = int(entry1.get())
    num_cells = int(entry2.get())

    if cage_sum < 1 or cage_sum > 45:
        label4.configure(text="The cage sum must be between 1 and 45.")
        return
    if num_cells < 1 or num_cells > 9:
        label4.configure(text="The number of cells must be between 1 and 9.")
        return

    for button in buttons:
        button.destroy()
    buttons = []
    label4.configure(text="")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_combinations = list(itertools.combinations(nums, num_cells))

    # Calculate the sum of each combination and add it to the list if it matches the cage sum
    results = []
    for combination in all_combinations:
        if sum(combination) == cage_sum:
            results.append(combination)
    # Display the results as clickable buttons
    if len(results) == 0:
        label4.configure(text="There are no possible combinations.")
        result_frame.configure(bg="white")
    else:
        for i, combination in enumerate(results):
            if len(combination) == 1:
                button_text = '(' + str(combination[0]) + ')'
            else:
                button_text = str(combination)
            button = tk.Button(
                result_frame,
                text=button_text,
                font=ARIAL_12,
                bg="#abdbe3",
                command=lambda x=combination, index=i: toggle_button(x, index),
            )
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col, padx=5, pady=5)
            buttons.append(button)
            result_frame.configure(bg="#1e81b0")

        label4.pack()


def toggle_button(combination, button_index):
    """Toggle button appearance when clicked"""
    button = buttons[button_index]
    if button["relief"] == "raised":
        button.configure(relief="sunken", bg="#6b898e")
        print(f"{combination} selected")
    else:
        button.configure(relief="raised", bg="#abdbe3")
        print(f"{combination} unselected")


window = tk.Tk()
window.title("Killer Sudoku Combination Calculator")
window.geometry("600x450")
window.configure(bg="white")

label1 = tk.Label(
    window,
    text="Enter the cage sum and the number of cells in the cage:",
    font=ARIAL_14,
    bg="white",
)
label1.pack(pady=10)

input_frame = tk.Frame(window, bg="#1e81b0")
input_frame.pack(pady=10)

label2 = tk.Label(input_frame, text="Cage Sum (1-45):", font=ARIAL_12, bg="#abdbe3", justify="center")
label2.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(input_frame, font=ARIAL_14, justify="center")
entry1.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(input_frame, text="Number of Cells (1-9):", font=ARIAL_12, bg="#abdbe3", justify="center")
label3.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(input_frame, font=ARIAL_14, justify="center")
entry2.grid(row=1, column=1, padx=5, pady=5)

button1 = tk.Button(
    window, text="Calculate Combinations", font=ARIAL_12, command=calculate
)
button1.pack(pady=10)

label4 = tk.Label(window, text="", font=ARIAL_12, bg="white")
label4.pack(pady=10)

result_frame = tk.Frame(window, bg="#1e81b0")
result_frame.pack(pady=10)

window.mainloop()
