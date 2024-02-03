import tkinter

surf = tkinter.Tk()
surf.geometry("800x600+100+10")

button_quit = tkinter.Button(surf ,text="quit" ,command = surf.quit)
button_quit.pack()
surf.mainloop()
