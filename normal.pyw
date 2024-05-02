import tkinter as tk


app = tk.Tk()
app.title("Calculator")
app.geometry("310x360")



def calculate():
    try:
        equationToDo = equation.cget('text')
        answer = str(eval(equationToDo))
        equation.configure(text=answer)
        print("Successfully Calculated")
    except Exception as e:
        print(e)


def addToEquation(letter):
    try:
        textEquation = equation.cget('text')
        textEquation += letter
        equation.configure(text=textEquation)
        print("Added letter")
    except Exception as e:
        print(e)
    

def clearEquations(event):
    try:
        equation.configure(text="")
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
app.bind('<parenleft>', lambda event: addToEquation("("))
app.bind('<parenright>', lambda event: addToEquation(")"))
app.bind('<BackSpace>', lambda event: removeFromEquation())
app.bind('<Return>', lambda event: calculate())

equation = tk.Label(app, text="", width=30, height=5)
equation.grid(row=0, column=0, columnspan=3)

one = tk.Button(app, text="1", command=lambda: addToEquation("1"), height=4, width=10)
one.grid(row=1, column=0, sticky='nswe')

two = tk.Button(app, text="2", command=lambda: addToEquation("2"), height=4, width=10)
two.grid(row=1, column=1, sticky='nswe')

three = tk.Button(app, text="3", command=lambda: addToEquation("3"), height=4, width=10)
three.grid(row=1, column=2, sticky='nswe')

four = tk.Button(app, text="4", command=lambda: addToEquation("4"), height=4, width=10)
four.grid(row=2, column=0, sticky='nswe')

five = tk.Button(app, text="5", command=lambda: addToEquation("5"), height=4, width=10)
five.grid(row=2, column=1, sticky='nswe')

six = tk.Button(app, text="6", command=lambda: addToEquation("6"), height=4, width=10)
six.grid(row=2, column=2, sticky='nswe')

seven = tk.Button(app, text="7", command=lambda: addToEquation("7"), height=4, width=10)
seven.grid(row=3, column=0, sticky='nswe')

eight = tk.Button(app, text="8", command=lambda: addToEquation("8"), height=4, width=10)
eight.grid(row=3, column=1, sticky='nswe')

nine = tk.Button(app, text="9", command=lambda: addToEquation("9"), height=4, width=10)
nine.grid(row=3, column=2, sticky='nswe')

zero = tk.Button(app, text="0", command=lambda: addToEquation("0"), height=4, width=10)
zero.grid(row=4, column=0, sticky='nswe')

decimal = tk.Button(app, text=".", command=lambda: addToEquation("."), height=4, width=10)
decimal.grid(row=4, column=1, sticky='nswe')

enter = tk.Button(app, text="=", command=calculate, height=4, width=10)
enter.grid(row=4, column=2, sticky='nswe')

addition = tk.Button(app, text="+", command=lambda: addToEquation("+"), height=4, width=10)
addition.grid(row=2, column=3, sticky='nswe')

subtract = tk.Button(app, text="-", command=lambda: addToEquation("-"), height=4, width=10)
subtract.grid(row=3, column=3, sticky='nswe')

multiply = tk.Button(app, text="*", command=lambda: addToEquation("*"), height=4, width=10)
multiply.grid(row=1, column=3, sticky='nswe')

division = tk.Button(app, text="/", command=lambda: addToEquation("/"), height=4, width=10)
division.grid(row=4, column=3, sticky='nswe')

app.mainloop()
