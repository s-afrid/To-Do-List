from tkinter import *
#Tasks
def add_to_list():
    pass
window = Tk()
#Window Settings
window.geometry("800x600")
window.title("To-Do-List")
app_icon = PhotoImage(file="images/app_icon.png")
window.iconphoto(True, app_icon)
window.config(bg="#b1c7c7")
#Window Widgets
#Add button
add_button = Button(window,
                    text="Add",
                    command=add_to_list,
                    relief=FLAT,
                    fg="white",
                    bg="black",
                    activeforeground="white",
                    activebackground="black")
add_button.place(x=700,y=50)
window.mainloop()