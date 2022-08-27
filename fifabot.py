from cProfile import label
from logging import root
from tkinter import *

def initView(root):

    xLabel = Label(root, text="X:").grid(row=0, column=1)

    yLabel = Label(root, text="Y:").grid(row=0, column=2)

    searchLabel = Label(root, text="Search:").grid(row=1, column=0)

    xsearchLabel = Entry(root).grid(row=1, column=1)

    ysearchLabel = Entry(root).grid(row=1, column=2)

    backLabel = Label(root, text="Back Button:").grid(row=2, column=0)

    xbackLabel = Entry(root).grid(row=2, column=1)

    ybackLabel = Entry(root).grid(row=2, column=2)

    buyNowLabel = Label(root, text="Buy Now Button:").grid(row=3, column=0)

    xbuyNowLabel = Entry(root).grid(row=3, column=1)

    ybuyNowLabel = Entry(root).grid(row=3, column=2)

    minBidPlusLabel = Label(root, text="Min Bid + Button:").grid(row=4, column=0)

    xMinBidPlusLabel = Entry(root).grid(row=4, column=1)

    yMinBidPlusLabel = Entry(root).grid(row=4, column=2)

    minBidMinusLabel = Label(root, text="Min Bid - Button:").grid(row=5, column=0)

    xMinBidMinusLabel = Entry(root).grid(row=5, column=1)

    yMinBidMinusLabel = Entry(root).grid(row=5, column=2)

    minBNPlusLabel = Label(root, text="Min Buy Now + Button:").grid(row=6, column=0)

    xMinBNPLabel = Entry(root).grid(row=6, column=1)

    yMinBNPLabel = Entry(root).grid(row=6, column=2)

    minBNMinusLabel = Label(root, text="Min Buy Now - Button:").grid(row=7, column=0)

    xminBNMinusLabel = Entry(root).grid(row=7, column=1)

    yminBNMinusLabel = Entry(root).grid(row=7, column=2)

    submitButton = Button(root, text="Submit !").grid(row=8, column= 1)



root = Tk()

initView(root)



root.mainloop()

