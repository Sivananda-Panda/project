from tkinter import *

import part_2_back_end_1

def get_selected_row(event):#special fn for bind method. Event arg is a special arg
    global selected_tuple
    index=list1.curselection()[0]#take the position of data in list box
    selected_tuple=list1.get(index)
    #return selected_tuple
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

    
def view_command():
    list1.delete(0,END) #to get rid of duplicate data. Deleting from first to end.
    for row in part_2_back_end_1.view():
        list1.insert(END, row)#takes two args, 1 index where to insert, 2nd the data
                              #END always put the new data end of previous data

def search_command():#getting the args from entry ie e1,e2,e3,e4
    list1.delete(0,END)
    for row in part_2_back_end_1.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    part_2_back_end_1.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    part_2_back_end_1.delete(selected_tuple[0])

def update_command():
    part_2_back_end_1.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window=Tk()

window.wm_title("BookStore")#title of the app.

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)#while we click a row in list box it will show to wntry boxes. So we have to bind the list box to a fn which get all the data of corresponding row.

b1=Button(window,text="View all", width=12,command=view_command)#dont call the fn. Just mention. coz python again will run and tkinter will also run the fn.
b1.grid(row=2,column=3)

b2=Button(window,text="Search an entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add an entry", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update entry", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
