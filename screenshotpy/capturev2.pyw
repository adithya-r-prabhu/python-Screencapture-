import webbrowser, os



import datetime
import pyautogui
import time

def getTime():
    #GET THE CURRENT DATE AND TIME
    now = datetime.datetime.now()
    now_str = time.strftime("%H.%M.%S")
    outFile = pyautogui.screenshot('ImageFile{}.PNG'.format(now_str))

# getTime()

from tkinter import *
from tkinter import messagebox

tkWindow = Tk()  
tkWindow.geometry('140x30')  
tkWindow.geometry('+50+980')



tkWindow.title('capyture')

def showMsg():  
    messagebox.showinfo('Message', 'You clicked the Submit button!')



button = Button(tkWindow,
	text = 'CAPTURE▷',
    font=50,
	command = getTime,
    activebackground="violet",
    bg="light blue",
    fg='dark blue',
)  


tkWindow.attributes('-topmost',True)

tkWindow.overrideredirect(True)# for removing title bar

def Close():
    tkWindow.destroy()

# Button for closing
exit_button = Button(tkWindow, text="X", command=Close,
font=50,
    activebackground="red",
    bg="light blue",
    fg='dark blue',)
    
def openfolder():
    path="C:/Users/user pc/Desktop/screenshotpy"
    webbrowser.open(os.path.realpath(path))

folder_button =Button(tkWindow,text='/',command=openfolder,
font=50,    
    activebackground="red",
    bg="light blue",
    fg='dark blue',)

button.grid(row=0, column=0)
folder_button.grid(row=0, column=1)
exit_button.grid(row=0, column=2)

tkWindow.mainloop()

