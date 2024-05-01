import cusomtkinter as ctk

app = ctk.CTk()
app.title("Calculator")
app.geometry("310x360")



def calculate():
    equationToDo = equation.cget('text')
    answer = str(eval(equationToDo))
    equation.configure(text=answer)


def addToEquation(letter):
    textEquation = equation.cget('text')
    textEquation += letter
    equation.configure(text=textEquation)


def clearEquations(event):
    equation.configure(text="")
    print('Cleared Equations')


app.bind('<space>', clearEquations)

equation = ctk.CTkLabel(app, text="", width=30, height=5)
equation.grid(row=0, column=0, columnspan=3)

one = ctk.CTkButton(app, text="1", command=lambda: addToEquation("1"), height=4, width=10)
one.grid(row=1, column=0, sticky='nswe')

two = ctk.CTkButton(app, text="2", command=lambda: addToEquation("2"), height=4, width=10)
two.grid(row=1, column=1, sticky='nswe')

three = ctk.CTkButton(app, text="3", command=lambda: addToEquation("3"), height=4, width=10)
three.grid(row=1, column=2, sticky='nswe')

four = ctk.CTkButton(app, text="4", command=lambda: addToEquation("4"), height=4, width=10)
four.grid(row=2, column=0, sticky='nswe')

five = ctk.CTkButton(app, text="5", command=lambda: addToEquation("5"), height=4, width=10)
five.grid(row=2, column=1, sticky='nswe')

six = ctk.CTkButton(app, text="6", command=lambda: addToEquation("6"), height=4, width=10)
six.grid(row=2, column=2, sticky='nswe')

seven = ctk.CTkButton(app, text="7", command=lambda: addToEquation("7"), height=4, width=10)
seven.grid(row=3, column=0, sticky='nswe')

eight = ctk.CTkButton(app, text="8", command=lambda: addToEquation("8"), height=4, width=10)
eight.grid(row=3, column=1, sticky='nswe')

nine = ctk.CTkButton(app, text="9", command=lambda: addToEquation("9"), height=4, width=10)
nine.grid(row=3, column=2, sticky='nswe')

zero = ctk.CTkButton(app, text="0", command=lambda: addToEquation("0"), height=4, width=10)
zero.grid(row=4, column=0, sticky='nswe')

decimal = ctk.CTkButton(app, text=".", command=lambda: addToEquation("."), height=4, width=10)
decimal.grid(row=4, column=1, sticky='nswe')

enter = ctk.CTkButton(app, text="=", command=calculate, height=4, width=10)
enter.grid(row=4, column=2, sticky='nswe')

addition = ctk.CTkButton(app, text="+", command=lambda: addToEquation("+"), height=4, width=10)
addition.grid(row=2, column=3, sticky='nswe')

subtract = ctk.CTkButton(app, text="-", command=lambda: addToEquation("-"), height=4, width=10)
subtract.grid(row=3, column=3, sticky='nswe')

multiply = ctk.CTkButton(app, text="*", command=lambda: addToEquation("*"), height=4, width=10)
multiply.grid(row=1, column=3, sticky='nswe')

division = ctk.CTkButton(app, text="/", command=lambda: addToEquation("/"), height=4, width=10)
division.grid(row=4, column=3, sticky='nswe')

app.mainloop()
