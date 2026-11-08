# python-calc-app
it's a GUI app built with python that performs basic calculations.

## How to run it 
it can be run by using the command "python (destination file name).py" in this case it is calculator.py

## the whole idea 
it uses the pyhton native gui library tkinter nicknamed tk to run the design ed interface, in this case a calculator interface which then opens the calculator app and run the logic.



### overall breakdown of each of the line of code

import tkinter as tk: loads Python’s built-in GUI library, nicknamed tk.
root = tk.Tk(): creates the main window.
root.title(...): sets the text in the window’s title bar.
root.resizable(False, False): stops the user from resizing the window.
expression = "": holds what the user has typed so far, as text.
display = tk.Entry(...): the text box at the top. font sets the text style, justify="right" aligns the numbers right, width sets the box width, and bd is the border thickness.
display.grid(...): places the box at row 0, column 0, spanning all 4 columns. padx and pady add spacing.
def press(value): runs when a number or operator button is clicked.
global expression: lets the function change the variable defined outside it.
expression += str(value): adds the clicked character to the text.
display.delete(0, tk.END): clears the box.
display.insert(0, expression): shows the updated text.
def clear(): resets expression to empty and clears the box (this is blank 1, delete).
def calculate(): runs when = is clicked.
eval(expression): evaluates the text as math, so "2+3" becomes 5 (blank 2). str(...) turns the answer back into text.
try / except Exception: if the expression is invalid (like 5++) or divides by zero, the result becomes “Error” instead of crashing.
expression = "" if result == "Error" else result: after an error, starts fresh. Otherwise the result becomes the start of the next calculation.
buttons = [...]: a list of (label, row, column), one entry per button.
for text, row, col in buttons:: loops over the list to build each button.
if text == "=": the equals button calls calculate.
else: cmd = lambda t=text: press(t): every other button calls press with its own label. The t=text part makes each button remember its own label instead of all using the last one.
tk.Button(...).grid(...): creates the button and places it in its row and column.
The last tk.Button for “C”: a full-width clear button in row 5.
root.mainloop(): starts the window’s event loop so it stays open and reacts to clicks (blank 3).