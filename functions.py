import sympy
import re
from widgets import *
from tkinter import filedialog as fd

# Figures out what function to run given prompts
def submit():
    exprs = txtBox.get('1.0', tk.END)

    if '=' in exprs:
        compute('solveEquality')
    else:
        if hasSymbol(exprs):
            plotExpression()
        else:
            compute('calculateExpression')

#Unused, would have run the graphing calc software
def plotExpression():
    exprs = processInput()
    print(exprs[0])
    ex = exprs[0]
    ex = ex.lower()
    print(ex)


def digitIndex(expr, char):
    startIndex = expr.index(char) + 1
    index = 0
    while True:
        if expr[startIndex].isdigit() or expr[startIndex].isalpha():
            index = startIndex
        else:
            return index
        startIndex += 1

# Simplifies so that sympy can solve
def processEquation(equation):
    equalIndex = equation.index('=')
    expr1 = sympy.sympify(equation[:equalIndex])
    expr2 = sympy.sympify(equation[equalIndex + 1:])
    return expr1 - expr2

# makes a list of all the numbers in the equation
def extractNumbers(expr):
    numbers = []
    for char in expr:
        if char.isdigit():
            numbers.append(char)
    return float(''.join(numbers))

# deals with different functions and variables
def hasSymbol(expr):
    try:
        rightParentheses = expr.index('(')
        leftParentheses = expr.index(')')

        for char in expr[rightParentheses + 1:leftParentheses]:
            if char.isalpha() and char != 'Ⲡ' and char != 'e':
                return True
        return False
    except:
        for char in expr:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                return True
        return False

# Deals with the adding of multiplication between expression for sympy

def addStar(expr):
    if 'sin' not in expr and 'cos' not in expr and 'tan' not in expr and 'cot' not in expr and 'log' not in expr:
        for i in range(len(expr)):
            if expr[i].isdigit() and expr[i + 1].isalpha() and expr[i + 1] != '°' or expr[i] == ')' and expr[i + 1] == '(' and expr[i + 1] != '°':
                expr = expr[:i + 1] + '*' + expr[i + 1:]
            if expr[i].isalpha() and expr[i + 1].isalpha() and expr[i + 1] != '°' or expr[i] == ')' and expr[i + 1] == '(' and expr[i + 1] != '°':
                if str(sympy.pi) not in expr:
                    expr = expr[:i + 1] + '*' + expr[i + 1:]
    return expr

#Fxies any improper chars for sympu
def processInput():
    exprs = []

    for i in range(1, int(txtBox.index(tk.INSERT)[0]) + 1):
        expr = txtBox.get(f'{i}.0', f'{i + 1}.0')
        expr = expr.replace('Ⲡ', str(sympy.pi))
        expr = expr.replace('e', str(sympy.E))
        expr = expr.replace('²', '** 2 ')
        expr = expr.replace('³', '** 3 ')
        expr = addStar(expr)
        if '(' in expr and expr[0] != '(':
            parenthesesIndexes = [m.start() for m in re.finditer("\(", expr)]
            for parenthesesIndex in parenthesesIndexes:
                if not expr[parenthesesIndex - 1].isalpha():
                    expr = expr[:parenthesesIndex] + '*' + expr[parenthesesIndex:]
        if '√' in expr:
            squareRootIndex = digitIndex(expr, '√')
            expr = expr.replace('√', '')
            expr = expr[:squareRootIndex] + '** 0.5 ' + expr[squareRootIndex:]
        if '∛' in expr:
            cubeRootIndex = digitIndex(expr, '∛')
            expr = expr.replace('∛', '')
            expr = expr[:cubeRootIndex] + '** (1/3) ' + expr[cubeRootIndex:]
        if '°' in expr:
            deg = extractNumbers(expr)
            func = expr[:3]
            expr = f'{func}({sympy.rad(deg)})'
        if '=' in expr:
            expr = processEquation(expr)
        exprs.append(expr)
    return exprs

# does teh actual computaton depending on the type of solve
def compute(operation):
    txtBox.config(state='normal')
    exprs = processInput()

    if operation == 'calculateExpression':
        result = f'{round(float(sympy.sympify(exprs[0])), 2)}'
    elif operation == 'solveEquality':
        solutions = None
        if len(exprs) == 1:
            solutions = sympy.solve(sympy.sympify(exprs[0]))
            if len(solutions) == 1:
                solutions = solutions[0]
        elif len(exprs) == 2:
            solutions = sympy.solve((sympy.sympify(exprs[0]), sympy.sympify(exprs[1])))

        result = solutions

    elif operation == 'factorExpression':
        result = sympy.sympify(exprs[0]).factor()
    elif operation == 'expandExpression':
        result = sympy.sympify(exprs[0]).expand()
    elif operation == 'limit':
        value = entLimitValue.get()
        value = value.replace('∞', str(sympy.S.Infinity))
        limit = sympy.Limit(sympy.sympify(exprs[0]), sympy.Symbol('x'), sympy.sympify(value)).doit()
        result = limit
    elif operation == 'derivative':
        derivative = sympy.Derivative(sympy.sympify(exprs[0]), sympy.Symbol('x')).doit()
        result = derivative
    elif operation == 'integral':
        integral = sympy.Integral(sympy.sympify(exprs[0]), sympy.Symbol('x')).doit()
        result = integral

    txtBox.insert(tk.END, f'\n{result}')
    txtBox.config(state='disabled')

#delete and remove buttons
def removeChar():
    txtBox.config(state='normal')
    txtBox.delete('end-2c', tk.END)
    txtBox.config(state='disabled')

def clearTxt():
    txtBox.config(state='normal')
    txtBox.delete('1.0', tk.END)
    txtBox.config(state='disabled')

#when a bytton is pressed, the placeholder is removed
def deletePlaceholder():
    if txtBox.get(1.0, "end-1c") == 'Enter your query':
        clearTxt()

# disables interaction so that user cant type

def insertBtnTxt(btn):
    deletePlaceholder()
    txtBox.config(state='normal')
    txtBox.insert(tk.END, btn['text'])
    txtBox.config(state='disabled')

# when the enter button is pressed, answer displayed on new line
def insertNewLine():
    deletePlaceholder()
    txtBox.config(state='normal')
    txtBox.insert(tk.END, '\n')
    txtBox.config(state='disabled')

#Deals with hidign and showing the buttons if thye are pressed twice
def showHideSymbols():
    if frmSymbols.winfo_ismapped():
        frmStandard.pack()
        frmSymbols.pack_forget()
        frmSci.pack_forget()
    else:
        frmSymbols.pack()
        frmStandard.pack_forget()
        frmSci.pack_forget()

def showHideSciFunctions():
    if frmSci.winfo_ismapped():
        frmStandard.pack()
        frmSci.pack_forget()
        frmSymbols.pack_forget()
    else:
        frmStandard.pack_forget()
        frmSymbols.pack_forget()
        frmSci.pack()
