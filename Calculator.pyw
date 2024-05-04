import customtkinter as ctk
from tkinter import messagebox
import re

app = ctk.CTk()
app.title("Calculator")
app.geometry("280x320")

history = []

def calculate():
    try:
        equationToDo = equation.cget('text')
        answer = str(eval(equationToDo))
        result.configure(text=answer)
        history.append((equationToDo, answer))  # Add calculation to history
        print("Successfully Calculated")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def addToEquation(letter):
    try:
        if re.match(r'^[\d+\-*/.()^]+$', letter):  # Validate input
            textEquation = equation.cget('text')
            textEquation += letter
            equation.configure(text=textEquation)
            print("Added letter")
        else:
            messagebox.showwarning("Invalid Input", "Invalid character entered")
    except Exception as e:
        print(e)

def help():
    try:
        messagebox.showinfo("Help (Keybinds)", "Spacebar: Clear the current equation\n\nPowers: Press the asterisk twice and then the power e.g. 3**2 would be 3 squared\n\nParentheses: Press the left parenthesis and then the right parenthesis e.g. ()\n\nBackspace: To delete the previous character\n\nReturn or equals: Do the calculation")
        print("Help UI on screen")
    except Exception as e:
        print(e)

def clearEquations(event):
    try:
        equation.configure(text="")
        result.configure(text="")
        print('Cleared Equations')
    except Exception as e:
        print(e)

def removeFromEquation():
    try:
        textEquation = equation.cget('text')
        textEquation = textEquation[:-1]
        equation.configure(text=textEquation)
        print("Removed letter")
    except Exception as e:
        print(e)


equation = ctk.CTkLabel(app, text="", width=220, height=75, font=('Calibri', 20, 'bold'))
equation.grid(row=0, column=0, columnspan=3)

result = ctk.CTkLabel(app, text="", width=60, height=75, font=('Calibri', 20, 'bold'))
result.grid(row=0, column=3, sticky="w")

helpButton = ctk.CTkButton(app, text="Help", command=help, width=40, height=20, font=('Calibri', 10, 'bold'))
helpButton.place(x=235, y=5)

app.bind('<space>', clearEquations)
app.bind('1', lambda event: addToEquation("1")) 
app.bind('2', lambda event: addToEquation("2")) 
app.bind('3', lambda event: addToEquation("3")) 
app.bind('4', lambda event: addToEquation("4")) 
app.bind('5', lambda event: addToEquation("5")) 
app.bind('6', lambda event: addToEquation("6")) 
app.bind('7', lambda event: addToEquation("7")) 
app.bind('8', lambda event: addToEquation("8")) 
app.bind('9', lambda event: addToEquation("9")) 
app.bind('0', lambda event: addToEquation("0")) 
app.bind('+', lambda event: addToEquation("+")) 
app.bind('-', lambda event: addToEquation("-")) 
app.bind('/', lambda event: addToEquation("/")) 
app.bind('*', lambda event: addToEquation("*"))
app.bind('.', lambda event: addToEquation("."))
app.bind('^', lambda event: addToEquation("**"))
app.bind('(', lambda event: addToEquation("("))
app.bind(')', lambda event: addToEquation(")"))
app.bind('=', lambda event: calculate())
app.bind('<BackSpace>', lambda event: removeFromEquation())
app.bind('<Return>', lambda event: calculate())

one = ctk.CTkButton(app, text="1", command=lambda letter="1": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
one.grid(row=1, column=0, sticky='nswe', padx=5, pady=5)

two = ctk.CTkButton(app, text="2", command=lambda letter="2": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
two.grid(row=1, column=1, sticky='nswe', padx=5, pady=5)

three = ctk.CTkButton(app, text="3", command=lambda letter="3": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
three.grid(row=1, column=2, sticky='nswe', padx=5, pady=5)

four = ctk.CTkButton(app, text="4", command=lambda letter="4": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
four.grid(row=2, column=0, sticky='nswe', padx=5, pady=5)

five = ctk.CTkButton(app, text="5", command=lambda letter="5": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
five.grid(row=2, column=1, sticky='nswe', padx=5, pady=5)

six = ctk.CTkButton(app, text="6", command=lambda letter="6": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
six.grid(row=2, column=2, sticky='nswe', padx=5, pady=5)

seven = ctk.CTkButton(app, text="7", command=lambda letter="7": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
seven.grid(row=3, column=0, sticky='nswe', padx=5, pady=5)

eight = ctk.CTkButton(app, text="8", command=lambda letter="8": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
eight.grid(row=3, column=1, sticky='nswe', padx=5, pady=5)

nine = ctk.CTkButton(app, text="9", command=lambda letter="9": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
nine.grid(row=3, column=2, sticky='nswe', padx=5, pady=5)

zero = ctk.CTkButton(app, text="0", command=lambda letter="0": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
zero.grid(row=4, column=0, sticky='nswe', padx=5, pady=5)

decimal = ctk.CTkButton(app, text=".", command=lambda letter=".": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
decimal.grid(row=4, column=1, sticky='nswe', padx=5, pady=5)

enter = ctk.CTkButton(app, text="=", command=calculate, height=50, width=10, font=('Calibri', 20, 'bold'))
enter.grid(row=4, column=2, sticky='nswe', padx=5, pady=5)

addition = ctk.CTkButton(app, text="+", command=lambda letter="+": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
addition.grid(row=2, column=3, sticky='nswe', padx=5, pady=5)

subtract = ctk.CTkButton(app, text="-", command=lambda letter="-": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
subtract.grid(row=3, column=3, sticky='nswe', padx=5, pady=5)

multiply = ctk.CTkButton(app, text="×", command=lambda letter="*": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
multiply.grid(row=1, column=3, sticky='nswe', padx=5, pady=5)

division = ctk.CTkButton(app, text="÷", command=lambda letter="/": addToEquation(letter), height=50, width=10, font=('Calibri', 20, 'bold'))
division.grid(row=4, column=3, sticky='nswe', padx=5, pady=5)

if __name__ == "__main__":
    app.mainloop()
