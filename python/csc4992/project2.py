from random import shuffle
from tkinter import *

root = Tk()
root.title("War")
root.geometry("1280x720")


def shuffle():
  pass

main_frame = Frame(root)
main_frame.pack(pady=20)

dealer_card = LabelFrame(main_frame, text = 'Dealer Card', bd=0)
dealer_card.grid(row = 0, column = 0, padx = 20, ipadx = 20)

player_card = LabelFrame(main_frame, text = 'Player Card', bd=0)
player_card.grid(row = 0, column = 1, padx = 0, ipadx = 20)

dealer_label = Label(dealer_card, text = '')
dealer_label.pack(pady=20)

player_label = Label(player_card, text = '')
player_label.pack(pady=20)

shuffle_btn = Button(root, text='Shuffle')
shuffle_btn.pack(pady=20)
root.mainloop()