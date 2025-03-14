from tkinter import *

from netaddr.strategy.ipv4 import width


#Tasks
def add_to_list():
    list_box.insert(list_box.size(),entry_box.get())
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
#Entry box
entry_box = Entry(window,
                  font=('Constantia',13,'bold'),
                  bg="#FAFFFF",
                  relief=FLAT)
entry_box.place(x=50,y=46,height=40,width=640)
#List Box
list_box = Listbox(window,
                   relief=FLAT,
                   bg="#c7eded",
                   font=("Constantia",13,"bold"))
list_box.place(x=50,y=150,width=700)
window.mainloop()