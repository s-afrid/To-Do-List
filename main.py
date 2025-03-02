from tkinter import *

window = Tk()
#Window Settings
window.geometry("800x600")
window.title("To-Do-List")
app_icon = PhotoImage(file="images/app_icon.png")
window.iconphoto(True, app_icon)
window.config(bg="#b1c7c7")
#Window Widgets

window.mainloop()