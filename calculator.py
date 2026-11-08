import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)  

expression = ""

display = tk.Entry(root, font=("Arial", 20), justify="right", width=20, bd=5)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)  


def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(0, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def calculate():
    global expression
    try:
        result = str(eval(expression))
    except Exception:
        result = "Error"
    display.delete(0, tk.END)
    display.insert(0, result)
    expression = "" if result == "Error" else result


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, row, col in buttons:
    if text == "=":
        cmd = calculate
    else:
        cmd = lambda t=text: press(t)
    tk.Button(root, text=text, width=5, height=2, background= "cyan", font=("Arial", 14, "bold"), command=cmd).grid(
        row=row, column=col, padx=2, pady=2
    )



tk.Button(root, text="C", width=15, height=2, font=("Arial", 14), command=clear).grid(
    row=5, column=1, columnspan=2, padx=2, pady=2
)
root.mainloop()