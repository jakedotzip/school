from tkinter import *
from tkinter import messagebox

# Create important variables
buttonClicked = False
used_rate = 0
root = Tk()
root.title("Currency Conversion")
root.geometry("480x640")

# Create currency dictionary
currencyDict = { 'EUR': 1.09, 'GBP': 1.31, 'AUD': 0.76, 'JPY': 0.0081, 'KRW': 0.00082}

# Create output file to write
out_file = open("currencyConversion.txt", "w")
out_file.write("Currency,Input,Output\n")



# This function to make sure user selected a currency
def clicked(code):
  global buttonClicked
  global used_rate
  buttonClicked = True
  # when user chose a currency, a code will be used to determine which currency is selected
  used_rate = currencyDict[code]
  

# Create separate functions for each currency
def eur_usd(code):
  global used_rate
  output_frame.config(text = "Euro (EUR) to US Dollar (USD)")
  convert_label.config(text = "1 EUR equals")
  convert_rate.config(text = f'{currencyDict[code]} USD')
  clicked(code)
  
def gbp_usd(code):
  global used_rate
  output_frame.config(text = "Pound (GBP) to US Dollar (USD)")
  convert_label.config(text = "1 GBP equals")
  convert_rate.config(text = f'{currencyDict[code]} USD')
  clicked(code)
  
def aud_usd(code):
  global used_rate
  output_frame.config(text = "Australian Dollar (AUD) to US Dollar (USD)")
  convert_label.config(text = "1 AUD equals")
  convert_rate.config(text = f'{currencyDict[code]} USD')
  clicked(code)

def jpy_usd(code):
  global used_rate
  output_frame.config(text = "Japanese Yen (JPY) to US Dollar (USD)")
  convert_label.config(text = "1 JPY equals")
  convert_rate.config(text = f'{currencyDict[code]} USD')
  clicked(code)

def krw_usd(code):
  global used_rate
  output_frame.config(text = "South Korean Won (KRW) to US Dollar (USD)")
  convert_label.config(text = "1 KRW equals")
  convert_rate.config(text = f'{currencyDict[code]} USD')
  clicked(code)

# When convert button clicked  
def convert():
  if not input_entry.get():   # throw error if nothing in entry box
    messagebox.showwarning("ERROR!", "You must enter a number before pressing 'Convert'")
  elif buttonClicked == False:   # throw error if user havent selected a currency
    messagebox.showwarning("ERROR!", "You forget to choose currency")
  else:
    # calculation
    converted_result = float(input_entry.get()) * used_rate
    converted_result = round(converted_result, 2)
    # write to output file
    write2file(list(currencyDict.keys())[list(currencyDict.values()).index(used_rate)], input_entry.get(), converted_result)
    # make it not look weird
    converted_result = '{:,}'.format(converted_result)
    output_label.config(text = f'${converted_result}')
    
# Function to write to .txt file
def write2file(rate,entry,result):
  out_file.write(str(rate) + "," + str(entry) + "," + str(result) + "\n")


# currency frame
currency_frame = LabelFrame(root, text = "Choose a currency", width = 450, pady = 20)
currency_frame.pack(fill = 'x', padx = 20, pady = 10)

# currency buttons
eur = Button(currency_frame, text = "Euro (EUR)", bg = "#525151", padx = 25, command = lambda: eur_usd("EUR"))
eur.pack(padx = 20, pady = 8)

gbp = Button(currency_frame, text= "Pound (GBP)", padx = 25, command = lambda: gbp_usd("GBP"))
gbp.pack(padx = 20, pady = 8)

aud = Button(currency_frame, text= "Australian Dollar (AUD)", padx = 25, command = lambda: aud_usd("AUD"))
aud.pack(padx = 20, pady = 8)

jpy = Button(currency_frame, text= "Japanese Yen (JPY)", padx = 25, command = lambda: jpy_usd("JPY"))
jpy.pack(padx = 20, pady = 8)

krw = Button(currency_frame, text= "South Korean Won (KRW)", padx = 25, command = lambda: krw_usd("KRW"))
krw.pack(padx = 20, pady = 8)

# display convert rate
convert_label = LabelFrame(root, text = "Conversion rate", width = 450, height = 80)
convert_label.pack(padx = 20, pady=10)
convert_rate = Label(convert_label, font = ("Calibri", 24), text = "0", width = 450)
convert_rate.pack(pady=5)

# input frame
input_frame = LabelFrame(root, text = "Amount to convert", width = 450, height = 300)
input_frame.pack(fill = 'x', padx = 20)

# entry box 
input_entry = Entry(input_frame, font = ("Calibri" , 24), background="#dedddc")
input_entry.pack(pady=5, padx=20)

# convert button
convert_button = Button(input_frame, text = "Convert", highlightbackground="#8ea390", padx = 15, pady = 8, command=convert)
convert_button.pack(padx = 20, pady = 10)

# output frame
output_frame = LabelFrame(root, text = "to US Dollar (USD)", width = 450, height = 200)
output_frame.pack(fill='both', padx = 20, pady = 20)
output_label = Label(output_frame, text = "", font = ("Calibri", 24), width = 400, height = 150)
output_label.pack(fill = 'x', padx = 20)

root.mainloop()



