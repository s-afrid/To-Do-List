from tkinter import *
from tkinter import messagebox


#Tasks
def import_from():
    with open('log.txt','r') as file:
        for i in file.readlines():
            list_box.insert(END,i.strip())

def on_closing():
    if messagebox.askokcancel(title="Quit",message="Do you want to close?"):
        with open('log.txt','w') as file:
            for i in list_box.get(0,END):
                file.write(i+"\n")
        window.destroy()
def add_to_list():
    list_box.insert(list_box.size(),entry_box.get())
window = Tk()
#Window Settings
window.geometry("800x600")
window.title("To-Do-List")
#All icon photo images
app_icon = PhotoImage(file="images/app_icon.png")

window.iconphoto(True, app_icon)
window.config(bg="#b1c7c7")
window.resizable(0,0)
window.protocol("WM_DELETE_WINDOW",on_closing)
#Window Widgets
app_title = Label(window,text="To-Do List",
                  bg="#b1c7c7",
                  fg="black",
                  font=('Arial',30,'bold'))
app_title.pack()
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
#Label
label1 = Label(frame2,
               text="Tasks",
               font=('Arial',15,'bold'),
               bg="#b1c7c7",
               fg="black")
label1.grid(row=0,column=0,columnspan=12)
#List Box
list_box = Listbox(frame2,
                   relief=FLAT,
                   bg="#c7eded",
                   font=("Constantia",13,"bold"),
                   width=55,
                   height=10,
                   selectmode=MULTIPLE)
list_box.grid(row=1,column=0,columnspan=12)
import_from()
#Button to check mark tasks
mark_complete = Button(frame2,command=mark_complete,borderwidth=0,
                       text="\U00002713",
                       bg="black",
                       fg="white",
                       activebackground="black",
                       activeforeground="white")
mark_complete.grid(row=2,column=0)
#Button to uncheck tasks
mark_incomplete = Button(frame2,command=mark_incomplete,borderwidth=0,
                         text="\U00010102",
                         bg="black",
                         fg="white",
                         activebackground="black",
                         activeforeground="white"
                         )
mark_incomplete.grid(row=2,column=1)
delete_button = Button(frame2,command=delete_task,borderwidth=0,
                       text="Delete",
                       bg="black",
                       fg="white",
                       activebackground="black",
                       activeforeground="white"
                       )
delete_button.grid(row=2,column=2)
window.mainloop()