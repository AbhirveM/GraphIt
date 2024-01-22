from widgets import win
from gui import initGuiLayout, assignBtnFuncs

#Runs the main loop

initGuiLayout()
assignBtnFuncs()
win.iconbitmap('wolframLogo.ico')

win.mainloop()
