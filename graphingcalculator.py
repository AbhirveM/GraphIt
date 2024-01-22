from tkinter import *
from tkinter import ttk
from math import pow, sin, cos, tan, pi, e, sinh, cosh, tanh, log10, log

formula = "2*x"

maxSize = 64.0
minSize = 1.0
increment = 2.0
computationDistance = 0.001
asymptoteMulti = 2.0
viewSize = 8.0

def printFormula(preText):
    Label(rootGraph, text=preText + "[{0:.0f}".format(viewSize) + "] f(x) = " + formula, relief=RIDGE,
          width=1).grid(row=1, column=0, columnspan=5, sticky=W + E)


# Changes the coordinate system from the tkinter one to cartesian
def translate(xCurrent, yCurrent):
    tc = [0, 0]
    xMul = int(canvas["width"]) / (viewSize * 2)
    yMul = (int(canvas["height"]) / (viewSize * -2))
    xCurrent = (xCurrent + viewSize) * xMul
    yCurrent = (yCurrent + viewSize) * yMul + int(canvas["height"])
    tc[0] = xCurrent
    tc[1] = yCurrent
    return tc


# Draws line between two points, used to plot
def drawLine(xFrom, yFrom, xTo, yTo, colour):
    fromCoord = translate(xFrom, yFrom)
    toCoord = translate(xTo, yTo)
    if yTo - yFrom > viewSize * asymptoteMulti or yFrom - yTo > viewSize * asymptoteMulti:
        fromCoord = toCoord
    canvas.create_line(fromCoord[0], fromCoord[1], toCoord[0], toCoord[1], fill=colour)


# Draws the gridlines centred at the middle of screen
def drawGrid():
    drawLine(viewSize * -1, 0, viewSize, 0, "darkgray")
    drawLine(0, viewSize * -1, 0, viewSize, "darkgray")


# Does the calculating and drawing of func
def drawGraph(xd):
    canvas.delete("all")
    drawGrid()
    yPrevious = 0.0
    x = viewSize * -1
    while x <= viewSize:
        try:
            y = eval(formula)
        except ValueError:
            y = 1000000000
            x = computationDistance * viewSize
            if eval(formula) < 0:
                y *= -1
        except:
            printFormula("SYNTAX ERROR")
            break
        try:
            drawLine(x - computationDistance * viewSize, yPrevious, x, y, "black")
        except:
            printFormula("SYNTAX ERROR")
            break
        yPrevious = y
        x += computationDistance * viewSize


# Deals with making the prompt usable for math module
def appendFormula(thing):
    global formula
    if formula.endswith('.') and thing == '.':
        formula = formula[:-1]
        formula += ","
    else:
        formula += thing
    printFormula("")

# Clear button
def clearFormula():
    global formula
    while formula != "":
        deleteFormula()
    printFormula("")

#Delete button
def deleteFormula():
    global formula
    formula = formula[:-1]
    printFormula("")

# Zooms the grid in by afactor of 2
def zoomIn():
    global viewSize, btnZoomIn, btnZoomOut
    btnZoomOut = ttk.Button(rootGraph, text="Zoom Out", command=lambda: zoomOut()).grid(row=8, column=3)
    if viewSize > minSize:
        viewSize /= increment
        drawGraph("xd")
    if viewSize == minSize:
        btnZoomIn = ttk.Button(rootGraph, text="Zoom In", command=lambda: zoomIn(), state=DISABLED).grid(row=8, column=2)
    drawGraph(None)

# Zooms out by a factor of 2
def zoomOut():
    global viewSize, btnZoomOut, btnZoomIn
    btnZoomIn = ttk.Button(rootGraph, text="Zoom In", command=lambda: zoomIn()).grid(row=8, column=2)
    if viewSize < maxSize:
        viewSize *= increment
        drawGraph("xd")
    if viewSize == maxSize:
        btnZoomOut = ttk.Button(rootGraph, text="Zoom Out", command=lambda: zoomOut(),
                                  state=DISABLED).grid(row=8, column=3)
    drawGraph(None)

# Makes sure that expressions are different from equations
def correctEndingNoNumber(name):
    return name.endswith('x') or name.endswith('e') or (name.endswith('i') and name[-2:] != "si") or name.endswith(')')

def correctEnding(thing):
    return thing[-1:].isdigit() or correctEndingNoNumber(thing)

# Changes into proper  notation for math
def appendImplicit(thing):
    global formula
    if correctEnding(formula):
        if thing == "**":
            formula += thing
        else:
            formula += "*" + thing
    elif formula[-2:] == "**" and thing == "**":
        formula = formula[:-2]
        if correctEnding(formula):
            formula += "*pow(x,"
        else:
            formula += "pow(x,"
    else:
        formula += thing
    printFormula("")


def appendNumberFormula(thing):
    global formula
    if correctEndingNoNumber(formula) and thing.isdigit():
        formula += "*"
    formula += thing
    printFormula("")

# Makes parentheses into multiplication
def appendClosingParenthesesFormula(thing):
    global formula
    if correctEnding(formula) and thing == '(':
        formula += "*"
    formula += thing
    printFormula("")

#initializes root and buttons

rootGraph = Tk()

rootGraph.wm_title('"Desmos"')
rootGraph.resizable(width=True, height=True)

horizontalScreen = rootGraph.winfo_screenwidth() / 2 - rootGraph.winfo_reqwidth()
verticalScreen = rootGraph.winfo_screenheight() / 2 - rootGraph.winfo_reqheight()
rootGraph.geometry("+%d+%d" % (horizontalScreen, verticalScreen))

canvas = Canvas(rootGraph)

printFormula("")

ttk.Button(rootGraph, text="0", command=lambda: appendNumberFormula("0")).grid(row=2, column=0)
ttk.Button(rootGraph, text="1", command=lambda: appendNumberFormula("1")).grid(row=2, column=1)
ttk.Button(rootGraph, text="2", command=lambda: appendNumberFormula("2")).grid(row=2, column=2)
ttk.Button(rootGraph, text="3", command=lambda: appendNumberFormula("3")).grid(row=2, column=3)
ttk.Button(rootGraph, text="4", command=lambda: appendNumberFormula("4")).grid(row=2, column=4)
ttk.Button(rootGraph, text="5", command=lambda: appendNumberFormula("5")).grid(row=3, column=0)
ttk.Button(rootGraph, text="6", command=lambda: appendNumberFormula("6")).grid(row=3, column=1)
ttk.Button(rootGraph, text="7", command=lambda: appendNumberFormula("7")).grid(row=3, column=2)
ttk.Button(rootGraph, text="8", command=lambda: appendNumberFormula("8")).grid(row=3, column=3)
ttk.Button(rootGraph, text="9", command=lambda: appendNumberFormula("9")).grid(row=3, column=4)
ttk.Button(rootGraph, text="sin", command=lambda: appendImplicit("sin(")).grid(row=4, column=0)
ttk.Button(rootGraph, text="cos", command=lambda: appendImplicit("cos(")).grid(row=4, column=1)
ttk.Button(rootGraph, text="tan", command=lambda: appendImplicit("tan(")).grid(row=4, column=2)
ttk.Button(rootGraph, text="π", command=lambda: appendImplicit("pi")).grid(row=4, column=3)
ttk.Button(rootGraph, text="e", command=lambda: appendImplicit("e")).grid(row=4, column=4)
ttk.Button(rootGraph, text="sinh", command=lambda: appendImplicit("sinh(")).grid(row=5, column=0)
ttk.Button(rootGraph, text="cosh", command=lambda: appendImplicit("cosh(")).grid(row=5, column=1)
ttk.Button(rootGraph, text="tanh", command=lambda: appendImplicit("tanh(")).grid(row=5, column=2)
ttk.Button(rootGraph, text="log", command=lambda: appendImplicit("log10(")).grid(row=5, column=3)
ttk.Button(rootGraph, text="ln", command=lambda: appendImplicit("log(")).grid(row=5, column=4)
ttk.Button(rootGraph, text="+", command=lambda: appendFormula("+")).grid(row=6, column=0)
ttk.Button(rootGraph, text="-", command=lambda: appendFormula("-")).grid(row=6, column=1)
ttk.Button(rootGraph, text="*", command=lambda: appendFormula("*")).grid(row=6, column=2)
ttk.Button(rootGraph, text="/", command=lambda: appendFormula("/")).grid(row=6, column=3)
ttk.Button(rootGraph, text="^", command=lambda: appendImplicit("**")).grid(row=6, column=4)
ttk.Button(rootGraph, text="(", command=lambda: appendClosingParenthesesFormula("(")).grid(row=7, column=0)
ttk.Button(rootGraph, text=")", command=lambda: appendFormula(")")).grid(row=7, column=1)
ttk.Button(rootGraph, text=".", command=lambda: appendFormula(".")).grid(row=7, column=2)
ttk.Button(rootGraph, text="Delete", command=lambda: deleteFormula()).grid(row=7, column=3)
ttk.Button(rootGraph, text="Clear", command=lambda: clearFormula()).grid(row=7, column=4)
ttk.Button(rootGraph, text="x", command=lambda: appendImplicit("x")).grid(row=8, column=0)
btnEnter = ttk.Button(rootGraph, text="Enter")
btnZoomIn = ttk.Button(rootGraph, text="Zoom In", command=lambda: zoomIn()).grid(row=8, column=2)
btnZoomOut = ttk.Button(rootGraph, text="Zoom Out", command=lambda: zoomOut()).grid(row=8, column=3)
ttk.Button(rootGraph, text="Exit App", command=lambda: exit(0)).grid(row=8, column=4)


rootGraph.iconbitmap("desmosLogo.ico")

btnEnter.bind('<Button-1>', drawGraph)

btnEnter.grid(row=8, column=1)
canvas.grid(row=0, column=0, columnspan=5)

drawGrid()
drawGraph("event")

rootGraph.mainloop()
