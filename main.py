from tkinter import *

from netaddr.strategy.ipv4 import width


#Tasks
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
def add_to_list():
    list_box.insert(list_box.size(),entry_box.get())

window = Tk()
#Window Settings
window.geometry("800x600")
window.title("To-Do-List")
app_icon = PhotoImage(file="images/app_icon.png")
window.iconphoto(True, app_icon)
window.config(bg="#b1c7c7")
window.resizable(0,0)
window.protocol("WM_DELETE_WINDOW",on_closing)
#Window Widgets
#Frame holding Entry box and add button
frame1 = Frame(window,padx=20,pady=20,relief=FLAT,bg="#b1c7c7",width=700)
frame1.pack()
#Add button
add_button = Button(frame1,
                    text="Add",
                    command=add_to_list,
                    relief=FLAT,
                    fg="white",
                    bg="black",
                    activeforeground="white",
                    activebackground="black",
                    padx=5,
                    pady=5)
add_button.grid(row=0,column=1)
#Entry box
entry_box = Entry(frame1,
                  font=('Constantia',13,'bold'),
                  bg="#FAFFFF",
                  relief=FLAT,
                  width=50)
entry_box.grid(row=0,column=0)
#Frame to add list box and few buttons
frame2 = Frame(window,padx=20,pady=20,relief=FLAT,bg="#b1c7c7")
frame2.pack()
#List Box
list_box = Listbox(frame2,
                   relief=FLAT,
                   bg="#c7eded",
                   font=("Constantia",13,"bold"),
                   width=55)
list_box.pack()
window.mainloop()