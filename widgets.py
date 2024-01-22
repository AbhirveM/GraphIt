import tkinter as tk

win = tk.Tk()
win.title('"Wolfram Alpha"')

frmTxtBox = tk.Frame()

txtBox = tk.Text(master=frmTxtBox, width=32, height=8, state='disabled', font=('default', 16))
txtBox.config(state='normal')
txtBox.insert(tk.INSERT, 'Enter your query')
txtBox.config(state='disabled')

frmNavButtons = tk.Frame(pady=8, padx=5)

btnSubmit = tk.Button(master=frmNavButtons, text='Submit', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btnRemove = tk.Button(master=frmNavButtons, text='⌫', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btnClearTxt = tk.Button(master=frmNavButtons, text='Clear', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btnNewLine = tk.Button(master=frmNavButtons, text='⤶', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btnSciFunctions = tk.Button(master=frmNavButtons, text='∑ⅆഽ', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btnSymbols = tk.Button(master=frmNavButtons, text='abc', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))

frmSci = tk.LabelFrame(text='Sci', font=('default', 12))

lblTrigonometry = tk.Label(master=frmSci, text='Trigonometry:', font=('default', 12))
lblInequality = tk.Label(master=frmSci, text='Inequality:', width=8, height=1, font=('default', 12))
lblCalculus = tk.Label(master=frmSci, text='Calculus:', width=8, height=1, font=('default', 12))
lblLog = tk.Label(master=frmSci, text='Log:', width=4, height=1, font=('default', 12))
lblOther = tk.Label(master=frmSci, text='Other:', width=4, height=1, font=('default', 12))

frmTrig = tk.Frame(master=frmSci, pady=8)

degTypeChoice = tk.IntVar()
btnSin = tk.Button(master=frmTrig, text='sin', width=5, height=1, font=('default', 12),  cursor='hand2')
btnCos = tk.Button(master=frmTrig, text='cos', width=5, height=1, font=('default', 12), cursor='hand2')
btnTan = tk.Button(master=frmTrig, text='tan', width=5, height=1, font=('default', 12), cursor='hand2')
btnCot = tk.Button(master=frmTrig, text='cot', width=5, height=1, font=('default', 12), cursor='hand2')
btnDegree = tk.Button(master=frmTrig, text='°', width=5, height=1, font=('default', 12), cursor='hand2')


frmCalculus = tk.Frame(master=frmSci, pady=8)

btnLimit = tk.Button(master=frmCalculus ,text='Limit:\n x-->', width=5, height=1, font=('default', 12), cursor='hand2')
entLimitValue = tk.Entry(master=frmCalculus, width=5, font=('default', 12))
btnInsertInfinity = tk.Button(master=frmCalculus, text='∞', width=5, height=1, font=('default', 12), cursor='hand2')
btnDerivative = tk.Button(master=frmCalculus, text='d/dx', width=5, height=1, font=('default', 12), cursor='hand2')
btnIntegral = tk.Button(master=frmCalculus, text='⎰', width=5, height=1, font=('default', 12), cursor='hand2')

frmLog = tk.Frame(master=frmSci, pady=8)

baseChoice = tk.IntVar()
btnLog = tk.Button(master=frmLog, text='log', width=5, height=1, font=('default', 12))
lblBase = tk.Label(master=frmLog, text='Base:', width=5, height=1, font=('default', 12))
entBase = tk.Entry(master=frmLog,  width=5, font=('default', 12))
btnE = tk.Button(master=frmLog, text='e', width=5, height=1, font=('default', 12), cursor='hand2')

frmExpandFactor = tk.Frame(master=frmSci, pady=8)

btnExpand = tk.Button(master=frmExpandFactor, text='Expand', bg='white', width=6, height=1, font=('default', 12), cursor='hand2')
btnFactor = tk.Button(master=frmExpandFactor, text='Factor', bg='white', width=6, height=1, font=('default', 12), cursor='hand2')

frmOtherSci = tk.Frame(master=frmSci, pady=8)


frmStandard = tk.LabelFrame(text='Standard', font=('default', 12))

btnParenthesesRight = tk.Button(master=frmStandard, text='(', width=5, height=2, cursor='hand2', font=('default', 12))
btnParenthesesLeft = tk.Button(master=frmStandard, text=')', width=5, height=2, cursor='hand2', font=('default', 12))
btnSeven = tk.Button(master=frmStandard, text='7', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnEight = tk.Button(master=frmStandard, text='8', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnNine = tk.Button(master=frmStandard, text='9', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnDivide = tk.Button(master=frmStandard, text='/', width=5, height=2, cursor='hand2', font=('default', 12))

btnSquare = tk.Button(master=frmStandard, text='²', width=5, height=2, cursor='hand2', font=('default', 12))
btnSquareRoot = tk.Button(master=frmStandard, text='√', width=5, height=2, cursor='hand2', font=('default', 12))
btnFour = tk.Button(master=frmStandard, text='4', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnFive = tk.Button(master=frmStandard, text='5', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnSix = tk.Button(master=frmStandard, text='6', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnMultiply = tk.Button(master=frmStandard, text='*', width=5, height=2, cursor='hand2', font=('default', 12))

btnCube = tk.Button(master=frmStandard, text='³', width=5, height=2, cursor='hand2', font=('default', 12))
btnCubeRoot = tk.Button(master=frmStandard, text='∛', width=5, height=2, cursor='hand2', font=('default', 12))
btnOne = tk.Button(master=frmStandard, text='1', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnTwo = tk.Button(master=frmStandard, text='2', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnThree = tk.Button(master=frmStandard, text='3', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnMinus = tk.Button(master=frmStandard, text='-', width=5, height=2, cursor='hand2', font=('default', 12))

btnPi = tk.Button(master=frmStandard, text='Ⲡ', width=5, height=2, cursor='hand2', font=('default', 12))
btnX = tk.Button(master=frmStandard, text='x', width=5, height=2, cursor='hand2', font=('default', 12))
btnZero = tk.Button(master=frmStandard, text='0', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btnDot = tk.Button(master=frmStandard, text='.', width=5, height=2, cursor='hand2', font=('default', 12))
btnEqual = tk.Button(master=frmStandard, text='=', width=5, height=2, cursor='hand2', font=('default', 12))
btnPlus = tk.Button(master=frmStandard, text='+', width=5, height=2, cursor='hand2', font=('default', 12))


frmSymbols = tk.LabelFrame(text='Symbols', font=('default', 12))

symbolBtns = [tk.Button(master=frmSymbols, text=chr(i), width=5, height=2, cursor='hand2', font=('default', 12))
                for i in range(97, 123)]
