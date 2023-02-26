from tkinter import *
import pickle, datetime, os, random, time, string

# Create Object
root = Tk()
root.title("Hotel Registration")


# Add new guest
def add_guest():

    with open ('hotelreg.pkl','rb') as F:
        db = pickle.load(F)
    

    # Get input info
    name = name_entry.get().translate(str.maketrans('', '', string.punctuation))
    address = addy_entry.get().translate(str.maketrans('', '', string.punctuation))
    if pay_var.get() == 1:
        payment = 'Cash'
    else:
        payment = 'Credit Card'
    duration = duration_entry.get().translate(str.maketrans('', '', string.punctuation))
    room = room_entry.get().translate(str.maketrans('', '', string.punctuation))
    Time = time.ctime()
    GuestID = ''.join(name[0] + str(random.randrange(1000,9999)))
    guest_attr=[name, address, payment, duration, room, Time]

    # add input data to list
    db[GuestID] = guest_attr
    
    # write guest data to file with pickle
    with open ('hotelreg.pkl', 'wb' ) as F:
        pickle.dump(db,F)

    info_output.configure(text= GuestID + '\n' + str(db[GuestID]))


# Frames
form_frame = LabelFrame(root, text='Form')
form_frame.grid(row=0,  columnspan=4, sticky='W',
                padx=5,  pady=5, ipadx=5, ipady=5)


# Name
name_label = Label(form_frame, text='Guest Name:')
name_label.grid(row=0, column=0, sticky='E', padx=5, pady=2)
name_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
name_entry.grid(row=0, column=1, sticky='E', padx=5, pady=2)

# Address
addy_label = Label(form_frame, text='Address:')
addy_label.grid(row=1, column=0, sticky='E', padx=5, pady=2)
addy_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
addy_entry.grid(row=1, column=1, sticky='E', padx=5, pady=2)

# Payment
pay_var = IntVar()
payment_label = Label(form_frame, text='Payment Type:')
payment_label.grid(row=2, column=0, sticky='E', padx=5, pady=2)
payment_cash = Radiobutton(form_frame, text="Cash", variable=pay_var, value=1)
payment_cash.grid(row=2, column=1, sticky='W', padx=5, pady=2)
payment_credit = Radiobutton(form_frame, text="Credit Card", variable=pay_var, value=0)
payment_credit.grid(row=2, column=1, padx=5, pady=2)

# Length of stay
duration_label = Label(form_frame, text='Length of stay:')
duration_label.grid(row=3, column=0, sticky='E', padx=5, pady=2)
duration_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
duration_entry.grid(row=3, column=1, sticky='E', padx=5, pady=2)

# Room number
room_label = Label(form_frame, text='Room Number:')
room_label.grid(row=4, column=0, sticky='E', padx=5, pady=2)
room_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
room_entry.grid(row=4, column=1, rowspan=2, sticky='E', padx=5, pady=2)

# Output
info_frame = LabelFrame(root, text='Entered Info')
info_frame.grid(row=7, columnspan=4, sticky='WE',
                padx=5,  pady=5, ipadx=5, ipady=5)
info_output = Label(info_frame, justify=LEFT)
info_output.grid(row=0, column=0, sticky='W', padx=5, pady=2)

# Submit
submit_button = Button(root, text='Add Data', command=add_guest)
submit_button.grid(row=10, column = 2, sticky='W',
                padx=5,  pady=5, ipadx=5, ipady=5)

root.mainloop()