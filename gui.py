from functions import *

# adds classes for each button
def placeNavPanel():
    txtBox.grid(row=1, column=0, sticky='new')
    i = 0
    for btn in frmNavButtons.children:
        frmNavButtons.children[btn].grid(row=0, column=i)
        i += 1

def placeStdBtns():
    i, j = 0, 0
    for btn in frmStandard.children:
        frmStandard.children[btn].grid(row=j, column=i)
        i += 1
        if i == 6:
            i = 0
            j += 1

def placeSymbolsBtns():
    i, j = 0, 0
    for btn in frmSymbols.children:
        frmSymbols.children[btn].grid(row=j, column=i)
        i += 1
        if i % 10 == 0:
            j += 1
            i = 0

def placeSciFuncBtns():
    i = 0
    for btn in frmCalculus.children:
        frmCalculus.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frmExpandFactor.children:
        frmExpandFactor.children[btn].grid(row=0, column=i, padx=4)
        i += 1

    i = 0
    for btn in frmLog.children:
        frmLog.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frmTrig.children:
        frmTrig.children[btn].grid(row=0, column=i)
        i += 1

    i = 0

def initGuiLayout():
    placeNavPanel()
    placeStdBtns()
    placeSciFuncBtns()
    placeSymbolsBtns()
    frmTxtBox.pack()
    frmNavButtons.pack()
    frmStandard.pack()

    lblTrigonometry.pack()
    frmTrig.pack()
    lblCalculus.pack()
    frmCalculus.pack()
    lblLog.pack()
    frmLog.pack()
    lblOther.pack()
    frmOtherSci.pack()
    frmExpandFactor.pack()

def assignBtnFuncs():
    btnLog.configure(command=lambda: insertBtnTxt(btnLog))

    btnE.configure(command=lambda: insertBtnTxt(btnE))
    btnDerivative.configure(command=lambda: compute('derivative'))
    btnIntegral.configure(command=lambda: compute('integral'))

    btnSubmit.configure(command=lambda: submit())
    btnRemove.configure(command=lambda: removeChar())
    btnClearTxt.configure(command=lambda: clearTxt())
    btnNewLine.configure(command=lambda: insertNewLine())
    btnSciFunctions.configure(command=lambda: showHideSciFunctions())
    btnSymbols.configure(command=lambda: showHideSymbols())

    btnExpand.configure(command=lambda: compute('expandExpression'))
    btnFactor.configure(command=lambda: compute('factorExpression'))

    btnLimit.configure(command=lambda: compute('limit'))
    btnInsertInfinity.configure(command=lambda: entLimitValue.insert(tk.END, '∞'))

    for btn in frmTrig.children:
        frmTrig.children[btn]['command'] = lambda x=frmTrig.children[btn]: insertBtnTxt(x)

    for btn in frmStandard.children:
        frmStandard.children[btn]['command'] = lambda x=frmStandard.children[btn]: insertBtnTxt(x)

    for btn in frmSymbols.children:
        frmSymbols.children[btn]['command'] = lambda x=frmSymbols.children[btn]: insertBtnTxt(x)
