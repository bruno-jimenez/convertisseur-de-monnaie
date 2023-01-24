from tkinter import *


# Global Layout

conv = Tk()
conv.geometry('480x360')
conv.title('convertisseur-de-monnaie')
frame = Frame(conv, width=480, height=480, bg='gray60')
frame.grid(row=0, column=0)

# Set list of currency and StringVar

currency_list = ['Dollar', 'Euro', 'Livre Sterling', 'Yen']
value1 = StringVar()
value2 = StringVar()
change = ''
result = StringVar()

# Button and choice layout

from_currency_label = Label(frame, text='FROM:', justify=LEFT)
from_currency_label.place(x=20, y=30)
to_currency_label = Label(frame, text='TO:', justify=RIGHT)
to_currency_label.place(x=240, y=30)

value1.set(currency_list[0])
from_currency_menu = OptionMenu(frame, value1, *currency_list)
from_currency_menu.place(x=20, y=60)

value2.set(currency_list[1])
to_currency_menu = OptionMenu(frame, value2, *currency_list)
to_currency_menu.place(x=240, y=60)

amount_label = Label(frame, text='AMOUNT:')
amount_label.place(x=20, y=120)

amount_entry = Entry(frame, width=55, textvariable=result)
amount_entry.place(x=20, y=150)

convert_button = Button(frame, text="CONVERT", bg='orange', fg='white', command=lambda: convert_calc(),width=15 ,height=5)
convert_button.place(x=20, y=240)


# Function to convert each currency into another


def convert_calc():
    global change 
    #dollars en euro
    if value1.get() == "Dollar" and value2.get() == "Euro":
        change = str(float(result.get())*0.90)
        result.set(change)

    #dollars en livre
    elif value1.get() == "Dollar" and value2.get() == "Livre Sterling":
        change = str(float(result.get()) * 0.80)
        result.set(change)

    #livre en euro
    elif value1.get() == "Livre Sterling" and value2.get() == "Euro":
        change = str(float(result.get()) * 1.1)
        result.set(change)

    #livre en dollars
    elif value1.get() == "Livre Sterling" and value2.get() == "Dollar":
        change = str(float(result.get()) * 1.2)
        result.set(change)

    #euro en dollar
    elif value1.get() == "Euro" and value2.get() == "Dollar":
        change = str(float(result.get()) * 1.08)
        result.set(change)

    #euro en livre
    elif value1.get() == "Euro" and value2.get() == "Livre Sterling":
        change = str(float(result.get()) * 0.88)
        result.set(change)

    #Yen en dollars
    elif value1.get() == "Yen" and value2.get() == "Dollar":
        change = str(float(result.get()) * 0.00768)
        result.set(change)

    #dollars en Yen
    elif value1.get() == "Dollar" and value2.get() == "Yen":
        change = str(float(result.get()) * 130.209)
        result.set(change)

    #euro en Yen
    elif value1.get() == "Euro" and value2.get() == "Yen":
        change = str(float(result.get()) * 141.491)
        result.set(change)

    #Yen en euro
    elif value1.get() == "Yen" and value2.get() == "Euro":
        change = str(float(result.get()) * 0.00707)
        result.set(change)

    #Yen en euro
    elif value1.get() == "Yen" and value2.get() == "Livre Sterling":
        change = str(float(result.get()) * 0.00623)
        result.set(change)

    #euro en Yen
    elif value1.get() == "Livre Sterling" and value2.get() == "Yen":
        change = str(float(result.get()) * 160.45)
        result.set(change)

conv.mainloop()
