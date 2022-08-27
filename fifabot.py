from tkinter import *
from collections import *

def initView(root):

    xLabel = Label(root, text="X:").grid(row=0, column=1)

    yLabel = Label(root, text="Y:").grid(row=0, column=2)

    searchLabel = Label(root, text="Search:").grid(row=1, column=0)

    xsearchLabel : Entry = Entry(root).grid(row=1, column=1)

    ysearchLabel : Entry  = Entry(root).grid(row=1, column=2)

    backLabel = Label(root, text="Back Button:").grid(row=2, column=0)

    xbackLabel : Entry  = Entry(root).grid(row=2, column=1)

    ybackLabel : Entry  = Entry(root).grid(row=2, column=2)

    buyNowLabel = Label(root, text="Buy Now Button:").grid(row=3, column=0)

    xbuyNowLabel : Entry  = Entry(root).grid(row=3, column=1)

    ybuyNowLabel : Entry  = Entry(root).grid(row=3, column=2)

    minBidPlusLabel = Label(root, text="Min Bid + Button:").grid(row=4, column=0)

    xMinBidPlusLabel : Entry  = Entry(root).grid(row=4, column=1)

    yMinBidPlusLabel : Entry  = Entry(root).grid(row=4, column=2)

    minBidMinusLabel = Label(root, text="Min Bid - Button:").grid(row=5, column=0)

    xMinBidMinusLabel : Entry  = Entry(root).grid(row=5, column=1)

    yMinBidMinusLabel : Entry  = Entry(root).grid(row=5, column=2)

    minBNPlusLabel = Label(root, text="Min Buy Now + Button:").grid(row=6, column=0)

    xMinBNPLabel : Entry  = Entry(root).grid(row=6, column=1)

    yMinBNPLabel : Entry  = Entry(root).grid(row=6, column=2)

    minBNMinusLabel = Label(root, text="Min Buy Now - Button:").grid(row=7, column=0)

    xminBNMinusLabel : Entry  = Entry(root).grid(row=7, column=1)

    yminBNMinusLabel : Entry  = Entry(root).grid(row=7, column=2)

    submitButton = Button(root, text="Submit !").grid(row=8, column= 1)

    coordinates = {
        "xsearchLabel" : xsearchLabel.get(),
        "ysearchLabel" : ysearchLabel.get(),
        "xbackLabel" : xbackLabel.get(),
        "ybackLabel" : ybackLabel.get(),
        "xbuyNowLabel" : xbuyNowLabel.get(),
        "ybuyNowLabel" : ybuyNowLabel.get(),
        "xMinBidPlusLabel" : xMinBidPlusLabel.get(),
        "yMinBidPlusLabel" : yMinBidPlusLabel.get(),
        "xMinBidMinusLabel" : xMinBidMinusLabel.get(),
        "yMinBidMinusLabel" : yMinBidMinusLabel.get(),
        "xMinBNPLabel" : xMinBNPLabel.get(),
        "yMinBNPLabel" : yMinBNPLabel.get(),
        "xminBNMinusLabel" : xminBNMinusLabel.get(),
        "yminBNMinusLabel" : yminBNMinusLabel.get()
    }

    return coordinates

root = Tk()

buttonCoordinates = initView(root)

print(buttonCoordinates)



root.mainloop()

