import tkinter
from tkinter import *
from tkcalendar.dateentry import DateEntry
import voice_input
#from tkinter.ttk import *

root = tkinter.Tk()
root.geometry("800x630")
root.title('Prescription Maker')

def call1():
    print("Computer")

    for widget in root.winfo_children():
        widget.destroy()

    Label(root, text="Patient's Details",height=2,bg='blue',font=("bold", 20)).pack(fill='x')
   #name_Frame = Frame(root)
    #name_Frame.pack()

    name_entry_text = tkinter.StringVar()      #text variable for name field
    def name_entry_event(event):               #event handling for name field
        print("Hello name")
        text = voice_input.get_audio()
        print(text)
        name_entry_text.set(text)
    Label(root,text='Name').place(x=100,y=100)          #rendering for name field
    name_entry = Entry(root,width=50,text=name_entry_text)
    name_entry.place(x=200,y=100)
    name_entry.bind('<Button-1>',name_entry_event)   #Event binding with name field

    age_entry_text = tkinter.StringVar()
    def age_entry_event(event):               #event handling for age field
        print("Hello age")
        text = voice_input.get_audio()
        print(text)
        age_entry_text.set(text)
    Label(root, text='Age').place(x=100, y=130)
    age_entry = Entry(root, width=50,text=age_entry_text)
    age_entry.place(x=200,y=130)
    age_entry.bind('<Button-1>', age_entry_event)

    Label(root, text='Gender').place(x=100, y=170)
    v = IntVar()
    Radiobutton(root, text='Male', variable=v, value=1).place(x=200,y=170)
    Radiobutton(root, text='Female', variable=v, value=2).place(x=275,y=170)

    def address_text_event(event):                    # event handling with address field
        print("Hello address")
        text = voice_input.get_audio()
        print(text)
        address_text.insert("end-1c", text)
    Label(root, text='Address').place(x=100, y=210)     #rendering user interface of address text
    address_text=Text(root, height=4,width=37)
    address_text.place(x=200, y=210)
    address_text.bind('<Button-1>', address_text_event)   #event binding with address text

    mobile_entry_text = tkinter.StringVar()
    def mobile_entry_event(event):  # event handling for age field
        print("Hello Mobile")
        text = voice_input.get_audio()
        print(text)
        mobile_entry_text.set(text)
    Label(root, text='Mobile No.').place(x=100, y=300)
    mobile_entry = Entry(root, width=50,text=mobile_entry_text)
    mobile_entry.place(x=200, y=300)
    mobile_entry.bind('<Button-1>', mobile_entry_event)

    Label(root, text='Height').place(x=100, y=340)
    Entry(root, width=30).place(x=200, y=340)

    OPTION1 = [
        "cm",
        "ft",
        "in"
    ]  # etc

    variable1 = StringVar(root)
    variable1.set('unit')  # default value

    unit1= OptionMenu(root, variable1, *OPTION1)
    unit1.place(x=410, y=340)


    Label(root, text='Weight').place(x=100, y=380)
    Entry(root, width=30).place(x=200, y=380)

    OPTION1 = [
        "kg",
        "lb"
    ]  # etc

    variable1 = StringVar(root)
    variable1.set('unit')  # default value

    unit1 = OptionMenu(root, variable1, *OPTION1)
    unit1.place(x=410, y=380)

    Label(root, text='Diagnosis').place(x=100, y=420)
    Entry(root, width=50).place(x=200, y=420)

    Label(root, text='Investigations').place(x=100, y=460)
    Entry(root, width=50).place(x=200, y=460)

    Label(root, text='Advice/Referrals').place(x=100, y=500)
    Text(root, height=4,width=37).place(x=200, y=500)

    Button(root,text='Add Drug',width=10).place(x=250, y=590)
    Button(root, text='Save',width=10).place(x=350, y=590)

Button(root, text='New Prescription', command=call1).pack()
root.mainloop()
