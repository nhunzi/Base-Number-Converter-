from tkinter import *
import tkinter.messagebox


# function to get the key by value in python dictionary
def find_key(d, val):
    for key, value in d.items():
        if value == val:
            return key


def convert_number(n, startbase, endbase):
    # Pairs dictionary
    pairs = {"0": 0, "1": 1, "2": 2, "3": 3,
             "4": 4, "5": 5, "6": 6,
             "7": 7, "8": 8, "9": 9,
             "A": 10, "B": 11, "C": 12,
             "D": 13, "E": 14, "F": 15}
    # Deals with non capital letters
    n = n.upper()
    # Check to see if number is valid
    for i in range(len(n)):
        if n[i] not in pairs.keys():
            return -1
        if pairs.get(n[i]) > startbase:
            return -1

    # Check to make sure bases are different. If they aren't, just return the #
    if startbase == endbase:
        return n

    # Convert the number given to decimal
    decimalnumber = 0
    for i in range(len(n)):
        decimalnumber += pairs.get(n[i]) * (startbase ** (len(n) - i - 1))

    # Convert decimal number to the end base number
    convertednumber = ""
    while decimalnumber != 0:
        remainder = decimalnumber % endbase
        if remainder < 10:
            convertednumber += str(remainder)
        else:
            convertednumber += find_key(pairs, remainder)
        decimalnumber = decimalnumber // endbase

    convertednumber = convertednumber[::-1]
    return convertednumber


def print_to_screen():
    number = entry_1.get().upper()
    startbase = c.get()
    endbase = d.get()
    result = convert_number(number, int(startbase), int(endbase))
    successmessage = str(number) + " in base " + str(startbase) + " is equal to " + str(result) + " in base " + str(
        endbase)
    if result != -1:
        tkinter.messagebox.showinfo("Number Converter", successmessage)
    else:
        tkinter.messagebox.showinfo("Number Converter", "Sorry, there was a problem with the number you entered.")


# interface

root = Tk()
root.geometry('500x500')
root.title("Number Converter")

label_0 = Label(root, text="Base Number Converter", width=20, font=("bold", 20))
label_0.place(x=110, y=53)

label_1 = Label(root, text="Number", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_4 = Label(root, text="Start Base", width=20, font=("bold", 10))
label_4.place(x=70, y=180)

list1 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'];
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=15)
c.set('Select the start base')
droplist.place(x=240, y=180)

label_4 = Label(root, text="End Base", width=20, font=("bold", 10))
label_4.place(x=70, y=230)

list2 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'];
d = StringVar()
droplist = OptionMenu(root, d, *list2)
droplist.config(width=15)
d.set('Select the end base')
droplist.place(x=240, y=230)

Button(root, text='Submit', width=20, bg='green', fg='black', command=print_to_screen).place(x=180, y=280)

root.mainloop()
