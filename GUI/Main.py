# Things to be done
# And if you have time add other information on text[1] like block, valance electrons
# Then finally convert this to .exe


import tkinter as tk
import Main
from PIL import ImageTk, Image
from tkinter import PhotoImage, NW
from tkinter import messagebox as msg
from tkinter import ttk, Canvas, Menu, Label, Frame, Text
from tkinter import messagebox as msg
from tkinter import FLAT, RAISED, SUNKEN, GROOVE, RIDGE
import serial
import pyttsx3
from pyttsx3.drivers import sapi5
#import customtkinter


try:
    nano = serial.Serial(port='COM4', baudrate=9800, timeout=.1)
except:
    #print("Could not open port")
    pass

#customtkinter.set_appearance_mode("Dark")

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.winfo_toplevel().title("Periodic Table")
        self.topLabel = tk.Label(self, text="Click any element", font=('Helvetica 15 bold', 15))
        self.topLabel.grid(row=0, column=0)

        # numbers for the series and the groups
        # Row numbers
        r1 = Label(self, text="1", font=7)
        r1.grid(column=1, row=3)

        r2 = Label(self, text="2", font=7)
        r2.grid(column=1, row=4)

        r3 = Label(self, text="3", font=7)
        r3.grid(column=1, row=5)

        r4 = Label(self, text="4", font=7)
        r4.grid(column=1, row=6)

        r5 = Label(self, text="5", font=7)
        r5.grid(column=1, row=7)

        r6 = Label(self, text="6", font=7)
        r6.grid(column=1, row=8)

        r7 = Label(self, text="7", font=7)
        r7.grid(column=1, row=9)
        #Column numbers
        c1 = Label(self, text="1", font=7)
        c1.grid(column=2, row=2)

        column1_1 = [
            ('H', 'Hydrogen', 'Atomic # = 1\nAtomic Weight =1.01\nState = Gas\nCategory = Alkali Metals', '1', '1.01')]
        # create all tk.Buttons with a loop
        r = 3
        c = 2
        color1="green"
        for b in column1_1: 
            self.H = tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg=color1,
                      font=10,
                      borderwidth = 3,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color1, text[0], text[3], text[4])])
            self.H.grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column1_2 = [
            ('Li', 'Lithium', 'Atomic # = 3\nAtomic Weight = 6.94\nState = Solid\nCategory = Alkali Metals', '3', '6.94'),
            ('Na', 'Sodium', 'Atomic # = 11\nAtomic Weight = 22.99\nState = Solid\nCategory = Alkali Metals', '11', '22.99'),
            ('K', 'Potassium', 'Atomic # = 19\nAtomic Weight = 39.10\nState = Solid\nCategory = Alkali Metals', '19', '39.10'),
            ('Rb', 'Rubidium', 'Atomic # = 37\nAtomic Weight = 85.47\nState = Solid\nCategory = Alkali Metals', '37', '85.41'),
            ('Cs', 'Cesium', 'Atomic # = 55\nAtomic Weight = 132.91\nState = Solid\nCategory = Alkali Metals', '55', '132.91'),
            ('Fr', 'Francium', 'Atomic # = 87\nAtomic Weight = 223.00\nState = Solid\nCategory = Alkali Metals', '87', '223')]
        # create all tk.Buttons with a loop
        r = 4
        c = 2
        color2="orange"
        self.alkali_c={}
        for b in column1_2: 
            self.alkali_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg=color2,
                      font=10,
                      borderwidth = 3,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color2, text[0], text[3], text[4])])
            self.alkali_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c2 = Label(self, text="2", font=7)
        c2.grid(column=3, row=3)
        
        column2 = [
            ('Be', 'Beryllium', 'Atomic # = 4\nAtomic Weight = 9.01\nState = Solid\nCategory = Alkaline Earth Metals', '4', '9.01'),
            ('Mg', 'Magnesium', 'Atomic # = 12\nAtomic Weight = 24.31\nState = Solid\nCategory = Alkaline Earth Metal', '12', '24.31'),
            ('Ca', 'Calcium', 'Atomic # = 20\nAtomic Weight = 40.08\nState = Solid\nCategory = Alkaline Earth Metals', '20', '40.08'),
            ('Sr', 'Strontium', 'Atomic # = 38\nAtomic Weight = 87.62\nState = Solid\nCategory = Alkaline Earth Metal', '38', '87.62'),
            ('Ba', 'Barium', 'Atomic # = 56\nAtomic Weight = 137.33\nState = Solid\nCategory = Alkaline Earth Metals', '56', '137.33'),
            ('Ra', 'Radium', 'Atomic # = 88\nAtomic Weight = 226.03\nState = Solid\nCategory = Alkaline Earth Metals', '88', '226.03')]
        r = 4
        c = 3
        self.alkaline_c={}
        color3="light goldenrod"
        for b in column2:
            self.alkaline_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color3,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color3, text[0], text[3], text[4])])
            self.alkaline_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
        #print(self.alkaline_c)
        c3 = Label(self, text="3", font=7)
        c3.grid(column=4, row=5)
        
        column3 = [
            ('Sc', 'Scandium', 'Atomic # = 21\nAtomic Weight = 44.96\nState = Solid\nCategory = Trans Metals', '21', '44.96'),
            ('Y', 'Yttrium', 'Atomic # = 39\nAtomic Weight = 88.91\nState = Solid\nCategory = Trans Metals', '39', '88.91')]
        r = 6
        c = 4
        self.trans_c3={}
        color4="yellow"
        for b in column3: 
            self.trans_c3[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color4,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color4, text[0], text[3], text[4])])
            self.trans_c3[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column3_1 = [
            ('La', 'Lanthanum', 'Atomic # = 57\nAtomic Weight = 138.91\nState = Solid\nCategory = Trans Metals', '57', '138.91')]
        r = 8
        c = 4
        self.La_c3_1={}
        color5="pink"
        for b in column3_1: 
            self.La_c3_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color5,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color5, text[0], text[3], text[4])])
            self.La_c3_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column3_2 = [
            ('Ac', 'Actinium', 'Atomic # = 89\nAtomic Weight = 227.03\nState = Solid\nCategory = Trans Metals', '89', '227.03')]
        r = 9
        c = 4
        self.Ac_c3_2={}
        color6="magenta"
        for b in column3_2: 
            self.Ac_c3_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color6,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color6, text[0], text[3], text[4])])
            self.Ac_c3_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c4 = Label(self, text="4", font=7)
        c4.grid(column=5, row=5)
        
        column4 = [
            ('Ti', 'Titanium', 'Atomic # = 22\nAtomic Weight = 47.90\nState = Solid\nCategory = Trans Metals', '22', '47.90'),
            ('Zr', 'Zirconium', 'Atomic # = 40\nAtomic Weight = 91.22\nState = Solid\nCategory = Trans Metals', '40', '91.22'),
            ('Hf', 'Hanium', 'Atomic # = 72\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals', '72', '178.49'),
            ('Rf', 'Rutherfordium', 'Atomic # = 104\nAtomic Weight = 261.00\nState = Synthetic\nCategory = Trans Metal', '104', '261.00')]
        r = 6
        c = 5
        self.trans_c4={}
        color7="yellow"
        for b in column4: 
            self.trans_c4[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c4[b[0]].grid(row=r, column=c)
            r += 1
            if r > 12: 
                r = 1
                c += 1
                
        c5 = Label(self, text="5", font=7)
        c5.grid(column=6, row=5)
        
        column5 = [
            ('V', 'Vanadium', 'Atomic # = 23\nAtomic Weight = 50.94\nState = Solid\nCategory = Trans Metals', '23', '50.94'),
            ('Nb', 'Niobium', 'Atomic # = 41\nAtomic Weight = 92.91\nState = Solid\nCategory = Trans Metals', '41', '92.91'),
            ('Ta', 'Tantalum', 'Atomic # = 73\nAtomic Weight = 180.95\nState = Solid\nCategory = Trans Metals', '73', '180.95'),
            ('Db', 'Dubnium', 'Atomic # = 105\nAtomic Weight = 268.00\nState = Synthetic\nCategory = Trans Metals', '105', '262.00')]
        r = 6
        c = 6
        self.trans_c5={}
        color8="yellow"
        for b in column5: 
            self.trans_c5[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color8,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color8, text[0], text[3], text[4])])
            self.trans_c5[b[0]].grid(row=r, column=c)
            r += 1
            if r > 12: 
                r = 1
                c += 1
                
        c6 = Label(self, text="6", font=7)
        c6.grid(column=7, row=5)
        
        column6 = [
            ('Cr', 'Chromium', 'Atomic # = 24\nAtomic Weight = 51.99\nState = Solid\nCategory = Trans Metals', '24', '51.99'),
            ('Mo', 'Molybdenum', 'Atomic # = 42\nAtomic Weight = 95.94\nState = Solid\nCategory = Trans Metals', '42', '95.94'),
            ('W', 'Tungsten', 'Atomic # = 74\nAtomic Weight = 183.85\nState = Solid\nCategory = Trans Metals', '74', '183.85'),
            ('Sg', 'Seaborgium', 'Atomic # = 106\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Trans Metals', '106', '266.00')]
        r = 6
        c = 7
        self.trans_c6={}
        color9="yellow"
        for b in column6: 
            self.trans_c6[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color9,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color9, text[0], text[3], text[4])])
            self.trans_c6[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c7 = Label(self, text="7", font=7)
        c7.grid(column=8, row=5)
        
        column7 = [
            ('Mn', 'Manganese', 'Atomic # = 25\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals', '25', '178.49'),
            ('Tc', 'Technetium', 'Atomic # = 43\nAtomic Weight = 178.49\nState = Synthetic\nCategory = Trans Metals', '43', '178.49'),
            ('Re', 'Rhenium', 'Atomic # = 75\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals', '75', '178.49'),
            ('Bh', 'Bohrium', 'Atomic # = 107\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Trans Metals', '107', '262.00')]
        r = 6
        c = 8
        self.trans_c7={}
        for b in column7: 
            self.trans_c7[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color9,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color9, text[0], text[3], text[4])])
            self.trans_c7[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        c8 = Label(self, text="8", font=7)
        c8.grid(column=9, row=5)
        
        column8 = [
            ('Fe', 'Iron', 'Atomic # = 26\nAtomic Weight = 55.85\nState = Solid\nCategory = Trans Metals', '26', '55.85'),
            ('Ru', 'Ruthenium', 'Atomic # = 44\nAtomic Weight = 101.07\nState = Solid\nCategory = Trans Metals', '44', '101.07'),
            ('Os', 'Osmium', 'Atomic # = 76\nAtomic Weight = 190.20\nState = Solid\nCategory = Trans Metals', '76', '190.20'),
            ('Hs', 'Hassium', 'Atomic # = 108\nAtomic Weight = 265.00\nState = Synthetic\nCategory = Trans Metals', '108', '265.00')]
        r = 6
        c = 9
        self.trans_c8={}
        for b in column8: 
            self.trans_c8[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color9,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color9, text[0], text[3], text[4])])
            self.trans_c8[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c9 = Label(self, text="9", font=7)
        c9.grid(column=10, row=5)
        
        column9 = [
            ('Co', 'Cobalt', 'Atomic # = 27\nAtomic Weight = 58.93\nState = Solid\nCategory = Trans Metals', '27', '58.93'),
            ('Rh', 'Rhodium', 'Atomic # = 45\nAtomic Weight = 102.91\nState = Solid\nCategory = Trans Metals', '45', '102.91'),
            ('Ir', 'Iridium', 'Atomic # = 77\nAtomic Weight = 192.22\nState = Solid\nCategory = Trans Metals', '77', '192.22')]
        r = 6
        c = 10
        self.trans_c9={}
        for b in column9: 
            self.trans_c9[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color9,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color9, text[0], text[3], text[4])])
            self.trans_c9[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column9_0 = [
            ('Mt', 'Meitnerium', 'Atomic # = 109\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Trans Metals', '109', '266.00')]
        r = 9
        c = 10
        colorUnk="white"
        self.trans_c9_0={}
        for b in column9_0: 
            self.trans_c9_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c9_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
        
        c10 = Label(self, text="10", font=7)
        c10.grid(column=11, row=5)
        
        column10 = [
            ('Ni', 'Nickle', 'Atomic # = 28\nAtomic Weight = 58.70\nState = Solid\nCategory = Trans Metals', '28', '58.70'),
            ('Pd', 'Palladium', 'Atomic # = 46\nAtomic Weight = 106.40\nState = Solid\nCategory = Trans Metals', '46', '106.40'),
            ('Pt', 'Platinum', 'Atomic # = 78\nAtomic Weight = 195.09\nState = Solid\nCategory = Trans Metals', '78', '195.09')]
        r = 6
        c = 11
        self.trans_c10={}
        for b in column10: 
            self.trans_c10[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color9,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color9, text[0], text[3], text[4])])
            self.trans_c10[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column10_0 = [
            ('Ds', 'Darmstadtium', 'Atomic # = 110\nAtomic Weight = 281\nState = Unknown\nCatagory = Trans Metals', '110', '281')]
        r = 9
        c = 11
        self.trans_c10_0={}
        for b in column10_0: 
            self.trans_c10_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c10_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        
        c11 = Label(self, text="11", font=7)
        c11.grid(column=12, row=5)
        
        column11 = [
            ('Cu', 'Copper', 'Atomic # = 29\nAtomic Weight = 63.55\nState = Solid\nCategory = Trans Metals', '29', '63.55'),
            ('Ag', 'Silver', 'Atomic # = 47\nAtomic Weight = 107.97\nState = Solid\nCategory = Trans Metals', '47', '107.97'),
            ('Au', 'Gold', 'Atomic # = 79\nAtomic Weight = 196.97\nState = Solid\nCategory = Trans Metals', '79', '196.97')]
        r = 6
        c = 12
        self.trans_c11={}
        for b in column11: 
            self.trans_c11[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color9,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color9, text[0], text[3], text[4])])
            self.trans_c11[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                c11 = Label(self, text="11", font=7)
        c11.grid(column=12, row=5)
        
        column11_0 = [
            ('Rg', 'Roentgenium', 'Atomic # = 111\nAtomic Weight = 282\nState = Unkown\nCategory = Trans Metals', '111', '282')]
        r = 9
        c = 12
        self.trans_c11_0={}
        for b in column11_0: 
            self.trans_c11_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c11_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

             
        c12 = Label(self, text="12", font=7)
        c12.grid(column=13, row=5)
        
        column12 = [
            ('Zn', 'Zinc', 'Atomic # = 30\nAtomic Weight = 65.37\nState = Solid\nCategory = Trans Metals', '30', '65.37'),
            ('Cd', 'Cadmium', 'Atomic # = 48\nAtomic Weight = 112.41\nState = Solid\nCategory = Trans Metals', '48', '112.41'),
            ('Hg', 'Mercury', 'Atomic # = 80\nAtomic Weight = 200.59\nState = Liquid\nCategory = Trans Metals', '80', '200.59')]
        r = 6
        c = 13
        self.trans_c12={}
        for b in column12: 
            self.trans_c12[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color9,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color9, text[0], text[3], text[4])])
            self.trans_c12[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                c12 = Label(self, text="12", font=7)
        c12.grid(column=13, row=5)
        
        column12_0 = [
            ('Cn', 'Copernicium', 'Atomic # = 112\nAtomic Weight = 285\nState = Unkown\nCategory = Trans Metals', '112', '285')]
        r = 9
        c = 13
        self.trans_c12_0={}
        for b in column12_0: 
            self.trans_c12_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c12_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c13 = Label(self, text="13", font=7)
        c13.grid(column=14, row=3)
        
        column13_1 = [
            ('B', 'Boron', 'Atomic # = 5\nAtomic Weight = 10.81\nState = Solid\nCategory = Nonmetals', '5', '10.81')]
        r = 4
        c = 14
        color10="indian red"
        self.metalloids_c12_1={}
        for b in column13_1: 
            self.metalloids_c12_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloids_c12_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column13_2 = [
            ('Al', 'Aluminum', 'Atomic # = 13\nAtomic Weight = 26.98\nState = Solid\nCategory = Other Metals', '13', '26.98'),
            ('Ga', 'Gallium', 'Atomic # = 31\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals', '31', '69.72'),
            ('In', 'Indium', 'Atomic # = 49\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals', '49', '69.72'),
            ('Ti', 'Thallium', 'Atomic # = 81\nAtomic Weight = 204.37\nState = Solid\nCategory = Other Metals', '81', '204.37')]
        r = 5
        c = 14
        color11="Light gray"
        self.othermetal_c13_2={}
        for b in column13_2: 
            self.othermetal_c13_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c13_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
        
        column13_2_0 = [
            ('Nh', 'Nihonium', 'Atomic # = 113\nAtomic Weight = 286\nState = Unkown\nCategory = ', '113', '286')]
        r = 9
        c = 14
        self.othermetal_c13_2_0={}
        for b in column13_2_0: 
            self.othermetal_c13_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c13_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c14 = Label(self, text="14", font=7)
        c14.grid(column=15, row=3)
        
        column14_0 = [
            ('C', 'Carbon', 'Atomic # = 6\nAtomic Weight = 12.01\nState = Solid\nCategory = Nonmetals', '6', '12.01')]
        r = 4
        c = 15
        self.othernon_c14_0={}
        for b in column14_0: 
            self.othernon_c14_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color1,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color1, text[0], text[3], text[4])])
            self.othernon_c14_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column14_1 = [
            ('Si', 'Silicon', 'Atomic # = 14\nAtomic Weight = 28.09\nState = Solid\nCategory = Nonmetals', '14', '28.09'),
            ('Ge', 'Germanium', 'Atomic # = 32\nAtomic Weight = 72.59\nState = Solid\nCategory = Other Metals', '32', '72.59'),]
        r = 5
        c = 15
        self.metalloid_c14_1={}
        for b in column14_1: 
            self.metalloid_c14_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloid_c14_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column14_2 = [
            ('Sn', 'Tin', 'Atomic # = 50\nAtomic Weight = 118.69\nState = Solid\nCategory = Other Metals', '50', '118.69'),
            ('Pb', 'Lead', 'Atomic # = 82\nAtomic Weight = 207.20\nState = Solid\nCategory = Other Metals', '82', '207.20')]
        r = 7
        c = 15
        self.othermetal_c14_2={}
        for b in column14_2: 
            self.othermetal_c14_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c14_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column14_2_0 = [
            ('Fl', 'Flerovium', 'Atomic # = 114\nAtomic Weight = 289\nState = Unkown\nCategory = ', '114', '289')]
        r = 9
        c = 15
        self.othermetal_c14_2_0={}
        for b in column14_2_0: 
            self.othermetal_c14_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c14_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                
        c15 = Label(self, text="15", font=7)
        c15.grid(column=16, row=3)
        
        column15_0 = [
            ('N', 'Nitrogen', 'Atomic # = 7\nAtomic Weight = 14.01\nState = Gas\nCategory = Nonmetals', '7', '14.01'),
            ('P', 'Phosphorus', 'Atomic # = 15\nAtomic Weight = 30.97\nState = Solid\nCategory = Nonmetals', '15', '30.97')]
        r = 4
        c = 16
        self.othernon_c15_0={}
        for b in column15_0: 
            self.othernon_c15_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color1,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color1, text[0], text[3], text[4])])
            self.othernon_c15_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column15_1 = [
            ('As', 'Arsenic', 'Atomic # = 33\nAtomic Weight = 74.92\nState = Solid\nCategory = Nonmetals', '33', '74.92'),
            ('Sb', 'Antimony', 'Atomic # = 51\nAtomic Weight = 121.75\nState = Solid\nCategory = Other Metals', '51', '121.75')]
        r = 6
        c = 16
        self.metalloids_c15_1={}
        for b in column15_1: 
            self.metalloids_c15_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloids_c15_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column15_2 = [    
            ('Bi', 'Bismuth', 'Atomic # = 83\nAtomic Weight = 208.98\nState = Solid\nCategory = Other Metals', '83', '208.98')]
        r = 8
        c = 16
        self.othermetal_c15_2={}
        for b in column15_2: 
            self.othermetal_c15_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c15_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column15_2_0 = [    
            ('Mc', 'Moscovium', 'Atomic # = 115\nAtomic Weight = 290\nState = Unkown\nCategory = ', '115', '290')]
        r = 9
        c = 16
        self.othermetal_c15_2_0={}
        for b in column15_2_0: 
            self.othermetal_c15_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c15_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                
        c16 = Label(self, text="16", font=7)
        c16.grid(column=17, row=3)
        
        column16_0 = [
            ('O', 'Oxygen', 'Atomic # = 8\nAtomic Weight = 15.99\nState = Gas\nCategory = Nonmetals', '8', '15.99'),
            ('S', 'Sulfur', 'Atomic # = 16\nAtomic Weight = 32.06\nState = Solid\nCategory = Nonmetals', '16', '32.06'),
            ('Se', 'Selenium', 'Atomic # = 34\nAtomic Weight = 78.96\nState = Solid\nCategory = Nonmetals', '34', '78.96')]
        r = 4
        c = 17
        self.othernon_c16_0={}
        for b in column16_0: 
            self.othernon_c16_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color1,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color1, text[0], text[3], text[4])])
            self.othernon_c16_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column16_1 = [
            ('Te', 'Tellurium', 'Atomic # = 52\nAtomic Weight = 127.60\nState = Solid\nCategory = Nonmetals', '52', '127.60')]
        r = 7
        c = 17
        self.metalloid_c16_1={}
        for b in column16_1: 
            self.metalloid_c16_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloid_c16_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column16_2 = [
            ('Po', 'Polonium', 'Atomic # = 84\nAtomic Weight = 209.00\nState = Solid\nCategory = Other Metals', '84', '209.00')]
        r = 8
        c = 17
        self.othermetal_c16_2={}
        for b in column16_2: 
            self.othermetal_c16_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c16_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column16_2_0 = [
            ('Lv', 'Livermorium', 'Atomic # = 116\nAtomic Weight = 293\nState = Unkown\nCategory = ', '116', '293.00')]
        r = 9
        c = 17
        self.othermetal_c16_2_0={}
        for b in column16_2_0: 
            self.othermetal_c16_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c16_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c17 = Label(self, text="17", font=7)
        c17.grid(column=18, row=3)
        
        column17 = [
            ('F', 'Fluorine', 'Atomic # = 9\nAtomic Weight = 18.99\nState = Gas\nCategory = Halogens', '9', '18.99'),
            ('Cl', 'Chlorine', 'Atomic # = 17\nAtomic Weight = 35.45\nState = Gas\nCategory = Halogens', '17', '35.45'),
            ('Br', 'Bromine', 'Atomic # = 35\nAtomic Weight = 79.90\nState = Liquid\nCategory = Halogens', '35', '79.90'),
            ('I', 'Iodine', 'Atomic # = 53\nAtomic Weight = 126.90\nState = Solid\nCategory = Halogens', '53', '126.90')]
        r = 4
        c = 18
        self.halogen_c={}
        color20="Navy blue"
        for b in column17: 
            self.halogen_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color20,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color20, text[0], text[3], text[4])])
            self.halogen_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column17_1 = [
            ('At', 'Astatine', 'Atomic # = 85\nAtomic Weight = 210.00\nState = Solid\nCategory = Halogens', '85', '210.00')]
        r = 8
        c = 18
        self.halogen_c_1={}
        color20="Navy blue"
        for b in column17_1: 
            self.halogen_c_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color20,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color20, text[0], text[3], text[4])])
            self.halogen_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column17_0 = [
            ('Ts', 'Tennessine', 'Atomic # = 117\nAtomic Weight = 294.00\nState = Unkown\nCategory = Halogens', '117', '294.00')]
        r = 9
        c = 18
        self.halogen_c_0={}
        for b in column17_0: 
            self.halogen_c_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.halogen_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c18 = Label(self, text="18", font=7)
        c18.grid(column=19, row=2)
        
        column18 = [
            ('He', 'Helium', 'Atomic # = 2\nAtomic Weight = 4.00\nState = Gas\nCategory = Nobel Gases', '2', '4.00'),
            ('Ne', 'Neon', 'Atomic # = 10\nAtomic Weight = 20.18\nState = Gas\nCategory = Nobel Gases', '10', '20.18'),
            ('Ar', 'Argon', 'Atomic # = 18\nAtomic Weight = 39.95\nState = Gas\nCategory = Nobel Gases', '18', '39.95'),
            ('Kr', 'Krypton', 'Atomic # = 36\nAtomic Weight = 83.80\nState = Gas\nCategory = Nobel Gases', '36', '83.80'),
            ('Xe', 'Xenon', 'Atomic # = 54\nAtomic Weight = 131.30\nState = Gas\nCategory = Nobel Gases', '54', '131.30'),
            ('Rn', 'Radon', 'Atomic # = 86\nAtomic Weight = 222.00\nState = Gas\nCategory = Nobel Gases', '86', '222.00')]
        r = 3
        c = 19
        self.nobel_c={}
        color21="cyan"
        for b in column18: 
            self.nobel_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color21,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color21, text[0], text[3], text[4])])
            self.nobel_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column18_0 = [
            ('Og', 'Oganesson', 'Atomic # = 118\nAtomic Weight = 294.00\nState = Unkown\nCategory = Nobel Gases', '118', '294.00')]
        r = 9
        c = 19
        self.nobel_c_0={}
        for b in column18_0: 
            self.nobel_c_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.nobel_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        self.fillerLine = tk.Label(self, text="")
        self.fillerLine.grid(row=12, column=0)

        lanthanide = [
            ('Ce', 'Cerium', 'Atomic # = 58\nAtomic Weight = 140.12\nState = Solid\nCategory = Trans Metals', '58', '140.12'),
            ('Pr', 'Praseodymium', 'Atomic # = 59\nAtomic Weight = 140.91\nState = Solid\nCategory = Trans Metals', '59', '140.91'),
            ('Nd', 'Neodymium', 'Atomic # = 60\nAtomic Weight = 144.24\nState = Solid\nCategory = Trans Metals', '60', '144.24'),
            ('Pm', 'Promethium', 'Atomic # = 61\nAtomic Weight = 145.00\nState = Synthetic\nCategory = Trans Metals', '61', '145.00'),
            ('Sm', 'Samarium', 'Atomic # = 62\nAtomic Weight = 150.40\nState = Solid\nCategory = Trans Metals', '62', '150.40'),
            ('Eu', 'Europium', 'Atomic # = 63\nAtomic Weight = 151.96\nState = Solid\nCategory = Trans Metals', '63', '151.96'),
            ('Gd', 'Gadolinium', 'Atomic # = 64\nAtomic Weight = 157.25\nState = Solid\nCategory = Trans Metals', '64', '157.25'),
            ('Tb', 'Terbium', 'Atomic # = 65\nAtomic Weight = 158.93\nState = Solid\nCategory = Trans Metals', '65', '158.93'),
            ('Dy', 'Dyprosium', 'Atomic # = 66\nAtomic Weight = 162.50\nState = Solid\nCategory = Trans Metals', '66', '162.50'),
            ('Ho', 'Holmium', 'Atomic # = 67\nAtomic Weight = 164.93\nState = Solid\nCategory = Trans Metals', '67', '164.93'),
            ('Er', 'Erbium', 'Atomic # = 68\nAtomic Weight = 167.26\nState = Solid\nCategory = Trans Metals', '68', '167.26'),
            ('Tm', 'Thulium', 'Atomic # = 69\nAtomic Weight = 168.93\nState = Solid\nCategory = Trans Metals', '69', '168.93'),
            ('Yb', 'Ytterbium', 'Atomic # = 70\nAtomic Weight = 173.04\nState = Solid\nCategory = Trans Metals', '70', '173.04'),
            ('Lu', 'Lutetium', 'Atomic # = 71\nAtomic Weight = 174.97\nState = Solid\nCategory = Trans Metals', '71', '174.97')]
        r = 13
        c = 5
        self.La_CA={}
        for b in lanthanide: 
            self.La_CA[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color5,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color5, text[0], text[3], text[4])])
            self.La_CA[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        actinide = [
            ('Th', 'Thorium', 'Atomic # = 90\nAtomic Weight = 232.04\nState = Solid\nCategory = Trans Metals', '90', '232.04'),
            ('Pa', 'Protactinium', 'Atomic # = 91\nAtomic Weight = 231.04\nState = Solid\nCategory = Trans Metals', '91', '231.04'),
            ('U', 'Uranium', 'Atomic # = 92\nAtomic Weight = 238.03\nState = Solid\nCategory = Trans Metals', '92', '238.03'),
            ('Np', 'Neptunium', 'Atomic # = 93\nAtomic Weight = 237.05\nState = Synthetic\nCategory = Trans Metals', '93', '237.05'),
            ('Pu', 'Plutonium', 'Atomic # = 94\nAtomic Weight = 244.00\nState = Synthetic\nCategory = Trans Metals', '94', '244.00'),
            ('Am', 'Americium', 'Atomic # = 95\nAtomic Weight = 243.00\nState = Synthetic\nCategory = Trans Metals', '95', '243.00'),
            ('Cm', 'Curium', 'Atomic # = 96\nAtomic Weight = 247.00\nState = Synthetic\nCategory = Trans Metals', '96', '247.00'),
            ('Bk', 'Berkelium', 'Atomic # = 97\nAtomic Weight = 247.00\nState = Synthetic\nCategory = Trans Metals', '97', '247.00'),
            ('Cf', 'Californium', 'Atomic # = 98\nAtomic Weight = 247.00\nState = Synthetic\nCategory = Trans Metals', '98', '247.00'),
            ('Es', 'Einsteinium', 'Atomic # = 99\nAtomic Weight = 252.00\nState = Synthetic\nCategory = Trans Metals', '99', '252.00'),
            ('Fm', 'Fermium', 'Atomic # = 100\nAtomic Weight = 257.00\nState = Synthetic\nCategory = Trans Metals', '100', '257.00'),
            ('Md', 'Mendelevium', 'Atomic # = 101\nAtomic Weight = 260.00\nState = Synthetic\nCategory = Trans Metals', '101', '260.00'),
            ('No', 'Nobelium', 'Atomic # = 102\nAtomic Weight = 259.00\nState = Synthetic\nCategory = Trans Metals', '102', '259.00'),
            ('Lr', 'Lawrencium', 'Atomic # = 103\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Trans Metals', '103', '262.00')]
        r = 14
        c = 5
        self.Ac_CA={}
        for b in actinide:
            self.Ac_CA[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=color6,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(color6, text[0], text[3], text[4])])
            self.Ac_CA[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        clear = [
            ('Clear', 'Click any element', 'clear')]
        r = 14
        c = 2
        for b in clear: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="black",
                      fg="white",
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[2])]).grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
        """=============================Groups======================================="""

        Alkali_metals = [('Alkali Metals', 'Alkali Metal elements', 'Alkali')]
        r = 1
        c = 4
        for b in Alkali_metals:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color2,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Alkali_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Alkaline_Earth_metals = [('Alkaline Earth Metals', 'Alkaline Earth Metal elements', 'AlkaliEart')]
        r = 1
        c = 6
        for b in Alkaline_Earth_metals:
            tk.Button(self,
                      text=b[0],
                      width=18,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color3,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Alkaline_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=3, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Transition_metals = [('Transition Metals', 'Transition Metal elements', 'Transition')]
        r = 1
        c = 9
        for b in Transition_metals:
            tk.Button(self,
                      text=b[0],
                      width=18,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color7,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Transition_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=3, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        Other_Non_Metals = [('Other Nonmetals', 'Other Nonmetal elements', 'OtherNon')]
        r = 1
        c = 12
        for b in Other_Non_Metals:
            tk.Button(self,
                      text=b[0],
                      width=18,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color1,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.OtherNon_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=3, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        Nobel_gas = [('Nobel Gas', 'Nobel Gas elements', 'NobleGas')]
        r = 1
        c = 15
        for b in Nobel_gas:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color21,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Nobel_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1


        Lanthanides = [('Lanthanides', 'Lanthanide elements', 'Lanthanoid')]
        r = 2
        c = 4
        for b in Lanthanides:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color5,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Lanthanides_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        Actinides = [('Actinides', 'Actinides elements', 'Actinod')]
        r = 2
        c = 6
        for b in Actinides:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color6,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Actinides_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Other_Metals = [('Other Metals', 'Other metal elements', 'OtherMetal')]
        r = 2
        c = 8
        for b in Other_Metals:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color11,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.OtherMetal_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        Metalloids = [('Metalloids', 'Metalloid elements', 'Metalloid')]
        r = 2
        c = 10
        for b in Metalloids:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color10,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Metalloids_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        

        Halogens = [('Halogens', 'Halogen elements', 'Halogen')]
        r = 2
        c = 12
        for b in Halogens:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg=color20,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Halogen_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        All_Metals = [('All Metals', 'All Metal elements', 'AllMetal')]
        r = 3
        c = 6
        colorAme="Teal"
        for b in All_Metals:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorAme,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.AllMetal_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        All_Non_Metals = [('All Nonmetals', 'All Nonmetal elements', 'AllNon')]
        r = 3
        c = 8
        colorAno="Aquamarine"
        for b in All_Non_Metals:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorAno,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.AllNon_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        Radioactive = [('Radioactive', 'Radioactive elements', 'Radioactive')]
        r = 3
        c = 10
        colorRa="Purple"
        for b in Radioactive:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorRa,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.Radioactive_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        """=========================================State========================================="""
        
        All = [('All', 'All elements')]
        r = 0
        c = 5
        colorA="white"
        for b in All:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorA,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[0]), self.all_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Solid = [('Solid', 'Solid elements')]
        r = 0
        c = 7
        colorS="black"
        colorFg="white"
        for b in Solid:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorS,
                      fg=colorFg,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[0]), self.solid_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Liquid = [('Liquid', 'Liquid elements')]
        r = 0
        c = 9
        colorL="Blue"
        for b in Liquid:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorL,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[0]), self.liquid_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Gas = [('Gas', 'Gas elements')]
        r = 0
        c = 11
        colorG="Red"
        for b in Gas:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorG,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[0]), self.gas_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Unknown = [('Unknown', 'Unknown elements')]
        r = 0
        c = 13
        colorU="gray"
        for b in Unknown:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorU,
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[0]), self.unknown_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        
        #setting up the canvas big elements image
        self.canvas = Canvas(self, height=100, width=100, bg="green", relief=GROOVE, borderwidth=0.5)
        #canvas.pack()
        self.canvas.create_rectangle(100, 100, 0, 0)
        self.canvas.grid(row=1, column=0, rowspan=2)
        self.sy = self.canvas.create_text(50, 50, text="H", fill="black", font=('Helvetica 15 bold', 35))
        self.an = self.canvas.create_text(10, 12, text="1", fill="black", font=('Helvetica 15 bold', 10))
        self.am = self.canvas.create_text(17, 90, text="1.001", fill="black", font=('Helvetica 15 bold', 8))
        self.infoLine = tk.Label(self, text="", justify='left', font=10)
        self.infoLine.grid(row=3, column=0, rowspan=2)
        #setting up voice
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)
        
        

        #self.mainloop() #Comment or remove it


    # Replaces Label at the top with the name of whichever element tk.Button was pressed
    def name(self, text): 
        self.topLabel.config(text=text)
        return(text)

    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, text): 
        self.infoLine.config(text=text)
        return(text)

    def canva(self, color, symbol, An, Am):
        self.canvas.config(bg=color)
        self.canvas.itemconfig(self.sy, text=symbol)
        self.canvas.itemconfig(self.an, text=An)
        self.canvas.itemconfig(self.am, text=Am)

    def all_f(self):
        # all elements correct color
        coloAlk = "orange"
        coloFg="black"
        for key in self.alkali_c:
            self.alkali_c[key].config(bg=coloAlk, fg=coloFg)

        coloAE = "light goldenrod"
        for key in self.alkaline_c:
            self.alkaline_c[key].config(bg=coloAE, fg=coloFg)
        
        coloTr = "yellow"
        for key in self.trans_c3:
            self.trans_c3[key].config(bg=coloTr, fg=coloFg)
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloTr, fg=coloFg)
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c4:
            self.trans_c4[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c5:
            self.trans_c5[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c6:
            self.trans_c6[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c7:
            self.trans_c7[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c8:
            self.trans_c8[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c9:
            self.trans_c9[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c10:
            self.trans_c10[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c11:
            self.trans_c11[key].config(bg=coloTr, fg=coloFg)
        for key in self.trans_c12:
            self.trans_c12[key].config(bg=coloTr, fg=coloFg)
        
        coloNoN = "green"
        self.H.config(bg=coloNoN)
        for key in self.othernon_c14_0:
            self.othernon_c14_0[key].config(bg=coloNoN, fg=coloFg)
        for key in self.othernon_c15_0:
            self.othernon_c15_0[key].config(bg=coloNoN, fg=coloFg)
        for key in self.othernon_c16_0:
            self.othernon_c16_0[key].config(bg=coloNoN, fg=coloFg)
            
        coloNo = "cyan"
        for key in self.nobel_c:
            self.nobel_c[key].config(bg=coloNo, fg=coloFg)


        coloLa = "pink"
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloLa, fg=coloFg)
        for key in self.La_CA:
            self.La_CA[key].config(bg=coloLa, fg=coloFg)

        coloAc = "magenta"
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloAc, fg=coloFg)
        for key in self.Ac_CA:
            self.Ac_CA[key].config(bg=coloAc, fg=coloFg)

        coloOth = "Light gray"
        for key in self.othermetal_c13_2:
            self.othermetal_c13_2[key].config(bg=coloOth, fg=coloFg)
        for key in self.othermetal_c14_2:
            self.othermetal_c14_2[key].config(bg=coloOth, fg=coloFg)
        for key in self.othermetal_c15_2:
            self.othermetal_c15_2[key].config(bg=coloOth, fg=coloFg)
        for key in self.othermetal_c16_2:
            self.othermetal_c16_2[key].config(bg=coloOth, fg=coloFg)

        colometa = "indian red"
        for key in self.metalloids_c12_1:
            self.metalloids_c12_1[key].config(bg=colometa, fg=coloFg)
        for key in self.metalloid_c14_1:
            self.metalloid_c14_1[key].config(bg=colometa, fg=coloFg)
        for key in self.metalloids_c15_1:
            self.metalloids_c15_1[key].config(bg=colometa, fg=coloFg)
        for key in self.metalloid_c16_1:
            self.metalloid_c16_1[key].config(bg=colometa, fg=coloFg)

        coloha="Navy blue"
        for key in self.halogen_c:
            self.halogen_c[key].config(bg=coloha, fg=coloFg)
        for key in self.halogen_c_1:
            self.halogen_c_1[key].config(bg=coloha, fg=coloFg)

    def white_f(self):
        # to make everything white
        coloId="white"
        coloFg="black"
        self.H.config(bg=coloId)
        for key in self.alkaline_c:
            self.alkaline_c[key].config(bg=coloId, fg=coloFg)
        for key in self.alkali_c:
            self.alkali_c[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c3:
            self.trans_c3[key].config(bg=coloId, fg=coloFg)
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloId, fg=coloFg)
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c4:
            self.trans_c4[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c5:
            self.trans_c5[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c6:
            self.trans_c6[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c7:
            self.trans_c7[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c8:
            self.trans_c8[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c9:
            self.trans_c9[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c10:
            self.trans_c10[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c11:
            self.trans_c11[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c12:
            self.trans_c12[key].config(bg=coloId, fg=coloFg)
        for key in self.metalloids_c12_1:
            self.metalloids_c12_1[key].config(bg=coloId, fg=coloFg)
        for key in self.othermetal_c13_2:
            self.othermetal_c13_2[key].config(bg=coloId, fg=coloFg)
        for key in self.othernon_c14_0:
            self.othernon_c14_0[key].config(bg=coloId, fg=coloFg)
        for key in self.metalloid_c14_1:
            self.metalloid_c14_1[key].config(bg=coloId, fg=coloFg)
        for key in self.othermetal_c14_2:
            self.othermetal_c14_2[key].config(bg=coloId, fg=coloFg)
        for key in self.othernon_c15_0:
            self.othernon_c15_0[key].config(bg=coloId, fg=coloFg)
        for key in self.metalloids_c15_1:
            self.metalloids_c15_1[key].config(bg=coloId, fg=coloFg)
        for key in self.othermetal_c15_2:
            self.othermetal_c15_2[key].config(bg=coloId, fg=coloFg)
        for key in self.othernon_c16_0:
            self.othernon_c16_0[key].config(bg=coloId, fg=coloFg)
        for key in self.metalloid_c16_1:
            self.metalloid_c16_1[key].config(bg=coloId, fg=coloFg)
        for key in self.othermetal_c16_2:
            self.othermetal_c16_2[key].config(bg=coloId, fg=coloFg)
        for key in self.halogen_c:
            self.halogen_c[key].config(bg=coloId, fg=coloFg)
        for key in self.halogen_c_1:
            self.halogen_c_1[key].config(bg=coloId, fg=coloFg)
        for key in self.nobel_c:
            self.nobel_c[key].config(bg=coloId, fg=coloFg)
        for key in self.La_CA:
            self.La_CA[key].config(bg=coloId, fg=coloFg)
        for key in self.Ac_CA:
            self.Ac_CA[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c9_0:
            self.trans_c9_0[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c10_0:
            self.trans_c10_0[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c11_0:
            self.trans_c11_0[key].config(bg=coloId, fg=coloFg)
        for key in self.trans_c12_0:
            self.trans_c12_0[key].config(bg=coloId, fg=coloFg)
        for key in self.othermetal_c13_2_0:
            self.othermetal_c13_2_0[key].config(bg=coloId, fg=coloFg)
        for key in self.othermetal_c14_2_0:
            self.othermetal_c14_2_0[key].config(bg=coloId, fg=coloFg) 
        for key in self.othermetal_c15_2_0:
            self.othermetal_c15_2_0[key].config(bg=coloId, fg=coloFg)
        for key in self.othermetal_c16_2_0:
            self.othermetal_c16_2_0[key].config(bg=coloId, fg=coloFg)
        for key in self.halogen_c_0:
            self.halogen_c_0[key].config(bg=coloId, fg=coloFg)
        for key in self.nobel_c_0:
            self.nobel_c_0[key].config(bg=coloId, fg=coloFg)

    # Alkali
    def Alkali_f(self):
        # define each color for the touched groups also
        coloFu = "orange"
        self.white_f()
        for key in self.alkali_c:
            self.alkali_c[key].config(bg=coloFu)
        pass
    # Alkaline Earth
    def Alkaline_f(self):
        coloFu = "light goldenrod"
        self.white_f()
        for key in self.alkaline_c:
            self.alkaline_c[key].config(bg=coloFu)
    # Transition
    def Transition_f(self):
        coloFu = "yellow"
        self.white_f()
        for key in self.trans_c3:
            self.trans_c3[key].config(bg=coloFu)
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloFu)
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloFu)
        for key in self.trans_c4:
            self.trans_c4[key].config(bg=coloFu)
        for key in self.trans_c5:
            self.trans_c5[key].config(bg=coloFu)
        for key in self.trans_c6:
            self.trans_c6[key].config(bg=coloFu)
        for key in self.trans_c7:
            self.trans_c7[key].config(bg=coloFu)
        for key in self.trans_c8:
            self.trans_c8[key].config(bg=coloFu)
        for key in self.trans_c9:
            self.trans_c9[key].config(bg=coloFu)
        for key in self.trans_c10:
            self.trans_c10[key].config(bg=coloFu)
        for key in self.trans_c11:
            self.trans_c11[key].config(bg=coloFu)
        for key in self.trans_c12:
            self.trans_c12[key].config(bg=coloFu)
    # Other Nonmetal
    def OtherNon_f(self):
        coloFu = "green"
        self.white_f()
        self.H.config(bg=coloFu)
        for key in self.othernon_c14_0:
            self.othernon_c14_0[key].config(bg=coloFu)
        for key in self.othernon_c15_0:
            self.othernon_c15_0[key].config(bg=coloFu)
        for key in self.othernon_c16_0:
            self.othernon_c16_0[key].config(bg=coloFu)
        
    # Nobel
    def Nobel_f(self):
        coloFu = "cyan"
        self.white_f()
        for key in self.nobel_c:
            self.nobel_c[key].config(bg=coloFu)
    # Lanthanides
    def Lanthanides_f(self):
        coloFu = "pink"
        self.white_f()
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloFu)
        for key in self.La_CA:
            self.La_CA[key].config(bg=coloFu)
            
    # Actinides
    def Actinides_f(self):
        coloFu = "magenta"
        self.white_f()
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloFu)
        for key in self.Ac_CA:
            self.Ac_CA[key].config(bg=coloFu)
    # Other Metal
    def OtherMetal_f(self):
        coloFu = "Light gray"
        self.white_f()
        for key in self.othermetal_c13_2:
            self.othermetal_c13_2[key].config(bg=coloFu)
        for key in self.othermetal_c14_2:
            self.othermetal_c14_2[key].config(bg=coloFu)
        for key in self.othermetal_c15_2:
            self.othermetal_c15_2[key].config(bg=coloFu)
        for key in self.othermetal_c16_2:
            self.othermetal_c16_2[key].config(bg=coloFu)
        
    # Metalloids
    def Metalloids_f(self):
        coloFu="indian red"
        self.white_f()
        for key in self.metalloids_c12_1:
            self.metalloids_c12_1[key].config(bg=coloFu)
        for key in self.metalloid_c14_1:
            self.metalloid_c14_1[key].config(bg=coloFu)
        for key in self.metalloids_c15_1:
            self.metalloids_c15_1[key].config(bg=coloFu)
        for key in self.metalloid_c16_1:
            self.metalloid_c16_1[key].config(bg=coloFu)
        for key in self.halogen_c_1:
            self.halogen_c_1[key].config(bg=coloFu)
        
    # Halogen
    def Halogen_f(self):
        coloFu="Navy blue"
        self.white_f()
        for key in self.halogen_c:
            self.halogen_c[key].config(bg=coloFu)
        for key in self.halogen_c_1:
            self.halogen_c_1[key].config(bg=coloFu)
            
    # All metals
    def AllMetal_f(self):
        coloFu = "Teal"
        self.white_f()
        for key in self.alkali_c:
            self.alkali_c[key].config(bg=coloFu)
        for key in self.alkaline_c:
            self.alkaline_c[key].config(bg=coloFu)
        for key in self.trans_c3:
            self.trans_c3[key].config(bg=coloFu)
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloFu)
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloFu)
        for key in self.trans_c4:
            self.trans_c4[key].config(bg=coloFu)
        for key in self.trans_c5:
            self.trans_c5[key].config(bg=coloFu)
        for key in self.trans_c6:
            self.trans_c6[key].config(bg=coloFu)
        for key in self.trans_c7:
            self.trans_c7[key].config(bg=coloFu)
        for key in self.trans_c8:
            self.trans_c8[key].config(bg=coloFu)
        for key in self.trans_c9:
            self.trans_c9[key].config(bg=coloFu)
        for key in self.trans_c10:
            self.trans_c10[key].config(bg=coloFu)
        for key in self.trans_c11:
            self.trans_c11[key].config(bg=coloFu)
        for key in self.trans_c12:
            self.trans_c12[key].config(bg=coloFu)
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloFu)
        for key in self.La_CA:
            self.La_CA[key].config(bg=coloFu)
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloFu)
        for key in self.Ac_CA:
            self.Ac_CA[key].config(bg=coloFu)
        for key in self.othermetal_c13_2:
            self.othermetal_c13_2[key].config(bg=coloFu)
        for key in self.othermetal_c14_2:
            self.othermetal_c14_2[key].config(bg=coloFu)
        for key in self.othermetal_c15_2:
            self.othermetal_c15_2[key].config(bg=coloFu)
        for key in self.othermetal_c16_2:
            self.othermetal_c16_2[key].config(bg=coloFu)
            
        pass
    # All non metals
    def AllNon_f(self):
        self.white_f()
        coloFu = "Aquamarine"
        self.H.config(bg=coloFu)
        for key in self.othernon_c14_0:
            self.othernon_c14_0[key].config(bg=coloFu)
        for key in self.othernon_c15_0:
            self.othernon_c15_0[key].config(bg=coloFu)
        for key in self.othernon_c16_0:
            self.othernon_c16_0[key].config(bg=coloFu)
        for key in self.nobel_c:
            self.nobel_c[key].config(bg=coloFu)
        for key in self.halogen_c:
            self.halogen_c[key].config(bg=coloFu)
        
        pass
    # Radioactive
    def Radioactive_f(self):
        self.white_f()
        pass
    # Solid
    def solid_f(self):
        self.white_f()
        coloFu="black"
        coloFg="white"
        for key in self.alkali_c:
            if key != "Fr":
                self.alkali_c[key].config(bg=coloFu, fg=coloFg)
        for key in self.alkaline_c:
            self.alkaline_c[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c3:
            self.trans_c3[key].config(bg=coloFu, fg=coloFg)
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloFu, fg=coloFg)
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c4:
            if key != "Rf":
                self.trans_c4[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c5:
            if key != "Db":
                self.trans_c5[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c6:
            if key != "Sg":
                self.trans_c6[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c7:
            if key != "Bh":
                self.trans_c7[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c8:
            if key != "Hs":
                self.trans_c8[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c9:
            self.trans_c9[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c10:
            self.trans_c10[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c11:
            self.trans_c11[key].config(bg=coloFu, fg=coloFg)
        for key in self.trans_c12:
            if key != "Hg":
                self.trans_c12[key].config(bg=coloFu, fg=coloFg)
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloFu, fg=coloFg)
        for key in self.La_CA:
            self.La_CA[key].config(bg=coloFu, fg=coloFg)
        for key in self.Ac_c3_2:
            self.Ac_c3_2[key].config(bg=coloFu, fg=coloFg)
        for key in self.Ac_CA:
            self.Ac_CA[key].config(bg=coloFu, fg=coloFg)
        for key in self.othermetal_c13_2:
            self.othermetal_c13_2[key].config(bg=coloFu, fg=coloFg)
        for key in self.othermetal_c14_2:
            self.othermetal_c14_2[key].config(bg=coloFu, fg=coloFg)
        for key in self.othermetal_c15_2:
            self.othermetal_c15_2[key].config(bg=coloFu, fg=coloFg)
        for key in self.othermetal_c16_2:
            self.othermetal_c16_2[key].config(bg=coloFu, fg=coloFg)
        for key in self.othernon_c14_0:
            self.othernon_c14_0[key].config(bg=coloFu, fg=coloFg)
        for key in self.othernon_c15_0:
            if key != "N":
                self.othernon_c15_0[key].config(bg=coloFu, fg=coloFg)
        for key in self.othernon_c16_0:
            if key != "O":
                self.othernon_c16_0[key].config(bg=coloFu, fg=coloFg)
        for key in self.metalloids_c12_1:
            self.metalloids_c12_1[key].config(bg=coloFu, fg=coloFg)
        for key in self.metalloid_c14_1:
            self.metalloid_c14_1[key].config(bg=coloFu, fg=coloFg)
        for key in self.metalloids_c15_1:
            self.metalloids_c15_1[key].config(bg=coloFu, fg=coloFg)
        for key in self.metalloid_c16_1:
            self.metalloid_c16_1[key].config(bg=coloFu, fg=coloFg)
        for key in self.halogen_c:
            if key != "F" and key != "Cl" and key != "Br": 
                self.halogen_c[key].config(bg=coloFu, fg=coloFg)

        for key in self.halogen_c_1:
            self.halogen_c_1[key].config(bg=coloFu, fg=coloFg)
        pass
    
    # liquid
    def liquid_f(self):
        self.white_f()
        coloFu="Blue"
        for key in self.alkali_c:
            if key == "Fr":
                self.alkali_c[key].config(bg=coloFu)
        for key in self.trans_c12:
            if key == "Hg":
                self.trans_c12[key].config(bg=coloFu)
        for key in self.halogen_c:
            if key == "Br": 
                self.halogen_c[key].config(bg=coloFu)     
        pass
    # Gas
    def gas_f(self):
        self.white_f()
        coloFu="Red"
        self.H.config(bg=coloFu)
        for key in self.othernon_c15_0:
            if key == "N":
                self.othernon_c15_0[key].config(bg=coloFu)
        for key in self.othernon_c16_0:
            if key == "O":
                self.othernon_c16_0[key].config(bg=coloFu)
        for key in self.halogen_c:
            if key == "F" or key == "Cl": 
                self.halogen_c[key].config(bg=coloFu)
        for key in self.nobel_c:
            self.nobel_c[key].config(bg=coloFu)

        pass
    # Unknown
    def unknown_f(self):
        self.white_f()
        coloFu = "gray"
        for key in self.trans_c4:
            if key == "Rf":
                self.trans_c4[key].config(bg=coloFu)
        for key in self.trans_c5:
            if key == "Db":
                self.trans_c5[key].config(bg=coloFu)
        for key in self.trans_c6:
            if key == "Sg":
                self.trans_c6[key].config(bg=coloFu)
        for key in self.trans_c7:
            if key == "Bh":
                self.trans_c7[key].config(bg=coloFu)
        for key in self.trans_c8:
            if key == "Hs":
                self.trans_c8[key].config(bg=coloFu)
        for key in self.trans_c9_0:
            self.trans_c9_0[key].config(bg=coloFu)
        for key in self.trans_c10_0:
            self.trans_c10_0[key].config(bg=coloFu)
        for key in self.trans_c11_0:
            self.trans_c11_0[key].config(bg=coloFu)
        for key in self.trans_c12_0:
            self.trans_c12_0[key].config(bg=coloFu)
        for key in self.othermetal_c13_2_0:
            self.othermetal_c13_2_0[key].config(bg=coloFu)
        for key in self.othermetal_c14_2_0:
            self.othermetal_c14_2_0[key].config(bg=coloFu)        
        for key in self.othermetal_c15_2_0:
            self.othermetal_c15_2_0[key].config(bg=coloFu)
        for key in self.othermetal_c16_2_0:
            self.othermetal_c16_2_0[key].config(bg=coloFu)
        for key in self.halogen_c_0:
            self.halogen_c_0[key].config(bg=coloFu)
        for key in self.nobel_c_0:
            self.nobel_c_0[key].config(bg=coloFu)

    # sends command to the arduino
    def arduino(self, text):
        byte_msg = text.encode('utf-8')
        #byte_msg = bytes(text, 'utf-8')
        if text == "exit":
            try:
                nano.close()
            except:
                # comment this out or chang the statement
                # print("close but nano is not connected")
                pass
        else:
            #print(byte_msg)
            try:
                nano.write(byte_msg)
            except:
                # comment this out or change the statement
                # print("some element but nano is not defined")
                pass

    # voice description
    def voice(self, text):
        self.engine.setProperty("rate", 170)
        self.engine.say(text)
        self.engine.runAndWait()

# This class is about blocks and electron configurartions
class Second(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.topLabel = tk.Label(self, text="Hydrogen", font=('Helvetica 15 bold', 15))
        self.topLabel.grid(row=0, column=0, columnspan=18)
        """=======================================blocks==================================="""
        r1 = Label(self, text="1", font=7)
        r1.grid(column=1, row=3)

        r2 = Label(self, text="2", font=7)
        r2.grid(column=1, row=4)

        r3 = Label(self, text="3", font=7)
        r3.grid(column=1, row=5)

        r4 = Label(self, text="4", font=7)
        r4.grid(column=1, row=6)

        r5 = Label(self, text="5", font=7)
        r5.grid(column=1, row=7)

        r6 = Label(self, text="6", font=7)
        r6.grid(column=1, row=8)

        r7 = Label(self, text="7", font=7)
        r7.grid(column=1, row=9)
        
        #Column numbers
        c1 = Label(self, text="1", font=7)
        c1.grid(column=2, row=2)
        
        c2 = Label(self, text="2", font=7)
        c2.grid(column=3, row=3)
        
        c3 = Label(self, text="3", font=7)
        c3.grid(column=4, row=5)
        
        c4 = Label(self, text="4", font=7)
        c4.grid(column=5, row=5)
        
        c5 = Label(self, text="5", font=7)
        c5.grid(column=6, row=5)

        c6 = Label(self, text="6", font=7)
        c6.grid(column=7, row=5)

        c7 = Label(self, text="7", font=7)
        c7.grid(column=8, row=5)

        c8 = Label(self, text="8", font=7)
        c8.grid(column=9, row=5)

        c9 = Label(self, text="9", font=7)
        c9.grid(column=10, row=5)

        c10 = Label(self, text="10", font=7)
        c10.grid(column=11, row=5)

        c11 = Label(self, text="11", font=7)
        c11.grid(column=12, row=5)

        c12 = Label(self, text="12", font=7)
        c12.grid(column=13, row=5)

        c13 = Label(self, text="13", font=7)
        c13.grid(column=14, row=3)

        c14 = Label(self, text="14", font=7)
        c14.grid(column=15, row=3)

        c15 = Label(self, text="15", font=7)
        c15.grid(column=16, row=3)

        c16 = Label(self, text="16", font=7)
        c16.grid(column=17, row=3)

        c17 = Label(self, text="17", font=7)
        c17.grid(column=18, row=3)

        c18 = Label(self, text="18", font=7)
        c18.grid(column=19, row=2)

        s_block_0 = [
            ('H', 'Hydrogen', 'Oxidation states: -1, 1\nConfiguration: 1s¹\nExpanded: - \n1s¹\nEnergy levels: 1\nQuantum numbers: l=0, m=0, n=1', '1', '1.01'),
            ('Li', 'Lithium', 'Oxidation states: 1\nConfiguration: [He] 2s¹\nExpanded: - \n1s² 2s¹\nEnergy levels: 2, 1\nQuantum numbers: l=0, m=0, n=2', '3', '6.94'),
            ('Na', 'Sodium', 'Oxidation states: -1, 1\nConfiguration: [Ne] 3s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s¹\nEnergy levels: 2, 8, 1\nQuantum numbers: l=0, m=0, n=3', '11', '22.99'),
            ('K', 'Potassium', 'Oxidation states: -1, 1\nConfiguration: [Ar] 4s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹\nEnergy levels: 2, 8, 8, 1\nQuantum numbers: l=0, m=0, n=4', '19', '39.10'),
            ('Rb', 'Rubidium', 'Oxidation states: -1, 1\nConfiguration: [Kr] 5s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹\nEnergy levels: 2, 8, 18, 8, 1\nQuantum numbers: l=0, m=0, n=5', '37', '85.41'),
            ('Cs', 'Cesium', 'Oxidation states: -1, 1\nConfiguration: [Xe] 6s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s¹\nEnergy levels: 2, 8, 18, 18, 8, 1\nQuantum numbers: l=0, m=0, n=6', '55', '132.91'),
            ('Fr', 'Francium', 'Oxidation states: 1\nConfiguration: [Rn] 7s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s¹\nEnergy levels: 2, 8, 18, 32, 18, 8, 1\nQuantum numbers: l=0, m=0, n=7', '87', '223')
            ]
        r = 3
        c = 2
        self.s_block_c_0={}
        colorS="pink"
        for b in s_block_0:
            self.s_block_c_0[b[0]]=tk.Button(self,
                                           text=b[0],
                                           width=5,
                                           height=2,
                                           font=10,
                                           borderwidth = 3,
                                           bg=colorS,
                                           command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorS, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.s_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9:
                r = 1
                c += 1
        
        s_block_1 = [
            ('Be', 'Beryllium', 'Oxidation states: 1, 2\nConfiguration: [He] 2s²\nExpanded: - \n1s² 2s²\nEnergy levels: 2, 2\nQuantum numbers: l=0, m=0, n=2', '4', '9.01'),
            ('Mg', 'Magnesium', 'Oxidation states: 1, 2\nConfiguration: [Ne] 3s²\nExpanded: - \n1s² 2s² 2p⁶ 3s²\nEnergy levels: 2, 8, 2\nQuantum numbers: l=0, m=0, n=3', '12', '24.31'),
            ('Ca', 'Calcium', 'Oxidation states: 1, 2\nConfiguration: [Ar] 4s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\nEnergy levels: 2, 8, 8, 2\nQuantum numbers: l=0, m=0, n=4', '20', '40.08'),
            ('Sr', 'Strontium', 'Oxidation states: 1, 2\nConfiguration: [Kr] 5s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s²\nEnergy levels: 2, 8, 18, 8, 2\nQuantum numbers: l=0, m=0, n=5', '38', '87.62'),
            ('Ba', 'Barium', 'Oxidation states: 2\nConfiguration: [Xe] 6s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s²\nEnergy levels: 2, 8, 18, 18, 8, 2\nQuantum numbers: l=0, m=0, n=6', '56', '137.33'),
            ('Ra', 'Radium', 'Oxidation states: 2\nConfiguration: [Rn] 7s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶\n 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s²\nEnergy levels: 2, 8, 18, 32, 18, 8, 2\nQuantum numbers: l=0, m=0, n=7', '88', '226.03')]
        r = 4
        c = 3
        self.s_block_c_1={}
        for b in s_block_1:
            self.s_block_c_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorS,
                      command=lambda text=b:  [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorS, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.s_block_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        
        d_block_0 = [
            ('Sc', 'Scandium', 'Oxidation states 1, 2, 3\nConfiguration [Ar] 4s² 3d¹\nExpanded - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹\nEnergy levels 2, 8, 9, 2\nQuantum numbers l=2, m=-2, n=3', '21', '44.96'),
            ('Y', 'Yttrium', 'Oxidation states 1, 2, 3\nConfiguration [Kr] 5s² 4d¹\nExpanded - \n 1s² 2s² 2p⁶ 3s² \n3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹\nEnergy levels 2, 8, 18, 9, 2\nQuantum numbers l=2, m=-2, n=4', '39', '88.91')]
        r = 6
        c = 4
        self.d_block_c_0={}
        colorD="light goldenrod"
        for b in d_block_0: 
            self.d_block_c_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        f_block_0 = [
            ('La', 'Lanthanum', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 5d¹\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 5d¹\nEnergy levels: 2, 8, 18, 18, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '57', '138.91'),
            ('Ac', 'Actinium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 6d¹\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰\n 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 6d¹\nEnergy levels: 2, 8, 18, 32, 18, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '89', '227.03')]
        r = 8
        c = 4
        self.f_block_c_0={}
        colorF="Teal"
        for b in f_block_0: 
            self.f_block_c_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorF,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorF, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.f_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_1 = [
            ('Ti', 'Titanium', 'Oxidation states: -1, 2, 3, 4\nConfiguration: [Ar] 4s² 3d²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d²\nEnergy levels: 2, 8, 10, 2\nQuantum numbers: l=2, m=-1, n=3', '22', '47.90'),
            ('Zr', 'Zirconium', 'Oxidation states:  1, 2, 3, 4\nConfiguration: [Kr] 5s² 4d²\nExpanded: - \n 1s² 2s² 2p⁶\n 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d²\nEnergy levels: 2, 8, 18, 10, 2\nQuantum numbers: l=2, m=-1, n=4', '40', '91.22'),
            ('Hf', 'Hafnium', 'Oxidation states: 2, 3, 4\nConfiguration: [Xe] 6s² 4f¹⁴ 5d²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d²\nEnergy levels: 2, 8, 18, 32, 10, 2\nQuantum numbers: l=2, m=-1, n=5', '72', '178.49'),
            ('Rf', 'Rutherfordium', 'Oxidation states: 4\nConfiguration: [Rn] 7s² 5f¹⁴ 6d²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d²\nEnergy levels: 2, 8, 18, 32, 32, 10, 2\nQuantum numbers: l=2, m=-1, n=6', '104', '261.00')]
        r = 6
        c = 5
        self.d_block_c_1={}
        for b in d_block_1: 
            self.d_block_c_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        d_block_2 = [
            ('V', 'Vanadium', 'Oxidation states: -1, 1, 2, 3, 4, 5\nConfiguration: [Ar] 4s² 3d³\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d³\nEnergy levels: 2, 8, 11, 2\nQuantum numbers: l=2, m=0, n=3', '23', '50.94'),
            ('Nb', 'Niobium', 'Oxidation states: -1, 2, 3, 4, 5\nConfiguration: [Kr] 5s¹ 4d⁴\nExpanded: - \n 1s² 2s² 2p⁶ \n3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d⁴\nEnergy levels: 2, 8, 18, 12, 1\nQuantum numbers: l=2, m=1, n=4', '41', '92.91'),
            ('Ta', 'Tantalum', 'Oxidation states: -1, 2, 3, 4, 5\nConfiguration: [Xe] 6s² 4f¹⁴ 5d³\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d³\nEnergy levels: 2, 8, 18, 32, 11, 2\nQuantum numbers: l=2, m=0, n=5', '73', '180.95'),
            ('Db', 'Dubnium', 'Oxidation states: 5\nConfiguration: [Rn] 7s² 5f¹⁴ 6d³\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d³\nEnergy levels: 2, 8, 18, 32, 32, 11, 2\nQuantum numbers: l=2, m=0, n=6', '105', '262.00')]
        r = 6
        c = 6
        self.d_block_c_2={}
        for b in d_block_2: 
            self.d_block_c_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_3 = [
            ('Cr', 'Chromium', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Ar] 4s¹ 3d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d⁵\nEnergy levels: 2, 8, 13, 1\nQuantum numbers: l=2, m=2, n=3', '24', '51.99'),
            ('Mo', 'Molybdenum', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Kr] 5s¹ 4d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s¹ 4d⁵\nEnergy levels: 2, 8, 18, 13, 1\nQuantum numbers: l=2, m=2, n=4', '42', '95.94'),
            ('W', 'Tungsten', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁴\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁴\nEnergy levels: 2, 8, 18, 32, 12, 2\nQuantum numbers: l=2, m=1, n=5', '74', '183.85'),
            ('Sg', 'Seaborgium', 'Oxidation states: 6\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁴\nEnergy levels: 2, 8, 18, 32, 32, 12, 2\nQuantum numbers: l=2, m=1, n=6', '106', '266.00')]
        r = 6
        c = 7
        self.d_block_c_3={}
        for b in d_block_3: 
            self.d_block_c_3[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_3[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_4 = [
            ('Mn', 'Manganese', 'Oxidation states: -3, -2, -1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Ar] 4s² 3d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁵\nEnergy levels: 2, 8, 13, 2\nQuantum numbers: l=2, m=2, n=3', '25', '178.49'),
            ('Tc', 'Technetium', 'Oxidation states: -3, -1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Kr] 5s² 4d⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d⁵\nEnergy levels: 2, 8, 18, 13, 2\nQuantum numbers: l=2, m=2, n=4', '43', '178.49'),
            ('Re', 'Rhenium', 'Oxidation states: -3, -1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁵\nEnergy levels: 2, 8, 18, 32, 13, 2\nQuantum numbers: l=2, m=2, n=5', '75', '178.49'),
            ('Bh', 'Bohrium', 'Oxidation states: 7\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁵\nEnergy levels: 2, 8, 18, 32, 32, 13, 2\nQuantum numbers: l=2, m=2, n=6', '107', '262.00')]
        r = 6
        c = 8
        self.d_block_c_4={}
        for b in d_block_4: 
            self.d_block_c_4[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_4[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_5 = [
            ('Fe', 'Iron', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Ar] 4s² 3d⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶\nEnergy levels: 2, 8, 14, 2\nQuantum numbers: l=2, m=-2, n=3', '26', '55.85'),
            ('Ru', 'Ruthenium', 'Oxidation states: -2, 1, 2, 3, 4, 5, 6, 7, 8\nConfiguration: [Kr] 5s¹ 4d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d⁷\nEnergy levels: 2, 8, 18, 15, 1\nQuantum numbers: l=2, m=-1, n=4', '44', '101.07'),
            ('Os', 'Osmium', 'Oxidation states: -2, 1, 2, 3, 4, 5, 6, 7, 8\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁶\nEnergy levels: 2, 8, 18, 32, 14, 2\nQuantum numbers: l=2, m=-2, n=5', '76', '190.20'),
            ('Hs', 'Hassium', 'Oxidation states: 8\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁶\nEnergy levels: 2, 8, 18, 32, 32, 14, 2\nQuantum numbers: l=2, m=-2, n=6', '108', '265.00')]
        r = 6
        c = 9
        self.d_block_c_5={}
        for b in d_block_5: 
            self.d_block_c_5[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_5[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_6 = [
            ('Co', 'Cobalt', 'Oxidation states: -1, 1, 2, 3, 4, 5\nConfiguration: [Ar] 4s² 3d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁷\nEnergy levels: 2, 8, 15, 2\nQuantum numbers: l=2, m=-1, n=3', '27', '58.93'),
            ('Rh', 'Rhodium', 'Oxidation states: -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Kr] 5s¹ 4d⁸\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d⁸\nEnergy levels: 2, 8, 18, 16, 1\nQuantum numbers: l=2, m=0, n=4', '45', '102.91'),
            ('Ir', 'Iridium', 'Oxidation states: -3, -1, 1, 2, 3, 4, 5, 6, 7, 8\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁷\nEnergy levels: 2, 8, 18, 32, 15, 2\nQuantum numbers: l=2, m=-1, n=5', '77', '192.22'),
            ('Mt', 'Meitnerium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁷\n\nEnergy levels: 2, 8, 18, 32, 32, 15, 2\nQuantum numbers: l=2, m=-1, n=6', '109', '266.00')]
        r = 6
        c = 10
        self.d_block_c_6={}
        for b in d_block_6: 
            self.d_block_c_6[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_6[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_7 = [
            ('Ni', 'Nickle', 'Oxidation states: -1, 1, 2, 3, 4\nConfiguration: [Ar] 4s² 3d⁸\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁸\nEnergy levels: 2, 8, 16, 2\nQuantum numbers: l=2, m=2, n=3',  '28', '58.70'),
            ('Pd', 'Palladium', 'Oxidation states: 2, 4\nConfiguration: [Kr] 4d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 4d¹⁰\nEnergy levels: 2, 8, 18, 18\nQuantum numbers: l=2, m=2, n=4', '46', '106.40'),
            ('Pt', 'Platinum', 'Oxidation states: 2, 4, 5, 6\nConfiguration: [Xe] 6s¹ 4f¹⁴ 5d⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s¹ 4f¹⁴ 5d⁹\nEnergy levels: 2, 8, 18, 32, 17, 1\nQuantum numbers: l=2, m=1, n=5', '78', '195.09'),
            ('Ds', 'Darmstadtium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s¹ 5f¹⁴ 6d⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰\n 6p⁶ 7s¹ 5f¹⁴ 6d⁹\nEnergy levels: 2, 8, 18, 32, 32, 17, 1\nQuantum numbers: l=2, m=1, n=6', '110', '281')]
        r = 6
        c = 11
        self.d_block_c_7={}
        for b in d_block_7: 
            self.d_block_c_7[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_7[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_8 = [
            ('Cu', 'Copper', 'Oxidation states: 1, 2, 3, 4\nConfiguration: [Ar] 4s¹ 3d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰\nEnergy level: s2, 8, 18, 1\nQuantum numbers: l=2, m=2, n=3', '29', '63.55'),
            ('Ag', 'Silver', 'Oxidation states: 1, 2, 3, 4\nConfiguration: [Kr] 5s¹ 4d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d¹⁰\nEnergy levels: 2, 8, 18, 18, 1\nQuantum numbers: l=2, m=2, n=4', '47', '107.97'),
            ('Au', 'Gold', 'Oxidation states: -1, 1, 2, 3, 5\nConfiguration: [Xe] 6s¹ 4f¹⁴ 5d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s¹ 4f¹⁴ 5d¹⁰\nEnergy levels: 2, 8, 18, 32, 18, 1\nQuantum numbers: l=2, m=1, n=6', '79', '196.97'),
            ('Rg', 'Roentgenium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹\n⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁹\nEnergy levels: 2, 8, 18, 32, 32, 17, 2\nQuantum numbers: l=2, m=2, n=3', '111', '282')]
        r = 6
        c = 12
        self.d_block_c_8={}
        for b in d_block_8: 
            self.d_block_c_8[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_8[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_9 = [
            ('Zn', 'Zinc', 'Oxidation states: 1, 2\nConfiguration: [Ar] 4s² 3d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰\nEnergy levels: 2, 8, 18, 2\nQuantum numbers: l=2, m=2, n=3', '30', '65.37'),
            ('Cd', 'Cadmium', 'Oxidation states: 1, 2\nConfiguration: [Kr] 5s² 4d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶\n 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰\nEnergy levels: 2, 8, 18, 18, 2\nQuantum numbers: l=2, m=2, n=4', '48', '112.41'),
            ('Hg', 'Mercury', 'Oxidation states: 1, 2, 4\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰\nEnergy levels: 2, 8, 18, 32, 18, 2\nQuantum numbers: l=2, m=-1, n=2', '80', '200.59'),
            ('Cn', 'Copernicium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰\nEnergy levels: 2, 8, 18, 32, 32, 18, 2\nQuantum numbers: l=2, m=2, n=6', '112', '285')]
        r = 6
        c = 13
        self.d_block_c_9={}
        for b in d_block_9: 
            self.d_block_c_9[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_9[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_0 = [
            ('B', 'Boron', 'Oxidation states: 1, 2, 3\nConfiguration: [He] 2s² 2p¹\nExpanded: - \n1s² 2s² 2p¹\nEnergy levels: 2, 3\nQuantum numbers: l=1, m=-1, n=2', '5', '10.81'),
            ('Al', 'Aluminum', 'Oxidation states: 1, 2, 3\nConfiguration: [Ne] 3s² 3p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p¹\nEnergy levels: 2, 8, 3\nQuantum numbers: l=1, m=-1, n=3', '13', '26.98'),
            ('Ga', 'Gallium', 'Oxidation states: 1, 2, 3\nConfiguration: [Ar] 4s² 3d¹⁰ 4p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² \n3p⁶ 4s² 3d¹⁰ 4p¹\nEnergy levels: 2, 8, 18, 3\nQuantum numbers: l=1, m=-1, n=4', '31', '69.72'),
            ('In', 'Indium', 'Oxidation states: 1, 2, 3\nConfiguration: [Kr] 5s² 4d¹⁰ 5p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p¹\nEnergy levels: 2, 8, 18, 18, 3\nQuantum numbers: l=1, m=-1, n=5', '49', '69.72'),
            ('Ti', 'Thallium', 'Oxidation states: 1, 3\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p¹\nEnergy levels: 2, 8, 18, 32, 18, 3\nQuantum numbers: l=1, m=-1, n=6', '81', '204.37'),
            ('Nh', 'Nihonium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ \n5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p¹\nEnergy levels: 2, 8, 18, 32, 32, 18, 3\nQuantum numbers: l=1, m=-1, n=7', '113', '286')]
        r = 4
        c = 14
        colorP="Aquamarine"
        self.p_block_c_0={}
        for b in p_block_0: 
            self.p_block_c_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorP,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.p_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_1 = [
            ('C', 'Carbon', 'Oxidation states: -4, -3, -2, -1, 1, 2, 3, 4\nConfiguration: [He] 2s² 2p²\nExpanded: - \n1s² 2s² 2p²\nEnergy levels: 2, 4\nQuantum numbers: l=1, m=0, n=2', '6', '12.01'),
            ('Si', 'Silicon', 'Oxidation states: -4, -3, -2, -1, 1, 2, 3, 4\nConfiguration: [Ne] 3s² 3p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p²\nEnergy levels: 2, 8, 4\nQuantum numbers: l=1, m=0, n=3', '14', '28.09'),
            ('Ge', 'Germanium', 'Oxidation states: -4, 1, 2, 3, 4\nConfiguration: [Ar] 4s² 3d¹⁰ 4p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p²\nEnergy levels: 2, 8, 18, 4\nQuantum numbers: l=1, m=0, n=4', '32', '72.59'),
            ('Sn', 'Tin', 'Oxidation states: -4, 2, 4\nConfiguration: [Kr] 5s² 4d¹⁰ 5p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p²\nEnergy levels: 2, 8, 18, 18, 4\nQuantum numbers: l=1, m=0, n=5', '50', '118.69'),
            ('Pb', 'Lead', 'Oxidation states: -4, 2, 4\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p²\nEnergy levels: 2, 8, 18, 32, 18, 4\nQuantum numbers: l=1, m=0, n=6', '82', '207.20'),
            ('Fl', 'Flerovium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p²\nEnergy levels: 2, 8, 18, 32, 32, 18, 4\nQuantum numbers: l=1, m=0, n=7', '114', '289')]
        r = 4
        c = 15
        self.p_block_c_1={}
        for b in p_block_1: 
            self.p_block_c_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorP,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.p_block_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_2 = [
            ('N', 'Nitrogen', 'Oxidation states: -3, -2, -1, 1, 2, 3, 4, 5\nConfiguration: [He] 2s² 2p³\nExpanded: - \n1s² 2s² 2p³\nEnergy levels: 2, 5\nQuantum numbers: l=1, m=1, n=2', '7', '14.01'),
            ('P', 'Phosphorus', 'Oxidation states: -3, -2, -1, 1, 2, 3, 4, 5\nConfiguration: [Ne] 3s² 3p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p³\nEnergy levels: 2, 8, 5\nQuantum numbers: l=1, m=1, n=3', '15', '30.97'),
            ('As', 'Arsenic', 'Oxidation states: -3, 2, 3, 5\nConfiguration: [Ar] 4s² 3d¹⁰ 4p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p³\nEnergy levels: 2, 8, 18, 5\nQuantum numbers: l=1, m=1, n=4', '33', '74.92'),
            ('Sb', 'Antimony', 'Oxidation states: -3, 3, 5\nConfiguration: [Kr] 5s² 4d¹⁰ 5p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p³\nEnergy levels: 2, 8, 18, 18, 5\nQuantum numbers: l=1, m=1, n=5', '51', '121.75'),
            ('Bi', 'Bismuth', 'Oxidation states: -3, 3, 5\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p³\nEnergy levels: 2, 8, 18, 32, 18, 5\nQuantum numbers: l=1, m=1, n=6', '83', '208.98'),
            ('Mc', 'Moscovium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p³\nEnergy levels: 2, 8, 18, 32, 32, 18, 5\nQuantum numbers: l=1, m=1, n=7', '115', '290')]
        r = 4
        c = 16
        self.p_block_c_2={}
        for b in p_block_2: 
            self.p_block_c_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorP,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.p_block_c_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        p_block_3 = [
            ('O', 'Oxygen', 'Oxidation states: -2, -1, 1, 2\n Configuration: [He] 2s² 2p⁴\nExpanded: - \n1s² 2s² 2p⁴\nEnergy levels: 2, 6\nQuantum numbers: l=1, m=-1, n=2', '8', '15.99'),
            ('S', 'Sulfur', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Ne] 3s² 3p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁴\nEnergy levels: 2, 8, 6\nQuantum numbers: l=1, m=-1, n=3', '16', '32.06'),
            ('Se', 'Selenium', 'Oxidation states: -2, 1, 2, 4, 6\nConfiguration: [Ar] 4s² 3d¹⁰ 4p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁴\nEnergy levels: 2, 8, 18, 6\nQuantum numbers: l=1, m=-1, n=4' '34', '78.96'),
            ('Te', 'Tellurium', 'Oxidation states: -2, 2, 4, 5, 6\nConfiguration: [Kr] 5s² 4d¹⁰ 5p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁴\nEnergy levels: 2, 8, 18, 18, 6\nQuantum numbers: l=1, m=-1, n=5', '52', '127.60'),
            ('Po', 'Polonium', 'Oxidation states: -2, 2, 4, 6\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁴\nEnergy levels: 2, 8, 18, 32, 18, 6\nQuantum numbers: l=1, m=-1, n=6', '84', '209.00'),
            ('Lv', 'Livermorium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ \n5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁴\nEnergy levels: 2, 8, 18, 32, 32, 18, 6\nQuantum numbers: l=1, m=-1, n=7', '116', '293.00')]
        r = 4
        c = 17
        self.p_block_c_3={}
        for b in p_block_3: 
            self.p_block_c_3[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorP,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.p_block_c_3[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_4 = [
            ('F', 'Fluorine', 'Oxidation states: -1\nConfiguration: [He] 2s² 2p⁵\nExpanded: - \n1s² 2s² 2p⁵\nEnergy levels: 2, 7\nQuantum numbers: l=1, m=0, n=2', '9', '18.99'),
            ('Cl', 'Chlorine', 'Oxidation states: \n-1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Ne] 3s² 3p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁵\nEnergy levels: 2, 8, 7\nQuantum numbers: l=1, m=0, n=3', '17', '35.45'),
            ('Br', 'Bromine', 'Oxidation states: -1, 1, 3, 4, 5, 7\nConfiguration: [Ar] 4s² 3d¹⁰ 4p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁵\nEnergy levels: 2, 8, 18, 7\nQuantum numbers: l=1, m=0, n=4', '35', '79.90'),
            ('I', 'Iodine', 'Oxidation states: -1, 1, 3, 4, 5, 7\nConfiguration: [Kr] 5s² 4d¹⁰ 5p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁵\nEnergy levels: 2, 8, 18, 18, 7\nQuantum numbers: l=1, m=0, n=5', '53', '126.90'),
            ('At', 'Astatine', 'Oxidation states: -1, 1, 3, 5, 7\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰\n 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁵\nEnergy levels: 2, 8, 18, 32, 18, 7\nQuantum numbers: l=1, m=0, n=6', '85', '210.00'),
            ('Ts', 'Tennessine', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁵\nEnergy levels: 2, 8, 18, 32, 32, 18, 7\nQuantum numbers: l=1, m=0, n=7', '117', '294.00')]
        r = 4
        c = 18
        self.p_block_c_4={}
        for b in p_block_4: 
            self.p_block_c_4[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorP,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.p_block_c_4[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        s_block_2 = [
            ('He', 'Helium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ \n5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁶\nEnergy levels: 2, 8, 18, 32, 32, 18, 8\nQuantum numbers: l=0, m=0, n=1', '2', '4.00')]
        r = 3
        c = 19
        self.s_block_c_2={}
        for b in s_block_2: 
            self.s_block_c_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorS,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorS, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.s_block_c_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        p_block_5 = [
            ('Ne', 'Neon', 'Oxidation states: N/A\nConfiguration: [He] 2s² 2p⁶\nExpanded: - \n1s² 2s² 2p⁶\nEnergy levels: 2, 8\nQuantum numbers: l=1, m=1, n=2', '10', '20.18'),
            ('Ar', 'Argon', 'Oxidation states: N/A\nConfiguration: [Ne] 3s² 3p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶\nEnergy levels: 2, 8, 8\nQuantum numbers: l=1, m=1, n=3', '18', '39.95'),
            ('Kr', 'Krypton', 'Oxidation states: 2\nConfiguration: [Ar] 4s² 3d¹⁰ 4p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶\nEnergy levels: 2, 8, 18, 8\nQuantum numbers: l=1, m=1, n=4', '36', '83.80'),
            ('Xe', 'Xenon', 'Oxidation states: 2, 4, 6, 8\nConfiguration: [Kr] 5s² 4d¹⁰ 5p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶\nEnergy levels: 2, 8, 18, 18, 8\nQuantum numbers: l=1, m=1, n=5', '54', '131.30'),
            ('Rn', 'Radon', 'Oxidation states: 2\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶\nEnergy levels: 2, 8, 18, 32, 18, 8\nQuantum numbers: l=1, m=1, n=6', '86', '222.00'),
            ('Og', 'Oganesson', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4\nf¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁶\nEnergy levels: 2, 8, 18, 32, 32, 18, 8\nQuantum numbers: l=1, m=1, n=7', '118', '294.00')]
        r = 4
        c = 19
        self.p_block_c_5={}
        for b in p_block_5: 
            self.p_block_c_5[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorP,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.p_block_c_5[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        self.fillerLine = tk.Label(self, text="")
        self.fillerLine.grid(row=12, column=0)
        
        f_block_2 = [
            ('Ce', 'Cerium', 'Oxidation states: 2, 3, 4\nConfiguration: [Xe] 6s² 4f¹ 5d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹ 5d¹\nEnergy levels: 2, 8, 18, 19, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '58', '140.12'),
            ('Pr', 'Praseodymium', 'Oxidation states: 2, 3, 4\nConfiguration: [Xe] 6s² 4f³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f³\nEnergy levels: 2, 8, 18, 21, 8, 2\nQuantum numbers: l=3, m=-1, n=4', '59', '140.91'),
            ('Nd', 'Neodymium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁴\nEnergy levels: 2, 8, 18, 22, 8, 2\nQuantum numbers: l=3, m=0, n=4', '60', '144.24'),
            ('Pm', 'Promethium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁵\nEnergy levels: 2, 8, 18, 23, 8, 2\nQuantum numbers: l=3, m=1, n=4', '61', '145.00'),
            ('Sm', 'Samarium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁶\nEnergy levels: 2, 8, 18, 24, 8, 2\nQuantum numbers: l=3, m=2, n=4', '62', '150.40'),
            ('Eu', 'Europium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁷\nEnergy levels: 2, 8, 18, 25, 8, 2\nQuantum numbers: l=3, m=3, n=4', '63', '151.96'),
            ('Gd', 'Gadolinium', 'Oxidation states: 1, 2, 3\nConfiguration: [Xe] 6s² 4f⁷ 5d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰\n 5p⁶ 6s² 4f⁷ 5d¹\nEnergy levels: 2, 8, 18, 25, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '64', '157.25'),
            ('Tb', 'Oxidation states: 1, 3, 4\nConfiguration: [Xe] 6s² 4f⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁹\nEnergy levels: 2, 8, 18, 27, 8, 2\nQuantum numbers: l=3, m=-2, n=4', '65', '158.93'),
            ('Dy', 'Dyprosium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁰\nEnergy levels: 2, 8, 18, 28, 8, 2\nQuantum numbers: l=3, m=-1, n=4', '66', '162.50'),
            ('Ho', 'Holmium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f¹¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹¹\nEnergy levels: 2, 8, 18, 29, 8, 2\nQuantum numbers: l=3, m=0, n=4', '67', '164.93'),
            ('Er', 'Erbium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f¹²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹²\nEnergy levels: 2, 8, 18, 30, 8, 2\nQuantum numbers: l=3, m=1, n=4', '68', '167.26'),
            ('Tm', 'Thulium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f¹³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹³\nEnergy levels: 2, 8, 18, 31, 8, 2\nQuantum numbers: l=3, m=2, n=4', '69', '168.93'),
            ('Yb', 'Ytterbium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f¹⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴\nEnergy levels: 2, 8, 18, 32, 8, 2\nQuantum numbers: l=3, m=3, n=4', '70', '173.04')]
        r = 13
        c = 5
        self.f_block_c_2={}
        for b in f_block_2: 
            self.f_block_c_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorF,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorF, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.f_block_c_2[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        d_block_20 = [
            ('Lu', 'Lutetium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹\nEnergy levels: 2, 8, 18, 32, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '71', '174.97')]
        r = 13
        c = 18
        self.d_block_c_20={}
        for b in d_block_20: 
            self.d_block_c_20[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_20[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        f_block_3 = [
            ('Th', 'Thorium', 'Oxidation states: 2, 3, 4\nConfiguration: [Rn] 7s² 6d²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 6d²\nEnergy levels: 2, 8, 18, 32, 18, 10, 2\nQuantum numbers: l=2, m=-1, n=6', '90', '232.04'),
            ('Pa', 'Protactinium', 'Oxidation states: 2, 3, 4, 5\nConfiguration: [Rn] 7s² 5f² 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f² 6d¹\nEnergy levels: 2, 8, 18, 32, 20, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '91', '231.04'),
            ('U', 'Uranium', 'Oxidation states: 2, 3, 4, 5, 6\nConfiguration: [Rn] 7s² 5f³ 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f³ 6d¹\nEnergy levels: 2, 8, 18, 32, 21, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '92', '238.03'),
            ('Np', 'Neptunium', 'Oxidation states: 3, 4, 5, 6, 7\nConfiguration: [Rn] 7s² 5f⁴ 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁴ 6d¹\nEnergy levels: 2, 8, 18, 32, 22, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '93', '237.05'),
            ('Pu', 'Plutonium', 'Oxidation states: 3, 4, 5, 6, 7, 8\nConfiguration: [Rn] 7s² 5f⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁶\nEnergy levels: 2, 8, 18, 32, 24, 8, 2\nQuantum numbers: l=3, m=3, n=5', '94', '244.00'),
            ('Am', 'Americium', 'Oxidation states: 2, 3, 4, 5, 6\nConfiguration: [Rn] 7s² 5f⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁷\nEnergy levels: 2, 8, 18, 32, 25, 8, 2\nQuantum numbers: l=3, m=3, n=5', '95', '243.00'),
            ('Cm', 'Curium', 'Oxidation states: 3, 4\nConfiguration: [Rn] 7s² 5f⁷ 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁷ 6d¹\nEnergy levels: 2, 8, 18, 32, 25, 9, 2\nQuantum numbers; l=2, m=-2, n=6', '96', '247.00'),
            ('Bk', 'Berkelium', 'Oxidation states: 3, 4\nConfiguration: [Rn] 7s² 5f⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ \n5d¹⁰ 6p⁶ 7s² 5f⁹\nEnergy levels: 2, 8, 18, 32, 27, 8, 2\nQuantum numbers: l=3, m=-2, n=5', '97', '247.00'),
            ('Cf', 'Californium', 'Oxidation states: 2, 3, 4\nConfiguration: [Rn] 7s² 5f¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶\n 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁰\nEnergy levels: 2, 8, 18, 32, 28, 8, 2\nQuantum numbers: l=3, m=-1, n=5', '98', '247.00'),
            ('Es', 'Einsteinium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹¹\nEnergy levels: 2, 8, 18, 32, 29, 8, 2\nQuantum numbers: l=3, m=0, n=5', '99', '252.00'),
            ('Fm', 'Fermium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹²\nEnergy levels: 2, 8, 18, 32, 30, 8, 2\nQuantum numbers: l=3, m=1, n=5', '100', '257.00'),
            ('Md', 'Mendelevium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ \n5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹³\nEnergy levels: 2, 8, 18, 32, 31, 8, 2\nQuantum numbers: l=3, m=2, n=5', '101', '260.00'),
            ('No', 'Nobelium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴\nEnergy levels: 2, 8, 18, 32, 32, 8, 2\nQuantum numbers: l=3, m=3, n=5', '102', '259.00')]
        r = 14
        c = 5
        self.f_block_c_3={}
        for b in f_block_3: 
            self.f_block_c_3[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorF,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorF, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.f_block_c_3[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        d_block_21 = [
            ('Lr', 'Lawrencium', 'Oxidation states: 3\nConfiguration: [Rn] 7s² 5f¹⁴ 7p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 7p¹\nEnergy levels: 2, 8, 18, 32, 32, 8, 3\nQuantum numbers: l=1, m=-1, n=7', '103', '262.00')]
        r = 14
        c = 18
        self.d_block_c_21={}
        for b in d_block_21: 
            self.d_block_c_21[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg=colorD,
                      command=lambda text=b: [self.name(text[1]) + self.info(text[2]), self.arduino(text[0]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0])])
            self.d_block_c_21[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1
        """===============================================================BLOCK_Buttons============================================================"""

        S_BLOCK = [('S block', 'S block elements', 'S-')]
        r = 1
        c = 4
        for b in S_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="pink",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.s_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        P_BLOCK = [('P block', 'P block elements', 'P-')]
        r = 1
        c = 6
        for b in P_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="Aquamarine",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.p_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        D_BLOCK = [('D block', 'D block elements', 'D-')]
        r = 1
        c = 8
        for b in D_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="light goldenrod",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.d_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        F_BLOCK = [('F block', 'F block elements', 'F-')]
        r = 1
        c = 10
        for b in F_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="Teal",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.f_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
        
        All_BLOCK = [('All blocks', 'All elements', 'All')]
        r = 1
        c = 12
        for b in All_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="white",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.all_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

       
        #setting up the canvas big elements image
        self.canv = Canvas(self, width=200, height=200)
        self.img = (Image.open("IMG/H.png"))
        self.resized = self.img.resize((205, 205), Image.ANTIALIAS)
        self.new_img = ImageTk.PhotoImage(self.resized)
        self.canv.create_image(10, 10, anchor=NW, image=self.new_img)
        self.canv.grid(row=7, column=0, rowspan=6)

        self.canvas = Canvas(self, height=100, width=100, bg="pink", relief=GROOVE, borderwidth=0.5)
        #canvas.pack()
        self.canvas.create_rectangle(100, 100, 0, 0)
        self.canvas.grid(row=1, column=0, rowspan=2)
        self.sy = self.canvas.create_text(50, 50, text="H", fill="black", font=('Helvetica 15 bold', 35))
        self.an = self.canvas.create_text(10, 12, text="1", fill="black", font=('Helvetica 15 bold', 10))
        self.am = self.canvas.create_text(17, 90, text="1.001", fill="black", font=('Helvetica 15 bold', 8))
        
        self.infoLine = tk.Label(self, text="Oxidation states -1, 1\nConfiguration 1s¹\nExpanded - \n1s¹\nEnergy levels 1\nQuantum numbers l=0, m=0, n=1", justify='left', font=10)
        self.infoLine.grid(row=3, column=0, rowspan=4)
        #setting up voice
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)

    def name(self, text): 
        self.topLabel.config(text=text)
        return(text)

    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, text): 
        self.infoLine.config(text=text)
        return(text)

    def canva(self, color, symbol, An, Am):
        self.canvas.config(bg=color)
        self.canvas.itemconfig(self.sy, text=symbol)
        self.canvas.itemconfig(self.an, text=An)
        self.canvas.itemconfig(self.am, text=Am)
        
    def canv_img(self, text):
        self.canvv = Canvas(self, width=200, height=200)
        self.img = (Image.open("IMG/{}.png".format(text)))
        self.resized = self.img.resize((205, 205), Image.ANTIALIAS)
        self.neww_img = ImageTk.PhotoImage(self.resized)
        self.canvv.create_image(10, 10, anchor=NW, image=self.neww_img)
        self.canvv.grid(row=7, column=0, rowspan=6)

    # sends command to the arduino
    def arduino(self, text):
        byte_msg = text.encode('utf-8')
        #byte_msg = bytes(text, 'utf-8')
        if text == "exit":
            try:
                nano.close()
            except:
                # comment this out or chang the statement
                # print("close but nano is not connected")
                pass
        else:
            #print(byte_msg)
            try:
                nano.write(byte_msg)
            except:
                # comment this out or change the statement
                # print("some element but nano is not defined")
                pass

    # voice description
    def voice(self, text):
        self.engine.setProperty("rate", 170)
        self.engine.say(text)
        self.engine.runAndWait()


    def clear_bloc(self):
        coloId = "white"
        #coloFg = "white"
        for key in self.s_block_c_0:
            self.s_block_c_0[key].config(bg=coloId)
            
        for key in self.s_block_c_1:
            self.s_block_c_1[key].config(bg=coloId)
            
        for key in self.d_block_c_0:
            self.d_block_c_0[key].config(bg=coloId)

        for key in self.f_block_c_0:
            self.f_block_c_0[key].config(bg=coloId)

        for key in self.d_block_c_1:
            self.d_block_c_1[key].config(bg=coloId)

        for key in self.d_block_c_2:
            self.d_block_c_2[key].config(bg=coloId)

        for key in self.d_block_c_3:
            self.d_block_c_3[key].config(bg=coloId)

        for key in self.d_block_c_4:
            self.d_block_c_4[key].config(bg=coloId)

        for key in self.d_block_c_5:
            self.d_block_c_5[key].config(bg=coloId)

        for key in self.d_block_c_6:
            self.d_block_c_6[key].config(bg=coloId)

        for key in self.d_block_c_7:
            self.d_block_c_7[key].config(bg=coloId)

        for key in self.d_block_c_8:
            self.d_block_c_8[key].config(bg=coloId)

        for key in self.d_block_c_9:
            self.d_block_c_9[key].config(bg=coloId)

        for key in self.p_block_c_0:
            self.p_block_c_0[key].config(bg=coloId)

        for key in self.p_block_c_1:
            self.p_block_c_1[key].config(bg=coloId)

        for key in self.p_block_c_2:
            self.p_block_c_2[key].config(bg=coloId)

        for key in self.p_block_c_3:
            self.p_block_c_3[key].config(bg=coloId)

        for key in self.p_block_c_4:
            self.p_block_c_4[key].config(bg=coloId)

        for key in self.s_block_c_2:
            self.s_block_c_2[key].config(bg=coloId)

        for key in self.p_block_c_5:
            self.p_block_c_5[key].config(bg=coloId)

        for key in self.f_block_c_2:
            self.f_block_c_2[key].config(bg=coloId)

        for key in self.f_block_c_3:
            self.f_block_c_3[key].config(bg=coloId)

        for key in self.d_block_c_20:
            self.d_block_c_20[key].config(bg=coloId)

        for key in self.d_block_c_21:
            self.d_block_c_21[key].config(bg=coloId)

    
    def all_block(self):
        colos = "pink"
        colop = "Aquamarine"
        colod = "light goldenrod"
        colof = "Teal"
        for key in self.s_block_c_0:
            self.s_block_c_0[key].config(bg=colos)
            
        for key in self.s_block_c_1:
            self.s_block_c_1[key].config(bg=colos)
            
        for key in self.d_block_c_0:
            self.d_block_c_0[key].config(bg=colod)

        for key in self.f_block_c_0:
            self.f_block_c_0[key].config(bg=colof)

        for key in self.d_block_c_1:
            self.d_block_c_1[key].config(bg=colod)

        for key in self.d_block_c_2:
            self.d_block_c_2[key].config(bg=colod)

        for key in self.d_block_c_3:
            self.d_block_c_3[key].config(bg=colod)

        for key in self.d_block_c_4:
            self.d_block_c_4[key].config(bg=colod)

        for key in self.d_block_c_5:
            self.d_block_c_5[key].config(bg=colod)

        for key in self.d_block_c_6:
            self.d_block_c_6[key].config(bg=colod)

        for key in self.d_block_c_7:
            self.d_block_c_7[key].config(bg=colod)

        for key in self.d_block_c_8:
            self.d_block_c_8[key].config(bg=colod)

        for key in self.d_block_c_9:
            self.d_block_c_9[key].config(bg=colod)

        for key in self.p_block_c_0:
            self.p_block_c_0[key].config(bg=colop)

        for key in self.p_block_c_1:
            self.p_block_c_1[key].config(bg=colop)

        for key in self.p_block_c_2:
            self.p_block_c_2[key].config(bg=colop)

        for key in self.p_block_c_3:
            self.p_block_c_3[key].config(bg=colop)

        for key in self.p_block_c_4:
            self.p_block_c_4[key].config(bg=colop)

        for key in self.s_block_c_2:
            self.s_block_c_2[key].config(bg=colos)

        for key in self.p_block_c_5:
            self.p_block_c_5[key].config(bg=colop)

        for key in self.f_block_c_2:
            self.f_block_c_2[key].config(bg=colof)

        for key in self.f_block_c_3:
            self.f_block_c_3[key].config(bg=colof)

        for key in self.d_block_c_20:
            self.d_block_c_20[key].config(bg=colod)

        for key in self.d_block_c_21:
            self.d_block_c_21[key].config(bg=colod)
        
 
    # S block
    def s_block(self):
        self.clear_bloc()
        colos = "pink"
        for key in self.s_block_c_0:
            self.s_block_c_0[key].config(bg=colos)
            
        for key in self.s_block_c_1:
            self.s_block_c_1[key].config(bg=colos)

        for key in self.s_block_c_2:
            self.s_block_c_2[key].config(bg=colos)

    # P block
    def p_block(self):
        self.clear_bloc()
        colop = "Aquamarine"
        for key in self.p_block_c_0:
            self.p_block_c_0[key].config(bg=colop)

        for key in self.p_block_c_1:
            self.p_block_c_1[key].config(bg=colop)

        for key in self.p_block_c_2:
            self.p_block_c_2[key].config(bg=colop)

        for key in self.p_block_c_3:
            self.p_block_c_3[key].config(bg=colop)

        for key in self.p_block_c_4:
            self.p_block_c_4[key].config(bg=colop)
            
        for key in self.p_block_c_5:
            self.p_block_c_5[key].config(bg=colop)

    # D block
    def d_block(self):
        self.clear_bloc()
        colod = "light goldenrod"
        for key in self.d_block_c_0:
            self.d_block_c_0[key].config(bg=colod)
            
        for key in self.d_block_c_1:
            self.d_block_c_1[key].config(bg=colod)

        for key in self.d_block_c_2:
            self.d_block_c_2[key].config(bg=colod)

        for key in self.d_block_c_3:
            self.d_block_c_3[key].config(bg=colod)

        for key in self.d_block_c_4:
            self.d_block_c_4[key].config(bg=colod)

        for key in self.d_block_c_5:
            self.d_block_c_5[key].config(bg=colod)

        for key in self.d_block_c_6:
            self.d_block_c_6[key].config(bg=colod)

        for key in self.d_block_c_7:
            self.d_block_c_7[key].config(bg=colod)

        for key in self.d_block_c_8:
            self.d_block_c_8[key].config(bg=colod)

        for key in self.d_block_c_9:
            self.d_block_c_9[key].config(bg=colod)

        for key in self.d_block_c_20:
            self.d_block_c_20[key].config(bg=colod)

        for key in self.d_block_c_21:
            self.d_block_c_21[key].config(bg=colod)

    # F block
    def f_block(self):
        self.clear_bloc()
        colof = "Teal"
        for key in self.f_block_c_0:
            self.f_block_c_0[key].config(bg=colof)
            
        for key in self.f_block_c_2:
            self.f_block_c_2[key].config(bg=colof)

        for key in self.f_block_c_3:
            self.f_block_c_3[key].config(bg=colof)

        
        
# This class is going to be used to make compounds like on Ptable       
class Third(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.topLabel = tk.Label(self, text="Compounds", font=('Helvetica 15 bold', 15))
        self.topLabel.grid(row=0, column=0, columnspan=18)
        """=======================================blocks==================================="""
    def name(self, text): 
        self.topLabel.config(text=text)
        return(text)

    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, text): 
        self.infoLine.config(text=text)
        return(text)

    # sends command to the arduino
    def arduino(self, text):
        byte_msg = text.encode('utf-8')
        #byte_msg = bytes(text, 'utf-8')
        if text == "exit":
            try:
                nano.close()
            except:
                # comment this out or chang the statement
                # print("close but nano is not connected")
                pass
        else:
            #print(byte_msg)
            try:
                nano.write(byte_msg)
            except:
                # comment this out or change the statement
                # print("some element but nano is not defined")
                pass

    # voice description
    def voice(self, text):
        self.engine.setProperty("rate", 170)
        self.engine.say(text)
        self.engine.runAndWait()

# This class is going to be used to define buttons like for basicCompounds, composition, Discovery, Animations and most probaly
#  will not contain periodic table for the sake of arduino

class Four(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.topLabel = tk.Label(self, text="Others", font=('Helvetica 15 bold', 15), justify="center")
        self.topLabel.grid(row=0, column=0, columnspan=10)
        """=======================================Basic comounds======================================="""
        basic_commpounds = [
            ('Glucose', 'Glucose C6H12O6', 'C6H12O6'),
            ('Water', 'Water H2O', 'H2O'),
            ('Carbon dioxide', 'Carbon dioxide CO2', 'CO2'),
            ('Baking soda', 'Baking soda NaHO3', 'NaHO3'),
            ('Sodium Chloride', 'Sodium Chloride NaCl', 'NaCl'),
            ('Silicon Dioxide', 'Silicon Dioxide SiO2', 'SiO2'),
            ('Hydrochloric Acid', 'Hydrochloric Acid HCl', 'HCl'),
            ('Lithium Hydroxide', 'Lithium Hydroxide LiOH', 'LiOH'),
            ('Methane', 'Methane CH4', 'CH4'),
            ('Ammonia', 'Ammonia NH3', 'NH3'),
            ('Sulfuric Acid', 'Sulfuric Acid H2S04', 'H2S04'),
            ('Citric Acid', 'Citric Acid C6H8O7', 'C6H8O7'),
            ('Hydrogen Peroxide', 'Hydrogen Peroxide H2O2', 'H2O2'),
            ('Acetic Acid', 'Acetic Acid C2H4O2', 'C2H4O2'),
            ('Calcium Carbonate', 'Calcium Carbonate CaCO3', 'CaCO3'),
            ('Iron Oxide', 'Iron Oxide Fe2O3', 'Fe2O3')]
        r = 1
        c = 4
        self.basic_commpounds_c={}
        for b in basic_commpounds: 
            self.basic_commpounds_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=14,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="gray",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.voice(text[0])])
            self.basic_commpounds_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2

        """=======================================Compositions======================================="""
        composition = [
            ('Human', 'Elements Composition\n in human body', 'human', 'Elements Composition in human body'),
            ('Plant', 'Elements Composition\n in plants', 'plant', 'Elements Composition in plants'),
            ('Solar', 'Elements Composition\n in the solar system', 'solar', 'Elements Composition in the solar system'),
            ('Atmosphere', 'Elements Composition\n in the Atmosphere', 'atm', 'Elements Composition in the Atmosphere'),
            ('Earth Crust', 'Elements Composition\n in the earth crust', 'crust', 'Elements Composition in the earth crust'),
            ('Ocean', 'Elements Composition\n in the Ocean', 'ocean', 'Elements Composition in the Ocean'),
            ('Universe', 'Elements Composition\n in the universe', 'universe', 'Elements Composition in the universe')]
        r = 1
        c = 8
        self.composition_c={}
        for b in composition: 
            self.composition_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=14,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="gray",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2]), self.voice(text[3])])
            self.composition_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2
        """=======================================Discovered======================================="""
        Discovery = [
            ('Early', 'Early discovered elements'),
            ('Eighteen', 'Elements discovered in Eighteen century'),
            ('Nineteen', 'Elements discovered in Nineteen century'),
            ('Twenty', 'Elements discovered in Twenty century'),
            ('Twenty one', 'Elements discovered in Twenty one century')]
        r = 1
        c = 10
        self.Discovery_c={}
        for b in Discovery: 
            self.Discovery_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=14,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="gray",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[0]), self.voice(text[1])])
            self.Discovery_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2

        """=======================================Animation======================================="""
        Animation = [
            ('TimeLine', 'Timeline Animation', 'Timeline'),
            ('Group Animation', 'Group Animation', 'columndance'),
            ('Column Animation', 'Column Animation', 'groupdance')]
        r = 1
        c = 12
        self.Animation_c={}
        for b in Animation: 
            self.Animation_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=14,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="gray",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[1]), self.arduino(text[2])])
            self.Animation_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2



        self.infoLine = tk.Label(self, text="Basic commpounds", justify='left', font=10)
        self.infoLine.grid(row=2, column=0, rowspan=2)
        #setting up voice
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)



    def name(self, text): 
        self.topLabel.config(text=text)
        return(text)

    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, text): 
        self.infoLine.config(text=text)
        return(text)

    # sends command to the arduino
    def arduino(self, text):
        byte_msg = text.encode('utf-8')
        #byte_msg = bytes(text, 'utf-8')
        if text == "exit":
            try:
                nano.close()
            except:
                # comment this out or chang the statement
                # print("close but nano is not connected")
                pass
        else:
            #print(byte_msg)
            try:
                nano.write(byte_msg)
            except:
                # comment this out or change the statement
                # print("some element but nano is not defined")
                pass

    # voice description
    def voice(self, text):
        self.engine.setProperty("rate", 170)
        self.engine.say(text)
        self.engine.runAndWait()



# Creates an instance of 'app' class
def main():
    root = tk.Tk()
    root.resizable(True, True)
    menu_bar = Menu(root)
    root.config(menu=menu_bar)
    help_menu = Menu(menu_bar, tearoff=0)
    # the buttons are not working and loading when importing undo that by __name__ == "__main__"
    help_menu.add_command(label="About", command=aboout)
    help_menu.add_command(label="Help", command=hellp)
    setting_menu = Menu(menu_bar, tearoff=0)
    setting_menu.add_command(label="Setting", command=settting)
    menu_bar.add_cascade(label="Setting", menu=setting_menu)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    tabControl = ttk.Notebook(root)

    #a = App(root)
    a = App(root)
    tabControl.add(a, text="Properties")

    b = Second(root)
    tabControl.add(b, text="Electrons")

    c = Third(root)
    tabControl.add(c, text="Compounds")

    d = Four(root)
    tabControl.add(d, text="Others")

    tabControl.pack(expand=1, fill="both")

    root.mainloop()


def hellp():
    # function to give help
    hell = tk.Tk()
    hell.title("Help")
    #hell.geometry("250x150")
    hell.resizable(False, False)
    l = ttk.Label(hell, text="Help", font=("Courier", 14))
    x = ttk.Label(hell, text="To control the arduino using this software\nfirst connect your arduino usng the USB\nthen configure the port and baud rate in the setting\nAnd enjoy the show")
    x.config(font=('Helvetica 15 bold', 13))
    b = tk.Button(hell, text="Exit",
               command = hell.destroy)
    l.pack()
    x.pack()
    b.pack()
    pass

def aboout():
    aboo = tk.Tk()
    aboo.title("About")
    # description on about
    aboo.resizable(False, False)
    l = ttk.Label(aboo, text="About", font=("Courier", 14))
    x = ttk.Label(aboo, text="This GUI is developed to control interactive periodic table\nTo contact me \nemail: eyasuhailegbr@gmail.com")
    x.config(font=('Helvetica 15 bold', 13))
    b = tk.Button(aboo, text="Exit",
               command = aboo.destroy)
    l.pack()
    x.pack()
    b.pack()
    pass

def settting():
    # description on setting
    settt = tk.Tk()
    settt.title("Setting")
    settt.resizable(False, False)
    
    mig = ttk.LabelFrame(settt, text="Setting")
    mig.grid(column=0, row=0, padx=9, pady=9, sticky='W')
    baud_text = ttk.Label(mig, text="Sellect Baud rate")
    baud_text.grid(column=0, row=0)
    port_text = ttk.Label(mig, text="Sellect Port")
    port_text.grid(column=1, row=0)
    voice_text = ttk.Label(mig, text="Sellect Voice")
    voice_text.grid(column=2, row=0)

    baud = tk.StringVar()
    nm = ttk.Combobox(mig, width=19, textvariable=baud, state='readonly')
    nm["values"] = ("9600 baud", "19200 baud", "38400 baud", "57600 baud")
    nm.grid(column=0, row=1)
    nm.current(0)
    
    port = tk.StringVar()
    num = ttk.Combobox(mig, width=19, textvariable=port, state='readonly')
    num["values"] = ("COM3", "COM4", "COM5", "COM8", "COM9")
    num.grid(column=1, row=1)
    num.current(3)

    voice = tk.StringVar()
    vo = ttk.Combobox(mig, width=19, textvariable=voice, state='readonly')
    vo["values"] = ("Male", "Female")
    vo.grid(column=2, row=1)
    vo.current(0)    

    def settup():
        # when the configured buttons are sent
        pass

    act = ttk.Button(mig, text="Settup", command=settup)
    act.grid(column=1, row=3, sticky=tk.W, columnspan=3)


# runs main function
if __name__ == "__main__":
    main()
