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




tkWindow = Tk()  
tkWindow.geometry('164x60')  
tkWindow.geometry('+50+980')



tkWindow.title('capyture')

tkWindow.iconbitmap("icons/Untitled design.ico")






button = Button(tkWindow,
	text = 'CAPTUR▷',
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

folder_button =Button(tkWindow,text='f:/',command=openfolder,
font=50,    
    activebackground="red",
    bg="light blue",
    fg='dark blue',)

#telegram
def opentelegram():
    path="D:/Telegram/Telegram.exe"
    webbrowser.open(os.path.realpath(path))
telegram = PhotoImage(file='icons/telegram.png')
telegram_button=Button(tkWindow,
text="TELEGRAM",
image=telegram,compound=LEFT,
command=opentelegram,
    activebackground="red",
    bg="light green",
    fg='dark blue',)

#whattsapp  
def openwhattsapp():
    path="C:/Users/user pc/AppData/Local/WhatsApp/WhatsApp.exe"
    webbrowser.open(os.path.realpath(path))
whattsapp = PhotoImage(file='icons/whattsapp.png')
whattsapp_button=Button(tkWindow,
text="",
image=whattsapp,
command=openwhattsapp,
font=50,
    activebackground="red",
    bg="light green",
    fg='dark blue',)

#edge
def openedge():
    path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
    webbrowser.open(os.path.realpath(path))
edge = PhotoImage(file='icons/edge.png')
edge_button=Button(tkWindow,
text="",
image=edge,
command=openedge,
font=50,
    activebackground="red",
    bg="light green",
    fg='dark blue',)

#minimizing

def minimizing():
    tkWindow.overrideredirect(False)
    tkWindow.wm_state('iconic')
    tkWindow.iconify()




minimizing_button=Button(tkWindow,
text="⇲",
font=60,
command=minimizing,
    activebackground="red",
    bg="light blue",
    fg='dark blue',)

n=True



def removetitlebar():
    global n
    
    if n:
        #with titlebar
        tkWindow.overrideredirect(False)
        tkWindow.geometry('240x60')
  
        n=False
    else: 
        # without title bar 
        tkWindow.overrideredirect(True)
        tkWindow.geometry('164x60') 
        n=True



    


removetitlebar_button=Button(tkWindow,
text="▭",
font=60,
command=removetitlebar,
    activebackground="red",
    bg="light blue",
    fg='dark blue',)

button.grid(row=0, column=0)
folder_button.grid(row=0, column=1)
minimizing_button.grid(row=0,column=2)
exit_button.grid(row=0, column=3)
telegram_button.grid(row=1,column=0)
whattsapp_button.grid(row=1,column=1)
edge_button.grid(row=1,column=2)
removetitlebar_button.grid(row=1,column=3)
tkWindow.mainloop()
