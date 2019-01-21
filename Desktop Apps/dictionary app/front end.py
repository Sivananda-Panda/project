''' A beautiful dictionary program that helps you to find the meaning of almost
all english words'''

from tkinter import *

import back_end

#commands for buttons to work

def search_command():
    list1.delete(0,END)
    list2.delete(0,END)
    result, flag1 = back_end.translate(word_text.get())#also u can take result as list and access the items in list(no need to take extra arg flag1)
    '''if type(back_end.translate(word_text.get()))==list:
        if not flag: #if u have mentioned left or right in back end, pass the condition as if left or if right
            for word in back_end.translate(word_text.get()):
                list1.insert(END, word)
        else:
            for word in back_end.translate(word_text.get()):
                list2.insert(END, word)
    else:
        list1.insert(END, back_end.translate(word_text.get()))'''
    if type(result)==list:
        if not flag1:
            for item in result:
                list1.insert(END, item)
        elif flag1:
            for item in result:
                list2.insert(END, item)
    else:
        list1.insert(END,result)

def get_selection(event):
    selection = list2.curselection()
    selected = list2.get(selection)
    e1.delete(0, END)
    e1.insert(END, selected)
    search_command()
        
window=Tk()
window.wm_title('Dictionary')

#lebels that display the names of the boxes

l1=Label(window,text='Enter the Word')
l1.grid(row=0, column=0)

l2=Label(window, text='Suggetions')
l2.grid(row=1, column=0)

l2=Label(window, text='Meaning')
l2.grid(row=1, column=1)

#Entry bar to enter the word

word_text=StringVar()#always write '_text' or else u get UnboundLocalError
e1=Entry(window,textvariable=word_text)
e1.grid(row=0, column=1)

#Button to search

b1=Button(window, text='Search', width=15, command=search_command)
b1.grid(row=0, column=2)

#List box to display all the contents

list1=Listbox(window, height=36, width=135)
list1.grid(row=2, column=1, rowspan=6, columnspan=3)

list2=Listbox(window, height=36, width=35)
list2.grid(row=2, column=0)

#to take the selected word into account

list2.bind("<<ListboxSelect>>", get_selection)

window.mainloop()
