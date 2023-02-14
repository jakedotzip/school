from tkinter import *

def add_to_list():
    """ Add to list """


# Set up the window
root = Tk()
root.title("political_poll")
root.geometry("750x450")
root.configure(bg='gray')

# Create the conversion Button and result display Label
add_info = Button(
    root,
    text="Enter Voter Name, Age, Address, Contact, YES/NO"    
)



root.mainloop()