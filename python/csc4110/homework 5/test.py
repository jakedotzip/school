from tkinter import *       
 
# Create Object
root = Tk()
root.title("Data Capture")
dataList = []
# Add to list
def add_to_list():
    name = name_entry.get()
    age = age_entry.get()
    address = addy_entry.get()
    email = email_entry.get()
    if v.get() == TRUE:
        p30 = 'YES'
    else:
        p30 = 'NO'
    comment = cmt_entry.get()
    printList = [name, age, address, email, p30 , comment]
    dataList.append(printList)
    info_output.configure(text = name + '\n' 
                                + email + '\n'
                                + age + '\n'
                                + address + '\n'
                                + p30 + '\n'
                                + comment)
    print(printList)

# Frames
form_frame = LabelFrame(root, text='Form')
form_frame.grid(row=0,  columnspan=4, sticky='W',
                padx=5,  pady=5, ipadx=5, ipady=5)


# Name
name_label = Label(form_frame, text='Voter Name:')
name_label.grid(row=0, column=0, sticky='E', padx=5, pady=2)
name_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
name_entry.grid(row=0, column=1, sticky='E', padx=5, pady=2)

# Age
age_label = Label(form_frame, text='Age:')
age_label.grid(row=1, column=0, sticky='E', padx=5, pady=2)
age_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
age_entry.grid(row=1, column=1, sticky='E', padx=5, pady=2)

# Address
addy_label = Label(form_frame, text='Address:')
addy_label.grid(row=2, column=0, sticky='E', padx=5, pady=2)
addy_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
addy_entry.grid(row=2, column=1, sticky='E', padx=5, pady=2)

# Email
email_label = Label(form_frame, text='Email:')
email_label.grid(row=3, column=0, sticky='E', padx=5, pady=2)
email_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
email_entry.grid(row=3, column=1, sticky='E', padx=5, pady=2)

# P30
v = IntVar()
p30_label = Label(form_frame, text='Prop 30?')
p30_label.grid(row=4, column=0, sticky='E', padx=5, pady=2)
p30_yes = Radiobutton(form_frame, text="Yes", variable=v, value=1)
p30_yes.grid(row=4, column=1, sticky='W', padx=5, pady=2)
p30_no = Radiobutton(form_frame, text="No", variable=v, value=0)
p30_no.grid(row=4, column=1, padx=5, pady=2)

# Comment
cmt_label = Label(form_frame, text='Comment:')
cmt_label.grid(row=5, column=0, sticky='E', padx=5, pady=2)
cmt_entry = Entry(form_frame, font = ("Calibri", 16), background="#dedddc")
cmt_entry.grid(row=5, column=1, rowspan=2, sticky='E', padx=5, pady=2)

# Output
info_frame = LabelFrame(root, text='Entered Info')
info_frame.grid(row=7, columnspan=4, sticky='WE',
                padx=5,  pady=5, ipadx=5, ipady=5)
info_output = Label(info_frame, justify=LEFT)
info_output.grid(row=0, column=0, sticky='W', padx=5, pady=2)



# Submit
submit_button = Button(root, text='Submit', command=add_to_list)
submit_button.grid(row=10, column = 2, sticky='W',
                padx=5,  pady=5, ipadx=5, ipady=5)

root.mainloop()