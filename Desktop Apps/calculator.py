from tkinter import *
import parser

#get the user input and place it in the textfield
i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1

#to get the expressions into display
def get_operation(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

#to get dine the calculations
def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()#to get dine the calculations we are using inbuilt fn
        result=eval(a)#to evaluate
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,'Error')
        
#for ac button
def clear_all():
    display.delete(0,END)

#for back clear fn
def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        display.insert(0,'Error')
    


root=Tk()
root.title('Calculator')

#adding the input field

display= Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

#adding buttos to the calculator

Button(root,text='1',width=2,command=lambda :get_variables(1)).grid(row=2,column=0)
Button(root,text='2',width=2,command=lambda :get_variables(2)).grid(row=2,column=1)
Button(root,text='3',width=2,command=lambda :get_variables(3)).grid(row=2,column=2)

Button(root,text='4',width=2,command=lambda :get_variables(4)).grid(row=3,column=0)
Button(root,text='5',width=2,command=lambda :get_variables(5)).grid(row=3,column=1)
Button(root,text='6',width=2,command=lambda :get_variables(6)).grid(row=3,column=2)

Button(root,text='7',width=2,command=lambda :get_variables(7)).grid(row=4,column=0)
Button(root,text='8',width=2,command=lambda :get_variables(8)).grid(row=4,column=1)
Button(root,text='9',width=2,command=lambda :get_variables(9)).grid(row=4,column=2)

#adding other buttons to the calculator
Button(root,text="AC",width=2, command=lambda :clear_all()).grid(row=5,column=0)
Button(root,text="0",width=2,command=lambda :get_variables(0)).grid(row=5,column=1)
Button(root,text="=",width=2,command=lambda :calculate()).grid(row=5,column=2)

Button(root,text="+",width=2,command=lambda :get_operation('+')).grid(row=2,column=3)
Button(root,text="-",width=2,command=lambda :get_operation('-')).grid(row=3,column=3)
Button(root,text="*",width=2,command=lambda :get_operation('*')).grid(row=4,column=3)
Button(root,text="/",width=2,command=lambda :get_operation('/')).grid(row=5,column=3)

#adding new operations
Button(root,text="pi",width=2,command=lambda :get_operation('*3.14')).grid(row=2,column=4)
Button(root,text="%",width=2,command=lambda :get_operation('%')).grid(row=3,column=4)
Button(root,text="(",width=2,command=lambda :get_operation('(')).grid(row=4,column=4)
Button(root,text="exp",width=2,command=lambda :get_operation('**')).grid(row=5,column=4)

Button(root,text="<-",width=2,command=lambda :undo()).grid(row=2,column=5)
Button(root,text="x!",width=2).grid(row=3,column=5)
Button(root,text=")",width=2,command=lambda :get_operation(')')).grid(row=4,column=5)
Button(root,text="^2",width=2,command=lambda :get_operation('**2')).grid(row=5,column=5)

root.mainloop()
