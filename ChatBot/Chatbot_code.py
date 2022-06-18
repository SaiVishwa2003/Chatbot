from tkinter import *

root = Tk()
root.title("Customer care service")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#ff0000"
TEXT_COLOR = "#ffffff"

FONT = "Helvetica 14"
FONT_BOLD = "Georgia 20 bold"

def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if user == "hello":
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help you?")

    elif user == "hi" or user == "hii" or user == "hiiii":
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help you?")

    elif user == "How to check my balance" or user == "View my balance" or user == "balance":
        txt.insert(END, "\n" + "Bot -> Give a missed call to 121, a Toll free number")

    elif user == "Contact customer care" or user == "customer care" or user == "help":
        txt.insert(END, "\n" + "Bot -> Dial - 2384728 (South)  \n Dial - 234673 (North)")

    elif user == "Thanks" or user == "Thank you" or user == "now its my time":
        txt.insert(END, "\n" + "Bot -> My pleasure !")

    elif user == "Plan" or user == "Offers":
        txt.insert(END, "\n" + "Bot -> Visit : airtel.com")

    elif user == "Goodbye" or user == "See you later" or user == "see yaa":
        txt.insert(END, "\n" + "Bot -> Have a nice day!")

    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")

    e.delete(0, END)


lables = Label(root, bg=TEXT_COLOR, fg=BG_COLOR, text="Welcome to Airtel", font=FONT_BOLD, pady=10, width=20, height=1)
lables.grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#9c9c9c", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT, bg=BG_GRAY, command=send)
send.grid(row=2, column=1)

root.mainloop()
