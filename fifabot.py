from logging import root
from tkinter import *

def initView(root):
    searchLabel = Label(root, text="Search:").grid(row=0, column=0)

    backLabel = Label(root, text="Back Button:").grid(row=1, column=0)

    buyNowLabel = Label(root, text="Buy Now Button:").grid(row=2, column=0)

    minBidPlusLabel = Label(root, text="Min Bid + Button:").grid(row=3, column=0)

    minBidMinusLabel = Label(root, text="Min Bid - Button:").grid(row=4, column=0)

    minBNPlusLabel = Label(root, text="Min Buy Now + Button:").grid(row=5, column=0)

    minBNMinusLabel = Label(root, text="Min Buy Now - Button:").grid(row=6, column=0)

    submitButton = Button(root, text="Submit !")



root = Tk()

initView(root)



root.mainloop()

