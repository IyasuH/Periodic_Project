#!/usr/bin/python3
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import PhotoImage, NW
from tkinter import messagebox as msg
from tkinter import ttk, Canvas, Menu, Label, Frame, Text, Frame
from tkinter import PhotoImage, Scrollbar, Listbox, LEFT, Y, END, BOTH, X
from tkinter import messagebox as msg
from tkinter import FLAT, RAISED, SUNKEN, GROOVE, RIDGE, DISABLED, NORMAL
import serial
import serial.tools.list_ports
import pyttsx3
import hashlib
from pyttsx3.drivers import sapi5
import re
import time
import sys
import turtle

#I hope that the next version of this is going to be built over customtkinter with better GUI
#import customtkinter

PPort = 'COM3'
BBaud = 9600

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'COMs' in p.description
    ]

if not arduino_ports:
    try:
        nano = serial.Serial(PPort, BBaud, timeout=1)
    except:
        rot = tk.Tk()
        rot.overrideredirect(1)
        rot.withdraw()
        msg.showwarning(title="SERIAL COMMUNICATION", message="YOU DIDN'T CONNECT THE ARDUINO WITH THE PC PLEASE CONNECT THE ARDUINO")
        rot.destroy()
else:
    nano = serial.Serial(arduino_ports[0], BBaud, timeout=1)

"""try:
    nano = serial.Serial(PPort, BBaud, timeout=1)
except:
    rot = tk.Tk()
    rot.overrideredirect(1)
    rot.withdraw()
    msg.showwarning(title="SERIAL COMMUNICATION", message="EITHER YOU DIDN'T CONNECT THE ARDUINO WITH THE PC OR THE PORT YOU CHOICE IS NOT CORRECT, PLEASE SETUP THE PORT IN THE SETTING OR CONNECT THE ARDUINO")
    rot.destroy()"""

# voice info
engine = pyttsx3.init()
voices = engine.getProperty("voices")
voicce = 1
engine.setProperty("voice", voices[voicce].id)
engine.setProperty("rate", 170)

#customtkinter.set_appearance_mode("Dark")
bacG = "lightcyan1"
bacG_2 = "azure2"
bacG_3 = "snow2"
bacG_4 = "honeydew1"

class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # this is about puting back ground image
        """bgA = PhotoImage(file = "IMG/black.png")
        lab = Label(self, image=bgA)
        lab.image = bgA
        lab.place(x=0, y=0, relwidth=1, relheight=1)"""
        self.winfo_toplevel().title("Periodic Table")
        self.topLabel = tk.Label(self, text="Click any element", font=('Helvetica 15 bold', 15), bg=bacG)
        self.topLabel.grid(row=0, column=0)

        # numbers for the series and the groups
        # Row numbers
        r1 = Label(self, text="1", font=7, bg=bacG)
        r1.grid(column=1, row=3)

        r2 = Label(self, text="2", font=7, bg=bacG)
        r2.grid(column=1, row=4)

        r3 = Label(self, text="3", font=7, bg=bacG)
        r3.grid(column=1, row=5)

        r4 = Label(self, text="4", font=7, bg=bacG)
        r4.grid(column=1, row=6)

        r5 = Label(self, text="5", font=7, bg=bacG)
        r5.grid(column=1, row=7)

        r6 = Label(self, text="6", font=7, bg=bacG)
        r6.grid(column=1, row=8)

        r7 = Label(self, text="7", font=7, bg=bacG)
        r7.grid(column=1, row=9)
        #Column numbers
        c1 = Label(self, text="1", font=7, bg=bacG)
        c1.grid(column=2, row=2)

        column1_1 = [
            ('H', 'Hydrogen', 'Atomic # = 1\nAtomic Weight =1.01\nState = Gas\nCategory = Alkali Metals\nElectronegativity (Pauling Scale)=2.2\nAtomic Radius (van der Waals)=120 pm\nIonization Energy=13.598 eV\nElectron Affinity=0.754 eV\nMelting Point=13.81 K\nBoiling Point=20.28 K\nDensity=0.00008988 g/cm³\nYear Discovered=1766', '1', '1.01')]
        # create all tk.Buttons with a loop
        r = 3
        c = 2
        color1="palegreen2"
        for b in column1_1: 
            self.H = tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg=color1,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.canva(color1, text[0], text[3], text[4]), self.voice(text[1])])
            self.H.grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column1_2 = [
            ('Li', 'Lithium', 'Atomic # = 3\nAtomic Weight = 6.94\nState = Solid\nCategory = Alkali Metals\nElectronegativity (Pauling Scale)=0.98\nAtomic Radius (van der Waals)182 pm\nIonization Energy=5.392 eV\nElectron Affinity=0.618 eV\nMelting Point453.65 K\nBoiling Point=1615 K\nDensity=0.534 g/cm³\nYear Discovered=1817', '3', '6.94'),
            ('Na', 'Sodium', 'Atomic # = 11\nAtomic Weight = 22.99\nState = Solid\nCategory = Alkali Metals\nElectronegativity (Pauling Scale)=0.93\nAtomic Radius (van der Waals)=227 pm\nIonization Energy=5.139 eV\nElectron Affinity=0.548 eV\nMelting Point=370.95 K\nBoiling Point=1156 K\nDensity=0.97 g/cm³\nYear Discovered=1807', '11', '22.99'),
            ('K', 'Potassium', 'Atomic # = 19\nAtomic Weight = 39.10\nState = Solid\nCategory = Alkali Metals\nElectronegativity (Pauling Scale)=0.82\nAtomic Radius (van der Waals)=275 pm\nIonization Energy=4.341 eV\nElectron Affinity=0.501 eV\nMelting Point=336.53 K\nBoiling Point=1032 K\nDensity=0.89 g/cm³\nYear Discovered=1807', '19', '39.10'),
            ('Rb', 'Rubidium', 'Atomic # = 37\nAtomic Weight = 85.47\nState = Solid\nCategory = Alkali Metals\nElectronegativity (Pauling Scale)=0.82\nAtomic Radius (van der Waals)=303 pm\nIonization Energy=4.177 eV\nElectron Affinity=0.468 eV\nMelting Point=312.46 K\nBoiling Point=961 K\nDensity=1.53 g/cm³\nYear Discovered=1861', '37', '85.41'),
            ('Cs', 'Cesium', 'Atomic # = 55\nAtomic Weight = 132.91\nState = Solid\nCategory = Alkali Metals\nElectronegativity (Pauling Scale)=0.79\nAtomic Radius (van der Waals)=343 pm\nIonization Energy=3.894 eV\nElectron Affinity=0.472 eV\nMelting Point=301.59 K\nBoiling Point=944 K\nDensity=1.93 g/cm³\nYear Discovered=1860', '55', '132.91'),
            ('Fr', 'Francium', 'Atomic # = 87\nAtomic Weight = 223.00\nState = Solid\nCategory = Alkali Metals\nElectronegativity (Pauling Scale)=0.7\nAtomic Radius (van der Waals)=348 pm\nIonization Energy=3.9 eV\nElectron Affinity=0.47 eV\nMelting Point=300 K\nYear Discovered=1939', '87', '223')]
        # create all tk.Buttons with a loop
        r = 4
        c = 2
        color2="light goldenrod"
        self.alkali_c={}
        for b in column1_2: 
            self.alkali_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      bg=color2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color2, text[0], text[3], text[4])])
            self.alkali_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c2 = Label(self, text="2", font=7, bg=bacG)
        c2.grid(column=3, row=3)
        
        column2 = [
            ('Be', 'Beryllium', 'Atomic # = 4\nAtomic Weight = 9.01\nState = Solid\nCategory = Alkaline Earth Metals\nElectronegativity (Pauling Scale)=1.57\nAtomic Radius (van der Waals)=153 pm\nIonization Energy=9.323 eV\nMelting Point=1560 K\nBoiling Point=2744 K\nDensity=1.85 g/cm³\nYear Discovered=1798', '4', '9.01'),
            ('Mg', 'Magnesium', 'Atomic # = 12\nAtomic Weight = 24.31\nState = Solid\nCategory = Alkaline Earth Metal\nElectronegativity (Pauling Scale)=1.31\nAtomic Radius (van der Waals)=173 pm\nIonization Energy=7.646 eV\nMelting Point=923 K\nBoiling Point=1363 K\nDensity=1.74 g/cm³\nYear Discovered=1808', '12', '24.31'),
            ('Ca', 'Calcium', 'Atomic # = 20\nAtomic Weight = 40.08\nState = Solid\nCategory = Alkaline Earth Metals\nElectronegativity (Pauling Scale)=1\nAtomic Radius (van der Waals)=231 pm\nIonization Energy=6.113 eV\nMelting Point=1115 K\nBoiling Point=1757 K\nDensity=1.54 g/cm³\nYear Discovered=Ancient', '20', '40.08'),
            ('Sr', 'Strontium', 'Atomic # = 38\nAtomic Weight = 87.62\nState = Solid\nCategory = Alkaline Earth Metal\nElectronegativity (Pauling Scale)=0.95\nAtomic Radius (van der Waals)=249 pm\nIonization Energy=5.695 eV\nMelting Point=1050 K\nBoiling Point=1655 K\nDensity=2.64 g/cm³\nYear Discovered=1790', '38', '87.62'),
            ('Ba', 'Barium', 'Atomic # = 56\nAtomic Weight = 137.33\nState = Solid\nCategory = Alkaline Earth Metals\nElectronegativity (Pauling Scale)=0.89\nAtomic Radius (van der Waals)=268 pm\nIonization Energy=5.212 eV\nMelting Point=1000 K\nBoiling Point=2170 K\nDensity=3.62 g/cm³\nYear Discovered=1808', '56', '137.33'),
            ('Ra', 'Radium', 'Atomic # = 88\nAtomic Weight = 226.03\nState = Solid\nCategory = Alkaline Earth Metals\nElectronegativity (Pauling Scale)=0.9\nAtomic Radius (van der Waals)=283 pm\nIonization Energy=5.279 eV\nMelting Point=973 K\nBoiling Point=1413 K\nDensity=5 g/cm³\nYear Discovered=1898', '88', '226.03')]
        r = 4
        c = 3
        self.alkaline_c={}
        color3="bisque4"
        for b in column2:
            self.alkaline_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color3,
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color3, text[0], text[3], text[4])])
            self.alkaline_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
        #print(self.alkaline_c)
        c3 = Label(self, text="3", font=7, bg=bacG)
        c3.grid(column=4, row=5)
        
        column3 = [
            ('Sc', 'Scandium', 'Atomic # = 21\nAtomic Weight = 44.96\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.36\nAtomic Radius (van der Waals)=211 pm\nIonization Energy=6.561 eV\nElectron Affinity=0.188 eV\nMelting Point=1814 K\nBoiling Point=3109 K\nDensity=2.99 g/cm³\nYear Discovered=1879', '21', '44.96'),
            ('Y', 'Yttrium', 'Atomic # = 39\nAtomic Weight = 88.91\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.22\nAtomic Radius (van der Waals)=219 pm\nIonization Energy=6.217 eV\nElectron Affinity=0.307 eV\nMelting Point=1795 K\nBoiling Point=3618 K\nDensity=4.47 g/cm³\nYear Discovered=1794', '39', '88.91')]
        r = 6
        c = 4
        self.trans_c3={}
        color4="tan1"
        for b in column3: 
            self.trans_c3[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color4,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color4, text[0], text[3], text[4])])
            self.trans_c3[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column3_1 = [
            ('La', 'Lanthanum', 'Atomic # = 57\nAtomic Weight = 138.91\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.1\nAtomic Radius (van der Waals)=240 pm\nIonization Energy=5.577 eV\nElectron Affinity=0.5 eV\nMelting Point=1191 K\nBoiling Point=3737 K\nDensity=6.15 g/cm³\nYear Discovered=1839', '57', '138.91')]
        r = 8
        c = 4
        self.La_c3_1={}
        color5="lightpink"
        for b in column3_1: 
            self.La_c3_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color5,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color5, text[0], text[3], text[4])])
            self.La_c3_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column3_2 = [
            ('Ac', 'Actinium', 'Atomic # = 89\nAtomic Weight = 227.03\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.1\nAtomic Radius (van der Waals)=260 pm\nIonization Energy=5.17 eV\nMelting Point=1324 K\nBoiling Point=3471 K\nDensity=10.07 g/cm³\nYear Discovered=1899', '89', '227.03')]
        r = 9
        c = 4
        self.Ac_c3_2={}
        color6="orchid2"
        for b in column3_2: 
            self.Ac_c3_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color6,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color6, text[0], text[3], text[4])])
            self.Ac_c3_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c4 = Label(self, text="4", font=7, bg=bacG)
        c4.grid(column=5, row=5)
        
        column4 = [
            ('Ti', 'Titanium', 'Atomic # = 22\nAtomic Weight = 47.90\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)1.54\nAtomic Radius (van der Waals)=187 pm\nIonization Energy=6.828 eV\nElectron Affinity=0.079 eV\nMelting Point=1941 K\nBoiling Point=3560 K\nDensity=4.5 g/cm³\nYear Discovered1791', '22', '47.90'),
            ('Zr', 'Zirconium', 'Atomic # = 40\nAtomic Weight = 91.22\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.33\nAtomic Radius (van der Waals)=186 pm\nIonization Energy=6.634 eV\nElectron Affinity=0.426 eV\nMelting Point=2128 K\nBoiling Point=4682 K\nDensity=6.52 g/cm³\nYear Discovered=1789', '40', '91.22'),
            ('Hf', 'Hanium', 'Atomic # = 72\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nAtomic Radius (van der Waals)=212 pm\nIonization Energy=6.825 eV\nMelting Point=2506 K\nBoiling Point=4876 K\nDensity=13.3 g/cm³\nYear Discovered=1923', '72', '178.49'),
            ('Rf', 'Rutherfordium', 'Atomic # = 104\nAtomic Weight = 261.00\nState = Synthetic\nCategory = Trans Metal\nYear Discovered=1964', '104', '261.00')]
        r = 6
        c = 5
        self.trans_c4={}
        color7="tan1"
        for b in column4: 
            self.trans_c4[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c4[b[0]].grid(row=r, column=c)
            r += 1
            if r > 12: 
                r = 1
                c += 1
                
        c5 = Label(self, text="5", font=7, bg=bacG)
        c5.grid(column=6, row=5)
        
        column5 = [
            ('V', 'Vanadium', 'Atomic # = 23\nAtomic Weight = 50.94\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.63\nAtomic Radius (van der Waals)=179 pm\nIonization Energy=6.746 eV\nElectron Affinity=0.525 eV\nMelting Point=2183 K\nBoiling Point=3680 K\nDensity=6.0 g/cm³\nYear Discovered=1801', '23', '50.94'),
            ('Nb', 'Niobium', 'Atomic # = 41\nAtomic Weight = 92.91\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.6\nAtomic Radius (van der Waals)=207 pm\nIonization Energy=6.759 eV\nElectron Affinity=0.893 eV\nMelting Point=2750 K\nBoiling Point=5017 K\nDensity=8.57 g/cm³\nYear Discovered=1801', '41', '92.91'),
            ('Ta', 'Tantalum', 'Atomic # = 73\nAtomic Weight = 180.95\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.5\nAtomic Radius (van der Waals)=217 pm\nIonization Energy=7.89 eV\nElectron Affinity=0.322 eV\nMelting Point=3290 K\nBoiling Point=5731 K\nDensity=16.4 g/cm³\nYear Discovered=1802', '73', '180.95'),
            ('Db', 'Dubnium', 'Atomic # = 105\nAtomic Weight = 268.00\nState = Synthetic\nCategory = Trans Metals\nYear Discovered=1967', '105', '262.00')]
        r = 6
        c = 6
        self.trans_c5={}
        for b in column5: 
            self.trans_c5[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c5[b[0]].grid(row=r, column=c)
            r += 1
            if r > 12: 
                r = 1
                c += 1
                
        c6 = Label(self, text="6", font=7, bg=bacG)
        c6.grid(column=7, row=5)
        
        column6 = [
            ('Cr', 'Chromium', 'Atomic # = 24\nAtomic Weight = 51.99\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.66\nAtomic Radius (van der Waals)=189 pm\nIonization Energy=6.767 eV\nElectron Affinity=0.666 eV\nMelting Point=2180 K\nBoiling Point=2944 K\nDensity=7.15 g/cm³\nYear Discovered=1797', '24', '51.99'),
            ('Mo', 'Molybdenum', 'Atomic # = 42\nAtomic Weight = 95.94\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.16\nAtomic Radius (van der Waals)=209 pm\nIonization Energy=7.092 eV\nElectron Affinity=0.746 eV\nMelting Point=2896 K\nBoiling Point=4912 K\nDensity=10.2 g/cm³\nYear Discovered=1778', '42', '95.94'),
            ('W', 'Tungsten', 'Atomic # = 74\nAtomic Weight = 183.85\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.36\nAtomic Radius (van der Waals)=210 pm\nIonization Energy=7.98 eV\nElectron Affinity=0.815 eV\nMelting Point=3695 K\nBoiling Point=5828 K\nDensity=19.3 g/cm³\nYear Discovered=1783', '74', '183.85'),
            ('Sg', 'Seaborgium', 'Atomic # = 106\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Trans Metals\nYear Discovered=1974', '106', '266.00')]
        r = 6
        c = 7
        self.trans_c6={}
        for b in column6: 
            self.trans_c6[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c6[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c7 = Label(self, text="7", font=7, bg=bacG)
        c7.grid(column=8, row=5)
        
        column7 = [
            ('Mn', 'Manganese', 'Atomic # = 25\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.55\nAtomic Radius (van der Waals)=197 pm\nIonization Energy=7.434 eV\nMelting Point=1519 K\nBoiling Point=2334 K\nDensity=7.3 g/cm³\nYear Discovered=1774', '25', '178.49'),
            ('Tc', 'Technetium', 'Atomic # = 43\nAtomic Weight = 178.49\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.9\nAtomic Radius (van der Waals)=209 pm\nIonization Energy=7.28 eV\nElectron Affinity=0.55 eV\nMelting Point=2430 K\nBoiling Point=4538 K\nDensity=11 g/cm³\nYear Discovered=1937', '43', '178.49'),
            ('Re', 'Rhenium', 'Atomic # = 75\nAtomic Weight = 178.49\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.9\nAtomic Radius (van der Waals)=217 pm\nIonization Energy=7.88 eV\nElectron Affinity=0.15 eV\nMelting Point=3459 K\nBoiling Point=5869 K\nDensity=20.8 g/cm³\nYear Discovered=1925', '75', '178.49'),
            ('Bh', 'Bohrium', 'Atomic # = 107\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Trans Metals\nYear Discovered=1976', '107', '262.00')]
        r = 6
        c = 8
        self.trans_c7={}
        for b in column7: 
            self.trans_c7[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c7[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        c8 = Label(self, text="8", font=7, bg=bacG)
        c8.grid(column=9, row=5)
        
        column8 = [
            ('Fe', 'Iron', 'Atomic # = 26\nAtomic Weight = 55.85\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.83\nAtomic Radius (van der Waals)=194 pm\nIonization Energy=7.902 eV\nElectron Affinity=0.163 eV\nMelting Point=1811 K\nBoiling Point=3134 K\nDensity=7.874 g/cm³\nYear Discovered=Ancient', '26', '55.85'),
            ('Ru', 'Ruthenium', 'Atomic # = 44\nAtomic Weight = 101.07\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.2\nAtomic Radius (van der Waals)=207 pm\nIonization Energy=7.361 eV\nElectron Affinity=1.05 eV\nMelting Point=2607 K\nBoiling Point=4423 K\nDensity=12.1 g/cm³\nYear Discovered=1827', '44', '101.07'),
            ('Os', 'Osmium', 'Atomic # = 76\nAtomic Weight = 190.20\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.2\nAtomic Radius (van der Waals)=216 pm\nIonization Energy=8.7 eV\nElectron Affinity=1.1 eV\nMelting Point=3306 K\nBoiling Point=5285 K\nDensity=22.57 g/cm³\nYear Discovered=1803', '76', '190.20'),
            ('Hs', 'Hassium', 'Atomic # = 108\nAtomic Weight = 265.00\nState = Synthetic\nCategory = Trans Metals\nYear Discovered=1984', '108', '265.00')]
        r = 6
        c = 9
        self.trans_c8={}
        for b in column8: 
            self.trans_c8[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c8[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        c9 = Label(self, text="9", font=7, bg=bacG)
        c9.grid(column=10, row=5)
        
        column9 = [
            ('Co', 'Cobalt', 'Atomic # = 27\nAtomic Weight = 58.93\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.88\nAtomic Radius (van der Waals)=192 pm\nIonization Energy=7.881 eV\nElectron Affinity=0.661 eV\nMelting Point=1768 K\nBoiling Point=3200 K\nDensity=8.86 g/cm³\nYear Discovered=1735', '27', '58.93'),
            ('Rh', 'Rhodium', 'Atomic # = 45\nAtomic Weight = 102.91\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.28\nAtomic Radius (van der Waals)=195 pm\nIonization Energy=7.459 eV\nElectron Affinity=1.137 eV\nMelting Point=2237 K\nBoiling Point=3968 K\nDensity=12.4 g/cm³\nYear Discovered=1803', '45', '102.91'),
            ('Ir', 'Iridium', 'Atomic # = 77\nAtomic Weight = 192.22\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.2\nAtomic Radius (van der Waals)=202 pm\nIonization Energy=9.1 eV\nElectron Affinity=1.565 eV\nMelting Point=2719 K\nBoiling Point=4701 K\nDensity=22.42 g/cm³\nYear Discovered=1803', '77', '192.22')]
        r = 6
        c = 10
        self.trans_c9={}
        for b in column9: 
            self.trans_c9[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c9[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column9_0 = [
            ('Mt', 'Meitnerium', 'Atomic # = 109\nAtomic Weight = 266.00\nState = Synthetic\nCategory = Trans Metals\nYear Discovered=1982', '109', '266.00')]
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
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c9_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
        
        c10 = Label(self, text="10", font=7, bg=bacG)
        c10.grid(column=11, row=5)
        
        column10 = [
            ('Ni', 'Nickle', 'Atomic # = 28\nAtomic Weight = 58.70\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.91\nAtomic Radius (van der Waals)=163 pm\nIonization Energy=7.640 eV\nElectron Affinity=1.156 eV\nMelting Point=1728 K\nBoiling Point=3186 K\nDensity=8.912 g/cm³\nYear Discovered=1751', '28', '58.70'),
            ('Pd', 'Palladium', 'Atomic # = 46\nAtomic Weight = 106.40\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.2\nAtomic Radius (van der Waals)=202 pm\nIonization Energy=8.337 eV\nElectron Affinity=0.557 eV\nMelting Point=1828.05 K\nBoiling Point=3236 K\nDensity=12.0 g/cm³\nYear Discovered=1803', '46', '106.40'),
            ('Pt', 'Platinum', 'Atomic # = 78\nAtomic Weight = 195.09\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.28\nAtomic Radius (van der Waals)=209 pm\nIonization Energy=9 eV\nElectron Affinity=2.128 eV\nMelting Point=2041.55 K\nBoiling Point=4098 K\nDensity=21.46 g/cm³\nYear Discovered=1735', '78', '195.09')]
        r = 6
        c = 11
        self.trans_c10={}
        for b in column10: 
            self.trans_c10[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c10[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column10_0 = [
            ('Ds', 'Darmstadtium', 'Atomic # = 110\nAtomic Weight = 281\nState = Unknown\nCatagory = Trans Metals\nYear Discovered=1994', '110', '281')]
        r = 9
        c = 11
        self.trans_c10_0={}
        for b in column10_0: 
            self.trans_c10_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c10_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        
        c11 = Label(self, text="11", font=7, bg=bacG)
        c11.grid(column=12, row=5)
        
        column11 = [
            ('Cu', 'Copper', 'Atomic # = 29\nAtomic Weight = 63.55\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.9\nAtomic Radius (van der Waals)=140 pm\nIonization Energy=7.726 eV\nElectron Affinity=1.228 eV\nMelting Point=1357.77 K\nBoiling Point=2835 K\nDensity=8.933 g/cm³\nYear Discovered=Ancient', '29', '63.55'),
            ('Ag', 'Silver', 'Atomic # = 47\nAtomic Weight = 107.97\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.93\nAtomic Radius (van der Waals)=172 pm\nIonization Energy=7.576 eV\nElectron Affinity=1.302 eV\nMelting Point=1234.93 K\nBoiling Point=2435 K\nDensity=10.501 g/cm³\nYear Discovered=Ancient', '47', '107.97'),
            ('Au', 'Gold', 'Atomic # = 79\nAtomic Weight = 196.97\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2.54\nAtomic Radius (van der Waals)=166 pm\nIonization Energy=9.226 eV\nElectron Affinity=2.309 eV\nMelting Point=1337.33 K\nBoiling Point=3129 K\nDensity=19.282 g/cm³\nYear Discovered=Ancient', '79', '196.97')]
        r = 6
        c = 12
        self.trans_c11={}
        for b in column11: 
            self.trans_c11[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c11[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                c11 = Label(self, text="11", font=7, bg=bacG)
        c11.grid(column=12, row=5)
        
        column11_0 = [
            ('Rg', 'Roentgenium', 'Atomic # = 111\nAtomic Weight = 282\nState = Unkown\nCategory = Trans Metals\nYear Discovered=1994', '111', '282')]
        r = 9
        c = 12
        self.trans_c11_0={}
        for b in column11_0: 
            self.trans_c11_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c11_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

             
        c12 = Label(self, text="12", font=7, bg=bacG)
        c12.grid(column=13, row=5)
        
        column12 = [
            ('Zn', 'Zinc', 'Atomic # = 30\nAtomic Weight = 65.37\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.65\nAtomic Radius (van der Waals)=139 pm\nIonization Energy=9.394 eV\nMelting Point=692.68 K\nBoiling Point=1180 K\nDensity=7.134 g/cm³\nYear Discovered=1746', '30', '65.37'),
            ('Cd', 'Cadmium', 'Atomic # = 48\nAtomic Weight = 112.41\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.69\nAtomic Radius (van der Waals)=158 pm\nIonization Energy=8.994 eV\nMelting Point=594.22 K\nBoiling Point=1040 K\nDensity=8.69 g/cm³\nYear Discovered=1817', '48', '112.41'),
            ('Hg', 'Mercury', 'Atomic # = 80\nAtomic Weight = 200.59\nState = Liquid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=2\nAtomic Radius (van der Waals)=209 pm\nIonization Energy=10.438 eV\nMelting Point=234.32 K\nBoiling Point=629.88 K\nDensity=13.5336 g/cm³\nYear Discovered=Ancient', '80', '200.59')]
        r = 6
        c = 13
        self.trans_c12={}
        for b in column12: 
            self.trans_c12[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color7,
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color7, text[0], text[3], text[4])])
            self.trans_c12[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                c12 = Label(self, text="12", font=7, bg=bacG)
        c12.grid(column=13, row=5)
        
        column12_0 = [
            ('Cn', 'Copernicium', 'Atomic # = 112\nAtomic Weight = 285\nState = Unkown\nCategory = Trans Metals\nYear Discovered=1996', '112', '285')]
        r = 9
        c = 13
        self.trans_c12_0={}
        for b in column12_0: 
            self.trans_c12_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.trans_c12_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c13 = Label(self, text="13", font=7, bg=bacG)
        c13.grid(column=14, row=3)
        
        column13_1 = [
            ('B', 'Boron', 'Atomic # = 5\nAtomic Weight = 10.81\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=2.04\nAtomic Radius (van der Waals)=192 pm\nIonization Energy=8.298 eV\nElectron Affinity=0.277 eV\nMelting Point=2348 K\nBoiling Point=4273 K\nDensity=2.37 g/cm³\nYear Discovered=1808', '5', '10.81')]
        r = 4
        c = 14
        color10="salmon"
        self.metalloids_c12_1={}
        for b in column13_1: 
            self.metalloids_c12_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloids_c12_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column13_2 = [
            ('Al', 'Aluminum', 'Atomic # = 13\nAtomic Weight = 26.98\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=1.61\nAtomic Radius (van der Waals)=184 pm\nIonization Energy=5.986 eV\nElectron Affinity=0.441 eV\nMelting Point=933.437 K\nBoiling Point=2792 K\nDensity=2.70 g/cm³\nYear Discovered=Ancient', '13', '26.98'),
            ('Ga', 'Gallium', 'Atomic # = 31\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=1.81\nAtomic Radius (van der Waals)=187 pm\nIonization Energy=5.999 eV\nElectron Affinity=0.3 eV\nMelting Point=302.91 K\nBoiling Point=2477 K\nDensity=5.91 g/cm³\nYear Discovered=1875', '31', '69.72'),
            ('In', 'Indium', 'Atomic # = 49\nAtomic Weight = 69.72\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=1.78\nAtomic Radius (van der Waals)=193 pm\nIonization Energy=5.786 eV\nElectron Affinity=0.3 eV\nMelting Point=429.75 K\nBoiling Point=2345 K\nDensity=7.31 g/cm³\nYear Discovered=1863', '49', '69.72'),
            ('Tl', 'Thallium', 'Atomic # = 81\nAtomic Weight = 204.37\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=1.62\nAtomic Radius (van der Waals)=196 pm\nIonization Energy=6.108 eV\nElectron Affinity=0.2 eV\nMelting Point=577 K\nBoiling Point=1746 K\nDensity=11.8 g/cm³\nYear Discovered=1861', '81', '204.37')]
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
                      activebackground="white",
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c13_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
        
        column13_2_0 = [
            ('Nh', 'Nihonium', 'Atomic # = 113\nAtomic Weight = 286\nState = Unkown\nCategory = \nYear Discovered=2004', '113', '286')]
        r = 9
        c = 14
        self.othermetal_c13_2_0={}
        for b in column13_2_0: 
            self.othermetal_c13_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c13_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c14 = Label(self, text="14", font=7, bg=bacG)
        c14.grid(column=15, row=3)
        
        column14_0 = [
            ('C', 'Carbon', 'Atomic # = 6\nAtomic Weight = 12.01\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=2.55\nAtomic Radius (van der Waals)=170 pm\nIonization Energy=11.260 eV\nElectron Affinity=1.263 eV\nMelting Point=3823 K\nBoiling Point=4098 K\nDensity=2.2670 g/cm³\nYear Discovered=Ancient', '6', '12.01')]
        r = 4
        c = 15
        self.othernon_c14_0={}
        for b in column14_0: 
            self.othernon_c14_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color1,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color1, text[0], text[3], text[4])])
            self.othernon_c14_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column14_1 = [
            ('Si', 'Silicon', 'Atomic # = 14\nAtomic Weight = 28.09\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=1.9\nAtomic Radius (van der Waals)=210 pm\nIonization Energy=8.152 eV\nElectron Affinity	1.385 eV\nMelting Point=1687 K\nBoiling Point=3538 K\nDensity=2.3296 g/cm³\nYear Discovered=1854', '14', '28.09'),
            ('Ge', 'Germanium', 'Atomic # = 32\nAtomic Weight = 72.59\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=2.01\nAtomic Radius (van der Waals)=211 pm\nIonization Energy=7.900 eV\nElectron Affinity=1.35 eV\nMelting Point=1211.4 K\nBoiling Point=3106 K\nDensity=5.323 g/cm³\nYear Discovered=1886', '32', '72.59'),]
        r = 5
        c = 15
        self.metalloid_c14_1={}
        for b in column14_1: 
            self.metalloid_c14_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloid_c14_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column14_2 = [
            ('Sn', 'Tin', 'Atomic # = 50\nAtomic Weight = 118.69\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=1.96\nAtomic Radius (van der Waals)=217 pm\nIonization Energy=7.344 eV\nElectron Affinity=1.2 eV\nMelting Point=505.08 K\nBoiling Point=2875 K\nDensity=7.287 g/cm³\nYear Discovered=Ancient', '50', '118.69'),
            ('Pb', 'Lead', 'Atomic # = 82\nAtomic Weight = 207.20\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=2.33\nAtomic Radius (van der Waals)=202 pm\nIonization Energy=7.417 eV\nElectron Affinity=0.36 eV\nMelting Point=600.61 K\nBoiling Point=2022 K\nDensity=11.342 g/cm³\nYear Discovered=Ancient', '82', '207.20')]
        r = 7
        c = 15
        self.othermetal_c14_2={}
        for b in column14_2: 
            self.othermetal_c14_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c14_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column14_2_0 = [
            ('Fl', 'Flerovium', 'Atomic # = 114\nAtomic Weight = 289\nState = Unkown\nCategory = \nYear Discovered=1998', '114', '289')]
        r = 9
        c = 15
        self.othermetal_c14_2_0={}
        for b in column14_2_0: 
            self.othermetal_c14_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c14_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                
        c15 = Label(self, text="15", font=7, bg=bacG)
        c15.grid(column=16, row=3)
        
        column15_0 = [
            ('N', 'Nitrogen', 'Atomic # = 7\nAtomic Weight = 14.01\nState = Gas\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=3.04\nAtomic Radius (van der Waals)=155 pm\nIonization Energy=14.534 eV\nMelting Point=63.15 K\nBoiling Point=77.36 K\nDensity=0.0012506 g/cm³\nYear Discovered=1772', '7', '14.01'),
            ('P', 'Phosphorus', 'Atomic # = 15\nAtomic Weight = 30.97\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=2.19\nAtomic Radius (van der Waals)=180 pm\nIonization Energy=10.487 eV\nElectron Affinity=0.746 eV\nMelting Point=317.3 K\nBoiling Point=553.65 K\nDensity=1.82 g/cm³\nYear Discovered=1669', '15', '30.97')]
        r = 4
        c = 16
        self.othernon_c15_0={}
        for b in column15_0: 
            self.othernon_c15_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color1,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color1, text[0], text[3], text[4])])
            self.othernon_c15_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column15_1 = [
            ('As', 'Arsenic', 'Atomic # = 33\nAtomic Weight = 74.92\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=2.18\nAtomic Radius (van der Waals)=185 pm\nIonization Energy=9.815 eV\nElectron Affinity=0.81 eV\nMelting Point=1090 K\nBoiling Point=887 K\nDensity=5.776 g/cm³\nYear Discovered=Ancient', '33', '74.92'),
            ('Sb', 'Antimony', 'Atomic # = 51\nAtomic Weight = 121.75\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=2.05\nAtomic Radius (van der Waals)=206 pm\nIonization Energy=8.64 eV\nElectron Affinity=1.07 eV\nMelting Point=903.78 K\nBoiling Point=1860 K\nDensity=6.685 g/cm³\nYear Discovered=Ancient', '51', '121.75')]
        r = 6
        c = 16
        self.metalloids_c15_1={}
        for b in column15_1: 
            self.metalloids_c15_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloids_c15_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column15_2 = [    
            ('Bi', 'Bismuth', 'Atomic # = 83\nAtomic Weight = 208.98\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=2.02\nAtomic Radius (van der Waals)=207 pm\nIonization Energy=7.289 eV\nElectron Affinity=0.946 eV\nMelting Point=544.55 K\nBoiling Point=1837 K\nDensity=9.807 g/cm³\nYear Discovered=1753', '83', '208.98')]
        r = 8
        c = 16
        self.othermetal_c15_2={}
        for b in column15_2: 
            self.othermetal_c15_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c15_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column15_2_0 = [    
            ('Mc', 'Moscovium', 'Atomic # = 115\nAtomic Weight = 290\nState = Unkown\nCategory = \nYear Discovered=2003', '115', '290')]
        r = 9
        c = 16
        self.othermetal_c15_2_0={}
        for b in column15_2_0: 
            self.othermetal_c15_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c15_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

                
        c16 = Label(self, text="16", font=7, bg=bacG)
        c16.grid(column=17, row=3)
        
        column16_0 = [
            ('O', 'Oxygen', 'Atomic # = 8\nAtomic Weight = 15.99\nState = Gas\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=3.44\nAtomic Radius (van der Waals)=152 pm\nIonization Energy=13.618 eV\nElectron Affinity=1.461 eV\nMelting Point=54.36 K\nBoiling Point90.2 K\nDensity=0.001429 g/cm³\nYear Discovered=1774', '8', '15.99'),
            ('S', 'Sulfur', 'Atomic # = 16\nAtomic Weight = 32.06\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=2.58\nAtomic Radius (van der Waals)=180 pm\nIonization Energy=10.360 eV\nElectron Affinity=2.077 eV\nMelting Point=388.36 K\nBoiling Point=717.75 K\nDensity=2.067 g/cm³\nYear Discovered=Ancient', '16', '32.06'),
            ('Se', 'Selenium', 'Atomic # = 34\nAtomic Weight = 78.96\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=2.55\nAtomic Radius (van der Waals)=190 pm\nIonization Energy=9.752 eV\nElectron Affinity=2.021 eV\nMelting Point=493.65 K\nBoiling Point=958 K\nDensity=4.809 g/cm³\nYear Discovered=1817', '34', '78.96')]
        r = 4
        c = 17
        self.othernon_c16_0={}
        for b in column16_0: 
            self.othernon_c16_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color1,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color1, text[0], text[3], text[4])])
            self.othernon_c16_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column16_1 = [
            ('Te', 'Tellurium', 'Atomic # = 52\nAtomic Weight = 127.60\nState = Solid\nCategory = Nonmetals\nElectronegativity (Pauling Scale)=2.1\nAtomic Radius (van der Waals)=206 pm\nIonization Energy=9.010 eV\nElectron Affinity=1.971 eV\nMelting Point=722.66 K\nBoiling Point=1261 K\nDensity=6.232 g/cm³\nYear Discovered=1782', '52', '127.60')]
        r = 7
        c = 17
        self.metalloid_c16_1={}
        for b in column16_1: 
            self.metalloid_c16_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color10,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color10, text[0], text[3], text[4])])
            self.metalloid_c16_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column16_2 = [
            ('Po', 'Polonium', 'Atomic # = 84\nAtomic Weight = 209.00\nState = Solid\nCategory = Other Metals\nElectronegativity (Pauling Scale)=2\nAtomic Radius (van der Waals)=197 pm\nIonization Energy=8.417 eV\nElectron Affinity=1.9 eV\nMelting Point=527 K\nBoiling Point=1235 K\nDensity=9.32 g/cm³\nYear Discovered=1898', '84', '209.00')]
        r = 8
        c = 17
        self.othermetal_c16_2={}
        for b in column16_2: 
            self.othermetal_c16_2[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color11,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color11, text[0], text[3], text[4])])
            self.othermetal_c16_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column16_2_0 = [
            ('Lv', 'Livermorium', 'Atomic # = 116\nAtomic Weight = 293\nState = Unkown\nCategory = \nYear Discovered=2000', '116', '293.00')]
        r = 9
        c = 17
        self.othermetal_c16_2_0={}
        for b in column16_2_0: 
            self.othermetal_c16_2_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.othermetal_c16_2_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c17 = Label(self, text="17", font=7, bg=bacG)
        c17.grid(column=18, row=3)
        
        column17 = [
            ('F', 'Fluorine', 'Atomic # = 9\nAtomic Weight = 18.99\nState = Gas\nCategory = Halogens\nElectronegativity (Pauling Scale)=3.98\nAtomic Radius (van der Waals)=135 pm\nIonization Energy=17.423 eV\nElectron Affinity=3.339 eV\nMelting Point=53.53 K\nBoiling Point=85.03 K\nDensity=0.001696 g/cm³\nYear Discovered=1670', '9', '18.99'),
            ('Cl', 'Chlorine', 'Atomic # = 17\nAtomic Weight = 35.45\nState = Gas\nCategory = Halogens\nElectronegativity (Pauling Scale)=3.16\nAtomic Radius (van der Waals)=175 pm\nIonization Energy=12.968 eV\nElectron Affinity=3.617 eV\nMelting Point=171.65 K\nBoiling Point=239.11 K\nDensity=0.003214 g/cm³\nYear Discovered=1774', '17', '35.45'),
            ('Br', 'Bromine', 'Atomic # = 35\nAtomic Weight = 79.90\nState = Liquid\nCategory = Halogens\nElectronegativity (Pauling Scale)=2.96\nAtomic Radius (van der Waals)=183 pm\nIonization Energy=11.814 eV\nElectron Affinity=3.365 eV\nMelting Point=265.95 K\nBoiling Point=331.95 K\nDensity=3.11 g/cm³\nYear Discovered=1826', '35', '79.90'),
            ('I', 'Iodine', 'Atomic # = 53\nAtomic Weight = 126.90\nState = Solid\nCategory = Halogens\nElectronegativity (Pauling Scale)=2.66\nAtomic Radius (van der Waals)=198 pm\nIonization Energy=10.451 eV\nElectron Affinity=3.059 eV\nMelting Point=386.85 K\nBoiling Point=457.55 K\nDensity=4.93 g/cm³\nYear Discovered=1811', '53', '126.90')]
        r = 4
        c = 18
        self.halogen_c={}
        color20="DodgerBlue2"
        for b in column17: 
            self.halogen_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color20,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color20, text[0], text[3], text[4])])
            self.halogen_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column17_1 = [
            ('At', 'Astatine', 'Atomic # = 85\nAtomic Weight = 210.00\nState = Solid\nCategory = Halogens\nElectronegativity (Pauling Scale)=2.2\nAtomic Radius (van der Waals)=202 pm\nIonization Energy=9.5 eV\nElectron Affinity=2.8 eV\nMelting Point=575 K\nDensity=7 g/cm³\nYear Discovered=1940', '85', '210.00')]
        r = 8
        c = 18
        self.halogen_c_1={}        
        for b in column17_1: 
            self.halogen_c_1[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color20,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color20, text[0], text[3], text[4])])
            self.halogen_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        column17_0 = [
            ('Ts', 'Tennessine', 'Atomic # = 117\nAtomic Weight = 294.00\nState = Unkown\nCategory = Halogens\nYear Discovered=2010', '117', '294.00')]
        r = 9
        c = 18
        self.halogen_c_0={}
        for b in column17_0: 
            self.halogen_c_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.halogen_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        c18 = Label(self, text="18", font=7, bg=bacG)
        c18.grid(column=19, row=2)
        
        column18 = [
            ('He', 'Helium', 'Atomic # = 2\nAtomic Weight = 4.00\nState = Gas\nCategory = Nobel Gases\nAtomic Radius (van der Waals)=140 pm\nIonization Energy=24.587 eV\nMelting Point=0.95 K\nBoiling Point=4.22 K\nDensity=0.0001785 g/cm³\nYear Discovered=1868', '2', '4.00'),
            ('Ne', 'Neon', 'Atomic # = 10\nAtomic Weight = 20.18\nState = Gas\nCategory = Nobel Gases\nAtomic Radius (van der Waals)=154 pm\nIonization Energy=21.565 eV\nMelting Point=24.56 K\nBoiling Point=27.07 K\nDensity=0.0008999 g/cm³\nYear Discovered=1898', '10', '20.18'),
            ('Ar', 'Argon', 'Atomic # = 18\nAtomic Weight = 39.95\nState = Gas\nCategory = Nobel Gases\nAtomic Radius (van der Waals)=188 pm\nIonization Energy=15.760 eV\nMelting Point=83.8 K\nBoiling Point=87.3 K\nDensity=0.0017837 g/cm³\nYear Discovered=1894', '18', '39.95'),
            ('Kr', 'Krypton', 'Atomic # = 36\nAtomic Weight = 83.80\nState = Gas\nCategory = Nobel Gases\nElectronegativity (Pauling Scale)=3\nAtomic Radius (van der Waals)=202 pm\nIonization Energy=14.000 eV\nMelting Point=115.79 K\nBoiling Point=119.93 K\nDensity=0.003733 g/cm³\nYear Discovered=1898', '36', '83.80'),
            ('Xe', 'Xenon', 'Atomic # = 54\nAtomic Weight = 131.30\nState = Gas\nCategory = Nobel Gases\nElectronegativity (Pauling Scale)=2.6\nAtomic Radius (van der Waals)=216 pm\nIonization Energy=12.130 eV\nMelting Point=161.36 K\nBoiling Point=165.03 K\nDensity=0.005887 g/cm³\nYear Discovered=1898', '54', '131.30'),
            ('Rn', 'Radon', 'Atomic # = 86\nAtomic Weight = 222.00\nState = Gas\nCategory = Nobel Gases\nAtomic Radius (van der Waals)=220 pm\nIonization Energy=10.745 eV\nMelting Point=202 K\nBoiling Point=211.45 K\nDensity=0.00973 g/cm³\nYear Discovered=1900', '86', '222.00')]
        r = 3
        c = 19
        self.nobel_c={}
        color21="turquoise2"
        for b in column18: 
            self.nobel_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color21,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color21, text[0], text[3], text[4])])
            self.nobel_c[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        column18_0 = [
            ('Og', 'Oganesson', 'Atomic # = 118\nAtomic Weight = 294.00\nState = Unkown\nCategory = Nobel Gases\nYear Discovered=2006', '118', '294.00')]
        r = 9
        c = 19
        self.nobel_c_0={}
        for b in column18_0: 
            self.nobel_c_0[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=colorUnk,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorUnk, text[0], text[3], text[4])])
            self.nobel_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        self.fillerLine = tk.Label(self, text="")
        self.fillerLine.grid(row=12, column=0)

        lanthanide = [
            ('Ce', 'Cerium', 'Atomic # = 58\nAtomic Weight = 140.12\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.12\nAtomic Radius (van der Waals)=235 pm\nIonization Energy=5.539 eV\nElectron Affinity=0.5 eV\nMelting Point=1071 K\nBoiling Point=3697 K\nDensity=6.770 g/cm³\nYear Discovered=1803', '58', '140.12'),
            ('Pr', 'Praseodymium', 'Atomic # = 59\nAtomic Weight = 140.91\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.13\nAtomic Radius (van der Waals)=239 pm\nIonization Energy=5.464 eV\nMelting Point=1204 K\nBoiling Point=3793 K\nDensity=6.77 g/cm³\nYear Discovered=1885', '59', '140.91'),
            ('Nd', 'Neodymium', 'Atomic # = 60\nAtomic Weight = 144.24\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.14\nAtomic Radius (van der Waals)=229 pm\nIonization Energy=5.525 eV\nMelting Point=1294 K\nBoiling Point=3347 K\nDensity=7.01 g/cm³\nYear Discovered=1885', '60', '144.24'),
            ('Pm', 'Promethium', 'Atomic # = 61\nAtomic Weight = 145.00\nState = Synthetic\nCategory = Trans Metals\nAtomic Radius (van der Waals)=236 pm\nIonization Energy=5.55 eV\nMelting Point=1315 K\nBoiling Point=3273 K\nDensity=7.26 g/cm³\nYear Discovered=1945', '61', '145.00'),
            ('Sm', 'Samarium', 'Atomic # = 62\nAtomic Weight = 150.40\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.17\nAtomic Radius (van der Waals)=229 pm\nIonization Energy=5.644 eV\nMelting Point=1347 K\nBoiling Point=2067 K\nDensity=7.52 g/cm³\nYear Discovered=1879', '62', '150.40'),
            ('Eu', 'Europium', 'Atomic # = 63\nAtomic Weight = 151.96\nState = Solid\nCategory = Trans Metals\nAtomic Radius (van der Waals)=233 pm\nIonization Energy=5.670 eV\nMelting Point=1095 K\nBoiling Point=1802 K\nDensity=5.24 g/cm³\nYear Discovered=1901', '63', '151.96'),
            ('Gd', 'Gadolinium', 'Atomic # = 64\nAtomic Weight = 157.25\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.2\nAtomic Radius (van der Waals)=237 pm\nIonization Energy=6.150 eV\nMelting Point=1586 K\nBoiling Point=3546 K\nDensity=7.90 g/cm³\nYear Discovered=1880', '64', '157.25'),
            ('Tb', 'Terbium', 'Atomic # = 65\nAtomic Weight = 158.93\nState = Solid\nCategory = Trans Metals\nAtomic Radius (van der Waals)=221 pm\nIonization Energy=5.864 eV\nMelting Point=1629 K\nBoiling Point=3503 K\nDensity=8.23 g/cm³\nYear Discovered=1843', '65', '158.93'),
            ('Dy', 'Dyprosium', 'Atomic # = 66\nAtomic Weight = 162.50\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.22\nAtomic Radius (van der Waals)=229 pm\nIonization Energy=5.939 eV\nMelting Point=1685 K\nBoiling Point=2840 K\nDensity=8.55 g/cm³\nYear Discovered=1886', '66', '162.50'),
            ('Ho', 'Holmium', 'Atomic # = 67\nAtomic Weight = 164.93\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.23\nAtomic Radius (van der Waals)=216 pm\nIonization Energy=6.022 eV\nMelting Point=1747 K\nBoiling Point=2973 K\nDensity=8.80 g/cm³\nYear Discovered=1878', '67', '164.93'),
            ('Er', 'Erbium', 'Atomic # = 68\nAtomic Weight = 167.26\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.24\nAtomic Radius (van der Waals)=235 pm\nIonization Energy=6.108 eV\nMelting Point=1802 K\nBoiling Point=3141 K\nDensity=9.07 g/cm³\nYear Discovered=1843', '68', '167.26'),
            ('Tm', 'Thulium', 'Atomic # = 69\nAtomic Weight = 168.93\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.25\nAtomic Radius (van der Waals)=227 pm\nIonization Energy=6.184 eV\nMelting Point=1818 K\nBoiling Point=2223 K\nDensity=9.32 g/cm³\nYear Discovered=1879', '69', '168.93'),
            ('Yb', 'Ytterbium', 'Atomic # = 70\nAtomic Weight = 173.04\nState = Solid\nCategory = Trans Metals\nAtomic Radius (van der Waals)=242 pm\nIonization Energy=6.254 eV\nMelting Point=1092 K\nBoiling Point=1469 K\nDensity=6.90 g/cm³\nYear Discovered=1878', '70', '173.04'),
            ('Lu', 'Lutetium', 'Atomic # = 71\nAtomic Weight = 174.97\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.27\nAtomic Radius (van der Waals)=221 pm\nIonization Energy=5.426 eV\nMelting Point=1936 K\nBoiling Point=3675 K\nDensity=9.84 g/cm³\nYear Discovered=1907', '71', '174.97')]
        r = 13
        c = 5
        self.La_CA={}
        for b in lanthanide: 
            self.La_CA[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color5,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color5, text[0], text[3], text[4])])
            self.La_CA[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        actinide = [
            ('Th', 'Thorium', 'Atomic # = 90\nAtomic Weight = 232.04\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nAtomic Radius (van der Waals)=237 pm\nIonization Energy=6.08 eV\nMelting Point=2023 K\nBoiling Point=5061 K\nDensity=11.72 g/cm³\nYear Discovered=1828', '90', '232.04'),
            ('Pa', 'Protactinium', 'Atomic # = 91\nAtomic Weight = 231.04\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.5\nAtomic Radius (van der Waals)=243 pm\nIonization Energy=5.89 eV\nMelting Point=1845 K\nDensity=15.37 g/cm³\nYear Discovered=1913', '91', '231.04'),
            ('U', 'Uranium', 'Atomic # = 92\nAtomic Weight = 238.03\nState = Solid\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.38\nAtomic Radius (van der Waals)=240 pm\nIonization Energy=6.194 eV\nMelting Point=1408 K\nBoiling Point=4404 K\nDensity=18.95 g/cm³\nYear Discovered=1789', '92', '238.03'),
            ('Np', 'Neptunium', 'Atomic # = 93\nAtomic Weight = 237.05\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.36\nAtomic Radius (van der Waals)=221 pm\nIonization Energy=6.266 eV\nMelting Point=917 K\nBoiling Point=4175 K\nDensity=20.25 g/cm³\nYear Discovered=1940', '93', '237.05'),
            ('Pu', 'Plutonium', 'Atomic # = 94\nAtomic Weight = 244.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.28\nAtomic Radius (van der Waals)=243 pm\nIonization Energy=6.06 eV\nMelting Point=913 K\nBoiling Point=3501 K\nDensity=19.84 g/cm³\nYear Discovered=1940', '94', '244.00'),
            ('Am', 'Americium', 'Atomic # = 95\nAtomic Weight = 243.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nAtomic Radius (van der Waals)=244 pm\nIonization Energy=5.993 eV\nMelting Point=1449 K\nBoiling Point=2284 K\nDensity=13.69 g/cm³\nYear Discovered=1944', '95', '243.00'),
            ('Cm', 'Curium', 'Atomic # = 96\nAtomic Weight = 247.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nAtomic Radius (van der Waals)=245 pm\nIonization Energy=6.02 eV\nMelting Point=1618 K\nBoiling Point=3400 K\nDensity=13.51 g/cm³\nYear Discovered=1944', '96', '247.00'),
            ('Bk', 'Berkelium', 'Atomic # = 97\nAtomic Weight = 247.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nAtomic Radius (van der Waals)=244 pm\nIonization Energy=6.23 eV\nMelting Point=1323 K\nDensity=14 g/cm³\nYear Discovered=1949', '97', '247.00'),
            ('Cf', 'Californium', 'Atomic # = 98\nAtomic Weight = 247.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nAtomic Radius (van der Waals)=245 pm\nIonization Energy=6.30 eV\nMelting Point=1173 K\nYear Discovered=1950', '98', '247.00'),
            ('Es', 'Einsteinium', 'Atomic # = 99\nAtomic Weight = 252.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nAtomic Radius (van der Waals)=245 pm\nIonization Energy=6.42 eV\nMelting Point=1133 K\nYear Discovered=1952', '99', '252.00'),
            ('Fm', 'Fermium', 'Atomic # = 100\nAtomic Weight = 257.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nIonization Energy=6.50 eV\nMelting Point=1800 K\nYear Discovered=1952', '100', '257.00'),
            ('Md', 'Mendelevium', 'Atomic # = 101\nAtomic Weight = 260.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nIonization Energy=6.58 eV\nMelting Point=1100 K\nYear Discovered=1955', '101', '260.00'),
            ('No', 'Nobelium', 'Atomic # = 102\nAtomic Weight = 259.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nIonization Energy=6.65 eV\nMelting Point=1100 K\nYear Discovered=1957', '102', '259.00'),
            ('Lr', 'Lawrencium', 'Atomic # = 103\nAtomic Weight = 262.00\nState = Synthetic\nCategory = Trans Metals\nElectronegativity (Pauling Scale)=1.3\nMelting Point=1900 K\nYear Discovered=1961', '103', '262.00')]
        r = 14
        c = 5
        self.Ac_CA={}
        for b in actinide:
            self.Ac_CA[b[0]]=tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      activebackground="white",
                      borderwidth = 3,
                      bg=color6,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(color6, text[0], text[3], text[4])])
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

        close = [
            ('close', 'SERIAL COMMUNICATION', 'Now the ARDUINO SERIAL communication is CLOSED and trying to run THE PROGRAM after these is ERROR PRONE so please EXIT the program if it doesn\'t or RESTART it', 'PORT IS CLOSED')]
        r = 14
        c = 3
        for b in close: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="black",
                      fg="white",
                      command=lambda text=b: [self.name(text[0]) + self.info(text[3]), self.arduino(text[0]), self.qmsg(text[2])]).grid(row=r, column=c)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Alkaline_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=3, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Transition_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=3, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.OtherNon_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=3, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        Nobel_gas = [('Noble Gas', 'Noble Gas elements', 'NobleGas')]
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Nobel_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Lanthanides_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Actinides_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.OtherMetal_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Metalloids_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Halogen_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.AllMetal_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.AllNon_f(), self.voice(text[0])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.Radioactive_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[0]) + self.info(text[1]), self.all_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[0]) + self.info(text[1]), self.solid_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Liquid = [('Liquid', 'Liquid elements')]
        r = 0
        c = 9
        colorL="blue"
        for b in Liquid:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorL,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[0]) + self.info(text[1]), self.liquid_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        Gas = [('Gas', 'Gas elements')]
        r = 0
        c = 11
        colorG="orange red"
        for b in Gas:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=1,
                      font=10,
                      borderwidth=3,
                      bg=colorG,
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[0]) + self.info(text[1]), self.gas_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[0]) + self.info(text[1]), self.unknown_f(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
                
        
        #setting up the canvas big elements image
        self.canvas = Canvas(self, height=100, width=100, bg="palegreen2", relief=GROOVE, borderwidth=0)
        #canvas.pack()
        self.canvas.create_rectangle(100, 100, 0, 0)
        self.canvas.grid(row=1, column=0, rowspan=2)
        self.sy = self.canvas.create_text(50, 50, text="H", fill="black", font=('Helvetica 15 bold', 35))
        self.an = self.canvas.create_text(10, 12, text="1", fill="black", font=('Helvetica 15 bold', 10))
        self.am = self.canvas.create_text(17, 90, text="1.001", fill="black", font=('Helvetica 15 bold', 8))
        self.infoLine = tk.Label(self, text="", justify='left', font=10, bg=bacG)
        self.infoLine.grid(row=3, column=0, rowspan=4)        
        

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
        coloAlk = "light goldenrod"
        coloFg="black"
        for key in self.alkali_c:
            self.alkali_c[key].config(bg=coloAlk, fg=coloFg)

        coloAE = "bisque4"
        for key in self.alkaline_c:
            self.alkaline_c[key].config(bg=coloAE, fg=coloFg)
        
        coloTr = "tan1"
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
        
        coloNoN = "palegreen2"
        self.H.config(bg=coloNoN)
        for key in self.othernon_c14_0:
            self.othernon_c14_0[key].config(bg=coloNoN, fg=coloFg)
        for key in self.othernon_c15_0:
            self.othernon_c15_0[key].config(bg=coloNoN, fg=coloFg)
        for key in self.othernon_c16_0:
            self.othernon_c16_0[key].config(bg=coloNoN, fg=coloFg)
            
        coloNo = "turquoise2"
        for key in self.nobel_c:
            self.nobel_c[key].config(bg=coloNo, fg=coloFg)


        coloLa = "lightpink"
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloLa, fg=coloFg)
        for key in self.La_CA:
            self.La_CA[key].config(bg=coloLa, fg=coloFg)

        coloAc = "orchid2"
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

        colometa = "salmon"
        for key in self.metalloids_c12_1:
            self.metalloids_c12_1[key].config(bg=colometa, fg=coloFg)
        for key in self.metalloid_c14_1:
            self.metalloid_c14_1[key].config(bg=colometa, fg=coloFg)
        for key in self.metalloids_c15_1:
            self.metalloids_c15_1[key].config(bg=colometa, fg=coloFg)
        for key in self.metalloid_c16_1:
            self.metalloid_c16_1[key].config(bg=colometa, fg=coloFg)

        coloha="DodgerBlue2"
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
        coloFu = "light goldenrod"
        self.white_f()
        for key in self.alkali_c:
            self.alkali_c[key].config(bg=coloFu)
        pass
    # Alkaline Earth
    def Alkaline_f(self):
        coloFu = "bisque4"
        self.white_f()
        for key in self.alkaline_c:
            self.alkaline_c[key].config(bg=coloFu)
    # Transition
    def Transition_f(self):
        coloFu = "tan1"
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
        coloFu = "palegreen2"
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
        coloFu = "turquoise2"
        self.white_f()
        for key in self.nobel_c:
            self.nobel_c[key].config(bg=coloFu)
    # Lanthanides
    def Lanthanides_f(self):
        coloFu = "lightpink"
        self.white_f()
        for key in self.La_c3_1:
            self.La_c3_1[key].config(bg=coloFu)
        for key in self.La_CA:
            self.La_CA[key].config(bg=coloFu)
            
    # Actinides
    def Actinides_f(self):
        coloFu = "orchid2"
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
        coloFu="salmon"
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
        coloFu="DodgerBlue2"
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
        coloFu="blue"
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
        coloFu="orange red"
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
        if text =="close":
            user_input = "clear"
            byte_msg = user_input.encode('utf-8')
            #time.sleep(0.1)
            nano.write(byte_msg)
            nano.close()
        else:
            #time.sleep(0.1)
            byte_msg = text.encode('utf-8')
            nano.write(byte_msg)
        time.sleep(2)

    # voice description
    beSound = True
    def voice(self, text):
        if self.beSound:
            engine.say(text)
            engine.runAndWait()

    # msg handling
    def qmsg(self, text):
        msg.showwarning(title="SERIAL COMMUNICATION", message=text)
        sys.exit(1)
        
# This class is about blocks and electron configurartions
class Second(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.topLabel = tk.Label(self, text="Hydrogen", font=('Helvetica 15 bold', 15))
        self.topLabel.grid(row=0, column=0, columnspan=2)
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
            ('H', 'Hydrogen', 'Oxidation states: -1, 1\nConfiguration: 1s¹\nExpanded: - \n1s¹\nEnergy levels: 1\nQuantum numbers: l=0, m=0, n=1', '1', '1.01', [1]),
            ('Li', 'Lithium', 'Oxidation states: 1\nConfiguration: [He] 2s¹\nExpanded: - \n1s² 2s¹\nEnergy levels: 2, 1\nQuantum numbers: l=0, m=0, n=2', '3', '6.94', [2, 1]),
            ('Na', 'Sodium', 'Oxidation states: -1, 1\nConfiguration: [Ne] 3s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s¹\nEnergy levels: 2, 8, 1\nQuantum numbers: l=0, m=0, n=3', '11', '22.99', [2, 8, 1]),
            ('K', 'Potassium', 'Oxidation states: -1, 1\nConfiguration: [Ar] 4s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹\nEnergy levels: 2, 8, 8, 1\nQuantum numbers: l=0, m=0, n=4', '19', '39.10', [2, 8, 8, 1]),
            ('Rb', 'Rubidium', 'Oxidation states: -1, 1\nConfiguration: [Kr] 5s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹\nEnergy levels: 2, 8, 18, 8, 1\nQuantum numbers: l=0, m=0, n=5', '37', '85.41', [2, 8, 18, 8, 1]),
            ('Cs', 'Cesium', 'Oxidation states: -1, 1\nConfiguration: [Xe] 6s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s¹\nEnergy levels: 2, 8, 18, 18, 8, 1\nQuantum numbers: l=0, m=0, n=6', '55', '132.91', [2, 8, 18, 18, 8, 1]),
            ('Fr', 'Francium', 'Oxidation states: 1\nConfiguration: [Rn] 7s¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s¹\nEnergy levels: 2, 8, 18, 32, 18, 8, 1\nQuantum numbers: l=0, m=0, n=7', '87', '223', [2, 8, 18, 32, 18, 8, 1])
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
                                           command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorS, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.s_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9:
                r = 1
                c += 1
        
        s_block_1 = [
            ('Be', 'Beryllium', 'Oxidation states: 1, 2\nConfiguration: [He] 2s²\nExpanded: - \n1s² 2s²\nEnergy levels: 2, 2\nQuantum numbers: l=0, m=0, n=2', '4', '9.01', [2, 2]),
            ('Mg', 'Magnesium', 'Oxidation states: 1, 2\nConfiguration: [Ne] 3s²\nExpanded: - \n1s² 2s² 2p⁶ 3s²\nEnergy levels: 2, 8, 2\nQuantum numbers: l=0, m=0, n=3', '12', '24.31', [2, 8, 2]),
            ('Ca', 'Calcium', 'Oxidation states: 1, 2\nConfiguration: [Ar] 4s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\nEnergy levels: 2, 8, 8, 2\nQuantum numbers: l=0, m=0, n=4', '20', '40.08', [2, 8, 8, 2]),
            ('Sr', 'Strontium', 'Oxidation states: 1, 2\nConfiguration: [Kr] 5s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s²\nEnergy levels: 2, 8, 18, 8, 2\nQuantum numbers: l=0, m=0, n=5', '38', '87.62', [2, 8, 18, 8, 2]),
            ('Ba', 'Barium', 'Oxidation states: 2\nConfiguration: [Xe] 6s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s²\nEnergy levels: 2, 8, 18, 18, 8, 2\nQuantum numbers: l=0, m=0, n=6', '56', '137.33', [2, 8, 18, 18, 8, 2]),
            ('Ra', 'Radium', 'Oxidation states: 2\nConfiguration: [Rn] 7s²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶\n 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s²\nEnergy levels: 2, 8, 18, 32, 18, 8, 2\nQuantum numbers: l=0, m=0, n=7', '88', '226.03', [2, 8, 18, 32, 18, 8, 2])]
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
                      command=lambda text=b:  [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorS, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.s_block_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        
        d_block_0 = [
            ('Sc', 'Scandium', 'Oxidation states 1, 2, 3\nConfiguration [Ar] 4s² 3d¹\nExpanded - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹\nEnergy levels 2, 8, 9, 2\nQuantum numbers l=2, m=-2, n=3', '21', '44.96', [2, 8, 9, 2]),
            ('Y', 'Yttrium', 'Oxidation states 1, 2, 3\nConfiguration [Kr] 5s² 4d¹\nExpanded - \n 1s² 2s² 2p⁶ 3s² \n3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹\nEnergy levels 2, 8, 18, 9, 2\nQuantum numbers l=2, m=-2, n=4', '39', '88.91', [2, 8, 18, 9, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        f_block_0 = [
            ('La', 'Lanthanum', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 5d¹\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 5d¹\nEnergy levels: 2, 8, 18, 18, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '57', '138.91', [2, 8, 18, 18, 9, 2]),
            ('Ac', 'Actinium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 6d¹\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰\n 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 6d¹\nEnergy levels: 2, 8, 18, 32, 18, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '89', '227.03', [2, 8, 18, 32, 18, 9, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorF, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.f_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_1 = [
            ('Ti', 'Titanium', 'Oxidation states: -1, 2, 3, 4\nConfiguration: [Ar] 4s² 3d²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d²\nEnergy levels: 2, 8, 10, 2\nQuantum numbers: l=2, m=-1, n=3', '22', '47.90', [2, 8, 10, 2]),
            ('Zr', 'Zirconium', 'Oxidation states:  1, 2, 3, 4\nConfiguration: [Kr] 5s² 4d²\nExpanded: - \n 1s² 2s² 2p⁶\n 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d²\nEnergy levels: 2, 8, 18, 10, 2\nQuantum numbers: l=2, m=-1, n=4', '40', '91.22', [2, 8, 18, 10, 2]),
            ('Hf', 'Hafnium', 'Oxidation states: 2, 3, 4\nConfiguration: [Xe] 6s² 4f¹⁴ 5d²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d²\nEnergy levels: 2, 8, 18, 32, 10, 2\nQuantum numbers: l=2, m=-1, n=5', '72', '178.49', [2, 8, 18, 32, 10, 2]),
            ('Rf', 'Rutherfordium', 'Oxidation states: 4\nConfiguration: [Rn] 7s² 5f¹⁴ 6d²\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d²\nEnergy levels: 2, 8, 18, 32, 32, 10, 2\nQuantum numbers: l=2, m=-1, n=6', '104', '261.00', [2, 8, 18, 32, 32, 10, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        d_block_2 = [
            ('V', 'Vanadium', 'Oxidation states: -1, 1, 2, 3, 4, 5\nConfiguration: [Ar] 4s² 3d³\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d³\nEnergy levels: 2, 8, 11, 2\nQuantum numbers: l=2, m=0, n=3', '23', '50.94', [2, 8, 11, 2]),
            ('Nb', 'Niobium', 'Oxidation states: -1, 2, 3, 4, 5\nConfiguration: [Kr] 5s¹ 4d⁴\nExpanded: - \n 1s² 2s² 2p⁶ \n3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d⁴\nEnergy levels: 2, 8, 18, 12, 1\nQuantum numbers: l=2, m=1, n=4', '41', '92.91', [2, 8, 18, 12, 1]),
            ('Ta', 'Tantalum', 'Oxidation states: -1, 2, 3, 4, 5\nConfiguration: [Xe] 6s² 4f¹⁴ 5d³\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d³\nEnergy levels: 2, 8, 18, 32, 11, 2\nQuantum numbers: l=2, m=0, n=5', '73', '180.95', [2, 8, 18, 32, 11, 2]),
            ('Db', 'Dubnium', 'Oxidation states: 5\nConfiguration: [Rn] 7s² 5f¹⁴ 6d³\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d³\nEnergy levels: 2, 8, 18, 32, 32, 11, 2\nQuantum numbers: l=2, m=0, n=6', '105', '262.00', [2, 8, 18, 32, 32, 11, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_3 = [
            ('Cr', 'Chromium', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Ar] 4s¹ 3d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d⁵\nEnergy levels: 2, 8, 13, 1\nQuantum numbers: l=2, m=2, n=3', '24', '51.99', [2, 8, 13, 1]),
            ('Mo', 'Molybdenum', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Kr] 5s¹ 4d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s¹ 4d⁵\nEnergy levels: 2, 8, 18, 13, 1\nQuantum numbers: l=2, m=2, n=4', '42', '95.94', [2, 8, 18, 13, 1]),
            ('W', 'Tungsten', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁴\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁴\nEnergy levels: 2, 8, 18, 32, 12, 2\nQuantum numbers: l=2, m=1, n=5', '74', '183.85', [2, 8, 18, 32, 12, 2]),
            ('Sg', 'Seaborgium', 'Oxidation states: 6\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁴\nEnergy levels: 2, 8, 18, 32, 32, 12, 2\nQuantum numbers: l=2, m=1, n=6', '106', '266.00', [2, 8, 18, 32, 32, 12, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_3[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_4 = [
            ('Mn', 'Manganese', 'Oxidation states: -3, -2, -1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Ar] 4s² 3d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁵\nEnergy levels: 2, 8, 13, 2\nQuantum numbers: l=2, m=2, n=3', '25', '178.49', [2, 8, 13, 2]),
            ('Tc', 'Technetium', 'Oxidation states: -3, -1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Kr] 5s² 4d⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d⁵\nEnergy levels: 2, 8, 18, 13, 2\nQuantum numbers: l=2, m=2, n=4', '43', '178.49', [2, 8, 18, 13, 2]),
            ('Re', 'Rhenium', 'Oxidation states: -3, -1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁵\nExpanded: - \n 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁵\nEnergy levels: 2, 8, 18, 32, 13, 2\nQuantum numbers: l=2, m=2, n=5', '75', '178.49', [2, 8, 18, 32, 13, 2]),
            ('Bh', 'Bohrium', 'Oxidation states: 7\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² \n4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁵\nEnergy levels: 2, 8, 18, 32, 32, 13, 2\nQuantum numbers: l=2, m=2, n=6', '107', '262.00', [2, 8, 18, 32, 32, 13, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_4[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_5 = [
            ('Fe', 'Iron', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Ar] 4s² 3d⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶\nEnergy levels: 2, 8, 14, 2\nQuantum numbers: l=2, m=-2, n=3', '26', '55.85', [2, 8, 14, 2]),
            ('Ru', 'Ruthenium', 'Oxidation states: -2, 1, 2, 3, 4, 5, 6, 7, 8\nConfiguration: [Kr] 5s¹ 4d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d⁷\nEnergy levels: 2, 8, 18, 15, 1\nQuantum numbers: l=2, m=-1, n=4', '44', '101.07', [2, 8, 18, 15, 1]),
            ('Os', 'Osmium', 'Oxidation states: -2, 1, 2, 3, 4, 5, 6, 7, 8\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁶\nEnergy levels: 2, 8, 18, 32, 14, 2\nQuantum numbers: l=2, m=-2, n=5', '76', '190.20', [2, 8, 18, 32, 14, 2]),
            ('Hs', 'Hassium', 'Oxidation states: 8\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁶\nEnergy levels: 2, 8, 18, 32, 32, 14, 2\nQuantum numbers: l=2, m=-2, n=6', '108', '265.00', [2, 8, 18, 32, 32, 14, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_5[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_6 = [
            ('Co', 'Cobalt', 'Oxidation states: -1, 1, 2, 3, 4, 5\nConfiguration: [Ar] 4s² 3d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁷\nEnergy levels: 2, 8, 15, 2\nQuantum numbers: l=2, m=-1, n=3', '27', '58.93', [2, 8, 15, 2]),
            ('Rh', 'Rhodium', 'Oxidation states: -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Kr] 5s¹ 4d⁸\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d⁸\nEnergy levels: 2, 8, 18, 16, 1\nQuantum numbers: l=2, m=0, n=4', '45', '102.91', [2, 8, 18, 16, 1]),
            ('Ir', 'Iridium', 'Oxidation states: -3, -1, 1, 2, 3, 4, 5, 6, 7, 8\nConfiguration: [Xe] 6s² 4f¹⁴ 5d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d⁷\nEnergy levels: 2, 8, 18, 32, 15, 2\nQuantum numbers: l=2, m=-1, n=5', '77', '192.22', [2, 8, 18, 32, 15, 2]),
            ('Mt', 'Meitnerium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁷\n\nEnergy levels: 2, 8, 18, 32, 32, 15, 2\nQuantum numbers: l=2, m=-1, n=6', '109', '266.00', [2, 8, 18, 32, 32, 15, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_6[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_7 = [
            ('Ni', 'Nickle', 'Oxidation states: -1, 1, 2, 3, 4\nConfiguration: [Ar] 4s² 3d⁸\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁸\nEnergy levels: 2, 8, 16, 2\nQuantum numbers: l=2, m=2, n=3',  '28', '58.70', [2, 8, 16, 2]),
            ('Pd', 'Palladium', 'Oxidation states: 2, 4\nConfiguration: [Kr] 4d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 4d¹⁰\nEnergy levels: 2, 8, 18, 18\nQuantum numbers: l=2, m=2, n=4', '46', '106.40', [2, 8, 18, 18]),
            ('Pt', 'Platinum', 'Oxidation states: 2, 4, 5, 6\nConfiguration: [Xe] 6s¹ 4f¹⁴ 5d⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s¹ 4f¹⁴ 5d⁹\nEnergy levels: 2, 8, 18, 32, 17, 1\nQuantum numbers: l=2, m=1, n=5', '78', '195.09', [2, 8, 18, 32, 17, 1]),
            ('Ds', 'Darmstadtium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s¹ 5f¹⁴ 6d⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰\n 6p⁶ 7s¹ 5f¹⁴ 6d⁹\nEnergy levels: 2, 8, 18, 32, 32, 17, 1\nQuantum numbers: l=2, m=1, n=6', '110', '281', [2, 8, 18, 32, 32, 17, 1])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_7[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_8 = [
            ('Cu', 'Copper', 'Oxidation states: 1, 2, 3, 4\nConfiguration: [Ar] 4s¹ 3d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰\nEnergy level: 2, 8, 18, 1\nQuantum numbers: l=2, m=2, n=3', '29', '63.55', [2, 8, 18, 1]),
            ('Ag', 'Silver', 'Oxidation states: 1, 2, 3, 4\nConfiguration: [Kr] 5s¹ 4d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹ 4d¹⁰\nEnergy levels: 2, 8, 18, 18, 1\nQuantum numbers: l=2, m=2, n=4', '47', '107.97', [2, 8, 18, 18, 1]),
            ('Au', 'Gold', 'Oxidation states: -1, 1, 2, 3, 5\nConfiguration: [Xe] 6s¹ 4f¹⁴ 5d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s¹ 4f¹⁴ 5d¹⁰\nEnergy levels: 2, 8, 18, 32, 18, 1\nQuantum numbers: l=2, m=1, n=6', '79', '196.97', [2, 8, 18, 32, 18, 1]),
            ('Rg', 'Roentgenium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹\n⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d⁹\nEnergy levels: 2, 8, 18, 32, 32, 17, 2\nQuantum numbers: l=2, m=2, n=3', '111', '282', [2, 8, 18, 32, 32, 17, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_8[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        d_block_9 = [
            ('Zn', 'Zinc', 'Oxidation states: 1, 2\nConfiguration: [Ar] 4s² 3d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰\nEnergy levels: 2, 8, 18, 2\nQuantum numbers: l=2, m=2, n=3', '30', '65.37', [2, 8, 18, 2]),
            ('Cd', 'Cadmium', 'Oxidation states: 1, 2\nConfiguration: [Kr] 5s² 4d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶\n 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰\nEnergy levels: 2, 8, 18, 18, 2\nQuantum numbers: l=2, m=2, n=4', '48', '112.41', [2, 8, 18, 18, 2]),
            ('Hg', 'Mercury', 'Oxidation states: 1, 2, 4\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰\nEnergy levels: 2, 8, 18, 32, 18, 2\nQuantum numbers: l=2, m=-1, n=2', '80', '200.59', [2, 8, 18, 32, 18, 2]),
            ('Cn', 'Copernicium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰\nEnergy levels: 2, 8, 18, 32, 32, 18, 2\nQuantum numbers: l=2, m=2, n=6', '112', '285', [2, 8, 18, 32, 32, 18, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_9[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_0 = [
            ('B', 'Boron', 'Oxidation states: 1, 2, 3\nConfiguration: [He] 2s² 2p¹\nExpanded: - \n1s² 2s² 2p¹\nEnergy levels: 2, 3\nQuantum numbers: l=1, m=-1, n=2', '5', '10.81', [2, 3]),
            ('Al', 'Aluminum', 'Oxidation states: 1, 2, 3\nConfiguration: [Ne] 3s² 3p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p¹\nEnergy levels: 2, 8, 3\nQuantum numbers: l=1, m=-1, n=3', '13', '26.98', [2, 8, 3]),
            ('Ga', 'Gallium', 'Oxidation states: 1, 2, 3\nConfiguration: [Ar] 4s² 3d¹⁰ 4p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² \n3p⁶ 4s² 3d¹⁰ 4p¹\nEnergy levels: 2, 8, 18, 3\nQuantum numbers: l=1, m=-1, n=4', '31', '69.72', [2, 8, 18, 3]),
            ('In', 'Indium', 'Oxidation states: 1, 2, 3\nConfiguration: [Kr] 5s² 4d¹⁰ 5p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p¹\nEnergy levels: 2, 8, 18, 18, 3\nQuantum numbers: l=1, m=-1, n=5', '49', '69.72', [2, 8, 18, 18, 3]),
            ('Tl', 'Thallium', 'Oxidation states: 1, 3\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p¹\nEnergy levels: 2, 8, 18, 32, 18, 3\nQuantum numbers: l=1, m=-1, n=6', '81', '204.37', [2, 8, 18, 32, 18, 3]),
            ('Nh', 'Nihonium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ \n5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p¹\nEnergy levels: 2, 8, 18, 32, 32, 18, 3\nQuantum numbers: l=1, m=-1, n=7', '113', '286', [2, 8, 18, 32, 32, 18, 3])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.p_block_c_0[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_1 = [
            ('C', 'Carbon', 'Oxidation states: -4, -3, -2, -1, 1, 2, 3, 4\nConfiguration: [He] 2s² 2p²\nExpanded: - \n1s² 2s² 2p²\nEnergy levels: 2, 4\nQuantum numbers: l=1, m=0, n=2', '6', '12.01', [2, 4]),
            ('Si', 'Silicon', 'Oxidation states: -4, -3, -2, -1, 1, 2, 3, 4\nConfiguration: [Ne] 3s² 3p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p²\nEnergy levels: 2, 8, 4\nQuantum numbers: l=1, m=0, n=3', '14', '28.09', [2, 8, 4]),
            ('Ge', 'Germanium', 'Oxidation states: -4, 1, 2, 3, 4\nConfiguration: [Ar] 4s² 3d¹⁰ 4p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p²\nEnergy levels: 2, 8, 18, 4\nQuantum numbers: l=1, m=0, n=4', '32', '72.59', [2, 8, 18, 4]),
            ('Sn', 'Tin', 'Oxidation states: -4, 2, 4\nConfiguration: [Kr] 5s² 4d¹⁰ 5p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p²\nEnergy levels: 2, 8, 18, 18, 4\nQuantum numbers: l=1, m=0, n=5', '50', '118.69', [2, 8, 18, 18, 4]),
            ('Pb', 'Lead', 'Oxidation states: -4, 2, 4\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p²\nEnergy levels: 2, 8, 18, 32, 18, 4\nQuantum numbers: l=1, m=0, n=6', '82', '207.20', [2, 8, 18, 32, 18, 4]),
            ('Fl', 'Flerovium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p²\nEnergy levels: 2, 8, 18, 32, 32, 18, 4\nQuantum numbers: l=1, m=0, n=7', '114', '289', [2, 8, 18, 32, 32, 18, 4])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.p_block_c_1[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_2 = [
            ('N', 'Nitrogen', 'Oxidation states: -3, -2, -1, 1, 2, 3, 4, 5\nConfiguration: [He] 2s² 2p³\nExpanded: - \n1s² 2s² 2p³\nEnergy levels: 2, 5\nQuantum numbers: l=1, m=1, n=2', '7', '14.01', [2, 5]),
            ('P', 'Phosphorus', 'Oxidation states: -3, -2, -1, 1, 2, 3, 4, 5\nConfiguration: [Ne] 3s² 3p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p³\nEnergy levels: 2, 8, 5\nQuantum numbers: l=1, m=1, n=3', '15', '30.97', [2, 8, 5]),
            ('As', 'Arsenic', 'Oxidation states: -3, 2, 3, 5\nConfiguration: [Ar] 4s² 3d¹⁰ 4p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p³\nEnergy levels: 2, 8, 18, 5\nQuantum numbers: l=1, m=1, n=4', '33', '74.92', [2, 8, 18, 5]),
            ('Sb', 'Antimony', 'Oxidation states: -3, 3, 5\nConfiguration: [Kr] 5s² 4d¹⁰ 5p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p³\nEnergy levels: 2, 8, 18, 18, 5\nQuantum numbers: l=1, m=1, n=5', '51', '121.75', [2, 8, 18, 18, 5]),
            ('Bi', 'Bismuth', 'Oxidation states: -3, 3, 5\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p³\nEnergy levels: 2, 8, 18, 32, 18, 5\nQuantum numbers: l=1, m=1, n=6', '83', '208.98', [2, 8, 18, 32, 18, 5]),
            ('Mc', 'Moscovium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p³\nEnergy levels: 2, 8, 18, 32, 32, 18, 5\nQuantum numbers: l=1, m=1, n=7', '115', '290', [2, 8, 18, 32, 32, 18, 5])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.p_block_c_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        p_block_3 = [
            ('O', 'Oxygen', 'Oxidation states: -2, -1, 1, 2\n Configuration: [He] 2s² 2p⁴\nExpanded: - \n1s² 2s² 2p⁴\nEnergy levels: 2, 6\nQuantum numbers: l=1, m=-1, n=2', '8', '15.99', [2, 6]),
            ('S', 'Sulfur', 'Oxidation states: -2, -1, 1, 2, 3, 4, 5, 6\nConfiguration: [Ne] 3s² 3p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁴\nEnergy levels: 2, 8, 6\nQuantum numbers: l=1, m=-1, n=3', '16', '32.06', [2, 8, 6]),
            ('Se', 'Selenium', 'Oxidation states: -2, 1, 2, 4, 6\nConfiguration: [Ar] 4s² 3d¹⁰ 4p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁴\nEnergy levels: 2, 8, 18, 6\nQuantum numbers: l=1, m=-1, n=4' '34', '78.96', [2, 8, 18, 6]),
            ('Te', 'Tellurium', 'Oxidation states: -2, 2, 4, 5, 6\nConfiguration: [Kr] 5s² 4d¹⁰ 5p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁴\nEnergy levels: 2, 8, 18, 18, 6\nQuantum numbers: l=1, m=-1, n=5', '52', '127.60', [2, 8, 18, 18, 6]),
            ('Po', 'Polonium', 'Oxidation states: -2, 2, 4, 6\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁴\nEnergy levels: 2, 8, 18, 32, 18, 6\nQuantum numbers: l=1, m=-1, n=6', '84', '209.00', [2, 8, 18, 32, 18, 6]),
            ('Lv', 'Livermorium', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ \n5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁴\nEnergy levels: 2, 8, 18, 32, 32, 18, 6\nQuantum numbers: l=1, m=-1, n=7', '116', '293.00', [2, 8, 18, 32, 32, 18, 6])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.p_block_c_3[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        p_block_4 = [
            ('F', 'Fluorine', 'Oxidation states: -1\nConfiguration: [He] 2s² 2p⁵\nExpanded: - \n1s² 2s² 2p⁵\nEnergy levels: 2, 7\nQuantum numbers: l=1, m=0, n=2', '9', '18.99', [2, 7]),
            ('Cl', 'Chlorine', 'Oxidation states: \n-1, 1, 2, 3, 4, 5, 6, 7\nConfiguration: [Ne] 3s² 3p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁵\nEnergy levels: 2, 8, 7\nQuantum numbers: l=1, m=0, n=3', '17', '35.45', [2, 8, 7]),
            ('Br', 'Bromine', 'Oxidation states: -1, 1, 3, 4, 5, 7\nConfiguration: [Ar] 4s² 3d¹⁰ 4p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁵\nEnergy levels: 2, 8, 18, 7\nQuantum numbers: l=1, m=0, n=4', '35', '79.90', [2, 8, 18, 7]),
            ('I', 'Iodine', 'Oxidation states: -1, 1, 3, 4, 5, 7\nConfiguration: [Kr] 5s² 4d¹⁰ 5p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁵\nEnergy levels: 2, 8, 18, 18, 7\nQuantum numbers: l=1, m=0, n=5', '53', '126.90', [2, 8, 18, 18, 7]),
            ('At', 'Astatine', 'Oxidation states: -1, 1, 3, 5, 7\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰\n 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁵\nEnergy levels: 2, 8, 18, 32, 18, 7\nQuantum numbers: l=1, m=0, n=6', '85', '210.00', [2, 8, 18, 32, 18, 7]),
            ('Ts', 'Tennessine', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁵\nEnergy levels: 2, 8, 18, 32, 32, 18, 7\nQuantum numbers: l=1, m=0, n=7', '117', '294.00', [2, 8, 18, 32, 32, 18, 7])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.p_block_c_4[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        s_block_2 = [
            ('He', 'Helium', 'Oxidation states: N/A\nConfiguration: 1s²\nExpanded: - \n1s²\nEnergy levels: 2\nQuantum numbers: l=0, m=0, n=1', '2', '4.00', [2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorS, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.s_block_c_2[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        p_block_5 = [
            ('Ne', 'Neon', 'Oxidation states: N/A\nConfiguration: [He] 2s² 2p⁶\nExpanded: - \n1s² 2s² 2p⁶\nEnergy levels: 2, 8\nQuantum numbers: l=1, m=1, n=2', '10', '20.18', [2, 8]),
            ('Ar', 'Argon', 'Oxidation states: N/A\nConfiguration: [Ne] 3s² 3p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶\nEnergy levels: 2, 8, 8\nQuantum numbers: l=1, m=1, n=3', '18', '39.95', [2, 8, 8]),
            ('Kr', 'Krypton', 'Oxidation states: 2\nConfiguration: [Ar] 4s² 3d¹⁰ 4p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶\nEnergy levels: 2, 8, 18, 8\nQuantum numbers: l=1, m=1, n=4', '36', '83.80', [2, 8, 18, 8]),
            ('Xe', 'Xenon', 'Oxidation states: 2, 4, 6, 8\nConfiguration: [Kr] 5s² 4d¹⁰ 5p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶\nEnergy levels: 2, 8, 18, 18, 8\nQuantum numbers: l=1, m=1, n=5', '54', '131.30', [2, 8, 18, 18, 8]),
            ('Rn', 'Radon', 'Oxidation states: 2\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹⁰ 6p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶\nEnergy levels: 2, 8, 18, 32, 18, 8\nQuantum numbers: l=1, m=1, n=6', '86', '222.00', [2, 8, 18, 32, 18, 8]),
            ('Og', 'Oganesson', 'Oxidation states: N/A\nConfiguration: [Rn] 7s² 5f¹⁴ 6d¹⁰ 7p⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4\nf¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 6d¹⁰ 7p⁶\nEnergy levels: 2, 8, 18, 32, 32, 18, 8\nQuantum numbers: l=1, m=1, n=7', '118', '294.00', [2, 8, 18, 32, 32, 18, 8])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorP, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.p_block_c_5[b[0]].grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1
                
        self.fillerLine = tk.Label(self, text="")
        self.fillerLine.grid(row=12, column=0)
        
        f_block_2 = [
            ('Ce', 'Cerium', 'Oxidation states: 2, 3, 4\nConfiguration: [Xe] 6s² 4f¹ 5d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹ 5d¹\nEnergy levels: 2, 8, 18, 19, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '58', '140.12', [2, 8, 18, 19, 9, 2]),
            ('Pr', 'Praseodymium', 'Oxidation states: 2, 3, 4\nConfiguration: [Xe] 6s² 4f³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f³\nEnergy levels: 2, 8, 18, 21, 8, 2\nQuantum numbers: l=3, m=-1, n=4', '59', '140.91', [2, 8, 18, 21, 8, 2]),
            ('Nd', 'Neodymium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁴\nEnergy levels: 2, 8, 18, 22, 8, 2\nQuantum numbers: l=3, m=0, n=4', '60', '144.24', [2, 8, 18, 22, 8, 2]),
            ('Pm', 'Promethium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f⁵\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁵\nEnergy levels: 2, 8, 18, 23, 8, 2\nQuantum numbers: l=3, m=1, n=4', '61', '145.00', [2, 8, 18, 23, 8, 2]),
            ('Sm', 'Samarium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁶\nEnergy levels: 2, 8, 18, 24, 8, 2\nQuantum numbers: l=3, m=2, n=4', '62', '150.40', [2, 8, 18, 24, 8, 2]),
            ('Eu', 'Europium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁷\nEnergy levels: 2, 8, 18, 25, 8, 2\nQuantum numbers: l=3, m=3, n=4', '63', '151.96', [2, 8, 18, 25, 8, 2]),
            ('Gd', 'Gadolinium', 'Oxidation states: 1, 2, 3\nConfiguration: [Xe] 6s² 4f⁷ 5d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰\n 5p⁶ 6s² 4f⁷ 5d¹\nEnergy levels: 2, 8, 18, 25, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '64', '157.25', [2, 8, 18, 25, 9, 2]),
            ('Tb', 'Oxidation states: 1, 3, 4\nConfiguration: [Xe] 6s² 4f⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f⁹\nEnergy levels: 2, 8, 18, 27, 8, 2\nQuantum numbers: l=3, m=-2, n=4', '65', '158.93', [2, 8, 18, 27, 8, 2]),
            ('Dy', 'Dyprosium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁰\nEnergy levels: 2, 8, 18, 28, 8, 2\nQuantum numbers: l=3, m=-1, n=4', '66', '162.50', [2, 8, 18, 28, 8, 2]),
            ('Ho', 'Holmium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f¹¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹¹\nEnergy levels: 2, 8, 18, 29, 8, 2nQuantum numbers: l=3, m=0, n=4', '67', '164.93', [2, 8, 18, 29, 8, 2]),
            ('Er', 'Erbium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f¹²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹²\nEnergy levels: 2, 8, 18, 30, 8, 2\nQuantum numbers: l=3, m=1, n=4', '68', '167.26', [2, 8, 18, 30, 8, 2]),
            ('Tm', 'Thulium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f¹³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹³\nEnergy levels: 2, 8, 18, 31, 8, 2\nQuantum numbers: l=3, m=2, n=4', '69', '168.93', [2, 8, 18, 31, 8, 2]),
            ('Yb', 'Ytterbium', 'Oxidation states: 2, 3\nConfiguration: [Xe] 6s² 4f¹⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴\nEnergy levels: 2, 8, 18, 32, 8, 2\nQuantum numbers: l=3, m=3, n=4', '70', '173.04', [2, 8, 18, 32, 8, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorF, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.f_block_c_2[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        d_block_20 = [
            ('Lu', 'Lutetium', 'Oxidation states: 3\nConfiguration: [Xe] 6s² 4f¹⁴ 5d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ \n4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹\nEnergy levels: 2, 8, 18, 32, 9, 2\nQuantum numbers: l=2, m=-2, n=5', '71', '174.97', [2, 8, 18, 32, 9, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_20[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        f_block_3 = [
            ('Th', 'Thorium', 'Oxidation states: 2, 3, 4\nConfiguration: [Rn] 7s² 6d²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 6d²\nEnergy levels: 2, 8, 18, 32, 18, 10, 2\nQuantum numbers: l=2, m=-1, n=6', '90', '232.04', [2, 8, 18, 32, 18, 10, 2]),
            ('Pa', 'Protactinium', 'Oxidation states: 2, 3, 4, 5\nConfiguration: [Rn] 7s² 5f² 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f² 6d¹\nEnergy levels: 2, 8, 18, 32, 20, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '91', '231.04', [2, 8, 18, 32, 20, 9, 2]),
            ('U', 'Uranium', 'Oxidation states: 2, 3, 4, 5, 6\nConfiguration: [Rn] 7s² 5f³ 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f³ 6d¹\nEnergy levels: 2, 8, 18, 32, 21, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '92', '238.03', [2, 8, 18, 32, 21, 9, 2]),
            ('Np', 'Neptunium', 'Oxidation states: 3, 4, 5, 6, 7\nConfiguration: [Rn] 7s² 5f⁴ 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁴ 6d¹\nEnergy levels: 2, 8, 18, 32, 22, 9, 2\nQuantum numbers: l=2, m=-2, n=6', '93', '237.05', [2, 8, 18, 32, 22, 9, 2]),
            ('Pu', 'Plutonium', 'Oxidation states: 3, 4, 5, 6, 7, 8\nConfiguration: [Rn] 7s² 5f⁶\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁶\nEnergy levels: 2, 8, 18, 32, 24, 8, 2\nQuantum numbers: l=3, m=3, n=5', '94', '244.00', [2, 8, 18, 32, 24, 8, 2]),
            ('Am', 'Americium', 'Oxidation states: 2, 3, 4, 5, 6\nConfiguration: [Rn] 7s² 5f⁷\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ \n4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ \n5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁷\nEnergy levels: 2, 8, 18, 32, 25, 8, 2\nQuantum numbers: l=3, m=3, n=5', '95', '243.00', [2, 8, 18, 32, 25, 8, 2]),
            ('Cm', 'Curium', 'Oxidation states: 3, 4\nConfiguration: [Rn] 7s² 5f⁷ 6d¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f⁷ 6d¹\nEnergy levels: 2, 8, 18, 32, 25, 9, 2\nQuantum numbers; l=2, m=-2, n=6', '96', '247.00', [2, 8, 18, 32, 25, 9, 2]),
            ('Bk', 'Berkelium', 'Oxidation states: 3, 4\nConfiguration: [Rn] 7s² 5f⁹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ \n5d¹⁰ 6p⁶ 7s² 5f⁹\nEnergy levels: 2, 8, 18, 32, 27, 8, 2\nQuantum numbers: l=3, m=-2, n=5', '97', '247.00', [2, 8, 18, 32, 27, 8, 2]),
            ('Cf', 'Californium', 'Oxidation states: 2, 3, 4\nConfiguration: [Rn] 7s² 5f¹⁰\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s²\n 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶\n 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁰\nEnergy levels: 2, 8, 18, 32, 28, 8, 2\nQuantum numbers: l=3, m=-1, n=5', '98', '247.00', [2, 8, 18, 32, 28, 8, 2]),
            ('Es', 'Einsteinium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹¹\nEnergy levels: 2, 8, 18, 32, 29, 8, 2\nQuantum numbers: l=3, m=0, n=5', '99', '252.00', [2, 8, 18, 32, 29, 8, 2]),
            ('Fm', 'Fermium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹²\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹²\nEnergy levels: 2, 8, 18, 32, 30, 8, 2\nQuantum numbers: l=3, m=1, n=5', '100', '257.00', [2, 8, 18, 32, 30, 8, 2]),
            ('Md', 'Mendelevium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹³\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ \n5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹³\nEnergy levels: 2, 8, 18, 32, 31, 8, 2\nQuantum numbers: l=3, m=2, n=5', '101', '260.00', [2, 8, 18, 32, 31, 8, 2]),
            ('No', 'Nobelium', 'Oxidation states: 2, 3\nConfiguration: [Rn] 7s² 5f¹⁴\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ \n6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴\nEnergy levels: 2, 8, 18, 32, 32, 8, 2\nQuantum numbers: l=3, m=3, n=5', '102', '259.00', [2, 8, 18, 32, 32, 8, 2])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorF, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.f_block_c_3[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1

        d_block_21 = [
            ('Lr', 'Lawrencium', 'Oxidation states: 3\nConfiguration: [Rn] 7s² 5f¹⁴ 7p¹\nExpanded: - \n1s² 2s² 2p⁶ 3s² 3p⁶ 4s² \n3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² \n4f¹⁴ 5d¹⁰ 6p⁶ 7s² 5f¹⁴ 7p¹\nEnergy levels: 2, 8, 18, 32, 32, 8, 3\nQuantum numbers: l=1, m=-1, n=7', '103', '262.00', [2, 8, 18, 32, 32, 8, 3])]
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
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[1]) + self.info(text[2]), self.voice(text[1]), self.canva(colorD, text[0], text[3], text[4]), self.canv_img(text[0]), self.turtle_bohr(len(text[5]), text[5])])
            self.d_block_c_21[b[0]].grid(row=r, column=c)
            c += 1
            if c > 20: 
                c = 1
                r += 1
        """===============================================================BLOCK_Buttons============================================================"""

        S_BLOCK = [('S block', 'S block elements', 'S-')]
        r = 1
        c = 3
        for b in S_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="pink",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.s_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        P_BLOCK = [('P block', 'P block elements', 'P-')]
        r = 1
        c = 13
        for b in P_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="Aquamarine",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.p_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        D_BLOCK = [('D block', 'D block elements', 'D-')]
        r = 1
        c = 5
        for b in D_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="light goldenrod",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.d_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1

        F_BLOCK = [('F block', 'F block elements', 'F-')]
        r = 1
        c = 15
        for b in F_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="Teal",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.f_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
            r += 1
            if r > 9:
                r = 1
                c += 1
        
        All_BLOCK = [('All blocks', 'All elements', 'All')]
        r = 1
        c = 17
        for b in All_BLOCK:
            tk.Button(self,
                      text=b[0],
                      width=11,
                      height=2,
                      font=10,
                      borderwidth=3,
                      bg="white",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.all_block(), self.voice(text[1])]).grid(row=r, column=c, columnspan=2, rowspan=1)
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

        self.turtle_B = Canvas(self, height=290, width=300, bg="white", borderwidth=0.5)
        self.turtle_B.grid(row=0, column=7, rowspan=6, columnspan=6)

        self.canvas = Canvas(self, height=100, width=100, bg="pink", relief=GROOVE, borderwidth=0)
        #canvas.pack()
        self.canvas.create_rectangle(100, 100, 0, 0)
        self.canvas.grid(row=1, column=0, rowspan=2)
        self.sy = self.canvas.create_text(50, 50, text="H", fill="black", font=('Helvetica 15 bold', 35))
        self.an = self.canvas.create_text(10, 12, text="1", fill="black", font=('Helvetica 15 bold', 10))
        self.am = self.canvas.create_text(17, 90, text="1.001", fill="black", font=('Helvetica 15 bold', 8))
        
        self.infoLine = tk.Label(self, text="Oxidation states -1, 1\nConfiguration 1s¹\nExpanded - \n1s¹\nEnergy levels 1\nQuantum numbers l=0, m=0, n=1", justify='left', font=10)
        self.infoLine.grid(row=3, column=0, rowspan=4)
        #setting up voice

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
        if text =="close":
            user_input = "clear"
            byte_msg = user_input.encode('utf-8')
            time.sleep(0.1)
            nano.write(byte_msg)
            nano.close()
        else:
            time.sleep(0.1)
            byte_msg = text.encode('utf-8')
            nano.write(byte_msg)
        time.sleep(2)

    beSound = True
    # voice description
    def voice(self, text):
        if self.beSound:
            engine.say(text)
            engine.runAndWait()

    def pen_jump(self, pen, x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()


    def turtle_pen(self, shape="turtle", speed=10, size=2, colors=("blue", "green")):
        pen = turtle.RawTurtle(self.turtle_B)
        pen.shape(shape)
        pen.shapesize(1, 1, 1)
        #pen.shape(shape)
        pen.speed(speed)
        pen.pensize(size)
        pen.color(*colors)
        self.pen_jump(pen, 0, 0)
        pen.stamp()
        return pen


    def draw_atom(self, pen, radius, levels, electrons_per_level, electron_size=15, electron_color="red"):
        full_circle = 360
        for level in range(levels):
            r = radius * (level + 1)                           # concentric circles
            electrons_in_level = electrons_per_level[level]
            arcs = full_circle / electrons_in_level            # arcs between each electron
            circumference = 0
            self.pen_jump(pen, 0, -r)                               # centering
            while circumference < full_circle:
                pen.dot(electron_size, electron_color)
                pen.circle(r, arcs)
                circumference = circumference + arcs

    
    
    def turtle_bohr(self, levels, totalE):
        #t = turtle.RawTurtle(self.turtle_B)
        first_level_radius = 20
        self.turtle_B.delete("all")
        pen = self.turtle_pen()
        self.draw_atom(pen, first_level_radius, levels, totalE)
        pen.hideturtle()



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
    """=======================================blocks==================================="""
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.topLabel = tk.Label(self, text="Compounds", font=('Helvetica 15 bold', 15), bg=bacG)
        self.topLabel.grid(row=0, column=0)

        H = ('H', 'Hydrogen', """'H2 hydrogen \n''3HH tritium hydride \n''AsH3 arsine \n''As2H4 diarsine\n''B2D6 diborane-d 610%in D2,electronic grade''B2H6 diborane \n''B4H10 tetraborane(10) \n''B5H9 pentaborane(9) \n''B5H11 pentaborane(11) \n''B6H10 hexaborane(10) \n''B6H12 hexaborane(12) \n''B9H15 nonaborane(15) \n''B10H14 decaborane(14) \n''B10H16 decaborane(16) \n''B12H16 dodecaborane(16) \n''B13H19 tridecaborane(19) \n''B14H18 tetradecaborane(18) \n''B16H20 hexadecaborane(20) \n''B18H22 octadecaborane(22) \n''BaH2 barium hydride \n''BeH2 beryllium hydride \n''DBr·D2O deuterium bromide \n''HBr hydrogen bromide \n''CD4 methane-d 4 \n''13CD4 methane-13 C,d 4 \n''H213C=13CH2 ethylene-13 C2 \n''CH4 liquid methane \n''CH4 methane \n''13CH4 methane-13 C \n''13C6H6 benzene-13 C6 \n''13CH313CH3 ethane-13 C2 \n''C2D2 acetylene-d 2 \n''CD2=CD2 ethylene-d 4 \n''(CD2CD2)n poly(ethylene-d 4) \n''CD3CD3 ethane-d 6 \n''C2H2 acetylene \n''CH2=CH2 ethylene \n''C2H4 poly(ethylene) chlorosulfonated \n''H(CH2CH2)nH polyethylene \n''CH3(CH2CH2)nCH2OH polyethylene monoalcohol \n''CH3CH3 ethane \n''C2H8 terminal dimethyl \n''CD3CD=CD2 propene-d 6 \n''CD3CD2CD3 propane-d 8 \n''H2C=C=CH2 propadiene \n''C3H4 cyclopropene \n''CH3C≡CH methylacetylene \n''C3H6 cyclopropane \n''[CH2CH(CH3)]n polypropylene \n''[CH2CH(CH3)]n polypropylene,isotactic \n''CH3CH=CH2 propylene \n''CH3CH2CH3 propane \n''D2C=CDCD=CD2 1,3-butadiene-d 6 \n''CD3CD2CD2CD3 butane-d 10 \n''C4H2 1,3-butadiyne \n''C4H4 1-buten-3-yne \n''C4H6 1,2-butadiene \n''CH2=CHCH=CH2 1,3-butadiene \n''CH3CH2C≡CH 1-butyne \n''CH3C≡CCH3 2-butyne \n''C4H6 cyclobutene \n''(CH2CH=CHCH2)n 1,3-butadiene, homopolymer \n''HO2C(CH2CH=CHCH2)nCO2H polybutadiene,dicarboxy terminated \n''CH2=CHCH2CH3 1-butene \n''CH3CH=CHCH3 butene (mixed isomers) \n''(CH3)2C=CH2 isobutylene \n''CH3CH=CHCH3 cis-2-butene \n''C4H8 cyclobutane \n''C4H8 methylcyclopropane \n''[CH2CH(C2H5)]n poly(1-butene),isotactic \n''[CH2C(CH3)2]n polyisobutylene \n''CH3CH=CHCH3 trans-2-butene \n''(CH3)3CH isobutane \n''CH3CH2CH2CH3 butane \n''CD3(CD2)3CD3 pentane-d 12 \n''C5H4 1,3-pentadiyne \n''C5H6 1,3-cyclopentadiene \n''C5H6 1-penten-3-yne \n''H2C=C(CH3)C≡CH 2-methyl-1-buten-3-yne \n''C5H6 (3Z)-3-penten-1-yne \n''(C3H5)C≡CH cyclopropylacetylene \n''C5H6 (E)-3-penten-1-yne \n''C5H8 1,2-pentadiene \n''CH2=CHCH=CHCH3 piperylene \n''CH2=CHCH2CH=CH 1,4-pentadiene \n''C5H8 1-methyl-1-cyclobutene \n''CH3CH2CH2C≡CH 1-pentyne \n''C5H8 2,3-pentadiene \n''CH3C≡CCH2CH3 2-pentyne \n''(CH3)2C=C=CH2 3-methyl-1,2-butadiene \n''C5H8 3-methyl-1-butyne \n''CH3CH=CHCH=CH2 cis-1,3-pentadiene \n''C5H8 cyclopentene \n''CH2=CHC(CH3)=CH2 isoprene \n''C4H6(=CH2) methylenecyclobutane \n''[CH2CH=C(CH3)CH2]n polyisoprene,cis 97%cis-1,4 \n''[CH2CH=C(CH3)CH2]n polyisoprene,trans pellets,99+%trans-1,4 \n''C5H8 spiropentane \n''CH3CH=CHCH=CH2 trans-1,3-pentadiene \n''C5H10 1,1-dimethylcyclopropane \n''CH3CH2CH2CH=CH2 1-pentene \n''CH3CH2C(CH3)=CH2 2-methyl-1-butene \n''CH3CH=C(CH3)2 2-methyl-2-butene \n''CH3CH2CH=CHCH3 2-pentene \n''(CH3)2CHCH=CH2 3-methyl-1-butene \n''CH3(CHCH2CH)CH3 cis-1,2-dimethylcyclopropane \n''C2H5CH=CHCH3 cis-2-pentene \n''C5H10 cyclopentane \n''C5H10 ethylcyclopropane \n''C5H10 isopentene \n''C5H10 methylbut-1-ene \n''C5H10 methylcyclobutane \n''C5H10 pentene \n''[CH2CH(CH3)]x(CH2CH2)y poly(ethylene-co-propylene) \n''CH3(CHCH2CH)CH3 trans-1,2-dimethylcyclopropane \n''C2H5CH=CHCH3 trans-2-pentene \n''C5H12 2,2-dimethylpropane \n''CH3CH2CH(CH3)2 isopentane \n''CH3(CH2)3CH3 N-pentane \n''C6D6 deuterated benzene (D6) \n''C6D10 cyclohexene-d 10 \n''C6D12 deuterated cyclohexane (D12) \n''CD3CD2CD2CD(CD3)2 2-methylpentane-d 14 \n''CD3(CD2)4CD3 deuterated hexane (D14) \n''C6H6 1,3-hexadien-5-yne \n''C6H6 1,4-hexadiyne \n''C6H6 1,5-hexadien-3-yne \n''C6H6 1,5-hexadiyne \n''C6H6 2,4-hexadiyne \n''C6H6benzene \n''C6H8 1,2-bis(methylene)cyclobutane \n''H2C=CHCH=CHCH=CH2 1,3,5-hexatriene \n''C6H8 1,3-cyclohexadiene \n''C6H8 1,4-cyclohexadiene \n''C6H8 1-hexen-3-yne \n''C6H8 2-methyl-1-penten-3-yne \n''C6H8 3-methyl-3-penten-1-yne \n''C6H8 3-methylenepent-1-yne \n''C6H8 cis-1,3,5-hexatriene \n''C6H8 cyclohexadiene \n''C6H8 MAPP \n''C6H8 methylcyclopentadiene \n''C6H8 trans-1,3,5-hexatriene \n''C6H10 1,2-hexadiene \n''C2H5CH=CHCH=CH2 1,3-hexadiene \n''CH3CH=CHCH2CH=CH2 1,4-hexadiene \n''H2C=CHCH2CH2CH=CH2 1,5-hexadiene \n''CH3(CH2)3C≡CH 1-hexyne \n''C5H7CH3 1-methylcyclopentene \n''C6H10 (1-methylethenyl)cyclopropane \n''CH2=C(CH3)C(CH3)=CH2 2,3-dimethyl-1,3-butadiene \n''C6H10 2,3-hexadiene \n''C6H10 2,4-hexadiene \n''C6H10 2-ethyl-1,3-butadiene \n''CH3CH2CH2C≡CCH3 2-hexyne \n''C6H10 2-methyl-1,3-pentadiene \n''H2C=CHCH2C(CH3)=CH2 2-methyl-1,4-pentadiene \n''C6H10 2-methyl-2,3-pentadiene \n''(CH3)3CC≡CH 3,3-dimethyl-1-butyne \n''C2H5C≡CC2H5 3-hexyne \n''C6H10 1-ethyl-1-methylallene \n''CH3CH=C(CH3)CH=CH2 3-methyl-1,3-pentadiene \n''CH2=CHCH(CH3)CH=CH2 3-methyl-1,4-pentadiene \n''C6H10 3-methyl-1-pentyne \n''C6H10 3-methylcyclopentene \n''C6H10 4-methyl-1,2-pentadiene \n''C6H10 4-methyl-1,3-pentadiene \n''CH≡CCH2CH(CH3)2 4-methyl-1-pentyne \n''CH3CH(CH3)C≡CCH3 4-methyl-2-pentyne \n''C6H10 4-methylcyclopentene \n''C6H10 cis,cis-2,4-hexadiene \n''C6H10 cis-1,3-hexadiene \n''C6H10 cis-1,4-hexadiene \n''C6H10 cyclohexene \n''C6H10 (E)-1,3-hexadiene \n''C6H10 1,3-pentadiene, 4-methyl- \n''C5H8(=CH2) methylenecyclopentane \n''C6H10 trans,cis-2,4-hexadiene \n''C6H10 trans,trans-2,4-hexadiene \n''C6H10 trans-1,4-hexadiene \n''CH3CH=CHC(CH3)=CH2 trans-2-methylpenta-1,3-diene \n''C6H10 (Z)-2-methyl-1,3-pentadiene \n''C6H12 1,1,2-trimethylcyclopropane \n''C6H12 1-ethyl-1-methylcyclopropane \n''CH3(CH2)3CH=CH2 1-hexene \n''(CH3)2CHC(CH3)=CH2 2,3-dimethyl-1-butene \n''(CH3)2C=C(CH3)2 2,3-dimethyl-2-butene \n''CH3CH2C(C2H5)=CH2 2-ethyl-1-butene \n''CH3CH2CH2CH=CHCH3 2-hexene \n''CH3CH2CH2C(CH3)=CH2 2-methyl-1-pentene \n''CH3CH2CH=C(CH3)2 2-methyl-2-pentene \n''C6H12 2-methylpentene \n''(CH3)3CCH=CH2 3,3-dimethyl-1-butene \n''C6H12 3-hexene \n''CH3CH2CH(CH3)CH=CH2 3-methyl-1-pentene \n''C2H5C(CH3)=CHCH3 3-methyl-2-pentene \n''(CH3)2CHCH2CH=CH2 4-methyl-1-pentene \n''C6H12 4-methyl-2-pentene \n''C6H12 4-methyl-trans-2-pentene \n''C6H12 cis-1-ethyl-2-methylcyclopropane \n''CH3CH2CH2CH=CHCH3 cis-2-hexene \n''C6H12 cis-3-hexene \n''C6H12 cis-3-methyl-2-pentene \n''(CH3)2CHCH=CHCH3 4-methyl-cis-2-pentene \n''C6H12 cyclohexane \n''C6H12 ethylcyclobutane \n''C6H12 hexene \n''C6H12 isopropylcyclopropane \n''C5H9CH3 methyl cyclopentane \n''(CH2CH[CH2CH(CH3)2])n poly(4-methyl-1-pentene) \n''(CH2CH2)x[CH2CH(C2H5)]y poly(ethylene-co-1-butene) \n''C6H12 propylcyclopropane \n''C6H12 propylene dimer \n''CH3CH2CH2CH=CHCH3 trans-2-hexene \n''C2H5CH=CHC2H5 trans-3-hexene \n''C6H12 trans-3-methyl-2-pentene \n''CH3CH2C(CH3)3 2,2-dimethylbutane \n''(CH3)2CHCH(CH3)2 2,3-dimethylbutane \n''CH3CH2CH2CH(CH3)2 2-methylpentane \n''(CH3CH2)2CH2CH3 3-methylpentane \n''CH3(CH2)4CH3 N-hexane \n''C6D5CD3 deuterated toluene (D8) \n''C6D11CD3 deuterated methylcyclohexane (D14) \n''CD3(CD2)2CD(CD3)CD2CD3 3-methylhexane-d 16 \n''CD3(CD2)5CD3 heptane-d 16 \n''HC≡C(CH2)3C≡CH 1,6-heptadiyne \n''C7H8 1,5-hexadien-3-yne, 2-methyl \n''C7H8 6-methylfulvene \n''C7H8 2,5-norbornadiene \n''C7H8 cycloheptatriene \n''C7H8 quadricyclane \n''C6H5CH3 toluene \n''C7H10 1,3-cycloheptadiene \n''C7H10 1-methyl-1,3-cyclohexadiene \n''C7H10 1-methyl-1,4-cyclohexadiene \n''C7H10 2-methyl-1,3-cyclohexadiene \n''C2H5C≡CC(CH3)=CH2 2-methyl-1-hexen-3-yne \n''C7H10 2-norbornene \n''C7H10 cyclopentylacetylene \n''C7H10 methylcyclohexadiene \n''C7H12 1,1'-methylenebiscyclopropane \n''C7H12 1,2-dimethylcyclopentene \n''C7H12 1,2-heptadiene \n''C7H12 1,3-dimethylcyclopentene \n''C7H12 1,4-dimethylcyclopentene \n''C7H12 1,5-dimethylcyclopentene \n''C7H12 1,5-heptadiene \n''CH2=CH(CH2)3CH=CH2 1,6-heptadiene \n''C7H12 1-ethylcyclopentene \n''CH3(CH2)4C≡CH 1-heptyne \n''C6H9CH3 1-methylcyclohexene \n''C7H12 1-methylbicyclo[3.1.0]hexane \n''(CH3)2C=CHC(CH3)=CH2 2,4-dimethyl-1,3-pentadiene \n''(CH3)2C=C=C(CH3)2 tetramethylallene \n''C7H12 2,4-heptadiene \n''CH3(CH2)3C≡CCH3 2-heptyne \n''CH2=CHCH2CH2C(CH3)=CH2 2-methyl-1,5-hexadiene \n''C7H12 3,3-dimethyl-1-pentyne \n''C7H12 3,3-dimethylcyclopentene \n''C7H12 3-ethylcyclopentene \n''CH3CH2C≡C(CH2)2CH3 3-heptyne \n''HC≡CCH(CH3)CH2CH2CH3 3-methyl-1-hexyne \n''C6H9CH3 3-methylcyclohexene \n''C7H12 4,4-dimethyl-2-pentyne \n''C7H12 4,4-dimethylcyclopentene \n''C6H9CH3 4-methylcyclohexene \n''HC≡CCH2CH2CH(CH3)2 5-methyl-1-hexyne \n''C7H12 5-methyl-2-hexyne \n''C7H12 bicyclo[4.1.0]heptane \n''C7H12 cis-3,4-dimethylcyclopentene \n''C7H12 cycloheptene \n''C7H12 ethylidenecyclopentane \n''C7H12 cyclohexene, 1-methyl- \n''C6H10(=CH2) methylenecyclohexane \n''C7H12 bicyclo[2.2.1]heptane \n''C7H12 3-methylcyclohexene, (+/-) \n''C7H12 trans-3,4-dimethylcyclopentene \n''C5H9CH=CH2 vinylcyclopentane \n''C7H14 1,1,2,2-tetramethylcyclopropane \n''C7H14 1,1-diethylcyclopropane \n''C7H14 1,1-dimethylcyclopentane \n''C7H14 1,2-dimethylcyclopentane \n''C7H14 1,3-dimethylcyclopentane \n''CH3(CH2)4CH=CH2 1-heptene \n''(CH3)3CC(CH3)=CH2 2,3,3-trimethyl-1-butene \n''C7H14 2,3-dimethyl-1-pentene \n''C7H14 2,3-dimethyl-2-pentene \n''C7H14 2,4-dimethyl-1-pentene \n''C7H14 2,4-dimethyl-2-pentene \n''C7H14 2-ethyl-1-pentene \n''C7H14 2-ethyl-3-methyl-1-butene \n''C7H14 2-heptene \n''CH3(CH2)3C(CH3)=CH2 2-methyl-1-hexene \n''C7H14 2-methyl-2-hexene \n''C7H14 3,3-dimethyl-1-pentene \n''C7H14 3,4-dimethyl-1-pentene \n''C7H14 3,4-dimethyl-2-pentene \n''C7H14 3-ethyl-1-pentene \n''CH3CH=C(CH2CH3)2 3-ethyl-2-pentene \n''C7H14 3-heptene \n''C7H14 3-methyl-1-hexene \n''CH2=CHCH2C(CH3)3 4,4-dimethyl-1-pentene \n''C7H14 4-methyl-1-hexene \n''C7H14 4-methyl-2-hexene \n''C7H14 5-methyl-1-hexene \n''C7H14 5-methyl-2-hexene \n''C7H14 cis-1,2-dimethylcyclopentane \n''C7H14 cis-1,3-dimethylcyclopentane \n''CH3(CH2)3CH=CHCH3 cis-2-heptene \n''C7H14 cis-2-methyl-3-hexene \n''C7H14 cis-3,4-dimethyl-2-pentene \n''CH3CH2CH2CH=CHC2H5 cis-3-heptene \n''C7H14 cis-3-methyl-2-hexene \n''C7H14 cis-3-methyl-3-hexene \n''C7H14 cis-4,4-dimethyl-2-pentene \n''C7H14 cis-5-methyl-2-hexene \n''C7H14 cycloheptane \n''C7H14 dimethylcyclopentane \n''C7H14 (E)-3-methyl-3-hexene \n''C5H9C2H5 ethylcyclopentane \n''C7H14 heptene \n''C6H11CH3 methylcyclohexane \n''[CH2CH(CH3)]x[CH2CH(C2H5)]y 1-butene-1-propene copolymer \n''C7H14 trans-1,2-dimethylcyclopentane \n''C7H14 trans-1,3-dimethylcyclopentane \n''CH3(CH2)3CH=CHCH3 trans-2-heptene \n''C7H14 trans-2-methyl-3-hexene \n''C7H14 trans-3,4-dimethyl-2-pentene \n''CH3CH2CH2CH=CHC2H5 trans-3-heptene \n''C7H14 trans-4,4-dimethyl-2-pentene \n''C7H14 trans-4-methyl-2-hexene \n''C7H14 trans-5-methyl-2-hexene \n''C7H14 (Z)-4-methyl-2-hexene \n''(CH3)2CHC(CH3)3 2,2,3-trimethylbutane \n''CH3CH2CH2C(CH3)3 2,2-dimethylpentane \n''C2H5CH(CH3)CH(CH3)2 2,3-dimethylpentane \n''(CH3)2CHCH2CH(CH3)2 2,4-dimethylpentane \n''CH3(CH2)3CH(CH3)2 2-methylhexane \n''CH3CH2C(CH3)2CH2CH3 3,3-dimethylpentane \n''C7H16 3-ethylpentane \n''CH3CH2CH2CH(CH3)CH2CH3 3-methylhexane \n''CH3(CH2)5CH3 N-heptane \n''C7H16 isoheptane \n''C6D5C≡CD phenylacetylene-d 6 \n''C6D5CD=CD2 deuterated styrene (D8) \n''C6D5CD2CD3 deuterated ethylbenzene (D10) \n''C6D4(CD3)2 m-xylene-d 10 \n''C6D4(CD3)2 (-{2}-h10)-o-xylene \n''C6D4(CD3)2 deuterated para-xylene (D10) \n''(CD3)2CDCD2C(CD3)3 2,2,4-trimethylpentane-d 18 \n''CD3(CD2)6CD3 deuterated octane (D18) \n''C6H5CCH phenylacetylene \n''C8H8 benzocyclobutene \n''C8H8 cubane \n''C8H8 cyclooctatetraene \n''C6H5CH=CH2 styrene \n''C8H10 1,3,5,7-octatetraene \n''C8H10 1,3,5-cyclooctatriene \n''C8H10 1,3,6-cyclooctatriene \n''HC≡C(CH2)4C≡CH 1,7-octadiyne \n''C6H9C≡CH 1-ethynylcyclohexene \n''C8H10 2,6-octadiyne \n''C8H10 3,5-octadiyne \n''C8H10 6,6-dimethylfulvene \n''C6H5C2H5 ethylbenzene \n''C6H4(CH3)2 m-xylene \n''C6H4(CH3)2 1,2-dimethylbenzene \n''C6H4(CH3)2 1,4-dimethylbenzene \n''C6H4(CH3)2 dimethylbenzene \n''C8H12 cyclopropane, 1,1'-ethenylidenebis \n''C8H12 1,2-dimethylenecyclohexane \n''C8H12 1,3-cyclooctadiene \n''C8H12 1,4-cyclooctadiene \n''C8H12 1,4-dimethyl-1,3-cyclohexadiene \n''C8H12 1,5-cyclooctadiene \n''C8H12 1-octen-3-yne \n''C8H12 1-vinylcyclohexene \n''C8H12 2,5-dimethyl-1,3,5-hexatriene \n''C8H12 3,5-dimethylhex-3-en-1-yne \n''C8H12 3-cyclopentyl-1-propyne \n''C6H9CH=CH2 4-vinylcyclohexene \n''C8H12 5-methyl-2-norbornene \n''C8H12 cis,cis-1,3-cyclooctadiene \n''C8H12 cis-1,2-divinylcyclobutane \n''C6H11C≡CH cyclohexylacetylene \n''C8H12 cyclooctadiene \n''C8H12 cyclooctyne \n''C8H12 dicyclobutylidene \n''C8H12 (E,E,E)-2,4,6-octatriene \n''C8H12 octa-1,3,7-triene \n''[CH2(CH2)4CH2CH=CH]n poly(hexamethylenevinylene),mixture of linear and cyclic forms \n''C8H12 trans-1,2-divinylcyclobutane \n''C8H12 1E,3Z-cyclooctadiene \n''C8H12 1,5-cyclooctadiene, (Z,Z) \n''C8H12 (Z)-oct-5-en-1-yne \n''C8H14 1,1,2-trimethylcyclopenta-2-ene \n''C8H14 1,2,3-trimethylcyclopentene \n''C8H14 1,2-dimethylcyclohexene \n''C8H14 1,3-dimethyl-1-cyclohexene \n''C8H14 1,4-endoethylenecyclohexane \n''C8H14 1,4-octadiene \n''CH2=CH(CH2)4CH=CH2 1,7-octadiene \n''C8H14 1-ethyl-2-methylcyclopentene \n''C8H14 1-ethylcyclohexene \n''C8H14 1-methylcycloheptene \n''CH3(CH2)5C≡CH 1-octyne \n''C8H14 1-propylcyclopentene \n''CH2=C(CH3)CH2CH2C(CH3)=CH2 2,5-dimethyl-1,5-hexadiene \n''(CH3)2C=CHCH=C(CH3)2 2,5-dimethyl-2,4-hexadiene \n''C8H14 2,6-octadiene \n''CH3C≡C(CH2)4CH3 2-octyne \n''C8H14 3,3-dimethylcyclohexene \n''C8H14 3,6-dimethylcyclohexene \n''C8H14 3-ethylcyclohexene \n''C8H14 3-methyl-1,5-heptadiene \n''C8H14 3-octyne \n''C8H14 4,4-dimethylcyclohexene \n''C8H14 4-ethylcyclohexene \n''CH3CH2CH2C≡CCH2CH2CH3 4-octyne \n''C8H14 6-methyl-2-heptyne \n''C8H14 6-methyl-3-heptyne \n''C8H14 allylcyclopentane \n''C8H14 bicyclo[4.2.0]octane \n''C8H14 cis-bicyclo[3.3.0]octane \n''C8H14 cis-cyclooctene \n''C8H14 cyclooctene \n''C6H10(=CHCH3) ethylidenecyclohexane \n''C8H14 trans-cyclooctene \n''C8H14 trans-octahydropentalene \n''C6H11CH=CH2 vinylcyclohexane \n''C8H16 1,1,2-trimethylcyclopentane \n''C8H16 1,1,3-trimethylcyclopentane \n''C6H10(CH3)2 1,1-dimethylcyclohexane \n''C8H16 1,2,3-trimethylcyclopentane \n''C8H16 1,2,4-trimethylcyclopentane \n''C8H16 1,2,4-trimethylcyclopentane \n''C6H10(CH3)2 1,2-dimethylcyclohexane \n''C6H10(CH3)2 1,3-dimethylcyclohexane \n''C6H10(CH3)2 1,4-dimethylcyclohexane \n''C8H16 1,cis-2,trans-4-trimethylcyclopentane \n''C8H16 1-ethyl-1-methylcyclopentane \n''CH3(CH2)5CH=CH2 1-octene \n''C8H16 1,2,3-trimethylcyclopentane, (1A,2A,3B) \n''C8H16 1,2,4-trimethylcyclopentane, (1A,2A,4A) \n''C8H16 2,2-dimethylhex-3-ene \n''C8H16 2,3,3-trimethyl-1-pentene \n''C8H16 2,3,4-trimethyl-1-pentene \n''(CH3)2C=C(CH3)CH(CH3)2 2,3,4-trimethyl-2-pentene \n''C8H16 2,3-dimethyl-1-hexene \n''C8H16 2,3-dimethyl-2-hexene \n''(CH3)3CCH2C(CH3)=CH2 diisobutylene \n'""",'1', '1.01')
        self.colorH=colorH="light steel blue"
        self.H = tk.Button(self, text=H[0], width=5, height=2, bg=colorH, font=10, borderwidth=3,
                           command=lambda text=H: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorH, text[0], text[3], text[4]), self.voice(text[1]), self.compound_H()])
        self.H.grid(row=3, column=2)

        Li = ('Li', 'Lithium', """'Li lithium \n''LiAl lithium-aluminum alloy \n''LiBr lithium bromide \n''LiCl lithium chloride \n''LiD lithium deuteride \n''LiF lithium fluoride \n''LiH lithium hydride \n''LiI lithium iodide \n''LiN3 lithium azide \n''Li2O lithium oxide \n''Li2O2 lithium peroxide \n''Li2S lithium sulfide \n''Li2Se lithium selenide \n''Li3Sb lithium antimonide \n''AlCl4Li lithium tetrachloroaluminate \n''LiAlD4 lithium aluminum deuteride \n''LiAlH4 lithium aluminum hydride \n''LiAlO2 lithium aluminate \n''LiAsF6 lithium hexafluoroarsenate \n''AuCl4Li lithium tetrachloroaurate(III) \n''LiBF4 lithium tetrafluoroborate \n''LiBH4 lithium borohydride \n''LiBO2 lithium metaborate \n''Li2B4O7 lithium tetraborate \n''Li2CuBr4 dilithium tetrabromocuprate(II) \n''Li2NiBr4 dilithium tetrabromonickelate(II) \n''CH3Li methyllithium \n''Li2CO3 lithium carbonate \n''CH3CH2Li ethyllithium \n''C2Li2O4 dilithium oxalate \n''(CH3)2CHLi isopropyllithium \n''CH3(CH2)3Li butyllithium \n''CH3CH2CH(CH3)Li sec-butyllithium \n''(CH3)3CLi tert-butyllithium \n''C5H5Li cyclopentadienyllithium \n''C6H5Li phenyllithium \n''CH3(CH2)5Li N-hexyllithium \n''C6H5C≡CLi lithium phenylacetylide \n''LiCH2CH(CH2CH3)(CH2)3CH3 2-ethylhexyllithium \n''LiC5H(CH3)4 lithium tetramethylcyclopentadienide \n''C10H15Li lithium pentamethylcyclopentadienide \n''ClLiO lithium hypochlorite \n''LiClO4 lithium perchlorate \n''(LiCl)(KCl) lithium chloride/potassium chloride eutectic \n''Li2CuCl4 dilithium tetrachlorocuprate(II) \n''Cl4GaLi lithium tetrachlorogallate \n''CoLiO2 lithium cobalt(III)oxide \n''CrLi2O4 lithium chromate \n''Li2Cr2O7 lithium dichromate \n''LiOD·D2O lithium deuteroxide \n''LiPF6 lithium hexafluorophosphate \n''FeLiO2 lithium iron(III)oxide \n''FeLiSi lithium ferrosilicon \n''LiOH lithium hydroxide \n''LiNH2 lithium amide \n''Li3N lithium nitride \n''LiOH·H2O lithium hydroxide monohydrate \n''6LiOH·H2O lithium-6Li hydroxide monohydrate \n''7LiOH·H2O lithium-7 li hydroxide monohydrate \n''LiIO3 lithium iodate \n''LiMn2O4 lithium manganese(III,IV)oxide \n''LiNO3 lithium nitrate \n''LiNbO3 lithium niobate \n''LiO3P lithium metaphosphate \n''LiTaO3 lithium tantalate \n''LiVO3 lithium metavanadate \n''LiSbF6 lithium hexafluoroantimonate \n''6Li2CO3 lithium-6 li 2carbonate \n''Li2MoO4 lithium molybdate \n''Li2O3Si lithium silicate \n''Li2O3Ti lithium titanate \n''Li2ZrO3 lithium zirconate \n''Li2SO4 lithium sulfate \n''Li2WO4 lithium tungstate \n''Li2Si5O11 lithium polysilicate \n''Li2SnF6 lithium hexafluorostannate \n''Li3PO4 lithium phosphate \n''Li4SiO4 lithium orthosilicate \n''LiBO2·2H2O lithium metaborate dihydrate \n''LiBr·xH2O lithium bromide hydrate \n''CH3OLi lithium methoxide \n''HCO2Li·H2O lithium formate monohydrate \n''CF3CO2Li lithium trifluoroacetate \n''LiOOCCH3 lithium acetate \n''C2H5LiO lithium ethoxide \n''(CH3)2NLi lithium dimethylamide \n''CH3COOLi·2H2O lithium acetate dihydrate \n''CH3CH(OH)CO2Li lithium (D)-lactate \n''CH3CH(OH)CO2Li lithium L-lactate \n''CH3CH(OH)CO2Li lithium lactate \n''(CH3)2CHOLi lithium isopropoxide \n''C4H3LiS 2-thienyllithium \n''NH2CH2CH2NH2·LiCCH lithium acetylide ethylenediamine \n''LiC≡CH·NH2CH2CH2NH2 lithium acetylide-ethylenediamine complex \n''(CH3)3COLi lithium tert-butoxide \n''(C2H5)2NLi lithium diethylamide \n''(CH3)3SiCH2Li (trimethylsilyl)methyllithium \n''CH3COCH=C(OLi)CH3 lithium acetylacetonate \n''(CH3)3SiC≡CLi lithium(trimethylsilyl)acetylide \n''C6H5OLi lithium phenoxide \n'""", '3', '6.94')
        self.colorLi=colorLi="medium orchid"
        self.Li = tk.Button(self, text=Li[0], width=5, height=2, bg=colorLi, font=10, borderwidth=3,
                           command=lambda text=Li: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorLi, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Li()])
        self.Li.grid(row=4, column=2)

        Na = ('Na', 'Sodium', """'Na sodium \n''NaBH4 sodium borohydride \n''NaBr sodium bromide \n''NaCl sodium chloride \n''Na35Cl sodium chloride-35 \n''NaF sodium fluoride \n''NaH sodium hydride \n''NaHg sodium mercury amalgam \n''NaI sodium iodide \n''K2Na sodium-potassium alloy \n''NaN3 sodium azide \n''NaO2 sodium superoxide \n''NaPb sodium-lead alloy \n''Na2O sodium oxide \n''Na2O2 sodium peroxide \n''Na2Se sodium selenide \n''Na3P sodium phosphide \n''Na3Sb sodium antimonide \n''NaAlCl4 sodium tetrachloroaluminate \n''Na3AlF6 sodium hexafluoroaluminate \n''NaAlH4 sodium aluminum hydride \n''AlNaO2 sodium aluminate \n''NaAsF6 sodium hexafluoroarsenate(V) \n''NaAsO2 sodium arsenite \n''Na3AsO4 sodium arsenate \n''AsNa3O4 arsenic acid, trisodium salt \n''AuCl4Na sodium gold chloride \n''NaBD4 sodium borodeuteride \n''NaBF4 sodium borofluoride \n''BNaO2 sodium metaborate \n''BNaO3 sodium peroxoborate \n''Na2B4O7 sodium tetraborate \n''NaBiO3 sodium bismuthate \n''NaBrO3 sodium bromate \n''Na2PdBr4 sodium tetrabromopalladate(II) \n''NaCN sodium cyanide \n''Na2CO3 soda ash \n''Na213CO3 sodium carbonate-13 C \n''Na213C2O4 sodium oxalate-13 C2 \n''CNa2S3 sodium trithiocarbonate \n''HC≡CNa sodium acetylide \n''NaN(CN)2 sodium dicyanamide \n''NaOOCCOONa sodium oxalate \n''C5H5Na sodium cyclopentadienylide \n''C6Na2O6 sodium rhodizonate \n''C8H11Na sodium isopropylcyclopentadienide \n''C10H15Na sodium pentamethylcyclopentadienide \n''C6H5C6H5·Na sodium biphenyl complex \n''[(CH2CH)2C6H4][CH2CH(C6H5)]Na amberlite®IR120 sodium form \n''(C6H5)3CNa triphenylmethyl sodium \n''NaOCl sodium hypochlorite \n''NaClO3 sodium chlorate \n''NaClO4 sodium perchlorate \n''Cl3Cs2Na cesium chloride/sodium chloride(2:1)eutectic \n''Na2PdCl4 sodium tetrachloropalladate(II) \n''Na3RhCl6 sodium hexachlororhodate(III) \n''Na2CrO4 sodium chromate \n''Na2Cr2O7 sodium bichromate \n''NaOD·D2O sodium deuteroxide \n''NaHF2 sodium hydrogen fluoride \n''Na3FeF6 sodium hexafluoroferrate(III) \n''NaPF6 sodium hexafluorophosphate \n''NaSbF6 sodium hexafluoroantimonate \n''Na2SiF6 sodium fluorosilicate \n''Na2TiF6 sodium hexafluorotitanate \n''Na2ZrF6 sodium hexafluorozirconate \n''NaOH sodium hydroxide \n''NaHS sodium bisulfide \n''Na2S sodium sulfide \n''NaNH2 sodium amide \n''NaIO3 sodium iodate \n''NaIO4 sodium periodate \n''NaMnO4 sodium permanganate \n''Na2MoO4 sodium molybdate \n''Na2MoO4·2H2O sodium molybdate dihydrate \n''C19H18O5·xH2O 2,4:3,5-di-O-benzylidene-aldehydo-D-ribose hydrate \n''NaNO2 sodium nitrite \n''Na15NO2 sodium nitrite-15 N \n''NaNO3 sodium nitrate \n''Na15NO3 sodium nitrate-15 N \n''NaClO2 sodium chlorite \n''NaNbO3 sodium niobate \n''NaVO3 sodium metavanadate \n''NaReO4 sodium perrhenate \n''NaPO3 calgon pT \n''Na2BeF4 sodium tetrafluoroberyllate \n''Na2GeO3 sodium germanate \n''Na2IrBr6 sodium hexabromoiridate(IV) \n''Na2SO3 sodium sulfite \n''Na2S2O3 sodium hyposulfite \n''Na2SeO3 sodium selenite \n''Na2SiO3 sodium metasilicate \n''Na2O3Si sodium orthosilicate \n''Na4O4Si sodium silicate \n''Na2SnO3 sodium stannate \n''Na2ZrO3 sodium zirconate \n''Na2O4S na4 \n''Na2SO4 sodium sulfate \n''Na2S2O4 sodium dithionite \n''Na2WO4 sodium tungstate \n''Na2S2O5 sodium metabisulfite \n''Na2Ti3O7 sodium metatitanate \n''Na2S2O8 sodium persulfate \n''Na2V4O11 sodium tetravanadate \n''Na3PO4 trisodium phosphate \n''Na3VO4 sodium orthovanadate \n''Na3O9P3 sodium trimetaphosphate \n''Na4O7P2 sodium pyrophosphate \n''Na4V2O7 sodium pyrovanadate \n''Na4O12P4 metaphosphoric acid, tetrasodium salt \n''Na4V6O17 sodium vanadate \n''Na5O10P3 polygon \n''3Na2WO4·9WO3 sodium metatungstate \n''AlNaO8S2 aluminum sodium sulfate \n''AsHNa2O4 disodium hydrogen arsenate \n''AsH2NaO4 monosodium arsenate \n''Na2HAsO4·7H2O disodium hydrogen arsenate heptahydrate \n''NaBO2·xH2O sodium metaborate hydrate \n''BNaO3·H2O sodium perborate monohydrate \n''NaBO3·4H2O sodium perborate tetrahydrate \n''Na2B4O7·10H2O sodium borate decahydrate \n''Ba2NaNb5O15 barium sodium niobium oxide \n''NaDCO2 sodium formate-d \n''13CD313CO2Na sodium acetate-13 C2,d 3 \n''NCNHNa sodium hydrogencyanamide \n''HCOONa sodium formate \n''H13CO2Na sodium formate-13 C \n''NaHCO3 sodium bicarbonate \n''CH313CO13CO2Na sodium pyruvate-1,2-13 C2 \n''NaH13CO3 sodium bicarbonate-13 C \n''Na2CO3·H2O sodium carbonate monohydrate \n''NaOCH3 sodium methoxide \n''13CH313CO2Na sodium acetate-13 C2 \n''13CH313CO13CO2Na sodium pyruvate-13 C3 \n''13CH313CH213CO2Na sodium propionate-13 C3 \n''13CH313CH(OH)13CO2Na sodium L-lactate-13 C3 \n''13CH3(13CH2)213CO2Na sodium butyrate-13 C4 \n''Na2CO3·10H2O sodium carbonate decahydrate \n''NaOCN sodium cyanate \n''NaSCN sodium thiocyanate \n''CNa3O5P foscarnet \n''NaAu(CN)2 sodium dicyanoaurate \n''CCl3CO2Na sodium trichloroacetate \n''NaO2CCD3 deuterated sodium acetate (D3) \n''CF3COONa sodium perfluoroacetate \n''C2HNa3O6 sodium sesquicarbonate \n''C2H2N3Na sodium 1H-1,2,4-triazolate \n''CH3COONa sodium acetate \n''CH3CH2ONa sodium ethylate \n''CH3CH2SNa sodium ethanethiolate \n''Na2CO3·1.5H2O2 sodium percarbonate \n''CH3COONa·3H2O sodium acetate trihydrate \n''NaOAc sodium acetate \n''Na2[Cu(CN)3] sodium cuprocyanide \n''CF3CF2COONa sodium pentafluoropropionate \n''C3H3N2Na imidazole sodium derivative \n''H2C=CHCO2Na sodium acrylate \n''C3H3NaO2 sodium malondialdehyde \n''CH3COCOONa sodium pyruvate \n''CH3CH2COONa sodium propionate \n''C3H5NaO3 sodium L-lactate \n''CH3C18O2Na sodium acetate-18 O2 \n''C4H2Na2O4 sodium dimaleate \n''NaOOCCH=CHCOONa disodium fumarate \n''NaOOCCH2CH2COONa sodium succinate \n''C4H2Na2O4·xH2O maleic acid disodium salt hydrate \n''C4H4Na2O6 sodium tartrate \n''C4H4Na2O8 disodium tetrahydroxysuccinate \n''H2C=C(CH3)CO2Na sodium methacrylate \n''NaO2CCH(OH)CH(OH)CO2H sodium hydrogentartrate \n''NaO2CCH2CH(OH)CO2Na·H2O L-malic acid disodium salt monohydrate \n''CH3CH2CH2COONa sodium butyrate \n''C2H5CH(OH)CO2Na 2-hydroxybutyric acid sodium salt \n''CH3CH(OH)CH2CO2Na 3-hydroxybutyric acid sodium salt \n''CH3CH(OH)CH2CO2Na (R)-(-)-3-hydroxybutyric acid sodium salt \n''C4H7NaO3 sodium 3-hydroxybutyrate \n''C4H7NaO3 sodium oxybate \n''C4H7NaO4 sodium diacetate \n''NaO(CH3)3 sodium 2-methylpropan-2-olate \n''(CH3)3CSNa sodium 2-methyl-2-propanethiolate \n''C4H4O4Na2·6H2O sodium succinate hexahydrate \n''C5Na2O5 croconic acid disodium salt \n''(CH3)2CHCOCOONa sodium 3-methyl-2-oxobutanoate \n''C5H9NaO2 sodium pivalate \n''NaOC(CH3)2CH2CH3 sodium 2-methylbutan-2-olate \n''(CH3)3CCO2Na·xH2O sodium trimethylacetate hydrate \n''C6H5NaO sodium phenolate \n''C6H5SNa sodium thiophenoxide \n''C6H5Na3O7 citrosodine \n''C6H7NaO6 (+)-sodium L-ascorbate \n''C6H7NaO6 sodium erythorbate \n''HOC(COONa)(CH2COOH)2 sodium dihydrogen citrate \n''C2H5CH(CH3)COCO2Na 3-methyl-2-oxopentanoic acid sodium salt \n''CH3C(ONa)=CHCO2C2H5 ethyl acetoacetate sodium salt \n''C6H9NaO3 sodium 4-methyl-2-oxovalerate \n''C6H9NaO3 sodium DL-3-methyl-2-oxopentanoate \n''C6H7NaO6·H2O sodium D-isoascorbate monohydrate \n''HOC(COOH)(CH2COONa)2·1.5H2O sodium hydrogencitrate sesquihydrate \n''HOC(CO2Na)(CH2CO2Na)2·2H2O trisodium citrate dihydrate \n''(CH3)2CHCH2COCO2Na·xH2O 4-methyl-2-oxopentanoic acid sodium salt hydrate \n''NaOC6H5·3H2O sodium phenoxide trihydrate \n''CH2(OH)(CHOH)4COONa sodium gluconate \n''(C2H5)3NaBH sodium triethylborohydride \n''C6D5CO2Na sodium benzoate-d 5 \n''C6H5COONa sodium benzoate \n''HOC6H4CO2Na 4-hydroxybenzoic acid sodium salt \n''HOC6H4COONa sodium salicylate \n''C7H7NaO 4-methylphenol sodium salt \n''C6H5CH2ONa sodium benzyloxide \n''CH3C6H4SNa 4-methylbenzenethiol sodium salt \n''(C2D5)4BNa sodium tetraethylborate-d 20 \n''C6H4(CO2Na)2 terephthalic acid disodium salt \n''C8H7NaO3 sodium p-methoxycarbonylphenoxide \n''C8H7NaO4 sodium dehydroacetate \n''C6H5OCH2CO2Na·xH2O phenoxyacetic acid sodium salt hydrate \n''C2H5OCOC(ONa)=CHCOOC2H5 diethyl oxalacetate sodium salt \n''CH3(CH2)3CH(C2H5)CO2Na sodium 2-ethylhexanoate \n''C8H15NaO2 sodium valproate \n''C8H15NaO8 carboxymethylcellulose sodium \n''(C2H5)4BNa sodium tetraethylborate \n''C6H5CH2COCOONa sodium phenylpyruvate \n''C10H7NaO3·xH2O 7-hydroxy-4-methylcoumarin sodium salt hydrate \n''[CH(CH3)CHC7H7NaO4S]n benzenesulfonic acid, methoxy(1-propenyl)-, sodium salt, homopolymer \n''NaC(CO2C2H5)3 triethyl methanetricarboxylate sodium derivative \n''C6H11(CH2)3CO2Na sodium 4-cyclohexylbutyrate \n''C6H5C6H4ONa sodium o-phenylphenolate \n''(C4H8)x(C4H4O4)y·xNa poly(isobutylene-co-maleic acid)sodium salt \n''C12H17NaO7 dikegulac sodium \n''C12H23NaO2 sodium laurate \n''NaB[CH(CH3)C2H5]3H N-selectride®1.0 M in tetrahydrofuran \n''C16H31NaO2 sodium palmitate \n''C16H31NaO4 divalproex sodium \n''CH3(CH2)7CH=CH(CH2)7COONa sodium oleate \n''C18H36O2Na sodium stearate \n''C20H10Na2O5 uranine \n''C20H31NaO5 prostacycline sodium salt \n''C22H11Na3O9 chrome violet g \n''NaB(C6H5)4 sodium tetraphenylborate \n''C24H39NaO4 sodium 7-deoxycholate \n''C24H39NaO5 sodium cholate \n''C24H39NaO4·H2O sodium deoxycholate monohydrate \n''C29H16Na2O6 naphthochrome green \n''C32H16N8Na2 sodium phthalocyanine \n''C36H61NaO11 monensin sodium \n''ClH2NaO5 sodium perchlorate monohydrate \n''ClH10NaO6 sodium hypochlorite pentahydrate \n''ClNa13O17P4 chlorinated trisodium phosphate \n''Na3Co(NO2)6 sodium hexanitrocobaltate(III) \n''CoN6Na3O12 sodium hexanitrocobaltate \n''Na2CrO4·4H2O sodium chromate tetrahydrate \n''Na2Cr2O7·2H2O sodium dichromate dihydrate \n''Na2FPO3 sodium fluorophosphate \n''FeNaP2O7 iron(III) sodium pyrophosphate \n''NaHSO3 sodium bisulfite \n''NaHSO4 sodium bisulfate \n''Na2HPO4 disodium hydrogen phosphate \n''NaI·2H2O sodium iodide dihydrate \n''Na3H2IO6 sodium hydrogen periodate \n''Na2N2O2·xH2O sodium trans-hyponitrite hydrate \n''NaH2PO2·H2O sodium hypophosphite monohydrate \n''Na2TeO3 sodium tellurite \n''NaH2PO4 sodium dihydrogen phosphate \n''Na2SeO4 sodium selenate \n''Na2SnO3·3H2O sodium stannate trihydrate \n''H2Na2P2O7 sodium acid pyrophosphate \n''(NaPO3)n·Na2O sodium hexametaphosphate \n''NaMnO4·H2O sodium permanganate monohydrate \n''NaSH·xH2O sodium hydrosulfide hydrate \n''H3NaO5S sodium bisulfate monohydrate \n''NaH2PO2·xH2O sodium hypophosphite hydrate \n''NaO3SS2SO3Na·2H2O sodium tetrathionate dihydrate \n''Na2TeO4·2H2O sodium tellurate dihydrate \n''Na2WO4·2H2O sodium tungstate dihydrate \n''NaH2PO4·H2O sodium dihydrogen phosphate monohydrate \n''NaH2PO4·2H2O sodium dihydrogen phosphate dihydrate \n''3Na2WO4·9WO3·xH2O sodium metatungstate hydrate \n''Na2S2O3·5H2O sodium thiosulfate \n''H10Na2O8Se sodium selenite pentahydrate \n''H10Na2O8Si sodium metasilicate pentahydrate \n''Na2Pt(OH)6 sodium hexahydroxyplatinate(IV) \n''H14Na2O10S sodium sulfite heptahydrate \n''Na2S·9H2O sodium sulfide nonahydrate \n''Na2SO4·10H2O sodium sulfate decahydrate \n''Na2SeO4·10H2O sodium selenate decahydrate \n''Na4P2O7·10H2O tetrasodium pyrophosphate decahydrate \n''Na3PO4·12H2O sodium phosphate dodecahydrate \n''H25Na2O16P sodium hydrogen phosphate dodecahydrate \n''Na3Ir(NO2)6 sodium hexanitroiridate(III) \n''NaBr·2H2O sodium bromide dihydrate \n''NaH2PO2 sodium phosphinate \n''Na2S·5H2O sodium sulfide pentahydrate \n''Na4Pb(S2O3)3 lead(II) sodium thiosulfate \n''AlHNa2O5P+ sodium phosphoaluminate \n''AlH24NaO20S2 sodium alum \n''NaAuCl4·xH2O sodium tetrachloroaurate(III)hydrate \n''13CD3CO2Na sodium acetate-2-13 C,d 3 \n''CD313CO2Na sodium acetate-1-13 C,d 3 \n''CF313CO2Na sodium trifluoroacetate-1-13 C \n''13CH3CO2Na sodium acetate-2-13 C \n''CH313CO2Na sodium acetate-1-13 C \n''13CH313COCO2Na sodium pyruvate-2,3-13 C2 \n''CH313CH213CO2Na sodium propionate-1,2-13 C2 \n''13CH313CH2CO2Na sodium propionate-2,3-13 C2 \n''NaBD3CN sodium cyanoborodeuteride \n''CF3SO3Na sodium trifluoromethanesulfonate \n''CH3AsNa2O3 disodium methanearsonate \n''NaBH3CN sodium cyanoborohydride \n''CH3NaO3S rongalite \n''CH3SO3Na sodium methanesulfonate \n''HOCH2SO3Na formaldehyde sodium bisulfite \n''CH3OSO3Na sodium methyl sulfate \n''CH4AsNaO3 sodium methanearsonate \n''NaCH3SO2 methanesulfinic acid sodium salt \n''HOP(O)(ONa)CH2P(O)(ONa)2·4H2O methylenediphosphonic acid trisodium salt tetrahydrate \n''HOCH2SO2Na·2H2O sodium formaldehydesulfoxylate dihydrate \n''NaO2C13CH=13CHCO2Na sodium fumarate-2,3-13 C2 \n''CH313COCO2Na sodium pyruvate-2-13 C \n''13CH3COCO2Na sodium pyruvate-3-13 C \n''CH3CO13CO2Na sodium pyruvate-1-13 C \n''CH313CH2CO2Na sodium propionate-2-13 C \n''13CH3CH2CO2Na sodium propionate-3-13 C \n''CH3CH213CO2Na sodium propionate-1-13 C \n''13CH3CH(OH)CO2Na sodium L-lactate-3-13 csolution \n''13CH3CH213CH2CO2Na sodium butyrate-2,4-13 C2 \n''CH313CH(OH)CH213CO2Na sodium DL-3-hydroxybutyrate-1,3-13 C2 \n''13CH3CH(OH)13CH2CO2Na sodium DL-3-hydroxybutyrate-2,4-13 C2 \n''ClCF2CO2Na sodium chlorodifluoroacetate \n''Cl2CHCO2Na sodium dichloroacetate \n''C2H2BrNaO2 sodium bromoacetate \n''ClCH2COONa sodium chloroacetate \n''NaOC(O)CH2F sodium fluoroacetate \n''ICH2COONa sodium iodoacetate \n''NH2COCOONa sodium oxamate \n''H2NC(ONa)=NCN 1-cyanoisourea sodium salt \n''C2H2Na2O5S acetic acid, sulfo-, disodium salt \n''C2H3NaO2S sodium thioglycolate \n''(C2H3NaO3S)n poly(vinylsulfonic acid,sodium salt) \n''CH2=CHSO3Na vinylsulfonic acid sodium salt \n''C2H4NNaO2 sodium glycinate \n''C2H4Na2O6S2 disodium 1,2-ethanedisulfonate \n''CH3S(O)CH2Na dimsyl sodium \n''HOCH2CH2SO3Na sodium 2-hydroxyethanesulfonate \n''(CH3)2AsO2Na sodium cacodylate \n''H2NCH2CO2Na·xH2O glycine sodium salt hydrate \n'""", '11', '22.99')
        self.colorNa = colorNa = "dark orchid"
        self.Na = tk.Button(self, text=Na[0], width=5, height=2, bg=colorNa, font=10, borderwidth=3,
                           command=lambda text=Na: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Na()])
        self.Na.grid(row=5, column=2)

        K = ('K', 'Potassium', """'K potassium \n''KBr potassium bromide \n''KCl potassium chloride \n''KF potassium fluoride \n''KH potassium hydride \n''KI potassium iodide \n''K2Na sodium-potassium alloy \n''KO2 potassium superoxide \n''K2O2 potassium peroxide \n''K2Se potassium selenide \n''KAlCl4 potassium tetrachloroaluminate \n''K3AlF6 potassium hexafluoroaluminate \n''KAsF6 potassium hexafluoroarsenate(V) \n''AsKO2 potassium arsenite \n''KAuBr4 potassium tetrabromoaurate(III) \n''KBF4 potassium fluoroborate \n''KBH4 potassium borohydride \n''KBO2 potassium metaborate \n''KBrO3 potassium bromate \n''K2PdBr4 potassium tetrabromopalladate(II) \n''K2PtBr4 potassium tetrabromoplatinate(II) \n''K2PtBr6 potassium hexabromoplatinate(IV) \n''K2ReBr6 potassium hexabromorhenate(IV) \n''K2TeBr6 potassium hexabromotellurate(IV) \n''KCN potassium cyanide \n''K13CN potassium cyanide-13 C \n''K13C15N potassium cyanide-13 C,15 N \n''KC15N potassium cyanide-15 N \n''K2CO3 pearl ash \n''K213CO3 potassium carbonate-13 C \n''C2K2O4 potassium oxalate \n''C6O6K2 potassium rhodizonate \n''C9H13K potassium tetramethylcyclopentadienide \n''C10H15K potassium pentamethylcyclopentadienide \n''KClO3 potassium chlorate \n''KClO4 potassium perchlorate \n''(LiCl)(KCl) lithium chloride/potassium chloride eutectic \n''K2PdCl4 potassium tetrachloropalladate(II) \n''K2PtCl4 potassium tetrachloroplatinate \n''K2IrCl6 potassium hexachloroiridate(IV) \n''K3IrCl6 potassium hexachloroiridate(III) \n''K2OsCl6 potassium hexachloroosmate(IV) \n''K2PdCl6 potassium hexachloropalladate(IV) \n''K2PtCl6 potassium hexachloroplatinate \n''K2PtCl6 potassium chloroplatinate \n''K2ReCl6 potassium hexachlororhenate(IV) \n''K3RhCl6 potassium hexachlororhodate(III) \n''K3RuCl6 potassium hexachlororuthenate(III) \n''Cl6K3Rh selenomycin \n''K2CrO4 potassium chromate \n''K2Cr2O7 potassium dichromate \n''KOD potassium deuteroxide \n''KHF2 potassium bifluoride \n''KPF6 potassium hexafluorophosphate \n''KSbF6 potassium hexafluoroantimonate(V) \n''K2SiF6 potassium hexafluorosilicate \n''K2(TiF6) potassium hexafluorotitanate(IV) \n''K2NbF7 potassium heptafluoroniobate(V) \n''K2TaF7 potassium heptafluorotantalate \n''K2FeO4 potassium ferrate(VI) \n''KOH potassium hydroxide \n''K2Sx potassium polysulfide \n''K2HgI4 mercury potassium iodide \n''KIO3 potassium iodate \n''KIO4 potassium periodate \n''K2PtI6 potassium hexaiodoplatinate(IV) \n''K2ReI6 potassium hexaiodorhenate(IV) \n''KAsO3 potassium metaarsenate \n''KAuCl4 potassium gold(III)chloride \n''KMnO4 potassium permanganate \n''KNH2 potassium amide \n''K15N18O3 potassium nitrate-15 N,18 O3 \n''KNO2 potassium nitrite \n''KNO3 potassium nitrate \n''KNbO3 potassium niobate \n''KTaO3 potassium tantalate \n''KVO3 potassium metavanadate \n''KReO4 potassium perrhenate \n''KRuO4 potassium perruthenate \n''K2CS3 potassium thiocarbonate \n''K2IrBr6 potassium hexabromoiridate(IV) \n''K2MnO4 potassium manganate \n''K2MoO4 potassium molybdate \n''K2NiF6 potassium hexafluoronickelate(IV) \n''K2SO3 potassium sulfite \n''K2S2O3 potassium thiosulfate \n''K2SeO3 selenious acid, dipotassium salt \n''K2O3Sn potassium stannate \n''K2TeO3 potassium tellurite \n''K2TiO3 potassium titanate \n''K2RuO4 potassium ruthenate \n''K2SO4 potassium sulfate \n''K2S2O4 potassium dithionite \n''K2SeO4 potassium selenate \n''K2WO4 potassium tungstate \n''K2S2O5 potassium metabisulfite \n''K2O6S2 potassium dithionate \n''KOSO2SSSO3K potassium tetrathionate \n''K2S2O7 potassium pyrosulfate \n''K2S2O8 potassium persulfate \n''K2TeCl6 potassium hexachlorotellurate \n''K2U2O7 potassium uranate \n''K2ZrF6 potassium hexafluorozirconate \n''O2[P(O)(OK)2]2 potassium peroxydiphosphate \n''AlKO8S2 potassium alum \n''KH2AsO4 potassium dihydrogen arsenate \n''K2HAsO4·2H2O potassium hydrogenarsenate dihydrate \n''K2B4O7·4H2O potassium tetraborate tetrahydrate \n''BeK2(SO4)2 beryllium potassium sulfate \n''KDCO2 potassium formate-d \n''HCOOK potassium formate \n''KHCO3 potassium bicarbonate \n''CH3OK potassium methanolate \n''KOCN potassium cyanate \n''KSCN potassium thiocyanate \n''KS13CN potassium thiocyanate-13 C \n''KS13C15N potassium thiocyanate-13 C,15 N \n''KSC15N potassium thiocyanate-15 N \n''KSeCN potassium selenocyanate \n''K[Ag(CN)2] potassium silver cyanide \n''KAu(CN)2 potassium dicyanoaurate(I) \n''K[Cu(CN)2] potassium cuprocyanide \n''CF3COOK potassium trifluoroacetate \n''(COOK)2·H2O potassium oxalate monohydrate \n''CH3COOK potassium acetate \n''KOC2H5 potassium ethoxide \n''C2K2N2S3 dipotassium 1,3,4-thiadiazole-2,5-dithiolate \n''C2K2O2S2 ethanebis(thioic) acid, dipotassium salt \n''C4CdK2N4 cadmium dipotassium tetracyanide \n''HOOCC≡CCOOK 2-butynedioic acid, monopotassium salt \n''KC4H4O8 potassium quadroxalate \n''C4H5KO4 potassium methyl malonate \n''KO2CCH(OH)CH(OH)CO2H potassium hydrogen tartrate \n''KO2CCH(OH)CH(OH)CO2K potassium L-tartrate \n''KOCH2CH(CH3)2 potassium isobutoxide \n''(CH3)3COK potassium tert-butoxide \n''C4HgK2N4 mercuric potassium cyanide \n''K2Ni(CN)4 potassium tetracyanonickelate(II) \n''K2Pt(CN)4 potassium tetracyanoplatinate(II) \n''C4K2N4Zn potassium tetracyanozincate \n''K3Co(CN)6 potassium hexacyanocobaltate(III) \n''C2H5OCOCH2CO2K potassium ethyl malonate \n''K3Cr(CN)6 potassium hexacyanochromate(III) \n''K[Cu(CN)2]·K3[Cu(CN)4] potassium cyanocuprate(I) \n''K3Fe(CN)6 potassium hexacyanoferrate(III) \n''C6H5K3O7 potassium citrate \n''C6H7KO2 potassium sorbate \n''CH3CH=CHCH=CHCOOK trans,trans-2,4-hexadienoic acid potassium salt \n''C6H7KO7 potassium dihydrogen citrate \n''C6H7K3O8 potassium citrate monohydrate \n''C6H11KO7 potassium gluconate \n''KB(C2H5)3H potassium triethylborohydride \n''K2Pt(CN)6 potassium hexacyanoplatinate(IV) \n''K3Mn(CN)6 potassium hexacyanomanganate(III) \n''C6H5COOK potassium benzoate \n''HOOCC6H4COOK potassium hydrogen phthalate \n''C6H4(CO2K)2 phthalic acid dipotassium salt \n''C6H11(CH2)3CO2K potassium cyclohexanebutyrate \n''C10H6(CO2K)2 2,6-naphthalenedicarboxylic acid dipotassium salt \n''(C6H5)2PK potassium diphenylphosphide \n''K[CH(CH3)CH2CH3]3BH K-selectride \n''HOCH2CH(OH)CH2O2CCH2CH[CH2C(=CH2)CH2C(CH3)3]CO2K 4-(2,3-dihydroxypropyl)-2-(2-methylene-4,4-dimethylpentyl)succinate potassium salt \n''KB[CH(CH3)CH(CH3)2]3H KS-selectride \n''HOCH2CH(OH)CH2O2CCH2CH(C9H17)CO2K 4-(2,3-dihydroxypropyl)2-isononenylsuccinate potassium salt \n''KB(C6H5)3H potassium triphenylborohydride \n''CH3(CH2)7CH=CH(CH2)7COOK potassium oleate \n''(C6H5)4BK potassium tetraphenylborate \n''ClCrKO3 potassium chlorochromate \n''CrKO8S2 chrome potash alum \n''KD2PO4 potassium dideuterium phosphate \n''FH4KO2 potassium fluoride dihydrate \n''KH(IO3)2 potassium hydrogen diiodate \n''K15NO3 potassium nitrate-15 N \n''KHSeO3 potassium selenite \n''KHSO4 potassium bisulfate \n''K2HPO4 dipotassium hydrogen phosphate \n''(K2S)(K2S2O3) potash,sulfurated \n''KH2PO4 potassium dihydrogen phosphate \n''K2SnO3·3H2O potassium stannate trihydrate \n''K2OsO4·2H2O potassium osmate(VI)dihydrate \n''K2TeO4·xH2O potassium tellurate hydrate \n''H2K4O13S3 potassium peroxomonosulfate \n''K4P2O7 tetrapotassium pyrophosphate \n''KSb(OH)6 potassium hexahydroxyantimonate \n''K2Pt(OH)6 potassium hexahydroxoplatinate \n''K3Ir(NO2)6 potassium hexanitroiridate(III) \n''KH2PO2 potassium phosphinate \n''KH2PO3 potassium dihydrogen phospho nate \n''KI3·H2O potassium triiodide monohydrate \n''K(NOsO3) potassium nitridotrioxoosmate(VIII) \n''K2Pd(NO2)4 potassium tetranitropalladate(II) \n''K2Pt(NO2)4 potassium tetranitroplatinate(II) \n''K2S·5H2O potassium sulfide pentahydrate \n''K3Rh(NO2)6 potassium hexanitrorhodate(III) \n''AlK(SO4)2·12H2O potassium aluminum sulfate dodecahydrate \n''KF3BOH potassium trifluorohydroxyborate \n''KD3BCN potassium cyanoborodeuteride \n''CH3BF3K potassium methyltrifluoroborate \n''CH3KO4S potassium methyl sulfate \n''Cl2CHCO2K potassium dichloroacetate \n''CH2=CHBF3K potassium vinyltrifluoroborate \n''CH3COSK potassium thioacetate \n''[CH2CH(OSO3K)]n poly(vinyl sulfate)potassium salt \n''C2H3KO4S potassium poly(vinyl sulfate) \n''C2H4Cl3KPt potassium trichloroethyleneplatinate \n''C2H5KO4S potassium 2-hydroxyethanesulfonate \n''C3Cl2KN3O3 potassium dichloro-s-triazinetrione \n''KOP(O)(OH)OC(=CH2)CO2H potassium hydrogen 2-(phosphonatooxy)acrylate \n''C2H5OCSSK potassium xanthogenate \n''(CH3)3SiOK potassium trimethylsilanolate \n''C4H2KN3O4 potassium oxonate \n''C4H4KNaO6 potassium sodium tartrate \n''KOCOCH(OH)CH(OH)COONa·4H2O rochelle salt \n''K2Pt(C2O4)2·2H2O potassium bis(oxalato)platinate(II)dihydrate \n''HO2CCH2CH(NH2)CO2K·xH2O L-aspartic acid monopotassium salt \n''(CH3)2CHOCS2K O-isopropylxanthic acid potassium salt \n''CH3CH2CH2CH2BF3K potassium butyltrifluoroborate \n''C4HgK2N4S4 mercury dipotassium tetrathiocyanate \n''C5H2KN3O6·H2O 5-nitroorotic acid, potassium salt monohydrate \n''C6H3BF5K potassium 2,4-difluorophenyltrifluoroborate \n''F2C6H3BF3K potassium 2,6-difluorophenyltrifluoroborate \n''C6H4BF4K potassium 3-fluorophenyltrifluoroborate \n''C6H4(SO3K)2 potassium benzene-1,2-disulfonate \n''C6H5BF3K potassium phenyltrifluoroborate \n''(HO)2C6H3SO3K benzenesulfonic acid, 2,5-dihydroxy-, monopotassium salt \n''K3Cr(C2O4)3·3H2O potassium chromium(III)oxalate trihydrate \n''H2C=CHCO2(CH2)3SO3K 3-sulfopropyl acrylate potassium salt \n''C6H11K2O9P alpha-D-galactose 1-(dipotassium phosphate) \n''[(CH3)3Si]2NK potassium bis(trimethylsilyl)amide \n''F3CC6H5BF3·K potassium 4-(trifluoromethyl)phenyltrifluoroborate \n''C7H6KNO2 potassium 4-aminobenzoate \n''KO3SC6H4CO2H 4-sulfobenzoic acid \n''C6H5CH2BF3K potassium benzyltrifluoroborate \n''CH3C6H4BF3K potassium o-tolyltrifluoroborate \n''CH3C6H4BF3K potassium p-tolyltrifluoroborate \n''O2NC6H3(OCH3)OK·xH2O 4-nitroguaiacol potassium salt hydrate \n''H2C=C(CH3)CO2(CH2)3SO3K 3-sulfopropyl methacrylate potassium salt \n''(CF3)2C6H3BF3K potassium 3,5-bis(trifluoromethyl)phenyltrifluoroborate \n''K4Hf[C2O4]4 potassium tetraoxalatohafnate(IV) \n''C8H4KNO2 potassium phthalimide \n''K15NO2CC6H4 phthalimide-15 npotassium salt \n''K4Zr[C2O4]4 potassium tetraoxalatozirconate(IV) \n''C8H5KN2S3 5-mercapto-3-phenyl-1,3,4-thiadiazole-2(3H)-thione potassium salt \n''C8H4K2O12Sb2·xH2O potassium antimony(III)tartrate hydrate \n''C6H5(CH)2BF3K potassium trans-styryltrifluoroborate \n''C6H5CH2CH2BF3K potassium phenethyltrifluoroborate \n''C10H5KO5S 2-naphthalenesulfonic acid, 1,4-dihydro-1,4-dioxo-, potassium salt \n''C10H5KO5S potassium 1,2-naphthoquinone-4-sulfonate \n''C10H6K2O7S2 dipotassium 7-hydroxynaphthalene-1,3-disulfonate \n''C10H7BF3K potassium 2-naphthalenetrifluoroborate \n''C10H7KO4S 2-naphthalenesulfonic acid, 1-hydroxy-, monopotassium salt \n''C10H7KO4S potassium naphthalene-2-sulfonate \n''C4H9C6H4BF3K potassium 4-tert-butylphenyltrifluoroborate \n''C10H19BF3K potassium trans-1-decenyltrifluoroborate \n''C10H20K2O10Si2 dipotassium[μ-(1,2-ethanediolato-O:O')]tetrakis(1,2-ethanediolato-O,O')disilicate \n''KO3S(CH2)3O2CCH2C(=CH2)CO2(CH2)3SO3K bis(3-sulfopropyl)itaconate dipotassium salt \n''C12H5KO6S 4-sulfo-1,8-naphthalic anhydride potassium salt \n''C13H14KNO5 D-(-)-4-hydroxyphenylglycine dane salt \n''C6H5CH[NHC(CH3)=CHCO2C2H5]CO2K (R)-(-)-α-[(3-ethoxy-1-methyl-3-oxo-1-propenyl)amino]benzeneacetic acid potassium salt \n''CH3(CH2)1413CO2K potassium palmitate-1-13 C \n''C16H12BKS4 potassium tetrakis(2-thienyl)borate \n''CH3(CH2)13CD2CO2K potassium palmitate-2,2-d 2 \n''C6H12GeK2O6 dipotassium tris(1,2-benzenediolato-O,O')germanate \n''K2Si(O2C6H4)3 dipotassium tris(1,2-benzenediolato-O,O')silicate \n''C22H11Br4KO5 methyl eosin \n''C22H13Br4KO4 3',3'',5',5''-tetrabromophenolphthalein ethyl ester potassium salt \n''(ClC6H4)4BK potassium tetrakis(4-chlorophenyl)borate \n''KPt(NH3)Cl3 potassium aminetrichloroplatinate(II) \n''K2RuCl5(H2O) potassium aquapentachlororuthenate(III) \n''K2Ru(NO)Cl5 potassium pentachloronitrosylruthenate(II) \n''K4[(RuCl5)2O]·xH2O potassiumμ-oxobis[pentachlororuthenate(IV)]hydrate \n''CrK(SO4)2·12H2O chrome alum \n''Cr2HKO9Zn2 zinc potassium chromate \n''FSO3K potassium fluorosulfate \n''HN(SO3K)2 potassium imidodisulfonate \n''K2DPO4 dipotassium deuterium phosphate \n''K2Pd(S2O3)2·H2O palladium(II)potassium thiosulfate monohydrate \n''(KSO3)2NO potassium nitrosodisulfonate \n''K(UO2)(NO3)3 potassium uranyl nitrate \n''K2Al2O4·3H2O potassium aluminate trihydrate \n''K2B4O7·5H2O potassium tetraborate pentahydrate \n''K2CO3·1.5H2O potassium carbonate sesquihydrate \n''K2C2O6·H2O potassium percarbonate monohydrate \n''K2[Ir(NO)Cl5] potassium pentachloronitrosyliridate(III) \n''K2SO3·2H2O potassium sulfite dihydrate \n''K2TeO4·3H2O potassium tellurate(VI) trihydrate \n''K4P2O7·3H2O potassium pyrophosphate trihydrate \n''CF3SO3K potassium trifluoromethanesulfonate \n''BrCH2BF3K potassium(bromomethyl)trifluoroborate \n''CH3COOP(O)(OK)(OLi) lithium potassium acetyl phosphate \n''K[(H2C=CH2)PtCl3]·xH2O potassium trichloro(ethylene)platinate(II)hydrate \n''C3H2KNO2Se potassium selenocyanoacetate \n''CF3(CF2)3SO3K potassium nonafluoro-1-butanesulfonate \n''K2Ni(CN)4·xH2O potassium tetracyanonickelate(II)hydrate \n''K2Pt(CN)4·xH2O potassium tetracyanoplatinate(II)hydrate \n''C4H3BF3KS potassium 3-thiophenetrifluoroborate \n''C4H4KNO4S acesulfame potassium \n'""", '19', '39.10')
        self.colorK = colorK = "purple"
        self.K = tk.Button(self, text=K[0], width=5, height=2, bg=colorK, font=10, borderwidth=3,
                           command=lambda text=K: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorK, text[0], text[3], text[4]), self.voice(text[1]), self.compound_K()])
        self.K.grid(row=6, column=2)

        Rb = ('Rb', 'Rubidium', """'RbBr rubidium bromide\n''RbCl rubidium chloride\n''RbF rubidium fluoride\n''RbI rubidium iodide\n''RbO2 rubidium superoxide\n''Rb2Se rubidium selenide\n''Rb3Sb rubidium antimonide\n''BF4Rb rubidium fluoroborate\n''Br2ClRb rubidium chlorobromo bromide\n''Rb2CO3 rubidium carbonate\n''RbClO4 rubidium perchlorate\n''RbOH rubidium hydroxide\n''RbOH·xH2O rubidium hydroxide hydrate\n''RbNO3 rubidium nitrate\n''O3RbV rubidium vanadium trioxide\n''Rb2GeF6 rubidium hexafluorogermanate\n''RbH2AsO4 rubidium dihydrogenarsenate\n''HCO2Rb rubidium formate\n''CH3CO2Rb rubidium acetate\n'""", '37', '85.41')
        self.colorRb = colorRb = "dark violet"
        self.Rb = tk.Button(self, text=Rb[0], width=5, height=2, bg=colorRb, font=10, borderwidth=3,
                           command=lambda text=Rb: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRb, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Rb()])
        self.Rb.grid(row=7, column=2)

        Cs = ('Cs', 'Cesium', """'CsBr cesium bromide\n''CsBr3 cesium tribromide\n''CsCl cesium chloride\n''CsF cesium fluoride\n''CsI cesium iodide\n''CsI3 cesium triiodide\n''CsN3 cesium azide\n''CsO2 cesium superoxide\n''Cs2O3 cesium trioxide\n''Cs3Sb cesium antimonide\n''Cs2AlF5 cesium fluoroaluminate\n''AsCs3O4 cesium arsenate\n''BCsO2 cesium metaborate\n''Br2CsI cesium dibromoiodate\n''Cs2CO3 cesium carbonate\n''CsClO3 cesium chlorate\n''CsClO4 cesium perchlorate\n''Cl2CsI cesium dichloroiodide\n''Cs2CrO4 cesium chromate\n''CsAlCl4 cesium tetrachloroaluminate\n''CsBF4 cesium fluoroborate\n''CsOH cesium hydroxide\n'""", '55', '132.91')
        self.colorCs = colorCs = "blue violet"
        self.Cs = tk.Button(self, text=Cs[0], width=5, height=2, bg=colorCs, font=10, borderwidth=3,
                           command=lambda text=Cs: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCs, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cs()])
        self.Cs.grid(row=8, column=2)

        Fr = ('Fr', 'Francium', """'Fr francium metal\n'""", '87', '223')
        self.colorFr = colorFr = "MediumOrchid4"
        self.Fr = tk.Button(self, text=Fr[0], width=5, height=2, bg=colorFr, font=10, borderwidth=3,
                           command=lambda text=Fr: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorFr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Fr()])
        self.Fr.grid(row=9, column=2)

        
        Be = ('Be', 'Beryllium', """'Be beryllium \n''B2Be beryllium boride \n''B6Be beryllium hexaboride \n''BeBr2 beryllium bromide \n''BeCl2 beryllium chloride \n''BeF2 beryllium fluoride \n''BeH2 beryllium hydride \n''BeI2 beryllium iodide \n''BeO beryllium oxide \n''BeS beryllium sulfide \n''BeSe beryllium selenide \n''BeTe beryllium telluride \n''Be12Nb beryllium compound with niobium (12:1) \n''Be12Ti beryllium compound with titanium (12:1) \n''Be12V beryllium compound with vanadium (12:1) \n''CBe2 beryllium carbide \n''Be(OH)2 beryllium hydroxide \n''Be(NO3)2 beryllium nitrate \n''BeSO4 beryllium sulfate \n''Be2O4Si diberyllium monosilicate \n''Be3(PO4)2 beryllium phosphate \n''BeCO3 beryllium carbonate \n''Na2BeF4 sodium tetrafluoroberyllate \n''Al2Be3O18Si6 beryl \n''BeHPO4 beryllium hydrogen phosphate \n''Be2SiO4 beryllium silicate \n''BeH6N2O9 nitric acid, beryllium salt, trihydrate \n''BeH8N2O10 beryllium nitrate tetrahydrate \n''BeSO4·4H2O beryllium sulfate tetrahydrate \n''BeK2(SO4)2 beryllium potassium sulfate \n''C4H6BeO4 beryllium acetate \n''C6H10BeO6 lactic acid, beryllium salt \n''Be[CH3COCH=C(O)CH3]2 beryllium acetylacetonate \n''C12H18Be4O13 beryllium oxide acetate \n''BeCO3·4H2O beryllium carbonate tetrahydrate \n''BeC2O4·3H2O beryllium oxalate trihydrate \n''Be(ClO4)2·4H2O beryllium perchlorate tetrahydrate \n''BeSO4·2H2O beryllium sulfate dihydrate \n'""", '4', '9.01') 
        self.colorBe=colorBe="chartreuse2"
        self.Be = tk.Button(self, text=Be[0], width=5, height=2, bg=colorBe, font=10, borderwidth=3,
                           command=lambda text=Be: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorBe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Be()])
        self.Be.grid(row=4, column=3)
        
        Mg = ('Mg', 'Magnesium', """'Mg magnesium\n''As2Mg3 magnesium arsenide\n''MgBr2 magnesium bromide\n''MgCl2 magnesium chloride\n''MgF2 magnesium fluoride\n''MgH2 magnesium hydride\n''MgI2 magnesium iodide\n''MgB2 magnesium diboride\n''MgB6 magnesium hexaboride\n''MgB12 magnesium dodecaboride\n''MgO magnesium oxide\n''MgO2·xMgO magnesium peroxide\n''MgS magnesium sulfide\n''MgSe magnesium selenide\n''Mg2Ge magnesium germanide\n''Mg2Si magnesium silicide\n''Mg2Sn magnesium stannide\n''Mg3N2 magnesium nitride\n''Mg3P2 magnesium phosphide\n''Mg3Sb2 magnesium antimonide\n''MgO·Al2O3 magnesium aluminate\n''Mg3(AsO4)2 magnesium arsenate\n''As2Mg6O11 arsenic acid, magnesium salt (1:6)\n''MgCO3 magnesium carbonate\n''MgC2O4 magnesium oxalate\n''C4H10Mg diethylmagnesium\n''[CH3(CH2)3]2Mg di-n-butylmagnesium\n''Mg(C5H5)2 bis(cyclopentadienyl)magnesium(II)\n''C12H10Mg magnesium diphenyl\n''C20H30Mg bis(pentamethylcyclopentadienyl)magnesium\n''Mg(ClO4)2 magnesium perchlorate\n''Mg(OH)2 magnesium hydroxide\n''MgCr2O4 magnesium chromite\n''MgMoO4 magnesium molybdate\n''Mg(NH2)2 magnesium amide\n''Mg(NO3)2 magnesium nitrate\n''MgO3Si magnesium metasilicate\n''MgTiO3 magnesium titanate\n''MgZrO3 magnesium zirconate\n''MgSO4 magnesium sulfate\n''MgWO4 magnesium tungstate\n''Mg2GeO4 magnesium germanate\n''Mg2P2O7 magnesium pyrophosphate\n''Mg(V2O7) magnesium pyrovanadate\n''Mg2O8Si3 magnesium trisilicate\n''Mg2SiO4 magnesium orthosilicate\n''Mg2TiO4 magnesium orthotitanate\n''Mg3(PO4)2·5H2O Trimagnesium diphosphate pentahydrate\n''BaMgO6Si2 barium magnesium silicate\n''MgBr2·6H2O magnesium bromide hexahydrate\n''Br2H12MgO12 magnesium bromate hexahydrate\n''CD3MgI methyl-d 3-magnesium iodide solution\n''CH3MgBr methylmagnesium bromide\n''CH3MgCl methylmagnesium chloride\n''CH3MgI methylmagnesium iodide\n''HC≡CMgBr ethynylmagnesium bromide\n''CH≡CMgCl ethynylmagnesium chloride\n''CH2=CHMgBr vinylmagnesium bromide\n''CH2=CHMgCl vinylmagnesium chloride\n''C2H4MgO6 magnesium oxalate dihydrate\n''CH3CH2MgBr ethylmagnesium bromide\n''CH3CH2MgCl ethylmagnesium chloride\n''Mg(OCH3)2 magnesium methoxide\n''C2H6MgO6 magnesium formate dihydrate\n''CH3C≡CMgBr 1-propynylmagnesium bromide\n''CH3CH=CHMgBr 1-propenylmagnesium bromide\n''CH2=CHCH2MgBr allylmagnesium bromide\n''C3H5BrMg cyclopropylmagnesium bromide\n''CH2=C(CH3)MgBr isopropenylmagnesium bromide\n''CH2=CHCH2MgCl allylmagnesium chloride\n''CH3OMgOCO2CH3 magnesium methyl carbonate\n''(CH3)2CHMgCl isopropylmagnesium chloride\n''CH3CH2CH2MgCl propylmagnesium chloride\n''CH3CH=C(CH3)MgBr 1-methyl-1-propenylmagnesium bromide\n''(CH3)2C=CHMgBr 2-methyl-1-propenylmagnesium bromide\n''H2C=CHCH2CH2MgBr 3-butenylmagnesium bromide\n''H2C=CHCH(CH3)MgCl 1-methyl-2-propenylmagnesium chloride\n''CH3CH=CHCH2MgCl 2-butenylmagnesium chloride\n''H2C=C(CH3)CH2MgCl 2-methylallylmagnesium chloride\n''(CH3)2CHCH2MgBr isobutylmagnesium bromide\n''CH3(CH2)3MgCl butylmagnesium chloride\n''(CH3)2CHCH2MgCl isobutylmagnesium chloride\n''CH3CH2CH(CH3)MgCl sec-butylmagnesium chloride\n''(CH3)3CMgCl tert-butylmagnesium chloride\n''Mg(OC2H5)2 magnesium ethoxide\n''(MgCO3)4·Mg(OH)2·5H2O magnesium carbonate hydroxide pentahydrate\n''(CH3COO)2Mg·4H2O magnesium acetate tetrahydrate\n''C5H9MgBr cyclopentylmagnesium bromide\n''C5H9ClMg cyclopentylmagnesium chloride\n''BrMg(CH2)5MgBr pentamethylenebis(magnesium bromide)\n''C5H11MgBr pentylmagnesium bromide\n''C2H5C(CH3)2MgCl 1,1-dimethylpropylmagnesium chloride\n''(CH3)3CCH2MgCl 2,2-dimethylpropylmagnesium chloride\n''CH3(CH2)4MgCl pentylmagnesium chloride\n''C6F5MgBr pentafluorophenylmagnesium bromide\n''C6H5MgBr phenylmagnesium bromide\n''C6H5MgCl phenylmagnesium chloride\n''C6H11ClMg cyclohexylmagnesium chloride\n''CH3(CH2)5MgBr hexylmagnesium bromide\n''C6H13ClMg hexylmagnesium chloride\n''BrC6H4CH2MgBr 2-bromobenzylmagnesium bromide\n''BrC6H4CH2MgBr 3-bromobenzylmagnesium bromide\n''CH3C6H4MgBr o-tolylmagnesium bromide\n''CH3C6H4MgBr p-tolylmagnesium bromide\n''C6H5CH2MgCl benzylmagnesium chloride\n''CH3C6H4MgCl m-tolylmagnesium chloride\n''CH3C6H4MgCl o-tolylmagnesium chloride\n''CH3(CH2)6MgBr heptylmagnesium bromide\n''C8H5MgBr phenylethynylmagnesium bromide\n''(CH3)2C6H3MgBr 2,3-dimethylphenylmagnesium bromide\n''(CH3)2C6H3MgBr 2,4-dimethylphenylmagnesium bromide\n''(CH3)2C6H3MgBr 2,5-dimethylphenylmagnesium bromide\n''(CH3)2C6H3MgBr 2,6-dimethylphenylmagnesium bromide\n''(CH3)2C6H3MgBr 3,5-dimethylphenylmagnesium bromide\n''C2H5C6H4MgBr 4-ethylphenylmagnesium bromide\n''H3CC6H4CH2MgCl 2-methylbenzylmagnesium chloride\n''(CH3)2C6H3MgCl 3,4-dimethylphenylmagnesium chloride\n''CH3C6H4CH2MgCl 3-methylbenzylmagnesium chloride\n''C6H4CH3CH2MgCl 4-methylbenzylmagnesium chloride\n''C6H5CH2CH2MgCl phenethylmagnesium chloride\n''C8H17BrMg (2-ethylhexyl)magnesium bromide\n''CH3(CH2)7MgBr octylmagnesium bromide\n''C8H17MgCl octylmagnesium chloride\n''(CH3)3COMgOC(CH3)3 magnesium di-tert-butoxide\n''(CH3)3C6H2MgBr 2-mesitylmagnesium bromide\n''C6H4CH2CH2CH3MgBr 4-n-propylphenylmagnesium bromide\n''CH3(CH2)8MgBr nonylmagnesium bromide\n''C10H7BrMg 1-naphthylmagnesium bromide\n''C10H7BrMg 2-naphthylmagnesium bromide\n''(CH3)3CC6H4MgBr 4-tert-butylphenylmagnesium bromide\n''C6H5C(CH3)2CH2MgCl 2-methyl-2-phenylpropylmagnesium chloride\n''[CH3COCHC(O)CH3]2Mg·2H2O magnesium acetylacetonate dihydrate\n''C10H21BrMg 3,7-dimethyloctylmagnesium bromide\n''CH3(CH2)9MgBr decylmagnesium bromide\n''C10H6CH3MgBr 2-methyl-1-naphthylmagnesium bromide\n''C11H9BrMg (2-naphthalenylmethyl)magnesium bromide\n''C10H6CH3MgBr 4-methyl-1-naphthylmagnesium bromide\n''C11H25LiMg lithium dibutyl(isopropyl)magnesate\n''C6H5C6H4MgBr 2-biphenylmagnesium bromide\n''C6H5C6H4MgBr 4-biphenylmagnesium bromide\n''C12H10Mg3O14 magnesium citrate\n''(C2H5O2CCH=CHCO2)2Mg fumaric acid monoethyl ester magnesium salt\n''[HOCH2[CH(OH)]4CO2]2Mg·xH2O magnesium D-gluconate hydrate\n''CH3(CH2)11MgBr dodecylmagnesium bromide\n''C12H27LiMg tri-n-butyllithium magnesate\n''C14H9BrMg 9-phenanthrylmagnesium bromide\n''CH3(CH2)13MgCl tetradecylmagnesium chloride\n''CH3(CH2)14MgBr pentadecylmagnesium bromide\n''(HO2CC6H4CO3)2Mg·6H2O magnesium bis(monoperoxyphthalate)hexahydrate\n''CH3(CH2)17MgCl octadecylmagnesium chloride\n''[(CH3)3CCOCHC(O)C(CH3)3]2Mg·xH2O magnesium bis(2,2,6,6-tetramethyl-3,5-heptanedionate)hydrate\n''C32H16MgN8 magnesium phthalocyanine\n''C36H44MgN4 2,3,7,8,12,13,17,18-octaethyl-21H,23 H-porphine magnesium(II)\n''[CH3(CH2)16CO2]2Mg magnesium stearate\n''MgCl2·6H2O magnesium chloride hexahydrate\n''Mg(ClO4)2·6H2O magnesium perchlorate hexahydrate\n''MgCrO4·xH2O magnesium chromate hydrate\n''MgHPO4·3H2O magnesium phosphate\n''Mg(MnO4)2·xH2O magnesium permanganate hydrate\n''MgSO4·H2O magnesium sulfate monohydrate\n''Mg(HSO3)2 magnesium bisulfite\n''Mg3(PO4)2·xH2O magnesium phosphate hydrate\n''H2Mg3O12Si4 talc\n''H4MgN2O8 magnesium nitrate dihydrate\n''H4Mg3O9Si2 chrysotile\n''MgHPO4·3H2O magnesium hydrogen phosphate trihydrate\n''Mg(NO3)2·6H2O magnesium nitrate hexahydrate\n''MgS2O3·6H2O magnesium thiosulfate hexahydrate\n''MgSO4·7H2O magnesium sulfate heptahydrate\n''MgI2·8H2O magnesium iodide octahydrate\n''MgI2·6H2O magnesium iodide hexahydrate\n''Mg(NH4)(AsO4) magnesium ammonium arsenate\n''Mg6Al2(CO3)(OH)16·4H2O hydrotalcite,synthetic\n''(CF3SO3)2Mg magnesium trifluoromethanesulfonate\n''C3H7Cl2LiMg isopropylmagnesium chloride lithium chloride complex\n''C4H3BrMgS 2-thienylmagnesium bromide\n''C4H3IMgS 3-thienylmagnesium iodide\n''C4H7BrMgO2 (1,3-dioxolan-2-ylmethyl)magnesium bromide\n''MgBr2·O(C2H5)2 magnesium bromide ethyl etherate\n''(CH3)3SiCH2MgCl (trimethylsilyl)methylmagnesium chloride\n''C5H5BrMgS 3-methyl-2-thienylmagnesium bromide\n''F3C6H2MgBr 3,4,5-trifluorophenylmagnesium bromide\n''Cl2C6H3MgBr 3,4-dichlorophenylmagnesium bromide\n''Cl2C6H3MgBr 3,5-dichlorophenylmagnesium bromide\n''F2C6H3MgBr 3,4-difluorophenylmagnesium bromide\n''F2C6H3MgBr 3,5-difluorophenylmagnesium bromide\n''C6H4BrClMg 3-chlorophenylmagnesium bromide\n''ClC6H4MgBr 4-chlorophenylmagnesium bromide\n''FC6H4MgBr 3-fluorophenylmagnesium bromide\n''FC6H4MgBr 4-fluorophenylmagnesium bromide\n''C6H11BrMgO2 (1,3-dioxan-2-ylethyl)magnesium bromide\n''C7H5BrMgO2 3,4-(methylenedioxy)phenylmagnesium bromide\n''ClC6H3(CH3)MgBr 4-chloro-2-methylphenylmagnesium bromide\n''FC6H3(CH3)MgBr 3-fluoro-4-methylphenylmagnesium bromide\n''FC6H3(CH3)MgBr 4-fluoro-2-methylphenylmagnesium bromide\n''FC6H3(CH3)MgBr 4-fluoro-3-methylphenylmagnesium bromide\n''FC6H3(CH3)MgBr  5-fluoro-2-methylphenylmagnesium bromide\n''C6H3FCH3MgCl 3-fluoro-2-methylphenylmagnesium chloride\n''FC6H4CH2MgCl 4-fluorobenzylmagnesium chloride\n''CH3OC6H4MgBr 2-methoxyphenylmagnesium bromide\n'""", '12', '24.31')
        self.colorMg=colorMg="chartreuse3"
        self.Mg = tk.Button(self, text=Mg[0], width=5, height=2, bg=colorMg, font=10, borderwidth=3,
                           command=lambda text=Mg: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorMg, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Mg()])
        self.Mg.grid(row=5, column=3)

        Ca = ('Ca', 'Calcium', """'Ca calcium\n''CaB6 calcium hexaboride\n''CaBr2 calcium bromide\n''CaC2 calcium carbide\n''CaCl2 calcium chloride\n''CaF2 calcium fluoride\n''CaF2 fluorspar\n''CaH2 calcium hydride\n''CaI2 calcium iodide\n''CaO lime\n''CaO2 calcium peroxide\n''CaS calcium sulfide\n''CaSe calcium selenide\n''CaSi calcium silicide\n''CaTe calcium telluride\n''Ca3N2 calcium nitride\n''Ca3P2 calcium phosphide\n''Al2CaO4 calcium aluminate\n''As2Ca3O8 pencal calcium arsenate\n''As2Ca3O8 tricalcium orthoarsenate calcium arsenate\n''B2CaO4 calcium metaborate\n''Br2CaO6 calcium bromate\n''CaNCN calcium cyanamide\n''CaCO3 aragonite\n''CaCO3 calcium carbonate\n''Ca13CO3 calcium carbonate-13 C\n''C2CaN2 calcium cyanide\n''CaC2O4 calcium oxalate\n''Ca(AlH4)2 calcium tetrahydroaluminate\n''CaAsO3 calcium arsenite\n''Ca(ClO2)2 calcium chlorite\n''CaCl2O6 calcium chlorate\n''Ca(ClO4)2 calcium perchlorate\n''CaCrO4 calcium chromate\n''CaSiF6 calcium hexafluorosilicate\n''Ca(OH)2 calcium hydroxide\n''CaSx calcium polysulfide calcium sulfide\n''CaMn2O8 calcium permanganate\n''CaMoO4 calcium molybdate\n''Ca(15NO3)2 calcium nitrate-15 N2\n''Ca(NO2)2 calcium nitrite\n''Ca(NO3)2 calcium nitrate\n''CaS2O3·6H2O calcium thiosulfate hexahydrate\n''CaSiO3 calcium silicate\n''CaTiO3 calcium titanate\n''CaZrO3 calcium zirconate\n''CaSO4 drierite®without indicator, 10-20 mesh\n''CaWO4 calcium tungstate\n''Ca(ReO4)2 calcium perrhenate\n''Ca2PbO4 calcium plumbate\n''Ca3O5Si tricalcium silicate\n''Ca3(PO4)2 tricalcium diphosphate\n''AsCaHO4 arsenic acid, calcium salt (1:1)\n''(Ba,Ca)TiO3 barium calcium titanate\n''CaBr2·xH2O calcium bromide hydrate\n''C2BaCaO6 carbonic acid, barium calcium salt\n''C2H2CaO4 calcium formate\n''C2CaO4·xH2O calcium oxalate hydrate\n''CaC2O4·H2O calcium oxalate monohydrate\n''Ca(OCH3)2 calcium methoxide\n''(CH3CO2)2Ca calcium acetate\n''(CH3COO)2Ca·xH2O calcium acetate hydrate\n''C6H7CaO7 isocitrate calcium complex\n''C6H8CaO8 calcium d-glucarate\n''(CH3CH2COO)2Ca calcium propionate\n''C6H10CaO6 calcium lactate\n''Ca(OCH(CH3)2)2 calcium isopropoxide\n''[HOCH2CH(OH)CO2]2Ca·2H2O D-glyceric acid calcium salt dihydrate\n''[HOCH2CH(OH)CO2]2Ca·2H2O L-glyceric acid calcium salt dihydrate\n''C6H20CaO11 calcium lactate pentahydrate\n''C8H14CaO10 L-threonic acid hemicalcium salt\n''[CH3(CH2)3CH(C2H5)CO2]2Ca calcium 2-ethylhexanoate\n''Ca(C5H7O2)2·xH2O calcium acetylacetonate hydrate\n''(C2H5O2CCH=CHCO2)2Ca fumaric acid monoethyl ester calcium salt\n''C12H14CaO12·2H2O calcium L-ascorbate dihydrate\n''[O2CCH2C(OH)(CO2)CH2CO2]2Ca3·4H2O calcium citrate tetrahydrate\n''[C2H5CH(CH3)COCO2]2Ca·2H2O 3-methyl-2-oxopentanoic acid calcium salt dihydrate\n''[HOCH2[CH(OH)]4CO2]2Ca calcium gluconate\n''C12H18O14·2H2O 2-keto-D-gluconic acid hemicalcium salt dihydrate\n''C14H22CaO10 3,4-O-isopropylidene-L-threonic acid calcium salt\n''[C6H11(CH2)3CO2]2Ca calcium cyclohexanebutyrate\n''Ca(OCC(CH3)3CHCOC(CH3)3)2 calcium bis(2,2,6,6-tetramethyl-3,5-heptanedionate)\n''C36H66CaO4 calcium oleate\n''C36H70CaO4 calcium stearate\n''C40H58CaO4 calcium resinate\n''C41H70CaO9 calcium ionomycin\n''CaBr2·6H2O calcium bromide hexahydrate\n''Ca(ClO4)2·4H2O calcium perchlorate tetrahydrate\n''CaCl2·xH2O calcium chloride hydrate\n''CaCl2·H2O calcium chloride monohydrate\n''CaCl2·4H2O calcium chloride tetrahydrate\n''CaCl2·2H2O calcium chloride dihydrate\n''CaCl2H4O8 calcium chlorate dihydrate\n''CaCl2·6H2O calcium chloride hexahydrate\n''CaCrH4O6 calcium chromate dihydrate\n''Ca(IO3)2 calcium iodate\n''CaHPO4 calcium hydrogen phosphate\n''CaI2·xH2O calcium iodide hydrate\n''Ca(NO3)2·xH2O calcium nitrate hydrate\n''Ca(HSO3)2 calcium bisulfite\n'""", '20', '40.08')
        self.colorCa=colorCa="green2"
        self.Ca = tk.Button(self, text=Ca[0], width=5, height=2, bg=colorCa, font=10, borderwidth=3,
                           command=lambda text=Ca: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ca()])
        self.Ca.grid(row=6, column=3)

        Sr = ('Sr', 'Strontium', """'Sr strontium\n''SrB6 strontium hexaboride\n''SrBr2 strontium bromide\n''SrCl2 strontium chloride\n''SrF2 strontium fluoride\n''H2Sr strontium hydride\n''SrI2 strontium iodide\n''SrO strontium oxide\n''SrO2 strontium peroxide\n''Sr3P2 strontium phosphide\n''SrS strontium sulfide\n''SrSe strontium selenide\n''SrSi2 strontium silicide\n''Sr3(AsO4)2 strontium arsenate\n''SrCO3 strontium carbonate\n''SrC2O4 strontium oxalate\n''Cl2O6Sr strontium chlorate\n''Sr(ClO4)2 strontium perchlorate\n''SrCrO4 strontium chromate\n''SrFe12O19 strontium ferrite\n''Sr(OH)2 strontium hydroxide\n''Sr(OH)2·8H2O strontium hydroxide octahydrate\n''SrIO3 strontium iodate\n''SrMoO4 strontium molybdate\n''Sr(NO3)2 strontium nitrate\n''SrTiO3 strontium titanate\n''SrZrO3 strontium zirconate\n''SrSO4 strontium sulfate\n''SrSeO4 strontium selenate\n''SrNb2O6 strontium niobate\n''As2H8O8Sr strontium arsenite tetrahydrate\n''BaSr(NbO3)4 barium strontium niobate\n''SrBr2·6H2O strontium bromide hexahydrate\n''(CH3CO2)2Sr strontium acetate\n''Sr(OCH(CH3)2)2 strontium isopropoxide\n''[CH3COCH=C(O)CH3]2Sr strontium acetylacetonate\n''C20H34O4Sr strontium cyclohexanebutyrate\n''Sr(OCC(CH3)3CHCOC(CH3)3)2·2H2O strontium bis(2,2,6,6-tetramethyl-3,5-heptanedionate)dihydrate\n''SrCl2·6H2O strontium chloride hexahydrate\n''SrHPO4 strontium hydrogenphosphate\n''SrI2·6H2O strontium iodide hexahydrate\n''SrLaAlO4 strontium lanthanum aluminate\n''Ba2SrWO6 barium strontium tungsten oxide\n''Sr(OCC(CH3)3CHCOCF2CF2CF3)2 strontium bis(6,6,7,7,8,8,8-heptafluoro-2,2-dimethyl-3,5-octanedionate)\n''Sr(BrO3)2·H2O strontium bromate monohydrate\n''Sr(CN)2·4H2O strontium cyanide dihydrate\n''Sr(MnO4)2·3H2O strontium permanganate trihydrate\n''SrS2O3·5H2O strontium thiosulfate pentahydrate\n''Sr(CHO2)2·2H2O strontium formate dihydrate\n''SrFe(CN)6·15H2O strontium ferrocyanide pentadecahydrate\n'""", '38', '87.62')
        self.colorSr=colorSr="green3"
        self.Sr = tk.Button(self, text=Sr[0], width=5, height=2, bg=colorSr, font=10, borderwidth=3,
                           command=lambda text=Sr: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Sr()])
        self.Sr.grid(row=7, column=3)

        Ba = ('Ba', 'Barium', """'Ba barium\n''BaAl4 aluminium, compound with barium (4:1)\n''BaB6 barium hexaboride\n''BaBr2 barium bromide\n''BaC2 barium carbide\n''BaCl2 barium chloride\n''BaF2 barium fluoride\n''BaH2 barium hydride\n''BaI2 barium iodide\n''BaN6 barium azide\n''BaO barium oxide\n''BaO2 barium peroxide\n''BaS barium sulfide\n''BaSe barium selenide\n''BaSi2 barium silicide\n''BaTe barium telluride\n''Ba3Sb2 barium antimonide\n''Ba(BF4)2 barium fluoborate\n''Ba(BO2)2 barium borate\n''BaBiO3 barium bismuthate\n''BaClF barium chloride fluoride\n''BaCl2O6 barium chlorate\n''Ba(ClO4)2 barium perchlorate\n''BaCrO4 barium chromate\n''BaSiF6 barium hexafluorosilicate\n''BaFe12O19 barium iron oxide\n''BaGeF6 barium hexafluorogermanate\n''Ba(OH)2 barium hydroxide\n''BaH2S polybarit barium sulfide\n''Ba(OH)2·xH2O barium hydroxide hydrate\n''Ba(OH)2·H2O barium hydroxide monohydrate\n''BaH18O10 barium hydroxide actahydrate\n''BaHgI4 barium tetraiodomercurate(II)\n''BaI2O6 barium iodate\n''Ba(IO4)2 barium periodate\n''BaMn2O8 barium permanganate\n''BaMoO4 barium molybdate\n''BaN2O4 barium nitrite\n''Ba(NO3)2 barium nitrate\n''BaSO3 barium sulfite\n''BaSeO3 barium selenite\n''BaSiO3 barium metasilicate\n''BaO3Sn barium stannate\n''BaTiO3 barium titanate\n''BaZrO3 barium zirconate\n''BaSO4 barium sulfate\n''BaSeO4 barium selenate\n''BaSeO4 barium selenate(VI)\n''BaWO4 barium tungstate\n''Ba(PO3)2 barium dimetaphosphate\n''BaTi4O9 barium tetratitanate\n''BaPbO3 barium plumbate\n''Ba(NbO3)2 barium niobate\n''Ba2P2O7 barium pyrophosphate\n''Ba3(CrO4)2 barium chromate(V)\n''BaCO3 barium carbonate\n''Ba(CN)2 barium cyanide\n''BaC2O4 barium oxalate\n''Ba(BrO3)2 barium bromate\n''BaBr2H4O2 barium bromide dihydrate\n''(Ba,Ca)TiO3 barium calcium titanate\n''Ba(ClO3)2·H2O barium chlorate monohydrate\n''Ba(ClO4)2·xH2O barium perchlorate hydrate\n''BaCl2·2H2O barium chloride dihydrate\n''BaCr2O7·2H2O barium dichromate dihydrate\n''Ba(IO3)2·H2O barium iodate monohydrate\n''BaMnO4 barium manganate\n''BaS2O3 barium thiosulfate\n''BaHPO4 barium hydrogen phosphate\n''Bal2·2H2O barium iodide dihydrate\n''BaMgO6Si2 barium magnesium silicate\n''BaO5TiZr barium titanate zirconate\n''BaSr(NbO3)4 barium strontium niobate\n''BaTi(SiO3)3 barium titanium silicate\n''Ba2NaNb5O15 barium sodium niobium oxide\n''Ba13CO3 barium carbonate-13 C\n''C2BaCaO6 carbonic acid, barium calcium salt\n''C2BaN2S2 barium thiocyanate\n''C2H2BaO4 barium formate\n''C4BaN4Pt barium tetracyanoplatinate\n''C4H4BaO4 barium succinate\n''C4H4BaO6 barium tartrate\n''(CH3COO)2Ba barium acetate\n''BaC6Cl2O4 barium chloranilate\n''C6H10BaO6 barium dilactate\n''Ba(OCH(CH3)2)2 barium isopropoxide\n''[CH3(CH2)3CH(C2H5)CO2]2Ba barium bis(2-ethylhexanoate)\n''C10H14BaO4 barium acetylacetonate\n''C10H18BaO4 barium tetrahydrofurfuryl oxide\n''[C6H11(CH2)3CO2]2Ba barium cyclohexanebutyrate\n''C20H38BaO4 barium neodecanoate\n''Ba(OCC(CH3)3CHCOC(CH3)3)2·xH2O barium bis(2,2,6,6-tetramethyl-3,5-heptanedionate)hydrate\n''C24H40BaO2 bis(pentamethylcyclopentadienyl)barium,dimethoxyethane(DME)adduct\n''C36H66BaO6 ricinoleic acid, barium salt\n''C36H70BaO4barium stearate\n''YBa2Cu3Ox,x=(6.7) yttrium barium copper oxide\n''Ba(BO2)2·2H2O barium metaborate dihydrate\n''Ba(BO2)2·H2O barium metaborate monohydrate\n''Ba(BrO3)2·H2O barium bromate monohydrate\n''BaC2O4·H2O barium oxalate monohydrate\n''Ba(ClO4)2·3H2O barium perchlorate trihydrate\n''Ba(HS)2·4H2O barium hydrosulfide tetrahydrate\n''Ba(OH)2·8H2O barium hydroxide octahydrate\n''BaS2O3·H2O barium thiosulfate monohydrate\n''BaS2O6·2H2O barium dithionate dihydrate\n''BaSnO3·3H2O barium stannate trihydrate\n''Ba2CaWO6 barium calcium tungsten oxide\n''Ba2SrWO6 barium strontium tungsten oxide\n''Ba3Y2WO9 barium yttrium tungsten oxide\n''Ba(Fe(CN)5(NO)) barium nitroprusside\n''BaC6HN3O8 barium 2,4,6-trinitroresorcinolate\n''C6H11BaO9P D-fructose, 6-(dihydrogen phosphate), barium salt (1:1)\n''C6H11BaO9P D-glucose, 6-(dihydrogen phosphate), barium salt\n''BaC6H11O9P galactose 6-(barium phosphate)\n''C8H4BaO12Sb2 antimony barium tartrate\n''Ba(C5HF6O2)2 barium hexafluoroacetylacetonate\n''C12H8BaN2O6 phenol, p-nitro, barium salt\n''C12H10BaO6S2 barium di(benzenesulfonate)\n''(CH3C6H4SO3)2Ba barium di(toluene-4-sulfonate)\n''Ba(OCC(CH3)3CHCOCF2CF2CF3)2 barium bis(6,6,7,7,8,8,8-heptafluoro-2,2-dimethyl-3,5-octanedionate)\n''C22H36BaN2O18 barium N-acetylneuraminate\n''C28H28BaO8P2 barium dibenzylphosphate\n''C30H54BaO12Ti barium titanium(IV)tetrahydrofurfuryl oxide\n''Ba(C2H3O2)2·H2O barium acetate monohydrate\n''Ba(H2PO2)2·H2O barium hypophosphite monohydrate\n''Ba(SCN)2·2H2O barium thiocyanate dihydrate\n''Ba2Fe(CN)6·6H2O barium ferrocyanide hexahydrate\n''Ba3(C6H5O7)2·H2O barium citrate monohydrate\n''(CF3SO3)2Ba barium trifluoromethanesulfonate\n''Ba(SCN)2·xH2O barium thiocyanate hydrate\n''C2H6BaN2O3S2 barium thiocyanate trihydrate\n''NCCH2CH2OPO3Ba·xH2O barium 2-cyanoethylphosphate hydrate\n''BaPt(CN)4·xH2O barium tetracyanoplatinate(II)hydrate\n''C4H8BaN4O4Pt barium tetracyanoplatinate(II) tetrahydrate\n''C8H12BaCr2N12S8 barium reineckate\n''C12H24BaN2O6S2 barium cyclohexanesulfamate\n''(C12H10NO3S)2Ba barium diphenylamine-4-sulfonate\n''C18H13BaClN2O6S barium 4-[(4-chloro-5-methyl-2-sulfonatophenyl)azo]-3-hydroxy-2-naphthoate\n''C32H14BaCuN8O6S2 fast sky blue\n''Ba(CH3COCHCOCH3)2·8H2O barium 2,4-pentanedioate octahydrate\n'""", '56', '137.33')
        self.colorBa=colorBa="chartreuse4"
        self.Ba = tk.Button(self, text=Ba[0], width=5, height=2, bg=colorBa, font=10, borderwidth=3,
                           command=lambda text=Ba: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorBa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ba()])
        self.Ba.grid(row=8, column=3)


        Ra = ('Ra', 'Radium', """'Ra radium\n''RaSO4 radium sulfate\n'""", '88', '226.03')
        self.colorRa=colorRa="green4"
        self.Ra = tk.Button(self, text=Ra[0], width=5, height=2, bg=colorRa, font=10, borderwidth=3,
                           command=lambda text=Ra: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ra()])
        self.Ra.grid(row=9, column=3)


        Sc = ('Sc', 'Scandium', """'Sc scandium\n''ScCl3 scandium chloride\n''ScF3 scandium fluoride\n''ScI3 scandium(III)iodide\n''Sc2O3 scandium(III) oxide\n''ScSb scandium antimonide\n''ScB2 scandium boride\n''Sc2Te3 scandium telluride\n''Sc(C5H5)3 tris(cyclopentadienyl)scandium(III)\n''C27H39Sc tris(butylcyclopentadienyl)scandium(III)\n''Sc(OH)3 scandium hydroxide\n''N3O9Sc scandium nitrate\n''ScBr3 scandium tribromide\n''ScBr3·xH2O scandium(III)bromide hydrate\n''Sc(OCH(CH3)2)3 scandium(III)isopropoxide\n''Sc2(C2O4)3·xH2O scandium(III)oxalate hydrate\n''(CH3CO2)3Sc·xH2O scandium(III)acetate hydrate\n''[CH3COCH=C(O)CH3]3Sc·xH2O scandium(III)acetylacetonate hydrate\n''Sc(OCC(CH3)3CHCOC(CH3)3)3·xH2O scandium(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate)hydrate\n''ScCl3·6H2O scandium(III)chloride hexahydrate\n''ScCl3·xH2O scandium(III)chloride hydrate\n''Sc(ClO4)3 scandium(III)perchlorate\n''Sc2(SO4)3·5H2O scandium(III)sulfate pentahydrate\n''Sc(NO3)3·xH2O scandium(III)nitrate hydrate\n''Sc(SO3CF3)3 scandium(III)triflate\n''(NH4)2CO3·Sc2(CO3)3·H2O ammonium carbonate/scandium carbonate double salt monohydrate\n''Sc(C5HF6O2)3 scandium(III)hexafluoroacetylacetonate\n''Sc(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]scandium(III)\n'""", '21', '44.96')
        self.colorSc=colorSc="Slategray1"
        self.Sc = tk.Button(self, text=Sc[0], width=5, height=2, bg=colorSc, font=10, borderwidth=3,
                           command=lambda text=Sc: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSc, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Sc()])
        self.Sc.grid(row=6, column=4)

        Y = ('Y', 'Yttrium', """'Y yttrium\n''AsY yttrium arsenide\n''YBr3 yttrium(III)bromide\n''YC2 yttrium carbide\n''YCl3 yttrium chloride\n''YF3 yttrium fluoride\n''YI3 yttrium(III)iodide\n''Y2O3 yttrium oxide\n''PY yttrium phosphide\n''YB6 yttrium boride\n''YSb yttrium antimonide\n''Y2S3 yttrium sulfide\n''Y3Al5O12 yttrium aluminum oxide\n''YAG yttrium aluminum garnet\n''Y2(CO3)3 yttrium carbonate\n''Y(C5H5)3 tris(cyclopentadienyl)yttrium(III)\n''Y(C5H4CH2(CH2)2CH3)3 tris(butylcyclopentadienyl)yttrium(III)\n''Y3Fe5O12 yttrium iron oxide\n''Y(OH)3 yttrium hydroxide\n''Y(IO3)3 yttrium iodate\n''N3O9Y yttrium(III) nitrate\n''YPO4 yttrium(III)phosphate\n''YVO4 yttrium(III) orthovanadate\n''YVO4 yttrium vanadate\n''Y2(CO3)3·xH2O yttrium(III)carbonate hydrate\n''C3H6O12Y2 yttrium carbonate trihydrate\n''Y(OCH(CH3)2)3 yttrium(III)isopropoxide\n''(CH3CO2)3Y·xH2O yttrium(III)acetate hydrate\n''[CH3(CH2)3CH(C2H5)CO2]3Y yttrium(III)2-ethylhexanoate\n''Y(OC4H9)3 yttrium(III)butoxide\n''Y(C5H7O2)3·xH2O yttrium(III)acetylacetonate hydrate\n''Y(OCC(CH3)3CHCOC(CH3)3)3 yttrium(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate)\n''Y(ClO4)3 yttrium(III)perchlorate\n''YCl3·6H2O yttrium(III)chloride hexahydrate\n''Y(NO3)3·4H2O yttrium(III)nitrate tetrahydrate\n''Y(NO3)3·6H2O yttrium(III) nitrate hexahydrate\n''Y2(SO4)3·8H2O yttrium(III)sulfate octahydrate\n''YBa2Cu3Ox,x=(6.7) yttrium barium copper oxide\n''Ba3Y2WO9 barium yttrium tungsten oxide\n''Y(CF3SO3)3 yttrium(III)trifluoromethanesulfonate\n''Y(CF3CO2)3·xH2O yttrium(III)trifluoroacetate hydrate\n''Y(C5HF6O2)3·2H2O yttrium(III)hexafluoroacetylacetonate dihydrate\n''[[(CH3)3Si]2N]3Y tris[N,N-bis(trimethylsilyl)amide]yttrium\n'""", '39', '88.91')
        self.colorY=colorY="Slategray2"
        self.Y = tk.Button(self, text=Y[0], width=5, height=2, bg=colorY, font=10, borderwidth=3,
                           command=lambda text=Y: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorY, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Y()])
        self.Y.grid(row=7, column=4)
        
        La = ('La', 'Lanthanum', """'La lanthanum\n''Br3La lanthanum bromide\n''LaC2La lanthanum carbide\n''LaCl3 lanthanum(III)chloride\n''LaF3 lanthanum fluoride\n''H3La lanthanum hydride\n''I3La lanthanum iodide\n''LaB6 lanthanum hexaboride\n''LaN lanthanum nitride\n''LaS lanthanum monosulfide\n''LaSb lanthanum antimonide\n''LaSi2 lanthanum silicide\n''La2O3 lanthanum oxide\n''La2S3 lanthanum sulfide\n''LaAlO3 lanthanum aluminum oxide\n''La(C5H5)3 tris(cyclopentadienyl)lanthanum(III)\n''C27H39La tris(tetramethylcyclopentadienyl)lanthanum(III)\n''La(ClO4)3 lanthanum(III) perchlorate\n''La(OH)3 lanthanum hydroxide\n''LaIO3 lanthanum iodate\n''La2(SO4)3 lanthanum(III)sulfate\n''Br3La·xH2O lanthanum(III)bromide hydrate\n''(CH3COO)3La·xH2O lanthanum(III) acetate hydrate\n''La2(CO3)3·xH2O lanthanum(III)carbonate hydrate\n''C3H16La2O17 lanthanum carbonate actahydrate\n''La2(C2O4)3·xH2O lanthanum(III)oxalate hydrate\n''La(C5H7O2)3·xH2O lanthanum(III)acetylacetonate hydrate\n''LaCl3·xH2O lanthanum(III)chloride hydrate\n''Cl3H12LaO18 lanthanum perchlorate hexahydrate\n''LaCl3·7H2O lanthanum(III)chloride heptahydrate\n''LaPO4·xH2O lanthanum(III)phosphate hydrate\n''La2(SO4)3·9H2O lanthanum(III)sulfate nonahydrate\n''La(NO3)3·xH2O lanthanum(III) nitrate hydrate\n''La2(SO4)3·xH2O lanthanum(III)sulfate hydrate\n''La(NO3)3·6H2O lanthanum(III)nitrate hexahydrate\n''SrLaAlO4 strontium lanthanum aluminate\n''La(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]lanthanum(III)\n''LaBrO3·9H2O lanthanum bromate nonahydrate\n''La2(CO3)3·8H2O lanthanum carbonate octahydrate\n''La(CF3SO3)3 lanthanum(III)trifluoromethanesulfonate\n''La(CF3SO3)3·xH2O lanthanum(III)trifluoromethanesulfonate hydrate\n'""", '57', '138.91')
        self.colorLa=colorLa="Slategray3"
        self.La = tk.Button(self, text=La[0], width=5, height=2, bg=colorLa, font=10, borderwidth=3,
                           command=lambda text=La: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorLa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_La()])
        self.La.grid(row=8, column=4)

        Ac = ('Ac', 'Actinium', """'Ac actinium actinium metal\n'""", '89', '227.03')
        self.colorAc=colorAc="Slategray4"
        self.Ac = tk.Button(self, text=Ac[0], width=5, height=2, bg=colorAc, font=10, borderwidth=3,
                           command=lambda text=Ac: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAc, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ac()])
        self.Ac.grid(row=9, column=4)


        Ti = ('Ti', 'Titanium', """'Ti titanium \n''Be12Ti beryllium compound with titanium (12:1) \n''TiBr4 titanium(IV) bromide \n''TiCl2 titanium(II)chloride \n''TiCl3 titanium trichloride \n''TiCl4 titanium tetrachloride \n''CuTi titanium-copper alloy \n''TiF3 titanium trifluoride \n''TiF4 titanium tetrafluoride \n''TiH2 titanium hydride \n''TiI4 titanium(IV) iodide \n''TiN titanium nitride \n''TiO titanium monoxide \n''TiO2 titanium(IV) oxide (anatase) \n''TiO2 titanium(IV) oxide (rutile) \n''TiO2 titanium dioxide \n''Ti2O3 titanium(III) oxide \n''PTi titanium phosphide \n''TiS2 titanium disulfide \n''TiSi2 titanium silicide \n''TiB2 titanium boride \n''TiBr2 titanium(II) bromide \n''TiBr3 titanium(III) bromide \n''TiI2 titanium(II) iodide \n''TiI3 titanium(III) iodide \n''TiS titanium(II) sulfide \n''Ti2S3 titanium(III) sulfide \n''Ti3O5 titanium(III,IV) oxide \n''(TiCl3)3·AlCl3 titanium(III)chloride-aluminum chloride \n''Al2O3·TiO2 aluminum titanate \n''BaTiO3 barium titanate \n''BaTi4O9 barium tetratitanate \n''Bi2O3·2TiO2 bismuth titanate \n''C19H24Ti bis(2,4-cyclopentadien-1-yl)[(4-methylbicyclo[2.2.1]heptane-2,3-diyl)methylene]titanium(IV) \n''CaTiO3 calcium titanate \n''CdTiO3 cadmium titanate \n''CoO3Ti cobalt titanium oxide \n''Co2TiO4 cobalt(III) titanate \n''CuO3Ti copper(II) titanate \n''H2TiF6 hexafluorotitanic acid \n''K2(TiF6) potassium hexafluorotitanate(IV) \n''Na2TiF6 sodium hexafluorotitanate \n''HfTiO4 hafnium(IV) titanate \n''K2TiO3 potassium titanate \n''Li2O3Ti lithium titanate \n''MgTiO3 magnesium titanate \n''Mg2TiO4 magnesium orthotitanate \n''MnTiO3 manganese titanate \n''Na2Ti3O7 sodium metatitanate \n''NiTiO3 nickel(II) titanate \n''PbTiO3 lead(II) titanate \n''SrTiO3 strontium titanate \n''Zn2TiO4·Zn2TiO2 zinc titanate \n''O8S2Ti titanium(IV) sulfate \n''Ti2(SO4)3 titanium(III)sulfate \n''(Ba,Ca)TiO3 barium calcium titanate \n''BaO5TiZr barium titanate zirconate \n''BaTi(SiO3)3 barium titanium silicate \n''Ti(OCH3)4 titanium(IV)methoxide \n''C5H5Cl3Ti cyclopentadienyltrichlorotitanium \n''[(CH3)2N]4Ti tetrakis(dimethylamino)titanium \n''Ti(OC2H5)4 titanium(IV)ethoxide \n''C10H10Cl2Ti bis(cyclopentadienyl)titanium(IV)dichloride \n''C10H10S5Ti bis(cyclopentadienyl)titanium(IV)pentasulfide \n''C10H15Cl3Ti trichloro(pentamethylcyclopentadienyl)titanium(IV) \n''TiO[CH3COCH=C(O)CH3]2 titanium(IV)oxide acetylacetonate \n''Ti(N(CH3)2)2(N(CH2CH3)2)2 bis(diethylamido)bis(dimethylamido)titanium(IV) \n''[(CH3C2H5)N]4Ti tetrakis(ethylmethylamido)titanium(IV) \n''Ti[OCH(CH3)2]4 isopropyl titanate(IV) \n''Ti(OC3H7)4 titanium(IV)propoxide \n''C13H24O3Ti trimethoxy(pentamethylcyclopentadienyl)titanium(IV) \n''((CH3)2CHO)2Ti(C5H7O2)2 titanium(IV) bis(acetylacetonate) diisopropoxide \n''[(C2H5)2N]4Ti tetrakis(diethylamino)titanium \n''Ti(OCH2CH2CH2CH3)4 butyl titanate \n''[Ti(OCH2CH2CH2CH3)4]n titanium(IV)butoxide,polymer \n''Ti[OC(CH3)3]4 titanium(IV)tert-butoxide \n''C18H14Cl2Ti dichlorobis(indenyl)titanium(IV) \n''C18H26Cl2Ti bis(tert-butylcyclopentadienyl)titanium(IV)dichloride \n''[CH3CH2OCOCH=C(O)CH3]2Ti(OCH(CH3)2)2 titanium(IV)bis(ethyl acetoacetato)diisopropoxide \n''C20H24Cl2Ti dichloro[rac-ethylenebis(4,5,6,7-tetrahydro-1-indenyl)]titanium(IV) \n''C20H30Cl2Ti bis(pentamethylcyclopentadienyl)titanium(IV)dichloride \n''C20H36O8Ti titanium(IV)tetrahydrofurfuryloxide \n''Ti(OCC(CH3)3CHCOC(CH3)3)2(OC3H7)2 titanium(IV)diisopropoxidebis(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''Ti[OCH2CH(C2H5)(CH2)3CH3]4 titanium(IV) 2-ethylhexyloxide \n''(NH4)2TiF6 ammonium hexafluorotitanate \n''FeO3Ti iron(II)titanate \n''Ti(NO3)4 titanium(IV)nitrate \n''TiOSO4 titanium(IV)oxysulfate \n''TiOSO4·xH2SO4·xH2O titanium(IV)oxysulfate-sulfuric acid hydrate \n''(NH4)2TiO(C2O4)2·H2O ammonium titanyl oxalate monohydrate \n''[CH3CH(O)CO2NH4]2Ti(OH)2 titanium(IV)bis(ammonium lactato)dihydroxide \n''TiCl4·2THF titanium(IV)chloride tetrahydrofuran complex \n''[(CH3)2CHO]3TiCl titanium, chlorotris(2-propanolato)-, (t-4)- \n''C12H24Cl3O3Ti titanium(III)chloride tetrahydrofuran complex(1:3) \n''C13H18AlClTi tebbe reagent \n''C18H42N2O8Ti titanium(IV) bis(triethanolaminate) diisoproxide \n''(OCC(CH3)3CHCOC(CH3)3)2TiCl2 dichlorobis(2,2,6,6-tetramethyl-3,5-heptanedionato)titanium(IV) \n''C30H54BaO12Ti barium titanium(IV)tetrahydrofurfuryl oxide \n''C32H16Cl2N8Ti titanium(IV)phthalocyanine dichloride \n''C32H16N8OTi titanyl phthalocyanine \n'""", '22', '47.90')
        self.colorTi=colorTi="PaleTurquoise1"
        self.Ti = tk.Button(self, text=Ti[0], width=5, height=2, bg=colorTi, font=10, borderwidth=3,
                           command=lambda text=Ti: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTi, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ti()])
        self.Ti.grid(row=6, column=5)

        Zr = ('Zr', 'Zirconium', """'Zr zirconium \n''Al2Zr aluminum zirconium \n''ZrBr4 zirconium tetrabromide \n''ZrCl4 zirconium tetrachloride \n''F2Zr zirconium(II) fluoride \n''ZrF4 zirconium tetrafluoride \n''ZrH2 zirconium(II)hydride \n''ZrI4 zirconium tetraiodide \n''ZrN zirconium nitride \n''NiZr zirconium-nickel alloy (30:70) \n''NiZr zirconium-nickel alloy (70:30) \n''ZrO2 zirconium(IV) oxide \n''S2Zr zirconium(IV) sulfide \n''ZrSi2 zirconium silicide \n''ZrB2 zirconium diboride \n''ZrBr2 zirconium(II) bromide \n''ZrBr3 zirconium(III) bromide \n''ZrCl2 zirconium(II) chloride \n''ZrCl3 zirconium(III) chloride \n''ZrF3 zirconium(III) fluoride \n''ZrI2 zirconium(II) iodide \n''ZrI3 zirconium(III) iodide \n''ZrP2 zirconium phosphide \n''BaZrO3 barium zirconate \n''2Bi2O3·3ZrO2 bismuth(III)zirconate \n''ZrC zirconium(IV) carbide \n''C10H12Zr bis(cyclopentadienyl)zirconium(IV)dihydride \n''(C5H5)2Zn(CH3)2 bis(cyclopentadienyl)dimethylzirconium(IV) \n''[CH3C(CH3)2CH2]4Zr tetrakis(2,2-dimethylpropyl)zirconium(IV) \n''C22H36Zr dimethylbis(pentamethylcyclopentadienyl)zirconium(IV) \n''CaZrO3 calcium zirconate \n''(CeO2)·(ZrO2) cerium(IV)-zirconium(IV)oxide \n''H2ZrF6 hexafluorozirconic acid \n''Na2ZrF6 sodium hexafluorozirconate \n''Zr(OH)4 zirconium(IV)hydroxide \n''K2ZrF6 potassium hexafluorozirconate \n''Li2ZrO3 lithium zirconate \n''MgZrO3 magnesium zirconate \n''N4O12Zr zirconium nitrate \n''Na2ZrO3 sodium zirconate \n''PbZrO3 lead(II)zirconate \n''SrZrO3 strontium zirconate \n''ZrSiO4 zirconium silicate \n''ZrO2 zirconium(IV)oxide-yttria stabilized \n''Zr(SO4)2 zirconium(IV)sulfate \n''SnZrF6 tin(II) hexafluorozirconate \n''ZrP2O7 zirconium(IV) pyrophosphate \n''Zr(WO4)2 zirconium(IV) tungstate \n''BaO5TiZr barium titanate zirconate \n''Zr(OH)2CO3·ZrO2 zirconium(IV)carbonate hydroxide oxide \n''Zr(OC2H5)4 zirconium(IV)ethoxide \n''C4H8O6Zr zirconium(IV) acetate hydroxide \n''C5H5Cl3Zr cyclopentadienylzirconium(IV)trichloride \n''Zr(C2H3O2)4 zirconium acetate \n''[(CH3)2N]4Zr tetrakis(dimethylamido)zirconium(IV) \n''C9H7Cl3Zr indenylzirconium(IV)trichloride \n''C10H10ZrCl2 zirconocene dichloride \n''C10H11ClZr bis(cyclopentadienyl)zirconium(IV) chloride hydride \n''C10H15Cl3Zr pentamethylcyclopentadienylzirconium(IV)trichloride \n''C12H14Cl2Zr bis(methylcyclopentadienyl)zirconium dichloride \n''Zr(NCH3C2H5)4 tetrakis(ethylmethylamido)zirconium(IV) \n''Zr(OCH2CH2CH3)4 zirconium tetrapropanolate \n''Zr(OCH(CH3)2)4·(CH3)2CHOH zirconium(IV)isopropoxide isopropanol complex \n''C16H22Cl2Zr bis(isopropylcyclopentadienyl)zirconium(IV)dichloride \n''[(C2H5)2N]4Zr tetrakis(diethylamido)zirconium(IV) \n''Zr(OC4H9)4 zirconium(IV)butoxide \n''C18H14Cl2Zr dichlorobis(indenyl)zirconium(IV) \n''C18H26Cl2Zr bis(tert-butylcyclopentadienyl)zirconium(IV)dichloride \n''C18H26ZrCl2 bis(butylcyclopentadienyl)zirconium(IV)dichloride \n''C20H16Cl2Zr dichloro[rac-ethylenebis(indenyl)]zirconium(IV) \n''C20H18Cl2Zr dichlorobis(2-methylindenyl)zirconium(IV) \n''C20H24Cl2Zr dichloro[(R,R)-ethylenebis(4,5,6,7-tetrahydro-1-indenyl)]zirconium(IV) \n''C20H24Cl2Zr dichloro[rac-ethylenebis(4,5,6,7-tetrahydro-1-indenyl)]zirconium(IV) \n''C20H24Cl2Zr dichloro[(S,S)-ethylenebis(4,5,6,7-tetrahydro-1-indenyl)]zirconium(IV) \n''C20H30Cl2Zr bis(pentamethylcyclopentadienyl)zirconium(IV)dichloride \n''Zr(C5H7O2)4 zirconium(IV)acetylacetonate \n''C26H44O16Zr zirconium(IV)bis(diethyl citrato)dipropoxide \n''Zr(OCC(CH3)3CHCOC(CH3)3)2(OC3H7)2 zirconium(IV)diisopropoxidebis(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''Zr(OCC(CH3)3CHCOC(CH3)3)4 zirconium tetrakis(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''CdZrO3 cadmium zirconium trioxide \n''C6H5CH(CH3)NHCH2CH=CH2 (S)-(-)-N-allyl-α-methylbenzylamine \n''ZrOCl2 zirconyl chloride \n''ZrOCl2·xH2O zirconyl chloride hydrate \n''ZrF4·xH2O zirconium(IV)fluoride hydrate \n''ZrO(NO3)2 zirconyl nitrate \n''ZrO(NO3)2·xH2O zirconium(IV)oxynitrate hydrate \n''Zr(HPO4)2 zirconium(IV)hydrogenphosphate \n''Zr(SO4)2·xH2O zirconium(IV)sulfate hydrate \n''Zr(SO4)4 zirconium(IV)hydroxide,sulfated \n''(NH4)2ZrF6 ammonium hexafluorozirconate \n''K4Zr[C2O4]4 potassium tetraoxalatozirconate(IV) \n''ZrCl4·2OC4H8 zirconium(IV)chloride tetrahydrofuran complex(1:2) \n''(C5H5)2ZrDCl bis(cyclopentadienyl)zirconium chloride deuteride \n'""", '40', '91.22')
        self.colorZr=colorZr="PaleTurquoise2"
        self.Zr = tk.Button(self, text=Zr[0], width=5, height=2, bg=colorZr, font=10, borderwidth=3,
                           command=lambda text=Zr: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorZr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Zr()])
        self.Zr.grid(row=7, column=5)

        Hf = ('Hf', 'Hanium', """'Hf hafnium \n''HfBr4 hafnium(IV)bromide \n''HfC hafnium(IV)carbide \n''HfCl4 hafnium tetrachloride \n''HfF4 hafnium(IV)fluoride \n''HfH2 hafnium(II) hydride \n''HfB2 hafnium boride \n''HfBr2 hafnium(II) bromide \n''HfBr3 hafnium(III) bromide \n''HfCl2 hafnium(II) chloride \n''HfCl3 hafnium(III) chloride \n''HfI3 hafnium(III) iodide \n''HfI4 hafnium iodide \n''HfN hafnium nitride \n''HfO2 hafnium oxide \n''HfP hafnium phosphide \n''HfS2 hafnium(IV) sulfide \n''HfSe2 hafnium selenide \n''HfSi2 hafnium silicide \n''(C5H5)2Hf(CH3)2 dimethylbis(cyclopentadienyl)hafnium(IV) \n''(C9H7)2Hf(CH3)2 bis(indenyl)dimethylhafnium(IV) \n''C20H32Hf bis(tert-butylcyclopentadienyl)dimethylhafnium(IV) \n''Hf(NO3)4 hafnium(IV)nitrate \n''HfSiO4 hafnium(IV) silicate \n''HfTiO4 hafnium(IV) titanate \n''C5H5Cl3Hf cyclopentadienylhafnium(IV)trichloride \n''[(CH3)2N]4Hf tetrakis(dimethylamido)hafnium(IV) \n''C9H7Cl3Hf indenylhafnium(IV)trichloride \n''C10H10Cl2Hf bis(cyclopentadienyl)hafnium(IV)dichloride \n''[(CH3)C2H5)N]4HF tetrakis(ethylmethylamido)hafnium(IV) \n''C14H18Cl2Hf bis(ethylcyclopentadienyl)hafnium(IV)dichloride \n''C16H22Cl2Hf bis(isopropylcyclopentadienyl)hafnium(IV)dichloride \n''[(CH2CH3)2N]4Hf tetrakis(diethylamido)hafnium(IV) \n''C16H36HfO4 hafnium(IV)n-butoxide \n''Hf[OC(CH3)3]4 hafnium(IV)tert-butoxide \n''C18H10Cl2Hf dichlorobis(indenyl)hafnium \n''C18H26Cl2Hf bis(tert-butylcyclopentadienyl)hafnium(IV)dichloride \n''C20H30Cl2Hf bis(pentamethylcyclopentadienyl)hafnium(IV)dichloride \n''Hf(OC(CH3)2CH2OCH3)4 tetrakis(1-methoxy-2-methyl-2-propoxy)hafnium(IV) \n''Hf(SO4)2 hafnium(IV) sulfate \n''K4Hf[C2O4]4 potassium tetraoxalatohafnate(IV) \n'""", '72', '178.49')
        self.colorHf=colorHf="PaleTurquoise3"
        self.Hf = tk.Button(self, text=Hf[0], width=5, height=2, bg=colorHf, font=10, borderwidth=3,
                           command=lambda text=Hf: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorHf, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Hf()])
        self.Hf.grid(row=8, column=5)

        Rf = ('Rf', 'Rutherfordium', """'Rf rutherfordium rutherfordium metal\n'""", '104', '261.00')
        self.colorRf=colorRf="PaleTurquoise4"
        self.Rf = tk.Button(self, text=Rf[0], width=5, height=2, bg=colorRf, font=10, borderwidth=3,
                           command=lambda text=Rf: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRf, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Rf()])
        self.Rf.grid(row=9, column=5)
        
        V = ('V', 'Vanadium', """'V vanadium \n''BV vanadium boride \n''Be12V beryllium compound with vanadium (12:1) \n''VBr3 vanadium tribromide \n''VC vanadium(IV) carbide \n''VCl2 vanadium(II) chloride \n''VCl3 vanadium trichloride \n''VCl4 vanadium tetrachloride \n''VF3 vanadium trifluoride \n''VF4 vanadium(IV) fluoride \n''VF5 vanadium(V) fluoride \n''VI2 vanadium(II) iodide \n''VI3 vanadium(III) iodide \n''VN vanadium nitride \n''OV vanadium(II) oxide \n''V2O4 vanadium(IV)oxide \n''V2O3 vanadium(III)oxide \n''V2O5 vanadium pentoxide \n''PV vanadium phosphide \n''SV vanadium sulfide \n'Se2V vanadium diselenide \n''SiV3 trivanadium monosilicide \n''VSi2 vanadium silicide \n''Te2V vanadium telluride \n''VB2 vanadium diboride \n''VBr2 vanadium(II) bromide \n''VBr4 vanadium(IV) bromide \n''VF2 vanadium(II) fluoride \n''V2S3 vanadium(III) sulfide \n''V2S5 vanadium(V) sulfide \n''BiVO4 bismuth orthovanadate \n''V(C5H5)2 bis(cyclopentadienyl)vanadium(II) \n''C14H18V bis(ethylcyclopentadienyl)vanadium(II) \n''(C9H7)2V bis(indenyl)vanadium(II) \n''C20H30V bis(pentamethylcyclopentadienyl)vanadium(II) \n''CeVO4 cerium(III) orthovanadate \n''CsVO3 cesium metavanadate \n''Cs3VO4 cesium orthovanadate \n''Cu(VO3)2 copper(II) vanadate \n''Fe(VO3)3 iron(III) metavanadate \n''V(OH)2 vanadium dihydroxide \n''V(OH)3 vanadium trihydroxide \n''V(OH)4 vanadium tetrahydroxide \n''HgV4O11 mercury tetravanadate \n''KVO3 potassium metavanadate \n''LiVO3 lithium metavanadate \n''Mg(V2O7) magnesium pyrovanadate \n''Mn2(V2O7) manganese(II) pyrovanadate \n''NaVO3 sodium metavanadate \n''Na2V4O11 sodium tetravanadate \n''Na3VO4 sodium orthovanadate \n''Na4V2O7 sodium pyrovanadate \n''Na4V6O17 sodium vanadate \n''O3RbV rubidium vanadium trioxide \n''YVO4 yttrium(III) orthovanadate \n''YVO4 yttrium vanadate \n''VOSO4·2H2O vanadyl sulfate \n''Pb(VO3)2 lead(II) metavanadate \n''V2(SO4)3 vanadium(III) sulfate \n''V2(SO4)5 vanadium(V) sulfate \n''V(CO)6 vanadium carbonyl \n''VOBr vanadyl bromide \n''VOBr2 vanadyl dibromide \n''VOBr3 vanadyl tribromide \n''VOCl vanadyl chloride \n''VOCl2 vanadyl dichloride \n''VOF2 vanadyl difluoride \n''VO2Cl vanadium(V) dioxide chloride \n''VO2F vanadium(V) dioxide fluoride \n''AgVO3 silver vanadium trioxide \n''C4H4O8V vanadium(4+) tetraformate \n''(C5H5)2VBr bis(cyclopentadienyl)vanadium(III)bromide \n''OV(OC2H5)3 vanadium(V)oxytriethoxide \n''VO(OCH(CH3)2)3 vanadium(V)oxytriisopropoxide \n''OV(OC3H7)3 vanadium(V)oxytripropoxide n''(C5H5)2VCl bis(cyclopentadienyl)vanadium(III)chloride \n''C10H10Cl2V vanadocene dichloride \n''V(C5H5)(OCOCH(OH)CH3)2 vanadium cyclopentadienyldilactate \n''V(C5H7O2)3 vanadium(III) acetylacetonate \n''V(C5H5)2[C3H4OH(COOH)2(COO)] vanadocene citrate \n''C18H14BrV bromobis(indenyl)vanadium(III) \n''C18H14ClV chlorobis(indenyl)vanadium(III) \n''C18H14IV iodobis(indenyl)vanadium(III) \n''C5H5V(OCCH3O)4VC5H5 tetrakis(acetato)bis(cyclopentadienyl)divanadium(III) \n''C20H18O5V oxobis(1-phenylbutane-1,3-dionato-o,O')vanadium \n''(C5H5)2V(OOCC6H5)2 bis(benzoato)bis(cyclopentadienyl)vanadium(IV) \n''VOCl3 vanadium(V)oxychloride \n''VOF3 vanadium(V)oxyfluoride \n''(NH4)3VF6 ammonium hexafluorovanadate \n''VOSO4·xH2O vanadium(IV)oxide sulfate hydrate \n''NH4VO3 ammonium metavanadate \n''V6(OH)5O5(PO4)5 vanadium hydroxide oxide phosphate \n''H10O10SV vanadyl sulfate pentahydrate \n''(NH4)3VS4 ammonium tetrathiovandate \n''VF3·3H2O vanadium(III) fluoride trihydrate \n''V(OCOCH(OH)CH3)Cl2 vanadium dichlorolactate \n''C3H7NO7V serine vanadate \n'""", '23', '50.94')
        self.colorV=colorV="LightBlue1"
        self.V = tk.Button(self, text=V[0], width=5, height=2, bg=colorV, font=10, borderwidth=3,
                           command=lambda text=V: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorV, text[0], text[3], text[4]), self.voice(text[1]), self.compound_V()])
        self.V.grid(row=6, column=6)
        
        Nb = ('Nb', 'Niobium', """'Nb niobium \n''NbB niobium boride \n''Be12Nb beryllium compound with niobium (12:1) \n''NbBr5 niobium(V) bromide \n''Cl3Nb niobium(III) chloride \n''Cl4Nb niobium(IV) chloride \n''NbCl5 niobium(V) chloride \n''NbF5 niobium(V) fluoride \n''NbI5 niobium(V)iodide \n''NbN niobium nitride \n''NbB2 niobium diboride \n''NbBr3 niobium(III) bromide \n''NbBr4 niobium(IV) bromide \n''NbF3 niobium(III) fluoride \n''NbF4 niobium(IV) fluoride \n''NbI3 niobium(III) iodide \n''NbI4 niobium(IV) iodide \n''NbO niobium(II) oxide \n''NbO2 niobium(IV) oxide \n''NbP niobium phosphide \n''NbS2 niobium(IV) sulfide \n''NbSe2 niobium selenide \n''NbSi2 niobium silicide \n''NbTe2 niobium(IV) telluride \n''Nb2O5 niobium pentoxide \n''Ba(NbO3)2 barium niobate \n''NbC niobium(IV)carbide \n''Cd2Nb2O7 cadmium niobate \n''Cu(NbO3)2 copper(II)niobate \n''K2NbF7 potassium heptafluoroniobate(V) \n''KNbO3 potassium niobate \n''LiNbO3 lithium niobate \n''NaNbO3 sodium niobate \n''NbOBr3 niobium(V) oxybromide \n''NbOCl3 niobium(V) oxychloride \n''NbO2F niobium(V) dioxyfluoride \n''Pb(NbO3)2 lead(II)niobate \n''Zn(NbO3)2 zinc niobate \n''SrNb2O6 strontium niobate \n''BaSr(NbO3)4 barium strontium niobate \n''Ba2NaNb5O15 barium sodium niobium oxide \n''C5H5NbCl4 5-cyano-5-methylhexylzinc bromide \n''C10H10Cl2Nb bis(cyclopentadienyl)niobium(IV)dichloride \n''C10H25NbO5 niobium(V)ethoxide \n''(C5H4CH3)2NbCl2 bis(methylcyclopentadienyl)niobium(IV)dichloride \n''C14H18Cl2Nb bis(ethylcyclopentadienyl)niobium(IV)dichloride \n''F6H4NNb ammonium hexafluoroniobate(1-) \n''NbCl3·CH3OCH2CH2OCH3 niobium(III)chloride 1,2-dimethoxyethane complex \n''NbCl4(CO4H8)2 niobium(IV)chloride tetrahydrofuran complex \n''C36H51Cl2NbO3 tris(2,6-diisopropylphenoxy)niobium(V)chloride \n''C42H58Cl6Nb2O4 bis(2,6-diphenylphenoxy)niobium(V)chloride,benzene complex(2:1) \n'""", '41', '92.91')
        self.colorNb=colorNb="LightBlue2"
        self.Nb = tk.Button(self, text=Nb[0], width=5, height=2, bg=colorNb, font=10, borderwidth=3,
                           command=lambda text=Nb: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNb, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Nb()])
        self.Nb.grid(row=7, column=6)

        Ta = ('Ta', 'Tantalum', """'Ta tantalum \n''Al3Ta tantalum aluminide \n''TaB tantalum boride \n''TaBr5 tantalum(V)bromide \n''Cl3Ta tantalum(III) chloride \n''Cl4Ta tantalum(IV) chloride \n''TaCl5 tantalum(V) chloride \n''TaF5 tantalum(V) fluoride \n''TaI5 tantalum(V)iodide \n''TaN tantalum nitride \n''O2Ta tantalum(IV) oxide \n''Ta2O5 tantalum(V)oxide \n''S2Ta tantalum(IV) sulfide \n''TaSe2 tantalum(IV) selenide \n''TaSi2 tantalum silicide \n''TaB2 tantalum diboride \n''TaBr3 tantalum(III) bromide \n''TaBr4 tantalum(IV) bromide \n''TaH tantalum hydride \n''TaI4 tantalum(IV) iodide \n''TaTe2 tantalum(IV) telluride \n''TaC tantalum(IV)carbide \n''K2TaF7 potassium heptafluorotantalate \n''Fe(TaO3)2 iron(II) tantalate \n''KTaO3 potassium tantalate \n''LiTaO3 lithium tantalate \n''Pb(TaO3)2 lead(II) tantalate \n''Ta(OCH3)5 tantalum(V)methoxide \n''Ta(OCH2CH2CH2CH3)5 tantalum(V)butoxide \n''C10H15Cl4Ta pentamethylcyclopentadienyltantalum(IV)tetrachloride \n''Ta(N(CH3)2)5 pentakis(dimethylamino)tantalum(V) \n'""", '73', '180.95')
        self.colorTa=colorTa="LightBlue3"
        self.Ta = tk.Button(self, text=Ta[0], width=5, height=2, bg=colorTa, font=10, borderwidth=3,
                           command=lambda text=Ta: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ta()])
        self.Ta.grid(row=8, column=6)

        Db = ('Db', 'Dubnium', """'Db dubnium dubnium metal\n'""", '105', '262.00')
        self.colorDb=colorDb="LightBlue4"
        self.Db = tk.Button(self, text=Db[0], width=5, height=2, bg=colorDb, font=10, borderwidth=3,
                           command=lambda text=Db: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorDb, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Db()])
        self.Db.grid(row=9, column=6)


        Cr = ('Cr', 'Chromium', """'Cr chromium \n''CrB chromium boride \n''CrB2 chromium diboride \n''Br3Cr chromium tribromide \n''Cr3C2 chromium carbide \n''CrCl2 chromous chloride \n''CrCl3 chromic chloride \n''Cl4Cr chromium(IV) chloride \n''CrBr2 chromium(II) bromide \n''CrF2 chromium(II) fluoride \n''CrF3 chromium(III) fluoride \n''CrF4 chromium(IV) fluoride \n''CrF5 chromium(V) fluoride \n''CrF6 chromium(VI) fluoride \n''CrI3 chromium(III) iodide \n''CrO2 magtrieve™ \n''CrO3 chromium trioxide \n''CrP chromium phosphide \n''CrSb chromium antimonide \n''CrSe chromium selenide \n''CrSi2 chromium silicide \n''Cr2As chromium arsenide \n''Cr2O3 chromium(III) oxide \n''Cr2O5 chromium(V) oxide \n''Cr2S3 chromium(III) sulfide \n''Cr2Te3 chromium(III)telluride \n''Cr3O4 chromium(II,III) oxide \n''Cr5O12 chromic chromate \n''Ag2CrO4 silver(I) chromate \n''Ag2Cr2O7 silver(I) dichromate \n''BaCrO4 barium chromate \n''Ba3(CrO4)2 barium chromate(V) \n''CrC2O4 chromium(II) oxalate \n''Cr(CO)6 chromium(0) carbonyl \n''(C6H6)Cr(CO)3 benzene-chromium(0)tricarbonyl \n''Cr(C5H5)2 chromocene \n''C12H12Cr bis(benzene)chromium(0) \n''C14H18Cr bis(ethylcyclopentadienyl)chromium(II) \n''C18H26Cr bis(tetramethylcyclopentadienyl)chromium(II) \n''Cr(C5(CH3)5)2 bis(pentamethylcyclopentadienyl)chromium(II) \n''CaCrO4 calcium chromate \n''CoCrO4 cobalt(II) chromate \n''CoCr2O4 cobalt(II) chromite \n''Cr(ClO4)3 chromium(III) perchlorate \n''Cs2CrO4 cesium chromate \n''CrCuO4 copper chromate \n''H2CrO4 chromic acid \n''HgCrO4 mercury(II) chromate \n''CrHg2O4 mercury(I) chromate \n''K2CrO4 potassium chromate \n''CrLi2O4 lithium chromate \n''CrN3O9 chromium nitrate \n''Na2CrO4 sodium chromate \n''NiCr2O4 nickel chromium oxide \n''CrOF4 chromium(VI) tetrafluoride oxide \n''CrO2Cl2 chromyl chloride \n''CrO2F2 chromium(VI) difluoride dioxide \n''CrO4P chromium(III) phosphate \n''PbCrO4 lead(II) chromate \n''SrCrO4 strontium chromate \n''Tl2CrO4 thallium chromate \n''ZnCrO4 zinc chromate \n''CrO5Pb2 lead chromate oxide \n''2CuO·Cr2O3 copper chromite \n''H2Cr2O7 dichromic acid \n''Cr2HgO7 mercury(II) dichromate \n''K2Cr2O7 potassium dichromate \n''Li2Cr2O7 lithium dichromate \n''Na2Cr2O7 sodium bichromate \n''ZnCr2O7 zinc dichromate \n''Cr2(SO4)3 chromium sulfate \n''Cr3Fe2O12 iron(III) chromate \n''Cr6Fe2O21 iron(III) dichromate \n''CuCr2O4 copper(II) chromite \n''FeCr2O4 iron(II) chromite \n''MgCr2O4 magnesium chromite \n''NiCrO4 nickel(II) chromate \n''Sn(CrO4)2 tin(IV) chromate \n''BaCr2O7·2H2O barium dichromate dihydrate \n''Bi2O3·2CrO3 bismuth basic dichromate \n''CrBr3·6H2O chromium(III)bromide hexahydrate \n''[(CH3CO2)2Cr·H2O]2 chromium(II) acetate,dimer monohydrate \n''K3Cr(CN)6 potassium hexacyanochromate(III) \n''C6H9CrO6 chromium(III) acetate \n''C6H11CrO7 chromium(III) acetate monohydrate \n''C6H5CH3Cr(CO)3 (toluene)tricarbonylchromium(0) \n''C10H8CrO3 tricarbonyl(cycloheptatriene)chromium(0) \n''C6H5C2H5Cr(CO)3 (ethylbenzene)tricarbonylchromium(0) \n''[C6H3(CH3)3]Cr(CO)3 tricarbonyl(mesitylene)chromium(0) \n''C6H5CO2C2H5Cr(CO)3 (ethyl benzoate)tricarbonylchromium(0) \n''(C10H8)Cr(CO)3 tricarbonyl(naphthalene)chromium(0) \n'""", '24', '51.99')
        self.colorCr=colorCr="LightSteelBlue1"
        self.Cr = tk.Button(self, text=Cr[0], width=5, height=2, bg=colorCr, font=10, borderwidth=3,
                           command=lambda text=Cr: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cr()])
        self.Cr.grid(row=6, column=7)

        Mo = ('Mo', 'Molybdenum', """'Mo molybdenum \n''MoBr3 molybdenum bromide \n''Cl2Mo molybdenum(II) chloride \n''MoCl3 molybdenum(III) chloride \n''Cl4Mo molybdenum(IV) chloride \n''MoCl5 molybdenum pentachloride \n''F3Mo molybdenum(III) fluoride \n''F4Mo molybdenum(IV) fluoride \n''F5Mo molybdenum(V) fluoride \n''MoF6 molybdenum(vI) fluoride \n''MoBr2 molybdenum(II) bromide \n''MoBr4 molybdenum(IV) bromide \n''MoI2 molybdenum(II) iodide \n''MoI3 molybdenum(III) iodide \n''MoI4 molybdenum(IV) iodide \n''MoN molybdenum nitride (MaN) \n''MoN molybdenum nitride (1:1) \n''MoO2 molybdenum dioxide \n''MoO3 molybdenum trioxide \n''MoP molybdenum phosphide \n''MoS2 molybdenum disulfide \n''MoS3 molybdenum(VI) sulfide \n''MoSe2 molybdenum(IV) selenide \n''MoTe2 molybdenum(IV) telluride \n''Mo2O3 molybdenum(III) oxide \n''Ag2MoO4 silver molybdate \n''BaMoO4 barium molybdate \n''Bi2(MoO4)3 bismuth(III)molybdate \n''Mo2C molybdenum carbide \n''Mo(CO)6 molybdenum(0)hexacarbonyl \n''CaMoO4 calcium molybdate \n''CoMoO4 cobalt(II) molybdate \n''CuMoO4 copper(II)molybdate \n''FeMoO4 iron(II)molybdate \n''H2MoO4 molybdic acid \n''K2MoO4 potassium molybdate \n''Li2MoO4 lithium molybdate \n''MgMoO4 magnesium molybdate \n''MnMoO4 manganese(II) molybdate \n''Na2MoO4 sodium molybdate \n''Na2MoO4·2H2O sodium molybdate dihydrate \n''NiMoO4 nickel(II)molybdate \n''MoOCl3 molybdenum(V) oxytrichloride \n''MoOF4 molybdenum(VI) oxytetrafluoride \n''MoO2F2 molybdenum(VI) dioxydifluoride \n''PbMoO4 lead(II) molybdate \n''SrMoO4 strontium molybdate \n''ZnMoO4 zinc molybdate \n''Mo(PO3)6 molybdenum(VI) metaphosphate \n''Tl2MoO4 thallium(I) molybdate \n''C8H6MoO3 cyclopentadienylmolybdenum(I)tricarbonyl hydride \n''Mo2(OCOCH3)4 molybdenum(II)acetate dimer \n''C10H10Cl2Mo bis(cyclopentadienyl)molybdenum(IV)dichloride \n''[CH3C(=O)CH=C(O)CH3]2MoO2 bis(acetylacetonato)dioxomolybdenum(VI) \n''C7H8Mo(CO)4 (bicyclo[2.2.1]hepta-2,5-diene)tetracarbonylmolybdenum(0) \n''(Mo(CO)3(C5H5))2 cyclopentadienylmolybdenum(II)tricarbonyl,dimer \n''C18H14Mo2O6 methylcyclopentadienylmolybdenum(I)tricarbonyl,dimer \n''C22H22Mo2O6 (propylcyclopentadienyl)molybdenum(I)tricarbonyl dimer \n''CdMoO4 cadmium molybdate \n''MoO2Cl2 molybdenum(VI)dichloride dioxide \n''MoOCl4 molybdenum(VI)tetrachloride oxide \n''CoH2MoO5 cobalt(II) molybdate monohydrate \n''Fe7H21MoS9 fe-mo cofactor \n''Na3[P(Mo3O10)4]·xH2O sodium phosphomolybdate hydrate \n''H3[P(Mo3O10)4]·xH2O phosphomolybdic acid hydrate \n''(NH4)6Mo7O24·4H2O ammonium molybdate tetrahydrate \n''(NH4)2MoO4 ammonium molybdate \n''(NH3)3Mo(CO)3 triamminemolybdenum(0)tricarbonyl \n''(CH3CN)2MoCl4 bis(acetonitrile)molybdenum(IV)chloride \n''C7H8Mo(CO)3 tricarbonyl(cycloheptatriene)molybdenum(0) \n''C10H10BCl2F4Mo dichlorobis(cyclopentadienyl)molybdenum tetrafluoroborate \n''C6H5SCu copper(I)thiophenolate \n''(CO)4Mo(P(C6H5)2C5H4)2Fe (1,1'-bis(diphenylphosphino)ferrocene)tetracarbonylmolybdenum(0) \n''(NH4)3PO4·12MoO3 ammonium molybdophosphate \n''[(C2H5)2NCS2]2MoO2 bis(diethyldithiocarbamato)dioxomolybdenum(VI) \n''C10H10MoN5O7PS3 molybdenum cofactor (sulfide) \n'""", '42', '95.94')
        self.colorMo=colorMo="LightSteelBlue2"
        self.Mo = tk.Button(self, text=Mo[0], width=5, height=2, bg=colorMo, font=10, borderwidth=3,
                           command=lambda text=Mo: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorMo, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Mo()])
        self.Mo.grid(row=7, column=7)

        W = ('W', 'Tungsten', """'W tungsten \n''WB tungsten boride \n''Br4W tungsten(IV) bromide \n''WBr5 tungsten(V)bromide \n''WC tungsten carbide \n''WCl4 tungsten(IV)chloride \n''Cl5W tungsten(V) chloride \n''WCl6 tungsten hexachloride \n''F4W tungsten(IV) fluoride \n''F5W tungsten(V) fluoride \n''WF6 tungsten(VI)fluoride \n''WO2 tungsten dioxide \n''WO3 tungsten trioxide \n''WS2 tungsten(IV) sulfide \n''WSe2 tungsten(IV) selenide \n''WSi2 tungsten silicide \n''Te2W tungsten(IV) telluride \n''WBr2 tungsten(II) bromide \n''WBr3 tungsten(III) bromide \n''WBr6 tungsten(VI) bromide \n''WCl2 tungsten(II) chloride \n''WCl3 tungsten(III) chloride \n''WI2 tungsten(II) iodide \n''WI3 tungsten(III) iodide \n''WI4 tungsten(IV) iodide \n''WS3 tungsten(VI) sulfide \n''Ag2WO4 silver tungstate \n''BaWO4 barium tungstate \n''W(CO)6 tungsten hexacarbonyl \n''C10H12W bis(cyclopentadienyl)tungsten(IV)dihydride \n''C14H20W bis(ethylcyclopentadienyl)tungsten(IV)dihydride \n''(C5H4CH(CH3)2)2WH2 bis(isopropylcyclopentadienyl)tungsten(IV)dihydride \n''CaWO4 calcium tungstate \n''Ce2(WO4)3 cerium(III)tungstate \n''CoWO4 cobalt(II) tungstate \n''Cs2WO4 cesium tungstate \n''CuWO4 copper(II) tungstate \n''FeWO4 iron(II) tungstate \n''H2WO4 tungstic acid \n''HgWO4 mercury(II) tungstate \n''Hg2WO4 mercury(I) tungstate \n''K2WO4 potassium tungstate \n''Li2WO4 lithium tungstate \n''MgWO4 magnesium tungstate \n''MnO4W manganese(II) tungstate \n''Na2WO4 sodium tungstate \n''3Na2WO4·9WO3 sodium metatungstate \n''PbWO4 lead tungstate \n''WOBr3 tungsten(V) oxytribromide \n''WOBr4 tungsten(VI) oxytetrabromide \n''WOCl3 tungsten(V) oxytrichloride \n''WOF4 tungsten(VI) oxytetrafluoride \n''WO2Br2 tungsten(VI) dioxydibromide \n''WO2I2 tungsten(VI) dioxydiiodide \n''Zr(WO4)2 zirconium(IV) tungstate \n''C8H6O3W cyclopentadienyltungsten(II)tricarbonyl hydride \n''C10H10Cl2W bis(cyclopentadienyl)tungsten(IV)dichloride \n''C10H11ClW bis(cyclopentadienyl)tungsten(IV)chloride hydride \n''C10H8O3W tricarbonyl(1,3,5-cycloheptatriene)tungsten(0) \n''C6H3(CH3)3W(CO)3 tricarbonyl(mesitylene)tungsten(0) \n''C12H12O4W tetracarbonyl(1,5-cyclooctadiene)tungsten(0) \n''((CH3)3CN)2W(N(CH3)2)2 bis(tert-butylimino)bis(dimethylamino)tungsten(VI) \n'C14H18Cl2W bis(ethylcyclopentadienyl)tungsten(IV)dichloride \n''C16H22Cl2W bis(isopropylcyclopentadienyl)tungsten(IV)dichloride \n''C17H36O3W tris(tert-butoxy)(2,2-dimethylpropylidyne)tungsten(VI) \n''C18H26Cl2W bis(butylcyclopentadienyl)tungsten(IV)dichloride \n''C18H26I2W bis(butylcyclopentadienyl)tungsten(IV)diiodide \n''C18H26Br2W bis(butylcyclopentadienyl)tungsten(IV)dibromide \n''C22H22O6W2 (propylcyclopentadienyl)tungsten(I)tricarbonyl dimer \n''CdWO4 cadmium tungstate \n''WCl2O2 tungsten(VI)dichloride dioxide \n''WOCl4 tungsten(VI)oxychloride \n''H3PW12O40 phosphotungstic acid \n''Na2WO4·2H2O sodium tungstate dihydrate \n''H3[P(W3O10)4]·xH20 phosphotungstic acid hydrate \n''H4[Si(W3O10)4]·xH2O tungstosilicic acid hydrate \n''(NH4)10H2(W2O7)6·xH2O ammonium tungstate \n''3Na2WO4·9WO3·xH2O sodium metatungstate hydrate \n''(NH4)2WS4 ammonium tetrathiotungstate \n''W(C2H5O)5 tungsten(V) ethanolate \n''Ba2CaWO6 barium calcium tungsten oxide \n''Ba2SrWO6 barium strontium tungsten oxide \n''Ba3Y2WO9 barium yttrium tungsten oxide \n''(NH3)3W(CO)3 triamminetungsten(IV)tricarbonyl \n''C8H5ClO3W cyclopentadienyltungsten(II)tricarbonyl chloride \n''W(NCCH3)3(CO)3 tris(acetonitrile)tricarbonyltungsten(0) \n''C10H14N5O7W adenosine monotungstate \n''C10H15N5O10W2 adenosine-5'-ditungstate \n''C10H24N2S4W piperidine tetrathiotungstate \n''(CO)5WCN(CH2)4CH3 tungsten(0)pentacarbonyl-N-pentylisonitrile \n''[(C6H5)2PCH2CH2P(C6H5)2]W(CO)4 [1,2-bis(diphenylphosphino)ethane]tetracarbonyltungsten(0) \n''CuWO4·2H2O copper(II) tungstate dihydrate \n''Na3PO4·12WO3 sodium dodecatungstophosphate \n''Na3PO4·12WO3·xH2O sodium phosphotungstate hydrate \n''C10H10BCl2F4W dichlorobis(cyclopentadienyl)tungsten tetrafluoroborate \n'""", '74', '183.85')
        self.colorW=colorW="LightSteelBlue3"
        self.W = tk.Button(self, text=W[0], width=5, height=2, bg=colorW, font=10, borderwidth=3,
                           command=lambda text=W: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorW, text[0], text[3], text[4]), self.voice(text[1]), self.compound_W()])
        self.W.grid(row=8, column=7)

        Sg = ('Sg', 'Seaborgium', """'Sg seaborgium seaborgium metal\n'""", '106', '266.00')
        self.colorSg=colorSg="LightSteelBlue4"
        self.Sg = tk.Button(self, text=Sg[0], width=5, height=2, bg=colorSg, font=10, borderwidth=3,
                           command=lambda text=Sg: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSg, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Sg()])
        self.Sg.grid(row=9, column=7)

        
        Mn = ('Mn', 'Manganese', """'Mn manganese \n''MnBr2 manganese(II) bromide \n''MnCl2 manganese(II)chloride \n''MnF2 manganese(II) fluoride \n''MnF3 manganese(III) fluoride \n''MnI2 manganese(II) iodide \n''MnO manganese monoxide \n''MnO2 manganese dioxide \n''MnS manganese sulfide \n''MnSb manganese antimonide (1:1) \n''MnSe manganese(II) selenide \n''MnSi2 manganese silicide \n''MnTe manganese(II) telluride \n''Mn2O3 manganese(III) oxide \n''Mn2O7 manganese(VII) oxide \n''Mn2Sb manganese antimonide (2:1) \n''BaMn2O8 barium permanganate \n''MnCO3 manganese carbonate \n''MnC2O4 manganese oxalate \n''C10H10Mn manganocene \n''Mn2(CO)10 manganese(0)carbonyl \n''Mn(C5H4C2H5)2 bis(ethylcyclopentadienyl)manganese(II) \n''C18H26Mn bis(tetramethylcyclopentadienyl)manganese(II) \n''Mn(C5(CH3)5)2 bis(pentamethylcyclopentadienyl)manganese(II) \n''CaMn2O8 calcium permanganate \n''Mn(OH)2 manganese hydroxide \n''Mn3O4 manganese(II,III)oxide \n''MnIO3 manganese iodate \n''KMnO4 potassium permanganate \n''K2MnO4 potassium manganate \n''LiMn2O4 lithium manganese(III,IV)oxide \n''MnMoO4 manganese(II) molybdate \n''Mn(NO3)2 manganese(II) nitrate \n''NaMnO4 sodium permanganate \n''MnO3Si manganese(II) metasilicate \n''MnTiO3 manganese titanate \n''MnO4S manganese(II) sulfate \n''MnO4W manganese(II) tungstate \n''MnP2O7 manganese(IV) pyrophosphate \n''Mn2(V2O7) manganese(II) pyrovanadate \n''Mn2SiO4 manganese(II) orthosilicate \n''AgMnO4 silver(I)permanganate \n''BaMnO4 barium manganate \n''BrMn(CO)5 bromopentacarbonylmanganese(I) \n''MnBr2·4H2O manganese(II)bromide tetrahydrate \n''(CH3CO2)2Mn manganese(II)acetate \n''(HCO2)2Mn·xH2O manganese(II)formate hydrate \n''(CH3COO)2Mn·4H2O manganese(II) acetate tetrahydrate \n''(CH3COO)3Mn·2H2O manganese(III)acetate dihydrate \n''K3Mn(CN)6 potassium hexacyanomanganate(III) \n''C5H5Mn(CO)3 manganese cyclopentadienyl tricarbonyl \n''C5H4CH3Mn(CO)3 methylcyclopentadienyl manganese(I)tricarbonyl (MMT) \n''C10H7MnO4 acetylcyclopentadienylmanganese(I)tricarbonyl \n''C2H5C5H4Mn(CO)3 ethylcyclopentadienylmanganese(I)tricarbonyl \n''[CH3COCH=C(O)CH3]2Mn manganese(II)acetylacetonate \n''C11H11MnO4 hydroxyisopropylcyclopentadienylmanganese(I)tricarbonyl \n''MnC12H22O14 manganese gluconate \n''Mn(C5H7O2)3 manganese tris(4-oxopent-2-en-2-oate) \n''[C6H11(CH2)3CO2]2Mn manganese(II) hydrogen cyclohexanebutyrate \n''C32H16MnN8 manganese(II)phthalocyanine \n''Mn(ClO4)2·6H2O manganese(II)perchlorate hydrate \n''MnCl2·xH2O manganese(II)chloride hydrate \n''MnCl2·4H2O manganese(II)chloride tetrahydrate \n''Cl2H12MnO14 manganese(II) perchlorate hexahydrate \n''CsMnO4 cesium permanganate \n''Mg(MnO4)2·xH2O magnesium permanganate hydrate \n''Mn(NO3)2·xH2O manganese(II)nitrate hydrate \n''MnSO4·xH2O manganese(II)sulfate hydrate \n''MnSO4·H2O manganese(II) sulfate monohydrate \n''NaMnO4·H2O sodium permanganate monohydrate \n''NH4MnO4 ammonium permanganate \n''H8MnN2O10 manganese(II) nitrate tetrahydrate \n''MnI2·4H2O manganese(II) iodide tetrahydrate \n''MnO(OH) manganese(III) hydroxide \n''C4H6MnN2S4 maneb, stabilized \n''Mn(C5HF6O2)2·3H2O manganese(II)hexafluoroacetylacetonate trihydrate \n''C16H40Cl4MnN2 tetraethylammonium tetrachloromanganate(II) \n''C32H16ClMnN8 manganese(III)phthalocyanine chloride \n''C36H44ClMnN4 2,3,7,8,12,13,17,18-octaethyl-21H,23 H-porphine manganese(III)chloride \n''C44H28ClMnN4 5,10,15,20-tetraphenyl-21H,23 H-porphine manganese(III)chloride \n''Mg(MnO4)2·6H2O magnesium permanganate hexahydrate \n''MnB4O7·8H2O manganese(II) tetra borate octahydrate \n''MnC2O4·2H2O manganese(II) oxalate dihydrate \n''MnSO4·4H2O manganese(II) sulfate tetrahydrate \n''NaMnO4·3H2O sodium permanganate trihydrate \n''Sr(MnO4)2·3H2O strontium permanganate trihydrate \n'""", '25', '178.49')
        self.colorMn=colorMn="Plum1"
        self.Mn = tk.Button(self, text=Mn[0], width=5, height=2, bg=colorMn, font=10, borderwidth=3,
                           command=lambda text=Mn: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorMn, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Mn()])
        self.Mn.grid(row=6, column=8)

        Tc = ('Tc', 'Technetium', """'Tc technetium \n''TcF5 technetium(V) fluoride \n''TcF6 technetium(VI) fluoride\n'""", '43', '178.49')
        self.colorTc=colorTc="Plum2"
        self.Tc = tk.Button(self, text=Tc[0], width=5, height=2, bg=colorTc, font=10, borderwidth=3,
                           command=lambda text=Tc: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTc, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Tc()])
        self.Tc.grid(row=7, column=8)

        Re = ('Re', 'Rhenium', """'Re rhenium \n''Br3Re rhenium(III) bromide \n''ReCl3 rhenium(III) chloride \n''Cl4Re rhenium(IV) chloride \n''ReCl5 rhenium(V)chloride \n''ReF6 rhenium(VI)fluoride \n''F7Re rhenium(VII) fluoride \n''ReI3 rhenium(III)iodide \n''ReO2 rhenium oxide \n''ReO3 rhenium(vI) oxide \n''Re2O7 rhenium(VII) oxide \n''ReBr5 rhenium(V) bromide \n''ReCl6 rhenium(VI) chloride \n''ReF4 rhenium(IV) fluoride \n''ReF6 rhenium(V) fluoride \n''ReS2 rhenium(IV) sulfide \n''ReSe2 rhenium(IV) selenide \n''ReSi2 rhenium(IV) silicide \n''ReTe2 rhenium ditelluride \n''AgReO4 silver(I)perrhenate \n''K2ReBr6 potassium hexabromorhenate(IV) \n''Re2(CO)10 dirhenium decacarbonyl \n''Ca(ReO4)2 calcium perrhenate \n''K2ReCl6 potassium hexachlororhenate(IV) \n''HReO4 perrhenic acid \n''Re2S7 rhenium(VII) sulfide \n''K2ReI6 potassium hexaiodorhenate(IV) \n''KReO4 potassium perrhenate \n''NaReO4 sodium perrhenate \n''TlReO4 thallium(I)perrhenate \n''ReOCl4 rhenium(VI) oxytetrachloride \n''ReOF4 rhenium(VI) oxytetrafluoride \n''ReOF5 rhenium(VII) oxypentafluoride \n''ReO2F2 rhenium(VI) dioxydifluoride \n''ReO2F3 rhenium(VII) dioxytrifluoride \n''ReO3Cl rhenium(VII) trioxychloride \n''ReO3F rhenium(VII) trioxyfluoride \n''CH3ReO3 methyltrioxorhenium(VII) \n''Re(CO)5Br bromopentacarbonylrhenium(I) \n''Re(CO)5Cl pentacarbonylchlororhenium(I) \n''NH4ReO4 ammonium perrhenate \n''C15H8N2O3Re (1,10 phenanthroline)-(tri-carbon monoxide) rhenium (i) \n''(CH3CH2CH2CH2)4N(ReO4) tetrabutylammonium perrhenate \n''C18H15O4ReSi trioxo(triphenylsilyloxy)rhenium(VII) \n'""", '75', '178.49')
        self.colorRe=colorRe="Plum3"
        self.Re = tk.Button(self, text=Re[0], width=5, height=2, bg=colorRe, font=10, borderwidth=3,
                           command=lambda text=Re: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Re()])
        self.Re.grid(row=8, column=8)

        Bh = ('Bh', 'Bohrium', """'Bh bohrium bohrium metal\n'""", '107', '262.00')
        self.colorBh=colorBh="Plum4"
        self.Bh = tk.Button(self, text=Bh[0], width=5, height=2, bg=colorBh, font=10, borderwidth=3,
                           command=lambda text=Bh: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorBh, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Bh()])
        self.Bh.grid(row=9, column=8)
        
        Fe = ('Fe', 'Iron', """'Fe iron \n''AsFe iron arsenide \n''FeBr2 iron(II)bromide \n''FeBr3 iron(III) bromide \n''FeCl2 iron(II)chloride \n''FeCl3 iron(III)chloride \n''FeF2 ferrous fluoride \n''FeF3 ferric fluoride \n''FeI2 ferrous iodide \n''FeO iron(II) oxide \n''FeP iron phosphide (1:1) \n''FeS ferrous sulfide \n''FeS2 pyrite \n''FeSb2 iron diantimonide \n''FeSe iron(II) selenide \n''FeSi iron silicide \n''FeSi2 iron disilicide \n''FeTe iron(II) telluride \n''Fe2O3 iron(III) oxide \n''Fe3C iron carbide \n''FeO·Fe2O3 iron(II,III) oxide \n''Fe3P iron phosphide (3:1) \n''Fe3S3 fe3 iron-sulfur center \n''Fe3S4 fe4 iron-sulfur cluster \n''Fe4S4 fe4 iron-sulfur center \n''FeAsO4 ferric arsenate \n''Fe3(AsO4)2 iron(II) arsenate \n''BaFe12O19 barium iron oxide \n''CFeO3 ferrous carbonate \n''FeCO3 iron(II) carbonate \n''C2FeO4 ferrous oxalate \n''Fe(CO)5 iron(0)pentacarbonyl \n''Fe4[Fe(CN)6]3 iron(III) ferrocyanide \n''Fe(C5H5)2 ferrocene \n''(HC≡CC5H4)Fe(C5H5) ethynylferrocene \n''C12H12Fe vinylferrocene \n''C12H14Fe 1,1'-dimethylferrocene \n''C12H14Fe ethylferrocene \n''Fe(C5H5)(C5H4C(CH3)3) tert-butylferrocene \n''Fe(C5H4C2H5)2 1,1'-diethylferrocene \n''Fe(C5H5)(C5H4C4H9) butylferrocene \n''C18H26Fe bis(tetramethylcyclopentadienyl)iron(II) \n''Fe(C5(CH3)5)2 bis(pentamethylcyclopentadienyl)iron(II) \n''C22H6Fe2 1,2-diferrocenylethane \n''Cl2FeO8 iron(II) perchlorate \n''CoFe2O4 cobalt(II) diiron tetroxide \n''Cr3Fe2O12 iron(III) chromate \n''Cr6Fe2O21 iron(III) dichromate \n''CuFeS2 copper(II) ferrous sulfide \n''CuFe2O4 copper iron oxide \n''Na3FeF6 sodium hexafluoroferrate(III) \n''Fe(AlO2)2 iron(II) aluminate \n''FeCr2O4 iron(II) chromite \n''Fe(OH)O ferric hydroxide oxide \n''Fe(OH)2 iron(II) hydroxide \n''Fe(OH)3 iron(III) hydroxide \n''K2FeO4 potassium ferrate(VI) \n''FeLiO2 lithium iron(III)oxide \n''FeLiSi lithium ferrosilicon \n''FeMoO4 iron(II)molybdate \n''Fe(NO3)2 iron(II) nitrate \n''Fe(NO3)3 ferric nitrate \n''FePO4 iron(III) phosphate \n''FePO4 iron phosphate \n''FeSO4 duretter \n''Fe(TaO3)2 iron(II) tantalate \n''Fe(VO3)3 iron(III) metavanadate \n''FeWO4 iron(II) tungstate \n''Fe2(C2O4)3 iron(III) oxalate \n''Fe2NiO4 iron nickel oxide \n''Fe2(SO4)3 ferric sulfate \n''Fe2(SO4)3·xH2O iron(III)sulfate hydrate \n''Fe2SiO4 iron(II) orthosilieate \n''Fe4(P2O7)3·9H2O iron(III) pyrophosphate nonahydrate \n''Y3Fe5O12 yttrium iron oxide \n''SrFe12O19 strontium ferrite \n''Fe(C2O4)·2H2O iron(II) oxalate dihydrate \n''C3FeN3S3 iron(III) thiocyanate \n''C3H3FeO6 iron(III) formate \n''C4H2FeO4 ferrous fumarate \n''C4H2FeO4 tetraearbonyldihydroiron \n''Fe(CO2CH3)2 iron(II) acetate \n''C5FeN6O nitroprusside \n''K3Fe(CN)6 potassium hexacyanoferrate(III) \n''Fe2(C2O4)3·6H2O iron(III)oxalate hexahydrate \n''C6H4Fe2N7 ferric ammonium ferrocyanide \n''FeC6H10O6 iron(II) lactate \n''[HOCH2[CH(OH)]4CO2]2Fe·2H2O iron(II)-D-gluconate dihydrate \n''(NH4)4[Fe(CN)6]·xH2O tetraammonium hexacyanoferrate \n''C8H8FeO2 cyclopentadienyldicarbonyl(methyl)iron(II) \n''Fe2(CO)9 diironnonacarbonyl \n''[CH3COCH=C(O)CH3]2Fe bis(acetylacetonate)iron \n''C8H8Fe(CO)3 tricarbonyl(cyclooctatetraene)iron(II) \n''C5H5FeC5H4COH ferrocenecarboxaldehyde \n''C11H10FeO2 ferrocenecarboxylic acid \n''C11H12FeO ferrocenemethanol \n''C12H10FeO2 1,1'-ferrocenedicarboxaldehyde \n''Fe3(CO)12 triirondodecacarbonyl \n''C12H10FeO4 1,1'-ferrocenedicarboxylic acid \n''C12H11FeN ferroceneacetonitrile \n''C12H12FeO acetylferrocene \n''C12H12FeO2 ferroceneacetic acid \n''C12H14FeO 1-(ferrocenyl)ethanol \n''C12H14FeO2 1,1'-ferrocenedimethanol \n''C12H22FeO14 ferric dicitrate \n''C5H5FeC5H4CH2N(CH3)2 (dimethylaminomethyl)ferrocene \n''C14H10Fe2O4 cyclopentadienyl iron(II)dicarbonyl dimer \n''C14H14FeO2 1,1'-diacetylferrocene \n''C14H16FeO butyrylferrocene \n''C14H19FeN (R)-(+)-N,N-dimethyl-1-ferrocenylethylamine \n''C14H19FeN (S)-(-)-N,N-dimethyl-1-ferrocenylethylamine \n''C14H22FeSi2 1,1'-bis(dimethylsilyl)ferrocene \n''Fe(C5H7O2)3 iron(III) acetylacetonate \n''C5H4PC6H5C5H4Fe 1,1'-bis(phenylphosphinidene)ferrocene \n''C16H21BrFe (6-bromohexyl)ferrocene \n''C16H22FeS 6-(ferrocenyl)hexanethiol \n''C17H14FeO benzoylferrocene \n''C20H12FeN4 porphyrin fe(iii) \n''C22H20FeP2 1,1'-bis(phenylphosphino)ferrocene \n''C22H36FeP2 1,1'-bis(diisopropylphosphino)ferrocene \n''C26H16FeN6 dicyanobis(1,10-phenanthroline)iron \n''C30H27FeO6 tris(1-phenylbutane-1,3-dionato-o,O')iron \n''C30H36FeP2 1-diphenylphosphino-1'-(di-tert-butylphosphino)ferrocene \n''C32Cl16FeN8 iron(II)1,2,3,4,8,9,10,11,15,16,17,18,22,23,24,25-hexadecachloro-29H,31 H-phthalocyanine \n''C32H16FeN8 iron phthalocyanine \n''C32H40FeP2 (R)-1-[(1 S)-2-(diphenylphosphino)ferrocenyl]ethyldi-tert-butylphosphine \n''C32H40FeP2 (R)-1-[(S)-2-(di-tert-butylphosphino)ferrocenyl]ethyldiphenylphosphine \n''C32H40FeP2 (S)-1-[(1 R)-2-(diphenylphosphino)ferrocenyl]ethyldi-tert-butylphosphine \n''C32H40FeP2 (S)-1-[(R)-2-(di-tert-butylphosphino)ferrocenyl]ethyldiphenylphosphine \n''C32H52FeP2 (R)-1-[(S)-2-(dicyclohexylphosphino)ferrocenyl]ethyl­di-tert-butylphosphine \n''Fe[(CH3)3CCOCHCOC(CH3)3] iron(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''C34H28FeP2 1,1'-bis(diphenylphosphino)ferrocene \n'""", '26', '55.85')
        self.colorFe=colorFe="goldenrod1"
        self.Fe = tk.Button(self, text=Fe[0], width=5, height=2, bg=colorFe, font=10, borderwidth=3,
                           command=lambda text=Fe: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorFe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Fe()])
        self.Fe.grid(row=6, column=9)
        
        Ru = ('Ru', 'Ruthenium', """'Ru ruthenium \n''RuCl3 ruthenium(III) chloride \n''RuI3 ruthenium(III) iodide \n''RuO2 ruthenium dioxide \n''O4Ru ruthenium(VIII) oxide \n''RuF3 ruthenium(III) fluoride \n''RuF4 ruthenium(IV) fluoride \n''RuF5 ruthenium(V) fluoride \n''RuF6 ruthenium(VI) fluoride \n''C10H10Ru ruthenocene \n''Ru3(CO)12 triruthenium dodecacarbonyl \n''C7H9RuC7H9 bis(ethylcyclopentadienyl)ruthenium(II) \n''C16H22Ru (1,5-cyclooctadiene)(1,3,5-cyclooctatriene)ruthenium \n''Ru[H2C=C(CH3)CH2]2(COD) bis(2-methylallyl)(1,5-cyclooctadiene)ruthenium(II) \n''Ru(C5(CH3)5)2 decamethylruthenocene \n''RuO2·xH2O ruthenium(IV)oxide hydrate \n''KRuO4 potassium perruthenate \n''K2RuO4 potassium ruthenate \n''Ru(CO)5 ruthenium pentacarbonyl \n''Ru2(CO)9 ruthenium nonacarbonyl \n''RuBr3 ruthenium(III) bromide \n''Ru2(C6H6)2Cl2 benzeneruthenium(II)chloride dimer \n''(CH3CO2)7Ru3O·3H2O ruthenium(II,III)μ-oxoacetate trihydrate \n''Ru(C5H7O2)3 ruthenium(III)acetylacetonate \n''[Ru((CH3)2CC6H4CH3)Cl2]2 dichloro(p-cymene)ruthenium(II)dimer \n''C20H28I4Ru2 diiodo(p-cymene)ruthenium(II)dimer \n''C23H19N6Ru delta-bis(2,2'-bipyridine)imidazole ruthenium (ii) \n''C23H19N6Ru lambda-bis(2,2'-bipyridine)imidazole ruthenium (ii) \n''C40H60Ru4Cl4 chloro(pentamethylcyclopentadienyl)ruthenium(II)tetramer \n''C62H42O6Ru2 1-hydroxytetraphenyl-cyclopentadienyl(tetraphenyl-2,4-cyclopentadien-1-one)-μ-hydrotetracarbonyldiruthenium(II) \n''[(C6H5)3P]4RuH2 dihydridotetrakis(triphenylphosphine)ruthenium(II) \n''H15Cl2N5Ru chloropentaammineruthenium(II)chloride \n''RuCl3·xH2O ruthenium(III) chloride hydrate \n''[Ru(NH3)5Cl]Cl2 pentaamminechlororuthenium(III)chloride \n''[Ru(NH3)6]Cl3 hexaammineruthenium(III)chloride \n''(NH4)2RuCl6 diammonium hexachlororuthenate \n''Ru(NO)(NO3)x(OH)y,(x+y)=(3) ruthenium(III)nitrosyl nitrate \n''[Ru(CO)3Cl2]2 tricarbonyldichlororuthenium(II)dimer \n''XeFRuF6 xenon fluoride hexafluororuthenate \n''XeF5RuF6 xenon pentafluoride hexafluororuthenate \n''(C2H5)4N[(CH3CN)2RuCl4] tetraethylammonium bis(acetonitrile)tetrachlororuthenate(III) \n''C29H35Cl2N3Ru [1,3-bis(2,4,6-trimethylphenyl)-2-imidazolidinylidene]dichloro[3-(2-pyridinyl-κN)propylidene-κC]ruthenium(II) \n''[CH2CH(C6H5)]x[CH2CH(NC4H7O)]y N-vinylpyrrolidone styrene copolymer \n''C35H62Cl2P2Ru dichloro(3-methyl-2-butenylidene)bis(tricyclopentylphosphine)ruthenium(II) \n''C37H25ClO2Ru chlorodicarbonyl(1,2,3,4,5-pentaphenylcyclopentadienyl)ruthenium(II) \n''C37H44N4ORu 2,3,7,8,12,13,17,18-octaethyl-21H,23 H-porphine ruthenium(II)carbonyl \n''C41H35ClP2Ru chlorocyclopentadienylbis(triphenylphosphine)ruthenium(II) \n''C41H74Cl2P2Ru dichloro(3-methyl-2-butenylidene)bis(tricyclohexylphosphine)ruthenium(II) \n''C43H72Cl2P2Ru grubbs catalyst,1st generation \n''C45H28N4ORu 5,10,15,20-tetraphenyl-21H,23 H-porphine ruthenium(II)carbonyl \n''C9H7·RuCl·2(C18H15P) chloro(indenyl)bis(triphenylphosphine)ruthenium(II) \n''[(C10H15)Ru(P((C6H5)3))2Cl] pentamethylcyclopentadienylbis(triphenylphosphine)ruthenium(II)chloride \n''C50H57N7ORu delta-bis(2,2'-bipyridine)-(5-methyl-2-2'-bipyridine)-c9-adamantane ruthenium (ii) \n''C50H57N7ORu lambda-bis(2,2'-bipyridine)-(5-methyl-2-2'-bipyridine)-c9-adamantane ruthenium (ii) \n''C54H43F8N7Ru delta-bis(2,2'-bipyridine)-(5-methyl-2-2'-bipyridine)-c2-adamantane ruthenium (ii) \n''[(C6H5)3P]3RuCl2 tris(triphenylphosphine)ruthenium(II) dichloride \n''[(C6H5)3P]4RuCl2 dichlorotetrakis(triphenylphosphine)ruthenium(II) \n''Ru(NO)Cl3·xH2O ruthenium(III)nitrosyl chloride hydrate \n''K2RuCl5(H2O) potassium aquapentachlororuthenate(III) \n''K2Ru(NO)Cl5 potassium pentachloronitrosylruthenate(II) \n''K4[(RuCl5)2O]·xH2O potassiumμ-oxobis[pentachlororuthenate(IV)]hydrate \n''K4Ru(CN)6·xH2O potassium hexacyanoruthenate(II)hydrate \n''C16H24N3PRuF6 pentamethylcyclopentadienyltris(acetonitrile)ruthenium(II)hexafluorophosphate \n''C20H16Cl2N4Ru·xH2O cis-bis(2,2'-bipyridine)dichlororuthenium(II)hydrate \n''C22H25Cl3N3O8Ru+8 naphtha (petroleum), light oxidized, acetic acid manufg., light residue recycle \n''C28H32Cl2N2P2Ru dichlorobis(2-(diphenylphosphino)ethylamine)ruthenium(II) \n''C28H45Cl2OPRu hoveyda-grubbs catalyst 1st generation \n''(C10D8N2)3Ru(PF6)2 tris(2,2'-bipyridyl-d8)ruthenium(II)hexafluorophosphate \n''C30H24Cl2N6Ru·6H2O tris(2,2'-bipyridyl)dichlororuthenium(II)hexahydrate \n''C31H38Cl2N2ORu hoveyda-grubbs catalyst 2nd generation \n''C36H24Cl2N6Ru dichlorotris(1,10-phenanthroline)ruthenium(II) \n''[(C6H5)3P]2Ru(CO)2Cl2 bis(triphenylphosphine)ruthenium(II)dicarbonyl chloride \n'""", '44', '101.07')
        self.colorRu=colorRu="goldenrod2"
        self.Ru = tk.Button(self, text=Ru[0], width=5, height=2, bg=colorRu, font=10, borderwidth=3,
                           command=lambda text=Ru: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRu, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ru()])
        self.Ru.grid(row=7, column=9)

        Os = ('Os', 'Osmium', """'Os osmium \n''OsCl3 osmium(III) chloride \n''Cl4Os osmium(IV) chloride \n''F6Os osmium(VI) fluoride \n''OsO4 osmium tetroxide \n''OsBr3 osmium(III) bromide \n''OsCl2 osmium(II) chloride \n''OsF4 osmium(IV) fluoride \n''OsF5 osmium(V) fluoride \n''OsO2 osmium(IV) oxide \n''Os(CO)12 triosmium dodecacarbonyl \n''Os(C5(CH3)5)2 bis(pentamethylcyclopentadienyl)osmium(II) \n''K2OsCl6 potassium hexachloroosmate(IV) \n''Os(CO)5 osmium pentacarbonyl \n''OsOCl4 osmium(VI) tetrachloride oxide \n''Os2(CO)9 osmium nonacarbonyl \n''Os4H4(CO)12 dodecacarbonyltetra-μ-hydridotetraosmium \n''C23H19N6Os delta-bis(2,2'-bipyridine)imidazole osmium (ii) \n''C23H19N6Os lambda-bis(2,2'-bipyridine)imidazole osmium (ii) \n''[Os(N2)(NH3)5]Cl2 pentaammine(dinitrogen)osmium(II)chloride \n''OsCl3·xH2O osmium(III)chloride hydrate \n''(NH4)2OsCl6 ammonium hexachloroosmate(IV) \n''K2OsO4·2H2O potassium osmate(VI)dihydrate \n'""", '76', '190.20')
        self.colorOs=colorOs="goldenrod3"
        self.Os = tk.Button(self, text=Os[0], width=5, height=2, bg=colorOs, font=10, borderwidth=3,
                           command=lambda text=Os: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorOs, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Os()])
        self.Os.grid(row=8, column=9)

        Hs = ('Hs', 'Hassium', """'Hs hassium hassium metal\n'""", '108', '265.00')
        self.colorHs=colorHs="goldenrod3"
        self.Hs = tk.Button(self, text=Hs[0], width=5, height=2, bg=colorHs, font=10, borderwidth=3,
                           command=lambda text=Hs: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorHs, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Hs()])
        self.Hs.grid(row=9, column=9)

        
        Co = ('Co', 'Cobalt', """'Co cobalt \n''CoBr2 cobalt dibromide \n''CoCl2 cobalt dichloride \n''CoF2 cobalt difluoride \n''CoF3 cobalt trifluoride \n''CoI2 cobalt(II)iodide \n''CoO cobalt monoxide \n''CoS cobaltous sulfide \n''CoS2 cobalt disulfide \n''CoSb cobalt antimonide \n''CoSe cobalt(II) selenide \n''CoSi2 cobalt silicide \n''Sm2Co7 disamarium heptacobalt \n''CoTe cobalt(II) telluride \n''Co2O3 cobalt(III) oxide \n''Co2P cobalt phosphide \n''Co3O4 cobalt(II,III)oxide \n''SmCo5 samarium pentacobalt \n''CoAl2O4 cobalt aluminum oxide \n''Co3(AsO4)2 cobalt arsenate \n''CoCO3 cobaltous carbonate \n''C2CoN2 cobalt(II) cyanide \n''CoC2O4 cobalt(II) oxalate \n''Co(C5H5)2 cobaltocene \n''C14H18Co bis(ethylcyclopentadienyl)cobalt(II) \n''C20H30Co bis(pentamethylcyclopentadienyl)cobalt(II) \n''Cl2CoO8 cobalt(II) perchlorate \n''CoCrO4 cobalt(II) chromate \n''CoCr2O4 cobalt(II) chromite \n''CoFe2O4 cobalt(II) diiron tetroxide \n''Co(OH)2 cobalt hydroxide \n''Co(OH)2 cobalt(II)hydroxide \n''Co(IO3)2 cobalt(II) iodate \n''CoLiO2 lithium cobalt(III)oxide \n''CoMoO4 cobalt(II) molybdate \n''Co(NO2)2 cobalt(II) nitrite \n''Co(NO3)3 cobalt(III) nitrate \n''CoN2O6 cobaltous nitrate \n''NiOCoO nickel cobalt oxide \n''Co(OH)3 cobalt(III) hydroxide \n''CoO3Ti cobalt titanium oxide \n''CoSO4 cobalt(II) sulfate \n''CoWO4 cobalt(II) tungstate \n''Co2(CO)8 cobalt carbonyl \n''Co2SiO4 cobalt(II) orthosilieate \n''Co2SnO4 cobalt(II) stannate \n''Co2TiO4 cobalt(III) titanate \n''Co3(PO4)2 cobalt phosphate \n''Co4(CO)12 cobalt dodecacarbonyl \n''CoBr2·xH2O cobalt(II)bromide hydrate \n''CoCO3·xH2O cobalt(II)carbonate hydrate \n''Co(SCN)2 cobalt dithiocyanate \n''C2H2CoO4 cobaltous formate \n''CoC2O4·2H2O cobalt(II)oxalate dihydrate \n''(CH3CO2)2Co cobaltous acetate \n''(CH3COO)2Co·4H2O cobalt(II) acetate tetrahydrate \n''K3Co(CN)6 potassium hexacyanocobaltate(III) \n''C6H9CoO6 cobalt(III) acetate \n''C5H5Co(CO)2 cyclopentadienyl cobalt(I)dicarbonyl \n''Co(C5H7O2)2 bis(acetylacetonato)cobalt(II) \n''Co(C5H7O2)2·xH2O cobalt(II)acetylacetonate hydrate \n''[HCOC6H4O]2Co·2H2O bis(salicylaldehyde)cobalt(II) \n''Co(C5H7O2)3 cobalt(III)acetylacetonate \n''[CH3(CH2)3CH(C2H5)CO2]2Co cobalt(II) 2-ethylhexanoate \n''[C6H5COCH=C(O)CH3]2Co cobalt(II)benzoylacetonate \n''C20H34CoO4 cobalt bis(4-cyclohexylbutyrate) \n''Co(C11H7O2)2 cobalt(II) naphthenate \n''C32CoF16N8 cobalt(II)1,2,3,4,8,9,10,11,15,16,17,18,22,23,24,25-hexadecafluoro-29H,31 H-phthalocyanine \n''C32H16CoN8 cobalt phthalocyanine \n''Co(OCC(CH3)3CHCOC(CH3)3)3 cobalt tris(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''C36H44CoN4 2,3,7,8,12,13,17,18-octaethyl-21H,23 H-porphine cobalt(II) \n''C36H66CoO4 cobalt(II) oleate \n''Co(H3C(CH2)16CO2)2 cobalt(II)stearate \n''C44H28CoN4 5,10,15,20-tetraphenyl-21H,23 H-porphine cobalt(II) \n''C48H24CoN8 cobalt(II)2,3-naphthalocyanine \n''CoCl2·xH2O cobalt(II)chloride hydrate \n''Co(ClO4)2·6H2O cobalt(II)perchlorate hexahydrate \n''Cl2CoH12O6 cobalt(II) chloride hexahydrate \n''[Co(NH3)5Cl]Cl2 pentaamminechlorocobalt(III)chloride \n''[Co(NH3)6]Cl3 hexaamminecobalt(III)chloride \n''CoBr2·6H2O cobalt(II) bromide hexahydrate \n''CoCl2·2H2O cobalt(II) chloride dihydrate \n''CoF2·4H2O cobalt(II)fluoride tetrahydrate \n''CoH2MoO5 cobalt(II) molybdate monohydrate \n''CoSO4·xH2O cobalt(II)sulfate hydrate \n''Co(NO3)2·6H2O cobaltous nitrate hexahydrate \n''CoSO4·7H2O cobalt sulfate heptahydrate \n''[Co(NH3)6](NO3)3 hexaamminecobalt(III)nitrate \n''CoI2·2H2O cobalt(II) iodide dihydrate \n''CoI2·6H2O cobalt(II) iodide hexahydrate \n''Na3Co(NO2)6 sodium hexanitrocobaltate(III) \n''CoN6Na3O12 sodium hexanitrocobaltate \n''Co2F6·2H2O cobalt(III) fluoride dihydrate \n''Co2O3·H2O cobalt(III) oxide monohydrate \n''Co3[Fe(CN)6]2 cobalt(II) ferrieyanide \n''Co3(PO4)2 cobalt(II)phosphate hydrate \n''Co(CN)2·2H2O cobalt cyanide dihydrate \n''HgCo(SCN)4 mercury(II) tetrakis(thiocyanato-n)cobaltate(2-) \n''C4H16CoN7O7 trans-dinitrobis(ethylenediamine)cobalt(III)nitrate \n''[(C6H5)3P]3CoCl chlorotris(triphenylphosphine)cobalt(I) \n''(H2NCH2CH2NH2)3Co(NO3)3 tris(ethylenediamine)cobalt(III)nitrate \n''Co(C5HF6O2)2·xH2O cobalt(II)hexafluoroacetylacetonate hydrate \n''C10H10CoF6P bis(cyclopentadienyl)cobalt(III)hexafluorophosphate \n''C12H30Cl3CoN8 cobalt(III)sepulchrate trichloride \n''C14H18CoF6P bis(ethylcyclopentadienyl)cobalt(III)hexafluorophosphate \n''[CH2N=CHC6H4O]2Co N,N'-bis(salicylidene)ethylenediaminocobalt(II) \n''[CH2N=CHC6H4O]2Co·xH2O N,N'-bis(salicylidene)ethylenediaminocobalt(II)hydrate \n''C16H40Cl4CoN2 tetraethylammonium tetrachlorocobaltate(II) \n''C6H4[N=CHC6H4(O)]2Co·H2O N,N'-bis(salicylidene)-1,2-phenylenediaminocobalt(II)monohydrate \n''C20H30CoF6P bis(pentamethylcyclopentadienyl)cobalt(III)hexafluorophosphate \n''CH3N[(CH2)3N=CHC6H4(O)]2Co bis(salicylideniminato-3-propyl)methylaminocobalt(II) \n''[(C6H5)2PCH2CH2P(C6H5)2]CoCl2 [1,2-bis(diphenylphosphino)ethane]dichlorocobalt(II) \n''C30H28CoN4O4 co(iii)-(deuteroporphyrin ix) \n''C34H32CoN4O4 protoporphyrin ix containing co \n''[(C6H5)3P]2CoCl2 dichlorobis(triphenylphosphine)cobalt(II) \n''C36H36CoN4O8 coproporphyrin i containing co(iii) \n''[[[(CH3)3C]2C6H2(O)CH=N]2C6H10]Co (R,R)-(-)-N,N'-bis(3,5-di-tert-butylsalicylidene)-1,2-cyclohexanediaminocobalt(II) \n''[[[(CH3)3C]2C6H2(O)CH=N]2C6H10]Co (S,S)-(+)-N,N'-bis(3,5-di-tert-butylsalicylidene)-1,2-cyclohexanediaminocobalt(II) \n''C42H44CoN4O16 cobalt-sirohydrochlorin \n''C42H46CoN4O16 cobalt-precorrin-2 \n''C43H46CoN4O16 cobalt-factor iii \n''C43H48CoN4O16 cobalt-precorrin-3 \n''C43H51CoN4O16 cobalt-precorrin-5b \n''C44H52CoN4O16 cobalt-precorrin-4 \n''C44H54CoN4O16 cobalt-precorrin-6a \n''C44H56CoN4O16 cobalt-precorrin-6b \n''C45H54CoN4O16 cobalt-precorrin-5a \n''C45H58CoN4O16 cobalt-precorrin-7 \n''C45H60CoN4O14 cobalt-precorrin-8x \n''C45H60CoN4O14 cobyrinate \n''C45H61CoN6O12 cob(ii)yrinate a,c-diamide \n''C45H61CoN6O12 cob(i)yrinate a,c-diamide \n''C45H65CoN10O8 cobyrate \n''C48H36CoN4O4 5,10,15,20-tetrakis(4-methoxyphenyl)-21H,23 H-porphine cobalt(II) \n''C48H72CoN11O8 cobinamide \n''C55H73CoN11O15 adenosyl-cobyrinate a,c-diamide \n''C55H77CoN15O11 adenosyl-cobyrate \n''C58H84CoN16O11 adenosylcobinamide \n''Co(BF4)2·6H2O cobalt(II)tetrafluoroborate hexahydrate \n''Co(BrO3)2·6H2O cobalt(II) bromate hexahydrate \n''Co(ClO3)2·6H2O cobalt(II) chlorate hexahydrate \n''CoH4N2O6S2 cobaltous sulfamate \n''(NH4)2Co(SO4)2·6H2O ammonium cobalt(II)sulfate hexahydrate \n''CoNH4PO4 ammonium cobalt(II) phosphate \n''Co(OH)2·H2O cobalt(II) hydroxide monohydrate \n''CoSO4·H2O cobalt(II) sulfate monohydrate \n''CoSeO3·2H2O cobalt(II) selenite dihydrate \n''CoSeO4.5H2O cobalt(II) selenate pentahydrate \n''CoSiF6·6H2O cobalt(II) hexafluorosilicate hexahydrate \n''Co3(AsO4)2·8H2O cobalt(II) arsenate octahydrate \n''(H2NCH2CH2NH2)3CoCl3·2H2O tris(ethylenediamine)cobalt(III)chloride dihydrate \n''C13H19ClCoN5O4 chloro(pyridine)bis(dimethylglyoximato)cobalt(III) \n''C16H12CoF2N2O2 fluomine \n''Cl2Co(P(C6H5)2C5H4)2Fe (1,1'-bis(diphenylphosphino)ferrocene)dichlorocobalt(II) \n''C58H83CoN16O14P adenosyl-cobinamide phosphate \n''C60H89CoN13O15P co-5-hydroxybenzimidazolylcob(i)amide \n''C61H85CoN13O15P factor iiim \n''C62H88CoN13O14P cob(i)alamin \n''C62H88CoN13O14P cob(ii) alamin \n''C62H88CoN13O14P cobalamin \n''C62H89CoN13O15P aquacob(iii)alamin \n''C62H90CoN13O15P hydroxocobalamin \n''C63H88CoN14O14P cyanocobalamin \n''C63H91CoN13O14P co-methylcobalamin \n''C63H91CoN13O14P methylcobalamin \n''C67H93CoN15O16P 5-hydroxybenzimidazolylcobamide \n''C68H95CoN21O21P2 adenosylcobinamide-gdp \n''C72H100CoN18O20P2 adenosylcobalamin-5'-phosphate \n''C72H101CoN18O17P coenzyme b12 \n''C82H72O6N2Co2Pd2 (R)-(-)-COP-Oac catalyst \n''C82H72O6N2Co2Pd2 (S)-(+)-COP-Oac catalyst \n''Co(CHO2)2·2H2O cobalt(II) formate dihydrate \n''CoK2(SO4)2·6H2O cobalt(II) potassium sulfate hexahydrate \n''CoK3(NO2)6·1.5H2O cobalt(III) potassium nitrite sesquihydrate \n''Co(SCN)2·3H2O cobalt(II) thiocyanate trihydrate \n''Co3(C6H5O7)2·2H2O cobalt(II) citrate dihydrate \n'""", '27', '58.93')
        self.colorCo=colorCo="RosyBrown1"
        self.Co = tk.Button(self, text=Co[0], width=5, height=2, bg=colorCo, font=10, borderwidth=3,
                           command=lambda text=Co: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCo, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Co()])
        self.Co.grid(row=6, column=10)

        Rh = ('Rh', 'Rhodium', """'Rh rhodium \n''RhCl3 rhodium(III) chloride \n''I3Rh rhodium(III) iodide \n''RhO2 rhodium dioxide \n''Rh2O3 rhodium(III) oxide \n''PtRh platinum/rhodium alloy \n''RhBr3 rhodium(III) bromide \n''RhF3 rhodium(III) fluoride \n''RhF6 rhodium(VI) fluoride \n''Rh6(CO)16 hexarhodium(0)hexadecacarbonyl \n''K3RhCl6 potassium hexachlororhodate(III) \n''K3RuCl6 potassium hexachlororuthenate(III) \n''Cl6K3Rh selenomycin \n''Na3RhCl6 sodium hexachlororhodate(III) \n''Rh2O3·xH2O rhodium(III)oxide hydrate \n''Rh(NO3)3 rhodium(III) nitrate \n''RhBr3·xH2O rhodium(III)bromide hydrate \n''C4H6O4Rh rhodium diacetate \n''Rh(CO)2(C5H7O2) (acetylacetonato)dicarbonylrhodium(I) \n''C8H16Cl2Rh2 μ-dichlorotetraethylene dirhodium(I) \n''[Rh(CH3COO)2]2 rhodium(II) acetate dimer \n''Rh4(CO)12 tetrarhodium dodecacarbonyl \n''[(H2C=CHCH2CH2CH=CH2)RhCl]2 chloro(1,5-hexadiene)rhodium(I),dimer \n''C13H19O2Rh (acetylacetonato)(1,5-cyclooctadiene)rhodium(I) \n''C14H16Cl2Rh2 bicyclo[2.2.1]hepta-2,5-diene-rhodium(I)chloride dimer \n''[CH3COCH=COCH3]3Rh rhodium(III)acetylacetonate \n''C16H24Cl2Rh2 chloro(1,5-cyclooctadiene)rhodium(I)dimer \n''C16H26O2Rh2 hydroxy(cyclooctadiene)rhodium(I)dimer \n''C18H30O2Rh2 methoxy(cyclooctadiene)rhodium(I)dimer \n''[Rh(C5Me5)Cl2]2 pentamethylcyclopentadienylrhodium(III)chloride dimer \n''[[(CH3)3CCO2]2Rh]2 rhodium(II)trimethylacetate,dimer \n''[[CH3(CH2)4CO2]2Rh]2 rhodium(II)hexanoate,dimer \n''C32H40O8Rh2 bis[rhodium(α,α,α',α'-tetramethyl-1,3-benzenedipropionic acid)] \n''[[CH3(CH2)6CO2]2Rh]2 rhodium(II)octanoate,dimer \n''[Ru(NH3)6]Cl2 hexaammineruthenium(II)chloride \n''RhCl3·xH2O rhodium(III)chloride hydrate \n''Cl3H6O3Rh rhodium trichloride, trihydrate \n''[Rh(NH3)5Cl]Cl2 pentaamminechlororhodium(III)chloride \n''(NH4)3RhCl6 ammonium hexachlororhodate(III) \n''RhI3·H2O rhodium(III)iodide hydrate \n''Rh2(SO4)3 rhodium(III)sulfate \n''RhPO4 rhodium(III)phosphate \n''K3Rh(NO2)6 potassium hexanitrorhodate(III) \n''[Rh(CO)2Cl]2 μ-dichlorotetracarbonyldirhodium(I) \n''Rh2O3·5H2O rhodium(III) oxide pentahydrate \n''Na4[Rh2(CO3)4]·xH2O tetrasodium tetrakis(μ-carbonato)dirhodate hydrate \n''[(C6H5)3P]4RhH hydridotetrakis(triphenylphosphine)rhodium(I) \n''Rh(H2NCH2CH2NH2)3(NO3)3 tris(ethylenediamine)rhodium(III)nitrate \n''[(CF3COO)2Rh]2 rhodium(II)trifluoroacetate dimer \n''[Rh(NBD)BF4 bis(norbornadiene)rhodium(I)tetrafluoroborate \n''[(CF3CF2CF2CO2)2Rh]2 rhodium(II)heptafluorobutyrate,dimer \n''C20H20Cl3N4Rh trans-dichlorotetrakis(pyridine)rhodium(III)chloride \n''C30H68Cl2P2Rh+2 phosphosulfurized polybutene, barium salts \n''C31H41F6P4Rh [tris(dimethylphenylphosphine)](2,5-norbornadiene)rhodium(I)hexafluorophosphate \n''[CH3C[CH2P(C6H5)2]3]RhCl3 trichloro[1,1,1-tris(diphenylphosphinomethyl)ethane]rhodium(III) \n''C44H32Cl2N4Rh2 chlorobis(2-phenylpyridine)rhodium(III)dimer \n''[(C6H5)3P]3RhBr bromotris(triphenylphosphine)rhodium(I) \n''[(C6H5)3P]3RhCl tris(triphenylphosphine)rhodium(I) chloride \n''[(C6H5)3P]3Rh(CO)H carbonylhydrotris(triphenylphosphine)rhodium \n''[(C6H5)3P]3Ru(CO)H2 carbonyldihydridotris(triphenylphosphine)ruthenium(II) \n''(NH4)2Rh(H2O)Cl5 ammonium aquapentachlororhodate(III) \n''Na(NH4)2Rh(NO2)6 diammonium sodium hexanitrorhodate(III) \n''Rh(NO3)3·2H2O rhodium(III) nitrate dihydrate \n''(H2NCH2CH2NH2)3RhCl3·3H2O trichlorotris(ethylenediamine)rhodium(III)trihydrate \n''C6H24Cl3N6Rh tris(ethylenediamine)rhodium(III)chloride \n''C8H15Cl2N4O4Rh dichloro(dimethylglyoximato)(dimethylglyoxime)rhodium(III) \n''C12H18BF4N2Rh bis(acetonitrile)(1,5-cyclooctadiene)rhodium(I)tetrafluoroborate \n''C16H24BF4Rh·xH2O bis(1,5-cyclooctadiene)rhodium(I)tetrafluoroborate hydrate \n''C17H24F3O3RhS bis(1,5-cyclooctadiene)rhodium(I)trifluoromethanesulfonate \n''C22H40BF4P2Rh 1,2-bis[(2R,5 R)-2,5-(dimethylphospholano]ethane(cyclooctadiene)rhodium(I)tetrafluoroborate \n''C22H40BF4P2Rh 1,2-bis[(2S,5 S)-2,5-dimethylphospholano]ethane(cyclooctadiene)rhodium(I)tetrafluoroborate \n''C26H40BF4P2Rh 1,2-bis[(2R,5 R)-2,5-dimethylphospholano]benzene(cyclooctadiene)rhodium(I)tetrafluoroborate \n''C26H40BF4P2Rh 1,2-bis[(2S,5 S)-2,5-dimethylphospholano]benzene(cyclooctadiene)rhodium(I)tetrafluoroborate \n''C35H32ClO4P2Rh (bicyclo[2.2.1]hepta-2,5-diene)[(2S,3 S)-bis(diphenylphosphino)butane]rhodium(I)perchlorate \n''C36H40BF4P2Rh [1,4-bis(diphenylphosphino)butane](1,5-cyclooctadiene)rhodium(I)tetrafluoroborate \n''C45H44Cl2F6P3Rh (1,5-cyclooctadiene)bis(triphenylphosphine)rhodium(I)hexafluorophosphate dichloromethane complex(1:1) \n''[(C6H5)3P]3Ru(CO)(Cl)H carbonylchlorohydridotris(triphenylphosphine)ruthenium(II) \n''[(C6H5)3P]2RhCl(CO) bis(triphenylphosphine)rhodium(I)carbonyl chloride \n''C27H40F3O3P2RhS 1,2-bis[(2R,5 R)-2,5-dimethylphospholano]benzene(cyclooctadiene)rhodium(I)trifluoromethanesulfonate \n'""", '45', '102.91')
        self.colorRh=colorRh="RosyBrown2"
        self.Rh = tk.Button(self, text=Rh[0], width=5, height=2, bg=colorRh, font=10, borderwidth=3,
                           command=lambda text=Rh: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRh, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Rh()])
        self.Rh.grid(row=7, column=10)

        Ir = ('Ir', 'Iridium', """'Ir iridium \n''Br3Ir iridium(III) bromide \n''IrCl3 iridium(III) chloride \n''Cl4Ir iridium(IV) chloride \n''IrF3 iridium(III) fluoride \n''IrF6 iridium(VI) fluoride \n''IrI3 iridium(III) iodide \n''IrO2 iridium(IV) oxide \n''IrS2 iridium(IV) sulfide \n''Ir2O3 iridium(III) oxide \n''Ir2S3 iridium(III) sulfide \n''Ir4(CO)12 tetrairidium dodecacarbonyl \n''K2IrCl6 potassium hexachloroiridate(IV) \n''K3IrCl6 potassium hexachloroiridate(III) \n''IrO2·xH2O iridium(IV)oxide hydrate \n''K2IrBr6 potassium hexabromoiridate(IV) \n''Na2IrBr6 sodium hexabromoiridate(IV) \n''IrBr3·xH2O iridium(III)bromide hydrate \n''[CH3COCH=C(O)CH3]Ir(CO)2 (acetylacetonato)dicarbonyliridium(I) \n''C13H19IrO2 (acetylacetonato)(1,5-cyclooctadiene)iridium(I) \n''[CH3COCH=C(O)CH3]3Ir iridium(III)acetylacetonate \n''C16H24Cl2Ir2 bis(1,5-cyclooctadiene)diiridium(I)dichloride \n''C20H30Cl4Ir2 pentamethylcyclopentadienyliridium(III)chloride,dimer \n''C32H56Cl2Ir2 chlorobis(cyclooctene)iridium(I)dimer \n''IrCl3·xH2O iridium(III)chloride hydrate \n''[Ir(NH3)5Cl]Cl2 pentaamminechloroiridium(III)chloride \n''lrCl4·xH2O iridium(IV)chloride hydrate \n''IrCl3·xH2O·yHCl iridium(III)chloride hydrochloride hydrate \n''H2Cl6Ir·xH2O hexachloroiridic acid \n''(NH4)3IrCl6·H2O ammonium hexachloroiridate(III)monohydrate \n''(NH4)2IrCl6 ammonium hexachloroiridate(IV) \n''IrBr3·4H2O iridium(III) bromide tetrahydrate \n''K3Ir(NO2)6 potassium hexanitroiridate(III) \n''Na3Ir(NO2)6 sodium hexanitroiridate(III) \n''(NH4)3IrCl6 ammonium hexachloroiridate(III) \n''C15H15Cl3IrN3 trichlorotris(pyridine)iridium(III) \n''C34H38F6IrP3 (1,5-cyclooctadiene)bis(methyldiphenylphosphine)iridium(I)hexafluorophosphate \n''C44H32Cl2Ir2N4 dichlorotetrakis(2-(2-pyridinyl)phenyl)diiridium(III) \n''K2[Ir(NO)Cl5] potassium pentachloronitrosyliridate(III) \n''Na2IrCl6·6H2O sodium hexachloroiridate(IV)hexahydrate \n'""", '77', '192.22')
        self.colorIr=colorIr="RosyBrown3"
        self.Ir = tk.Button(self, text=Ir[0], width=5, height=2, bg=colorIr, font=10, borderwidth=3,
                           command=lambda text=Ir: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorIr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ir()])
        self.Ir.grid(row=8, column=10)

        Mt = ('Mt', 'Meitnerium', """'Mt meitnerium meitnerium metal\n'""", '109', '266.00')
        self.colorMt=colorMt="RosyBrown4"
        self.Mt = tk.Button(self, text=Mt[0], width=5, height=2, bg=colorMt, font=10, borderwidth=3,
                           command=lambda text=Mt: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorMt, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Mt()])
        self.Mt.grid(row=9, column=10)

        colorUnk="white"
    
        Ni = ('Ni', 'Nickle', """'Ni nickel \n''AlNi aluminum-nickel catalyst \n''AsNi nickel arsenide \n''Ni2B nickel boride \n''NiBr2 nickel bromide \n''NiBr2·xH2O nickel(II)bromide hydrate \n''NiCl2 nickel(II) chloride \n''NiF2 nickel(II) fluoride \n''NiI2 nickel iodide \n''NiO nickel monoxide \n''NiS nickel(II) sulfide \n''NiSe nickel(II) selenide \n''NiZr zirconium-nickel alloy (30:70) \n''NiZr zirconium-nickel alloy (70:30) \n''Ni2P nickel phosphide \n''Ni3S2 nickel sulfide \n''Ni3S4 nickel(II,III) sulfide \n''Ni3Sb nickel antimonide \n''Ni(BF4)2 nickel(II) fluoborate \n''Li2NiBr4 dilithium tetrabromonickelate(II) \n''NiCO3 nickel carbonate \n''Ni(CN)2 nickel cyanide \n''Ni(CO)4 nickel carbonyl \n''C8H10Ni allyl(cyclopentadienyl)nickel(II) \n''Ni(C5H5)2 nickelocene \n''Ni(C5H4CH3)2 bis(methylcyclopentadienyl)nickel(II) \n''Ni(C5H4C2H5)2 bis(ethylcyclopentadienyl)nickel(II) \n''C16H24Ni bis(1,5-cyclooctadiene)nickel \n''C18H26Ni bis(tetramethylcyclopentadienyl)nickel(II) \n''Ni(C5(CH3)5)2 bis(pentamethylcyclopentadienyl)nickel(II) \n''Cl2NiO8 nickel perchlorate \n''NiOCoO nickel cobalt oxide \n''NiCr2O4 nickel chromium oxide \n''Fe2NiO4 iron nickel oxide \n''Ni(OH)2 nickel(II)hydroxide \n''H4NiO3 nickel(II) hydroxide monohydrate \n''NiIO3 nickel(II) iodate \n''K2NiF6 potassium hexafluoronickelate(IV) \n''NiMoO4 nickel(II)molybdate \n''Ni(NO2)2 nickel(II) nitrite \n''Ni(NO3)2 nickel(II) nitrate \n''NiCrO4 nickel(II) chromate \n''NiSO4 nickel(II) sulfate \n''NiTiO3 nickel(II) titanate \n''Ni3(PO4)2 nickel phosphate \n''[Ni(NH3)6]Br2 hexaamminenickel(II)bromide \n''NiCO3·2Ni(OH)2·H2O nickel(II) carbonate hydroxide hydrate \n''NiC2O4·2H2O nickel(II)oxalate dihydrate \n''2NiCO3·3Ni(OH)2·4H2O nickel(II)carbonate hydroxide tetrahydrate \n''C2N2NiS2 nickel(II) thiocyanate \n''Ni(OCOCH3)2·4H2O nickel(II) acetate tetrahydrate \n''K2Ni(CN)4 potassium tetracyanonickelate(II) \n''[CH3(CH2)3CH(C2H5)CO2]2Ni nickel(II)2-ethylhexanoate \n''Ni(C5H7O2)2 nickel(II)acetylacetonate \n''C12H10Ni2O2 cyclopentadienylnickel(II)carbonyl,dimer \n''[CH3(CH2)6CO2]2Ni·xH2O nickel(II)octanoate hydrate \n''[C6H11(CH2)3CO2]2Ni nickel(II) bis(4-cyclohexylbutyrate) \n''Ni(OCC(CH3)3CHCOC(CH3)3)2 nickel(II)bis(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''C32H16N8Ni nickel(II)phthalocyanine \n''C32H36N4Ni etioporphyrin inickel \n''C36H44N4Ni 2,3,7,8,12,13,17,18-octaethyl-21H,23 H-porphine nickel(II) \n''Ni(H3C(CH2)16CO2)2 nickel(II)stearate \n''C44H28N4Ni 5,10,15,20-tetraphenyl-21H,23 H-porphine nickel(II) \n''C64H56N8Ni nickel(II)2,11,20,29-tetra-tert-butyl-2,3-naphthalocyanine \n''[(C6H5)3P]4Ni tetrakis(triphenylphosphine)nickel(0) \n''Ni(ClO4)2·6H2O nickel(II)perchlorate hexahydrate \n''NiCl2·xH2O nickel(II)chloride hydrate \n''NiCl2·6H2O nickel(II)chloride hexahydrate \n''[Ni(NH3)6]Cl2 hexaamminenickel(II)chloride \n''NiZnFe4O4 nickel zinc iron oxide \n''F2H8NiO4 nickel(II) fluoride tetrahydrate \n''[Ni(H2O)6](NO3)2 nickel(II) nitrate hexahydrate \n''NiSO4·6H2O nickel(II)sulfate hexahydrate \n''H12NiO10Se nickel(II) selenate hexahydrate \n''NiSO4·7H2O nickel(II)sulfate heptahydrate \n''[Ni(NH3)6]I2 hexaamminenickel(II)iodide \n''NiBr2·3H2O nickel(II) bromide trihydrate \n''NiI2·6H2O nickel(II) iodide hexahydrate \n''NiO2·xH2O nickel(II)peroxide hydrate \n''NiBr2·CH3OCH2CH2OCH3 nickel(II)bromide ethylene glycol dimethyl ether complex \n''NiBr2·O(CH2CH2OCH3)2 nickel(II)bromide 2-methoxyethyl ether complex \n''[((CH3)3P)]2NICl2 dichlorobis(trimethylphosphine)nickel(II) \n''Ni(C5HF6O2)2·xH2O nickel(II)hexafluoroacetylacetonate hydrate \n''[CH2N=CHC6H4O]2Ni N,N'-bis(salicylidene)ethylenediaminonickel(II) \n''C16H40Cl4N2Ni tetraethylammonium tetrachloronickelate(II) \n''C18H36N2NiS4 nickel dibutyldithiocarbamate \n''C23H20ClNiP chloro(cyclopentadienyl)(triphenylphosphine)nickel(II) \n''((CH3(CH2)3)3P)2NiBr2 dibromobis(tributylphosphine)nickel(II) \n''((CH3(CH2)3)3P)2NiCl2 dichlorobis(tributylphosphine)nickel(II) \n''C25H24ClNiP chloro(ethylcyclopentadienyl)(triphenylphosphinenickel(II) \n''[(C6H5)2PCH2CH2P(C6H5)2]NiCl2 [1,2-bis(diphenylphosphino)ethane]dichloronickel(II) \n''[(C6H5)2P(CH2)3P(C6H5)2]NiCl2 [1,3-bis(diphenylphosphino)propane]dichloronickel(II) \n''Ni(C16H15NS2)2 bis(4-dimethylaminodithiobenzil)nickel \n''[(C6H5)3P]2NiCl2 bis(triphenylphosphine)nickel(II)dichloride \n''[(C6H5)3P]2NiBr2 dibromobis(triphenylphosphine)nickel(II) \n''[(C6H5)3P]2Ni(CO)2 bis(triphenylphosphine)dicarbonylnickel \n''C42H48N6NiO14 pyrrocorphinate \n''C42H51N6NiO13 coenzyme f430 \n''C42H53N6NiO14 factor f430 seco-precursor \n''C64H80N8NiO8 nickel(II)1,4,8,11,15,18,22,25-octabutoxy-29H,31 H-phthalocyanine \n''[(C6H5O)3P]4Ni tetrakis(triphenylphosphite)nickel(0) \n''C80H88N8NiO8 nickel(II)5,9,14,18,23,27,32,36-octabutoxy-2,3-naphthalocyanine \n''Ni(NH4)2(SO4)2 ammonium disulfatonickelate(II) \n''Ni(SO3NH2)2·4H2O nickel(II)sulfamate tetrahydrate \n''Ni(CN)2·4H2O nickel(II) cyanide tetrahydrate \n''Ni(ClO3)2·6H2O nickel(II) chlorate hexahydrate \n''Ni(IO3)2·4H2O nickel(II) iodate tetrahydrate \n''NiSnO3·2H2O nickel(II) stannate dihydrate \n''Ni3(AsO4)2·8H2O nickel(II) arsenate octahydrate \n''Ni3(PO4)2·8H2O nickel(II) phosphate octahydrate \n'""", '28', '58.70')
        self.colorNi=colorNi="burlywood1"
        self.Ni = tk.Button(self, text=Ni[0], width=5, height=2, bg=colorNi, font=10, borderwidth=3,
                           command=lambda text=Ni: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNi, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ni()])
        self.Ni.grid(row=6, column=11)

        Pd = ('Pd', 'Palladium', """'Pd palladium \n''PdBr2 palladium(II)bromide \n''Cl2Pd palladium(II)chloride \n''F2Pd palladium(II) fluoride \n''I2Pd palladium(II) iodide \n''OPd palladium oxide \n''PdS palladium(II) sulfide \n''Pb(BF4)2 lead(II)tetrafluoroborate \n''K2PdBr4 potassium tetrabromopalladate(II) \n''Na2PdBr4 sodium tetrabromopalladate(II) \n''Pd(CN)2 palladium(II)cyanide \n''K2PdCl4 potassium tetrachloropalladate(II) \n''Na2PdCl4 sodium tetrachloropalladate(II) \n''K2PdCl6 potassium hexachloropalladate(IV) \n''OPd·xH2O palladium(II)oxide hydrate \n''Pd(OH)2 palladium hydroxide on carbon \n''PdSO4 palladium(II)sulfate \n''Pd(NH3)2Br2 diamminedibromopalladium(II) \n''Pd(NH3)4Br2 tetraamminepalladium(II)bromide \n''NCSPd+ palladium(II) thiocyanate \n''(CF3COO)2Pd palladium(II)trifluoroacetate \n''[(C4H7)PdCl]2 (2-methylallyl)palladium(II)chloride dimer \n''Pd(C2H3O2)2 palladium(II) acetate \n''C6H10Cl2Pd2 allylpalladium chloride dimer \n''(C2H5CO2)2Pd palladium(II)propionate \n''C7H8Cl2Pd (bicyclo[2.2.1]hepta-2,5-diene)dichloropalladium(II) \n''C8H12Cl2Pd dichloro(1,5-cyclooctadiene)palladium(II) \n''Pd(C5H7O2)2 palladium(II)acetylacetonate \n''C12H12O8Pd [1,2,3,4-tetrakis(methoxycarbonyl)-1,3-butadiene-1,4-diyl]palladium(II) \n''C24H54P2Pd bis(tri-tert-butylphosphine)palladium(0) \n''Pd(C6H5CH=CHCOCH=CHC6H5)2 bis(dibenzylideneacetone)palladium \n''C36H44N4Pd 2,3,7,8,12,13,17,18-octaethyl-21H,23 H-porphine palladium(II) \n''C42H44O10Pd bis(3,5,3',5'-dimethoxydibenzylideneacetone)palladium(0) \n''(C6H5CH=CHCOCH=CHC6H5)3Pd2 tris(dibenzylideneacetone)dipalladium(0) \n''[(C6H5)2PCH2CH2P(C6H5)2]2Pd bis[1,2-bis(diphenylphosphino)ethane]palladium(0) \n''[(C6H5)2PCH3]4Pd tetrakis(methyldiphenylphosphine)palladium(0) \n''Pd[(C6H5)3P]4 tetrakis(triphenylphosphine)palladium(0) \n''Pd(NH3)2Cl2 trans-diamminedichloropalladium(II) \n''(NH4)2PdCl4 ammonium chloropalladite \n''[Pd(NH3)4](PdCl4) tetraamminepalladium(II)tetrachloropalladate(II) \n''(NH4)2PdCl6 ammonium hexachloropalladate(IV) \n''Pd(NO3)2·xH2O palladium nitrate \n''Pd(NH3)2I2 diamminediiodopalladium(II) \n''Pd(NH3)4(NO3)2 tetraamminepalladium(II)nitrate \n''K2Pd(NO2)4 potassium tetranitropalladate(II) \n''PdCl2·2H2O palladium(II) chloride dihydrate \n''Pd(H2NCH2CH2NH2)Cl2 (ethylenediamine)palladium(II)chloride \n''PdCl2·(CH3CN)2 bis(acetonitrile)dichloropalladium \n''Pd(NH3)4(CH3CO2)2 tetraamminepalladium(II)acetate \n''[(CH3)2NCH2CH2N(CH3)2]PdCl2 dichloro(N,N,N,N-tetramethylethylenediamine)palladium(II) \n''Pd(C5HF6O2)2 palladium(II)hexafluoroacetylacetonate \n''C10H8Cl2N2Pd (2,2'-bipyridine)dichloropalladium(II) \n''C12H8Cl2N2Pd dichloro(1,10-phenanthroline)palladium(II) \n''[(C2H5)3P]2PdCl2 dichlorobis(triethylphosphine)palladium(II) \n''(C6H5CN)2PdCl2 bis(benzonitrile)palladium(II) chloride \n''[C6H5P(CH3)2]2PdCl2 cis-dichlorobis(dimethylphenylphosphine)palladium(II) \n''C18H24Cl2N2Pd2 di-μ-chlorobis[2-[(dimethylamino)methyl]phenyl-C,N]dipalladium(II) \n''C22H29O2PPd 2-(2'-di-tert-butylphosphine)biphenylpalladium(II)acetate \n''C24H29ClN2Pd allyl[1,3-bis(mesityl)imidazol-2-ylidene]palladium chloride \n''[(C6H5)2PCH2CH2P(C6H5)2]PdCl2 [1,2-bis(diphenylphosphino)ethane]dichloropalladium(II) \n''[(C6H5)2PCH3]2PdCl2 dichlorobis(methyldiphenylphosphine)palladium(II) \n''C30H42ClN2Pd allyl[1,3-bis(2,6-diisopropylphenyl)imidazol-2-ylidene]palladium(II)chloride \n''[(C6H5)3P]2PdBr2 trans-dibromobis(triphenylphosphine)palladium(II) \n''[(C6H5)3P]2PdCl2 bis(triphenylphosphine)palladium(II)dichloride \n''[(C6H11)3P]2PdCl2 dichlorobis(tricyclohexylphosphine)palladium(II) \n''[(C6H5)3P]2Pd(CH3COO)2 bis(triphenylphosphinepalladium(II)) acetate \n''[(CH3C6H4)3P]2PdCl2 dichlorobis(tri-o-tolylphosphine)palladium(II) \n''[C10H6P(C6H5)2]2PdCl2 [(R)-(+)-2,2'-bis(diphenylphosphino)-1,1'-binaphthyl]palladium(II)chloride \n''(C6H5CH=CHCOCH=CHC6H5)3Pd2·CHCl3 tris(dibenzylideneacetone)dipalladium(0)-chloroform adduct \n''C62H60N4O4Pd2 1,3-bis(2,4,6-trimethylphenyl)imidazol-2-ylidene(1,4-naphthoquinone)palladium(0)dimer \n''Pd(NH3)4Cl2·H2O tetraamminepalladium(II) chloride monohydrate \n''Li2PdCl4·xH2O lithium tetrachloropalladate(II)hydrate \n''Na2PdCl6·4H2O sodium hexachloropalladate(IV)tetrahydrate \n''K2Pd(S2O3)2·H2O palladium(II)potassium thiosulfate monohydrate \n''[Pd(C4H9)3PBr]2 bromo(tri-tert-butylphosphine)palladium(I)dimer \n''2(C8H8ClNO2) di-μ-chlorobis[5-hydroxy-2-[1-(hydroxyimino-κN)ethyl]phenyl-κC]palladium(II)dimer \n''C26H16Cl6N2O2Pd2 di-μ-chlorobis[5-chloro-2-[(4-chlorophenyl)(hydroxyimino-κN)methyl]phenyl-κC]palladium dimer \n''C8H9OPdBr·(C6H5)3P bromo[(2-(hydroxy-κO)methyl)phenylmethyl-κC](triphenylphosphine)palladium(II) \n''C32H56Cl2N2P2Pd bis(di-tert-butyl(4-dimethylaminophenyl)phosphine)dichloropalladium(II) \n''C35H30Cl4FeP2Pd [1,1'-bis(diphenylphosphino)ferrocene]dichloropalladium(II) \n''C82H72O6N2Co2Pd2 (R)-(-)-COP-Oac catalyst \n''C82H72O6N2Co2Pd2 (S)-(+)-COP-Oac catalyst \n''C26H28Cl2FeNPPd dichloro[(S)-N,N-dimethyl-1-[(R)-2-(diphenylphosphino)ferrocenyl]ethylamine]palladium(II) \n''C40H34BrNO2P2Pd bromo(N-succinimidyl)bis(triphenylphosphine)palladium(II) \n''Pd(P(C6H4SO3·Na)3)3·9H2O tris(3,3,3-phophinidynetris(benzenesulfonato)palladium(0)nonasodium salt C78H66Cl2Co2N2O2Pd2 (S)-(+)-COP-cl catalyst \n'""", '46', '106.40')
        self.colorPd=colorPd="burlywood2"
        self.Pd = tk.Button(self, text=Pd[0], width=5, height=2, bg=colorPd, font=10, borderwidth=3,
                           command=lambda text=Pd: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPd, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Pd()])
        self.Pd.grid(row=7, column=11)

        Pt = ('Pt', 'Platinum', """'Pt platinum \n''PtBr2 platinum(II) bromide \n''PtCl2 platinum(II)chloride \n''PtCl4 platinum(IV) chloride \n''F4Pt platinum(IV) fluoride \n''F6Pt-2 platinum(VI) fluoride \n''PtI2 platinum(II) iodide \n''I4Pt platinum(IV) iodide \n''OPt platinum(II) oxide \n''PtO2 platinum(IV) oxide \n''PtBr3 platinum(III) bromide \n''PtBr4 platinum(IV) bromide \n''PtCl3 platinum(III) chloride \n''PtRh platinum/rhodium alloy \n''PtS platinum(II) sulfide \n''PtS2 platinum(IV)sulfide \n''PtSi platinum silicide \n''K2PtBr4 potassium tetrabromoplatinate(II) \n''H2PtBr6·xH2O hydrogen hexabromoplatinate(IV)hydrate \n''K2PtBr6 potassium hexabromoplatinate(IV) \n''Pt(CN)2 platinum(II)cyanide \n''C5H4CH3Pt(CH3)3 trimethyl(methylcyclopentadienyl)platinum(IV) \n''C10H18Pt (1,5-cyclooctadiene)dimethylplatinum(II) \n''K2PtCl4 potassium tetrachloroplatinate \n''K2PtCl6 potassium hexachloroplatinate \n''K2PtCl6 potassium chloroplatinate \n''PtO2·H2O platinum(IV)oxide monohydrate \n''H2Pt(OH)6 dihydrogen hexahydroxyplatinate(IV) \n''K2PtI6 potassium hexaiodoplatinate(IV) \n''(NH4)2PtBr6 ammonium hexabromoplatinate \n''C4BaN4Pt barium tetracyanoplatinate \n''K2Pt(CN)4 potassium tetracyanoplatinate(II) \n''K2Pt(CN)6 potassium hexacyanoplatinate(IV) \n''C8H12Br2Pt dibromo(1,5-cyclooctadiene)platinum(II) \n''C8H12Cl2Pt dichloro(1,5-cyclooctadiene)platinum(II) \n''C8H8I2Pt (1,5-cyclooctadiene)diiodoplatinum(II) \n''Pt(C5H7O2)2 platinum(II)acetylacetonate \n''C36H44N4Pt platinum octaethylporphyrin \n''[(C6H5)3P]2Pt(H2C=CH2) ethylenebis(triphenylphosphine)platinum(0) \n''Pt[(C6H5)3P]4 tetrakis(triphenylphosphine)platinum \n''Pt(NH3)2Cl2 cisplatin \n''Pt(NH3)2Cl2 trans-platinum(II)diammine dichloride \n''(NH4)2PtCl4 ammonium tetrachloroplatinate(II) \n''[Pt(NH3)4](PtCl4) tetraammineplatinum(II)tetrachloroplatinate(II) \n''H2PtCl6 chloroplatinic acid \n''H2PtCl6·aq chloroplatinic acid hydrate \n''(NH4)2PtCl6 ammonium hexachloroplatinate(IV) \n''Cl6H14O6Pt chloroplatinic acid hexahydrate \n''Pt(NH3)2(NO2)2 diamminedinitritoplatinum(II) \n''H8N2PtS15 ammonium tris(pentasulfido)platinate(IV) \n''K2Pt(OH)6 potassium hexahydroxoplatinate \n''Na2Pt(OH)6 sodium hexahydroxyplatinate(IV) \n''(NH3)4Pt(NO3)2 tetraammineplatinum(II) nitrate \n''Pt(NH3)4(OH)2·xH2O tetraammineplatinum(II)hydroxide hydrate \n''K2Pt(NO2)4 potassium tetranitroplatinate(II) \n''C2H4Cl3KPt potassium trichloroethyleneplatinate \n''(H2NCH2CH2NH2)PtCl2 dichloro(ethylenediamine)platinum(II) \n''C2H14N4O6Pt tetraammineplatinum(II)hydrogencarbonate \n''K2Pt(C2O4)2·2H2O potassium bis(oxalato)platinate(II)dihydrate \n''(CH3CN)2PtCl2 cis-bis(acetonitrile)dichloroplatinum(II) \n''C4H12Cl2PtSe2 cis-dichlorobis(dimethylselenide)platinum(II) \n''(H2NCH2CH2NH2)2PtCl2 dichlorobis(ethylenediamine)platinum(II) \n''[C6H10(NH2)2]PtCl2 dichloro(1,2-diaminocyclohexane)platinum(II) \n''C6H12N2O4Pt carboplatin \n''C8H14N2O4Pt oxaliplatin \n''O[Si(CH3)2CH=CH2]2Pt platinum(0)-1,3-divinyl-1,1,3,3-tetramethyldisiloxane complex \n''[(C2H5)2S]2PtCl2 cis-dichlorobis(diethyl sulfide)platinum(II) \n''C10H8Cl2N2Pt (2,2'-bipyridine)dichloroplatinum(II) \n''C10H10Cl2N2Pt cis-dichlorobis(pyridine)platinum(II) \n''C12H8Cl2N2Pt dichloro(1,10-phenanthroline)platinum(II) \n''C12H24O4PtSi4 platinum(0)-2,4,6,8-tetramethyl-2,4,6,8-tetravinyl-1,3,5,7,2,4,6,8-tetraoxatetrasilocane \n''[(C2H5)3P]2PtCl2 cis-dichlorobis(triethylphosphine)platinum(II) \n''[(C2H5)3P]2PtCl2 trans-dichlorobis(triethylphosphine)platinum(II) \n''(C6H5CN)2PtCl2 cis-bis(benzonitrile)dichloroplatinum(II) \n''((CH3(CH2)3)4N)2PtCl6 tetrabutylammonium hexachloroplatinate(IV) \n''[(C6H5)3P]2PtCl2 cis-dichlorobis(triphenylphosphine)platinum(II) \n''[(C6H5)3P]2PtCl2 trans-dichlorobis(triphenylphosphine)platinum(II) \n''Pt(NH3)4Cl2·xH2O tetraammineplatinum(II)chloride hydrate \n''KPt(NH3)Cl3 potassium aminetrichloroplatinate(II) \n''Na2PtCl4·xH2O sodium tetrachloroplatinate(II)hydrate \n''Na2PtCl6·6H2O sodium hexachloroplatinate hexahydrate \n''Na2PtBr6·6H2O sodium hexabromoplatinate(IV) hexahydrate \n''Na2PtCl4·4H2O sodium tetraehloroplatinate(II) tetrahydrate \n''K[(H2C=CH2)PtCl3]·xH2O potassium trichloro(ethylene)platinate(II)hydrate \n''BaPt(CN)4·xH2O barium tetracyanoplatinate(II)hydrate \n''K2Pt(CN)4·xH2O potassium tetracyanoplatinate(II)hydrate \n''C4Li2N4Pt·xH2O lithium tetracyanoplatinate(II)hydrate \n''C4N4Na2Pt·xH2O sodium tetracyanoplatinate(II)hydrate \n''C4H8BaN4O4Pt barium tetracyanoplatinate(II) tetrahydrate \n''C6H14N2O4PtSe platinum, [rel-(1R,2R)-1,2-cyclohexanediamine-kN,kN'][selenato(2-)-kO,kO']-, (sP-4-2)- \n''C15H11Cl2N3Pt·2H2O dichloro(2,2:6,2-terpyridine)platinum(II)dihydrate \n'""", '78', '195.09')
        self.colorPt=colorPt="burlywood3"
        self.Pt = tk.Button(self, text=Pt[0], width=5, height=2, bg=colorPt, font=10, borderwidth=3,
                           command=lambda text=Pt: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPt, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Pt()])
        self.Pt.grid(row=8, column=11)
        
        Ds = ('Ds', 'Darmstadtium', """'Ds darmstadtium darmstadtium metal\n'""", '110', '281')
        self.colorDs=colorDs="burlywood4"
        self.Ds = tk.Button(self, text=Ds[0], width=5, height=2, bg=colorDs, font=10, borderwidth=3,
                           command=lambda text=Ds: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorDs, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ds()])
        self.Ds.grid(row=9, column=11)


        Cu = ('Cu', 'Copper', """'Cu copper \n''CuBr copper(I) bromide \n''CuBr2 cupric bromide \n''CuCl cuprous chloride \n''CuCl2 copper(II)chloride \n''CuC2 copper(II) acetylide \n''CuF copper(I) fluoride \n''CuF2 cupric fluoride \n''CuH copper(I) hydride \n''CuI cuprous iodide \n''CuN3 copper(I) azide \n''CuN6 copper(II) azide \n''CuO cupric oxide \n''CuP2 copper phosphide \n''CuS cupric sulfide \n''CuSe cupric selenide \n''CuSn copper-tin alloy \n''CuTe copper(II) telluride \n''CuTi titanium-copper alloy \n''Cu2C2 copper(I) acetylide \n''Cu2Se copper(I) selenide \n''Cu2Te copper(I) telluride \n''Cu3As copper arsenide \n''Cu3N copper nitride \n''Cu3Sb copper antimonide \n''Cu5Si copper silicide \n''AlCuZn devarda’s alloy \n''CuAl2O4 copper aluminum oxide \n''Cu3(AsO4)2 copper(II) arsenate \n''B2CuF8 borate(1-), tetrafluoro-, copper(2+) (2:1) \n''Li2CuBr4 dilithium tetrabromocuprate(II) \n''CuCN cuprous cyanide \n''Cu13CN copper(I)cyanide-13 C \n''CuC15N copper(I)cyanide-13 C,15 N \n''CuC15N copper(I)cyanide-15 N \n''CuCO3 copper(II) carbonate \n''C2CuN2 copper dicyanide \n''C2CuN2 cupric cyanide \n''CuC2O4 copper(II) oxalate \n''Cl2CuO6 copper chlorate hexahydrate \n''Cl2CuO8 copper(II) perchlorate \n''Li2CuCl4 dilithium tetrachlorocuprate(II) \n''CrCuO4 copper chromate \n''2CuO·Cr2O3 copper chromite \n''Cu(BO2)2 copper(II) barate \n''CuCr2O4 copper(II) chromite \n''CuFeS2 copper(II) ferrous sulfide \n''CuFe2O4 copper iron oxide \n''Cu(OH)2 copper hydroxide \n''Cu(OH)2 copper(II)hydroxide \n''CuIO3 copper iodate \n''CuI2O6 copper(II) iodate \n''CuMoO4 copper(II)molybdate \n''Cu(NO3)2 copper(II) nitrate \n''Cu(NbO3)2 copper(II)niobate \n''CuO3Te copper(II) tellurite \n''CuO3Ti copper(II) titanate \n''Cu3(PO4)2 copper phosphate \n''CuSO4 copper(II) sulfate \n''CuSeO4 copper(II) selenate \n''CuTeO4 copper(II) tellurate \n''CuWO4 copper(II) tungstate \n''CuSnO3 copper(II) stannate \n''Cu(VO3)2 copper(II) vanadate \n''Cu2S copper(I)sulfide \n''Cu2O copper(I)oxide \n''Cu2HgI4 copper(I) mercury iodide \n''Cu2O3S copper(I) sulfite monohydrate \n''Cu3(PO4)2 copper(II) phosphate \n''AsCuHO3 copper(II) arsenite \n''OC(OCuOH)2 dicopper(II) carbonate dihydroxide \n''Cu(OCH3)2 copper(II)methoxide \n''K[Cu(CN)2] potassium cuprocyanide \n''C2H2CuO4 cupric formate \n''CuCO2CH3 copper(I)acetate \n''(HCO2)2Cu·xH2O copper(II)formate hydrate \n''Na2[Cu(CN)3] sodium cuprocyanide \n''Cu[-CH(OH)CO2]2·xH2O copper(II)tartrate hydrate \n''Cu(CO2CH3)2 copper(II)acetate \n''Cu(CO2CH3)2·xH2O copper(II)acetate hydrate \n''Cu(CO2CH3)2·H2O copper(II) acetate monohydrate \n''CH3(CH2)3SCu copper(I)1-butanethiolate \n''[Cu(NHCH2CH2NH)2]+2 bis(ethylenediamine)copper(2+) \n''K[Cu(CN)2]·K3[Cu(CN)4] potassium cyanocuprate(I) \n''C8H14CuO4 copper(II) butanoate monohydrate \n''[CH3(CH2)3CH(C2H5)CO2]2Cu copper(II)2-ethylhexanoate \n''Cu(C5H7O2)2 copper(II)acetylacetonate \n''C12H18CuO6 copper(II) ethylacetoacetate \n''C12H22CuO14 copper(II) gluconate \n''C16H34Cu2N4 (N,N'-diisopropylacetamidinato)copper(I) \n''C20H18CuO4 copper(II) benzoylacetonate \n''[C6H11(CH2)3CO2]2Cu copper bis(4-cyclohexylbutyrate) \n''Cu(OCC(CH3)3CHCOC(CH3)3)2 copper bis(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''C25H24CuP (ethylcyclopentadienyl)(triphenylphosphine)copper(I) \n'""", '29', '63.55')
        self.colorCu=colorCu="thistle1"
        self.Cu = tk.Button(self, text=Cu[0], width=5, height=2, bg=colorCu, font=10, borderwidth=3,
                           command=lambda text=Cu: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCu, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cu()])
        self.Cu.grid(row=6, column=12)

        Ag = ('Ag', 'Silver', """'Ag silver \n''AgBr silver bromide \n''AgCl silver chloride \n''AgF silver fluoride \n''AgF2 silver difluoride \n''AgI silver(I) iodide \n''AgN3 silver azide \n''AgO silver(II) oxide \n''AgO silver oxide \n''Ag2C2 silver(I) acetylide \n''Ag2F silver subfluoride \n''Ag2Se silver selenide \n''Ag2Te silver telluride \n''AgAsF6 silver hexafluoroarsenate(V) \n''AgBF4 silver tetrafluoroborate \n''AgClO2 silver(I) chlorite \n''AgClO3 silver chlorate \n''AgClO4 silver perchlorate \n''AgHF2 silver(I)hydrogenfluoride \n''AgPF6 silver hexafluorophosphate \n''AgSbF6 silver(I) hexafluoroantimonate \n''AgIO3 silver iodate \n''AgNO2 silver nitrite \n''AgNO3 silver nitrate \n''AgO3P silver(I) metaphosphate \n''AgReO4 silver(I)perrhenate \n''Ag2CrO4 silver(I) chromate \n''Ag2Cr2O7 silver(I) dichromate \n''Ag2S silver(I) sulfide \n''Ag2O silver(I)oxide \n''Ag2HgI4 silver(I) tetraiodomercurate(II) \n''Ag2MoO4 silver molybdate \n''Ag2SO3 silver(I)sulfite \n''Ag2SO3 silver sulfite \n''Ag2O3Se silver(I) selenite \n''Ag2SO4 silver sulfate \n''Ag2WO4 silver tungstate \n''Ag2S2O3 silver(I) thiosulfate \n''Ag2SeO4 silver(I) selenate \n''Ag3AsO4 silver arsenate \n''Ag3PO4 silver phosphate \n''AgCN silver cyanide \n''Ag13C15N silver cyanide-13 C,15 N \n''Ag2C2O4 silver oxalate \n''C2Ag2O4 silver(I) oxalate \n''C2HAg silver acetylide \n''AgBrO3 silver bromate \n''AgClO4·xH2O silver perchlorate hydrate \n''AgClO4·H2O silver perchlorate monohydrate \n''AgMnO4 silver(I)permanganate \n''AgVO3 silver vanadium trioxide \n''CAgNO silver fulminate \n''Ag213CO3 silver carbonate-13 C \n''Ag2CO3 silver(I) carbonate \n''K[Ag(CN)2] potassium silver cyanide \n''CH3COOAg silver acetate \n''CH3CH(OH)COOAg silver lactate \n''[CH3COCH=C(O)CH3]Ag silver acetylacetonate \n''C6H5Ag3O7 silver(I) citrate \n''AgO2CCH2C(OH)(CO2Ag)CH2CO2Ag·xH2O silver citrate hydrate \n''CO2C6H5CO2Ag silver benzoate \n''C6H11(CH2)3CO2Ag silver cyclohexanebutyrate \n''CF3SO3Ag silver trifluoromethanesulfonate \n''AgOCN silver(I) cyanate \n''AgSCN silver(I) thiocyanate \n''AgSO3CH3 silver methylsulfonate \n''CF3COOAg silver trifluoroacetate \n''C2F5CO2Ag silver pentafluoropropionate \n''CF3CF2CF2CO2Ag silver heptafluorobutyrate \n''C5H10AgNS2 silver(I) diethyldithiocarbamate \n''CH3C6H4SO3Ag silver p-toluenesulfonate \n'""", '47', '107.97')
        self.colorAg=colorAg="thistle2"
        self.Ag = tk.Button(self, text=Ag[0], width=5, height=2, bg=colorAg, font=10, borderwidth=3,
                           command=lambda text=Ag: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAg, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ag()])
        self.Ag.grid(row=7, column=12)

        Au = ('Au', 'Gold', """'Au gold \n''AuBr3·xH2O gold(III) bromide \n''AuCl gold(I)chloride \n''AuCl3 gold(III)chloride \n''AuF3 gold(III) fluoride \n''AuI gold(I) iodide \n''AuI3 gold(III)iodide \n''Au2O3·xH2O gold(III) oxide \n''Au2S3 gold(III) sulfide \n''Au2Se3 gold(III) selenide \n''AuBr4H gold tetrabromide, acid \n''KAuBr4 potassium tetrabromoaurate(III) \n''HAuCl4·xH2O gold(III) chloride hydrate \n''HAuCl4·3H2O gold(III) chloride trihydrate \n''AuCl4Li lithium tetrachloroaurate(III) \n''AuCl4Na sodium gold chloride \n''Au(OH)3 gold(III)hydroxide \n''Au2S gold(I)sulfide \n''Au2(SeO4)3 gold(III) selenate \n''AuCN gold cyanide \n''KAuCl4 potassium gold(III)chloride \n''AuCl3·HCl gold(III) chloride monohydrochloride \n''KAu(CN)2 potassium dicyanoaurate(I) \n''NaAu(CN)2 sodium dicyanoaurate \n''C6H20AuP2+2 leach residues, zinc refining flue dust, cadmium thallium ppt. \n''Au(CN)3·3H2O gold(III) cyanide trihydrate \n''NaAuCl4·xH2O sodium tetrachloroaurate(III)hydrate \n''NH4AuCl4·xH2O ammonium tetrachloroaurate(III)hydrate \n''(CH3)2SAuCl chloro(dimethylsulfide)gold(I) \n''(CH3)3PAuCl chloro(trimethylphosphine)gold(I) \n''C5H5AuCl3N trichloro(pyridine)gold(III) \n''C6H11AuO5S aurothioglucose \n''(C2H5)3PAuCl chloro(triethylphosphine)gold(I) \n''C8H16Au2CdN8 bis(ethylenediamine)cadmium(II) bis[dicyanoaurate(1-)] \n''C10H20Au2CdN8 bis(Propane-1,2-diyldiamine-N,N')cadmium(II) bis[bis(cyano-c)aurate(1-)] \n''[(C6H5)3P]AuCl chloro(triphenylphosphine)gold(I) \n''C20H27AuClP (2-biphenyl)di-tert-butylphosphine gold(I)chloride \n''HAuBr4·xH2O hydrogen tetrabromoaurate(III) \n''NaAuBr4·xH2O sodium tetrabromoaurate(III)hydrate \n'""", '79', '196.97')
        self.colorAu=colorAu="thistle3"
        self.Au = tk.Button(self, text=Au[0], width=5, height=2, bg=colorAu, font=10, borderwidth=3,
                           command=lambda text=Au: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAu, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Au()])
        self.Au.grid(row=8, column=12)

        Rg = ('Rg', 'Roentgenium', """'Rg roentgenium roentgenium metal\n'""", '111', '282')
        self.colorRg=colorRg="thistle4"
        self.Rg = tk.Button(self, text=Rg[0], width=5, height=2, bg=colorRg, font=10, borderwidth=3,
                           command=lambda text=Rg: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRg, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Rg()])
        self.Rg.grid(row=9, column=12)

        Zn = ('Zn', 'Zinc', """'Zn zinc \n''ZnBr2 zinc bromide \n''ZnCl2 zinc chloride \n''ZnF2 zinc fluoride \n''ZnI2 zinc iodide \n''ZnO zinc oxide \n''ZnO2 zinc peroxide \n''ZnS zinc sulfide \n''ZnSe zinc selenide \n''ZnTe zinc telluride \n''ZnSb zinc antimonide \n''AlCuZn devarda’s alloy \n''ZnAs2O4 zinc arsenite \n''Zn3(AsO4)2 zinc arsenate \n''Zn(BH4)2 zinc borohydride \n''Br2O6Zn zinc bromate \n''ZnCO3 zinc carbonate \n''(CH3)2Zn dimethyl zinc \n''Zn(CN)2 zinc cyanide \n''ZnC2O4 zinc oxalate \n''(C2H5)2Zn diethylzinc \n''ZnC2O4·xH2O zinc oxalate hydrate \n''Zn(CH(CH3)2)2 diisopropyl zinc \n''(C6F5)2Zn bis(pentafluorophenyl)zinc \n''(C6H5)2Zn diphenylzinc \n''CdS2Zn cadmium primrose \n''CdS2Zn cadmium sulfide mixed with zinc sulfide (8:92) \n''Zn(ClO3)2 zinc chlorate \n''ZnCrO4 zinc chromate \n''ZnCr2O7 zinc dichromate \n''F6SiZn zinc silicofluoride \n''Zn(OH)2 zinc hydroxide \n''ZnO·xH2O zinc oxide hydrate \n''ZnIO3 zinc iodate \n''ZnMoO4 zinc molybdate \n''Zn(NbO3)2 zinc niobate \n''Zn2TiO4·Zn2TiO2 zinc titanate \n''ZnSO4 zinc sulfate \n''ZnS2O4 zinc dithionite \n''Zn3(PO4)2 zinc phosphate \n''AsH3O5Zn arsenic acid, zinc salt (1:1), monohydrate \n''ZnBr2·2H2O zinc bromide dihydrate \n''CH3ZnCl methylzinc chloride \n''(CH3)2CHZnBr 2-propylzinc bromide \n''CH3CH2CH2ZnBr propylzinc bromide \n''(CH3CO2)2Zn zinc acetate \n'CH3(CH2)3ZnBr butylzinc bromide \n''(CH3)2CHCH2ZnBr isobutylzinc bromide \n''C2H5CH(CH3)ZnBr sec-butylzinc bromide \n''(CH3)3CZnBr tert-butylzinc bromide \n''Zn(CH3COO)2·2H2O zinc acetate dihydrate \n''C4K2N4Zn potassium tetracyanozincate \n''H2C=CH(CH2)3ZnBr 4-pentenylzinc bromide \n''C5H9ZnBr cyclopentylzinc bromide \n''C2H5C(CH3)2ZnBr 1,1-dimethylpropylzinc bromide \n''(C2H5)2CHZnBr 1-ethylpropylzinc bromide \n''CH3CH2CH2CH(CH3)ZnBr 1-methylbutylzinc bromide \n''(CH3)2CHCH2CH2ZnBr 3-methylbutylzinc bromide \n''CH3(CH2)4ZnBr pentylzinc bromide \n''C6H5ZnBr phenylzinc bromide \n''C6H5ZnI phenylzinc iodide \n''(H2C=CHCO2)2Zn zinc acrylate \n''H2C=CH(CH2)4ZnBr 5-hexenylzinc bromide \n''C6H11ZnBr cyclohexylzinc bromide \n''CH3CH2CH2CH(C2H5)ZnBr 1-ethylbutylzinc bromide \n''CH3(CH2)3CH(CH3)ZnBr 1-methylpentylzinc bromide \n''(C2H5)2CHCH2ZnBr 2-ethylbutylzinc bromide \n''CH3(CH2)5ZnBr hexylzinc bromide \n''Cl2C6H3CH2ZnCl 2,6-dichlorobenzylzinc chloride \n''BrC6H4CH2ZnBr 2-bromobenzylzinc bromide \n''BrC6H4CH2ZnBr 4-bromobenzylzinc bromide \n''ClC6H4CH2ZnCl 2-chlorobenzylzinc chloride \n''ClC6H4CH2ZnCl 3-chlorobenzylzinc chloride \n''ClC6H4CH2ZnCl 4-chlorobenzylzinc chloride \n''C6H5CH2ZnBr benzylzinc bromide \n''CH3C6H4ZnI 2-methylphenylzinc iodide \n''CH3C6H4ZnI 3-methylphenylzinc iodide \n''CH3C6H4ZnI 4-methylphenylzinc iodide \n''C7H11ZnBr exo-2-norbornylzinc bromide \n''C6H11CH2ZnBr (cyclohexylmethyl)zinc bromide \n''CH3(CH2)3CH(C2H5)ZnBr 1-ethylpentylzinc bromide \n''CH3(CH2)4CH(CH3)ZnBr 1-methylhexylzinc bromide \n''(CH3CH2CH2)2CHZnBr 1-propylbutylzinc bromide \n''CH3(CH2)6ZnBr heptylzinc bromide \n''H2C=C(C6H5)ZnBr 1-phenylvinylzinc bromide \n''C6H5CH(CH3)ZnBr α-methylbenzylzinc bromide \n''C6H5CH2CH2ZnBr phenethylzinc bromide \n''CH3C6H4CH2ZnCl 2-methylbenzylzinc chloride \n''CH3C6H4CH2ZnCl 3-methylbenzylzinc chloride \n''CH3C6H4CH2ZnCl 4-methylbenzylzinc chloride \n''(CH3)2C6H3ZnI 2,3-dimethylphenylzinc iodide \n''(CH3)2C6H3ZnI 2,4-dimethylphenylzinc iodide \n''(CH3)2C6H3ZnI 2,5-dimethylphenylzinc iodide \n''(CH3)2C6H3ZnI 2,6-dimethylphenylzinc iodide \n''C2H5C6H4ZnI 2-ethylphenylzinc iodide \n''(CH3)2C6H3ZnI 3,4-dimethylphenylzinc iodide \n''(CH3)2C6H3ZnI 3,5-dimethylphenylzinc iodide \n''C2H5C6H4ZnI 4-ethylphenylzinc iodide \n''[H2C=C(CH3)CO2]2Zn zinc methacrylate \n''CH3(CH2)3CH(C2H5)CH2ZnBr 2-ethylhexylzinc bromide \n''(CH3)2CHC6H4ZnI 2-isopropylphenylzinc iodide \n''(CH3)2CHC6H4ZnI 4-isopropylphenylzinc iodide \n''C10H7ZnI 1-naphthylzinc iodide \n''C10H14O4Zn zinc 2,4-pentanedioate \n''C10H15BrZn 1-adamantylzinc bromide \n''C10H15BrZn 2-adamantylzinc bromide \n''Zn(C5H7O2)2·xH2O zinc acetylacetonate hydrate \n''C10H7CH2ZnBr (2-naphthylmethyl)zinc bromide \n''CH3(CH2)4C6H4ZnI 4-pentylphenylzinc iodide \n''[H2C=CH(CH2)8CO2]2Zn zinc undecylenate \n''Zn(SC6Cl5)2 zinc chlorothiophenolate \n''C6H5C6H4ZnBr 4-biphenylzinc bromide \n''(C2H5O2CCH=CHCO2)2Zn fumaric acid monoethyl ester zinc salt \n''(C6H5O7)2Zn3·2H2O zinc citrate dihydrate \n''C12H19ZnBr 3,5-dimethyl-1-adamantylzinc bromide \n''C6H5C6H4CH2ZnBr (2-biphenylylmethyl)zinc bromide \n''Zn(C8H15O2)2 zinc caprylate \n''C17H14N8Zn bis(5-amidino-benzimidazolyl)methane zinc \n''Zn(C11H7O2)2 zinc naphthenate \n''Zn(OCC(CH3)3CHCOC(CH3)3)2 bis(2,2,6,6-tetramethyl-3,5-heptanedionato)zinc(II) \n''C24H46O4Zn zinc laurate \n''[[(CH3)3C]2C6H2(OH)CO2]2Zn zinc 3,5-di-tert-butylsalicylate \n''C32F16N8Zn zinc 1,2,3,4,8,9,10,11,15,16,17,18,22,23,24,25-hexadecafluoro-29H,31 H-phthalocyanine \n''C32H16N8Zn zinc phthalocyanine \n''C36H44N4Zn 2,3,7,8,12,13,17,18-octaethyl-21H,23 H-porphine zinc(II) \n''C36H66O4Zn zinc oleate \n''[CH3(CH2)16COO]2Zn zinc stearate \n''C40H24N8Zn zinc 5,10,15,20-tetra(4-pyridyl)-21H,23 H-porphine \n''C44H28N4Zn 5,10,15,20-tetraphenyl-21H,23 H-porphine zinc \n''C48H48N8Zn zinc 2,9,16,23-tetra-tert-butyl-29H,31 H-phthalocyanine \n''C64H56N8Zn zinc 2,11,20,29-tetra-tert-butyl-2,3-naphthalocyanine \n''Zn(ClO4)2·6H2O zinc perchlorate hexahydrate \n''ZnCl2·2NH4Cl ammonium zinc chloride (NH4)2ZnCl4 \n''CuZnFe4O4 copper zinc iron oxide \n''Fe2O4Zn zinc iron oxide \n''ZnSeO3 zinc selenite \n''H2O5SZn zinc sulfate monohydrate \n''ZnSO3·2H2O zinc sulfite dihydrate \n''Zn(NO3)2·xH2O zinc nitrate hydrate \n''ZnSO4·7H2O zinc sulfate heptahydrate \n''(NH4)3ZnCl5 ammonium pentachlorozincate \n''ZnF2·4H2O zinc fluoride tetrahydrate \n''3ZnO·2B2O3 zinc barate \n''Zn(BF4)2·xH2O zinc tetrafluoroborate hydrate \n''(CF3SO3)2Zn zinc trifluoromethanesulfonate \n''NCCH2CH2ZnBr 2-cyanoethylzinc bromide \n''C4H2Br2SZn 5-bromo-2-thienylzinc bromide \n''C4H3SZnBr 2-thienylzinc bromide \n''C4H3ISZn 3-thienylzinc iodide \n''Zn(CF3COO)2·xH2O zinc trifluoroacetate hydrate \n''NC(CH2)3ZnBr 3-cyanopropylzinc bromide \n''C4H6N2S4Zn zineb \n''Cl(CH2)4ZnBr 4-chlorobutylzinc bromide \n''C5H4NZnBr 2-pyridylzinc bromide \n''C5H5BrSZn 3-methyl-2-thienylzinc bromide \n''NC(CH2)4ZnBr 4-cyanobutylzinc bromide \n''C5H8N2S4Zn propineb \n''C5H9BrO2Zn 2-(1,3-dioxolan-2-yl)]ethyl]zinc bromide \n''C2H5O2CCH2CH2ZnBr 3-ethoxy-3-oxopropylzinc bromide \n''CH3O2CCH(CH3)CH2ZnBr (R)-(+)-3-methoxy-2-methyl-3-oxopropylzinc bromide \n''CH3O2CCH(CH3)CH2ZnBr (S)-(-)-3-methoxy-2-methyl-3-oxopropylzinc bromide \n''Cl(CH2)5ZnBr 5-chloropentylzinc bromide \n''F2C6H3ZnBr 3,5-difluorophenylzinc bromide \n''Cl2C6H3ZnI 2,3-dichlorophenylzinc iodide \n''Cl2C6H3ZnI 2,4-dichlorophenylzinc iodide \n''Cl2C6H2ZnI 2,5-dichlorophenylzinc iodide \n''Cl2C6H3ZnI 3,4-dichlorophenylzinc iodide \n''Cl2C6H3ZnI 3,5-dichlorophenylzinc iodide \n''FC6H4ZnBr 4-fluorophenylzinc bromide \n''BrC6H4ZnI 3-bromophenylzinc iodide \n''BrC6H4ZnI 4-bromophenylzinc iodide \n''ClC6H4ZnI 2-chlorophenylzinc iodide \n''ClC6H4ZnI 3-chlorophenylzinc iodide \n''ClC6H4ZnI 4-chlorophenylzinc iodide \n''FC6H4ZnI 2-fluorophenylzinc iodide \n''FC6H4ZnI 3-fluorophenylzinc iodide \n''C6H5Cl2NZn (2-chloro-5-pyridyl)methylzinc chloride \n''CH3C5H3NZnBr 3-methyl-2-pyridylzinc bromide \n''CH3C5H3NZnBr 4-methyl-2-pyridylzinc bromide \n''CH3C5H3NZnBr 5-methyl-2-pyridylzinc bromide \n''CH3C5H3NZnBr 6-methyl-2-pyridylzinc bromide \n''C6H11BrO2Zn 2-(1,3-dioxan-2-yl)ethylzinc bromide \n''C2H5O2C(CH2)3ZnBr 4-ethoxy-4-oxobutylzinc bromide \n''Cl(CH2)6ZnBr 6-chlorohexylzinc bromide \n''C6H12Br2OZn3 nysted reagent \n''(CH3)2NCSSZnSCSN(CH3)2 ziram \n''[(CH3)2NCH2CH2N(CH3)2]ZnCl2 dichloro(N,N,N',N'-tetramethylethylenediamine)zinc \n''C6F5CH2ZnBr 2,3,4,5,6-pentafluorobenzylzinc bromide \n''C6F5CH2ZnCl 2,3,4,5,6-pentafluorobenzylzinc chloride \n''NCC6H4ZnBr 2-cyanophenylzinc bromide \n''NCC6H4ZnBr 4-cyanophenylzinc bromide \n''NCC6H4ZnI 3-cyanophenylzinc iodide \n''F2C6H3CH2ZnBr 2,4-difluorobenzylzinc bromide \n''F2C6H3CH2ZnBr 2,5-difluorobenzylzinc bromide \n''F2C6H3CH2ZnBr 3,4-difluorobenzylzinc bromide \n''F2C6H3CH2ZnBr 3,5-difluorobenzylzinc bromide \n''F2C6H3CH2ZnCl 2,5-difluorobenzylzinc chloride \n''ClC6H3(F)CH2ZnCl 2-chloro-6-fluorobenzylzinc chloride \n'""", '30', '65.37')
        self.colorZn=colorZn="CadetBlue1"
        self.Zn = tk.Button(self, text=Zn[0], width=5, height=2, bg=colorZn, font=10, borderwidth=3,
                           command=lambda text=Zn: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorZn, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Zn()])
        self.Zn.grid(row=6, column=13)

        Cd = ('Cd', 'Cadmium', """'Cd cadmium \n''CdBr2 cadmium bromide \n''CdCl2 cadmium chloride \n''CdCl2 cadmium chloride monohydrate \n''CdF2 cadmium fluoride \n''CdI2 cadmium iodide \n''CdO cadmium oxide \n''CdS cadmium sulfide \n''CdSb cadmium antimonide \n''CdSe cadmium selenide \n''CdTe cadmium telluride \n''Cd3P2 cadmium phosphide \n''Cd3(AsO4)2 cadmium arsenate \n''B2Cd3O6 cadmium borate \n''CdCO3 cadmium carbonate \n''C2CdN2 cadmium cyanide \n''CdC2O4 cadmiu oxalate \n''C2H6Cd dimethyl cadmium \n''C4H10Cd diethyl cadmium \n''CdCl2O8 perchloric acid, cadmium salt \n''CdF6Si cadmium fluosilicate \n''Cd(OH)2 cadmium hydroxide \n''Cd(IO3)2 cadmium iodate \n''Cd(NO2)2 cadmium nitrite \n''CdSO3 cadmium sulfite \n''CdO3Si cadmium metasilicate \n''CdO3Te cadmium tellurite \n''CdSeO4 cadmium selenate \n''CdTeO4 cadmium tellurate \n''CdS2Zn cadmium primrose \n''CdS2Zn cadmium sulfide mixed with zinc sulfide (8:92) \n''CdTiO3 cadmium titanate \n''Cd2Nb2O7 cadmium niobate \n''Cd3(PO4)2 cadmium phosphate \n''BiCdPbSn woods metal \n''CdBr2·4H2O cadmium bromide tetrahydrate \n''(HCO2)2Cd cadmium(II)formate \n''(CH3CO2)2Cd·xH2O cadmium acetate hydrate \n''C4CdK2N4 cadmium dipotassium tetracyanide \n''CdC4H4O4 cadmium succinate \n''C4H10CdO6 cadmium acetate dihydrate \n''C6H10CdO6 cadmium lactate \n''C10H18CdO4 cadmium divalerate \n''Cd(C2H7O2)2·xH2O cadmium acetylacetonate hydrate \n''C14H10CdO6 cadmium salicylate \n''C24H46CdO4 lauric acid, cadmium salt (2:1) \n''C32H16CdN8 cadmium phthalocyanine \n''C36H70CdO4 cadmium stearate \n''Cd(ClO4)2·xH2O cadmium perchlorate hydrate \n''CdCl2·2.5H2O cadmium chloride hemipentahydrate \n''CdCl2·xH2O cadmium chloride hydrate \n''CdMoO4 cadmium molybdate \n''CdZrO3 cadmium zirconium trioxide \n''CdWO4 cadmium tungstate \n''CdSO4·xH2O cadmium sulfate hydrate \n''CdSO4 cadmium sulfate \n''Cd(NO3)2·4H2O cadmium nitrate tetrahydrate \n''C6H7CdNO6 cadmium nitrilotriacetate \n''C6H10CdN2O4 [[N,N'-ethylenebis[glycinato]](2-)-N,N',O,O']cadmium \n''C6H12CdN2S4 cadmium bis(dimethyldithiocarbamate) \n''C8H16Au2CdN8 bis(ethylenediamine)cadmium(II) bis[dicyanoaurate(1-)] \n''C10H14CdN2O8 (ethylenedinitrilo)tetraacetic acid cadmium complex \n''C10H20Au2CdN8 bis(Propane-1,2-diyldiamine-N,N')cadmium(II) bis[bis(cyano-c)aurate(1-)] \n''C10H20CdN2S4 cadmium diethyldithiocarbamate \n''C12H24CdN2S4 cadmium, bis(pentyldithiocarbamato) \n''C18H36CdN2S4 cadmium dibutyldithiocarbamate \n''C20H38CdO4S2 bis(2-ethylhexyl mercaptoacetato -o',S)cadmium \n''C22H44CdN2S4 cadmium bis(dipentyldithiocarbamate) \n''C32H68CdO6P2 cadmium bis(2-ethylhexyl)phosphite \n''CdC2O4·3H2O cadmium oxalate trihydrate \n''Cd(ClO3)2·2H2O cadmium chlorate dihydrate \n''Cd(ClO4)2·6H2O cadmium perchlorate hexahydrate \n''CdCr2O7·H2O cadmium dichromate monohydrate \n''CdSO4·H2O cadmium sulfate monohydrate \n''CdSeO4·2H2O cadmium selenate dihydrate \n''C10H8CdN2O2S2 cadmium, bis(1-hydroxy-2(1H)-pyridinethionato) \n''C14H13CdN3OS cadmium, ammine(benzenecarbothioic acid ((2-hydroxyphenyl)methylene)hydrazidato(2-))-, (t-4) \n''Cd5(BW12O40)·18H2O cadmium borotungstate octadecahydrate \n'""", '48', '112.41')
        self.colorCd=colorCd="CadetBlue2"
        self.Cd = tk.Button(self, text=Cd[0], width=5, height=2, bg=colorCd, font=10, borderwidth=3,
                           command=lambda text=Cd: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCd, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cd()])
        self.Cd.grid(row=7, column=13)
        
        Hg = ('Hg', 'Mercury', """'Hg mercury \n''HgBr2 mercuric bromide \n''Hg2Br2 mercury(I) bromide \n''HgCl2 mercuric chloride \n''Hg2Cl2 mercury(I) chloride \n''HgF2 mercury(II) fluoride \n''Hg2F2 mercury(I) fluoride \n''Hg(IO3)2 mercury(II)iodate \n''HgI2 mercury(II) iodide \n''HgI2 mercuric iodide \n''NaHg sodium mercury amalgam \n''HgO mercuric oxide \n''HgS mercury(II) sulfide \n''HgS mercury(II) sulfide \n''HgSe mercury(II) selenide \n''HgTe mercury telluride \n''Hg2I2 mercury(I) iodide \n''Hg2N6 mercury azide \n''Hg2O mercury(I) oxide \n''Hg2S mercury(I) sulfide \n''Ag2HgI4 silver(I) tetraiodomercurate(II) \n''AsHgI4 donovan's solution \n''BaHgI4 barium tetraiodomercurate(II) \n''CH3Hg+ methylmercury ion \n''C2Cl6Hg bis(trichloromethyl)mercury \n''(CH3)2Hg dimethyl mercury \n''Hg(CN)2 mercuric cyanide \n''HgC2O4 mercury(II) oxalate \n''Hg2C2O4 mercury(I) oxalate \n''C4H10Hg diethyl mercury \n''C6H5Hg phenylmercury \n''C6H14Hg diisopropyl mercury \n''C6H14Hg dipropyl mercury \n''C8H18Hg di-sec-butylmercury \n''C10H22Hg mercury, bis(3-methylbutyl) \n''(C6H5)2Hg diphenylmercury \n''C14H14Hg dibenzylmercury \n''C14H30Hg diheptylmercury \n''Cl2HgO8 mercury diperchlorate \n''HgCrO4 mercury(II) chromate \n''CrHg2O4 mercury(I) chromate \n''Cr2HgO7 mercury(II) dichromate \n''Cu2HgI4 copper(I) mercury iodide \n''Hg(BrO3)2 mercury(II) bromate \n''Hg(ClO3)2 mercury(II) chlorate \n''K2HgI4 mercury potassium iodide \n''Hg(NO3)2 mercury(II) nitrate \n''HgSO4 mercuric sulfate \n''HgV4O11 mercury tetravanadate \n''HgWO4 mercury(II) tungstate \n''Hg2(BrO3)2 mercury(I) bromate \n''Hg2CO3 mercury(I) carbonate \n''Hg2(ClO3)2 mercury(I) chlorate \n''Hg2(IO3)2 mercury(I) iodate \n''Hg2(NO2)2 mercury(I) nitrite \n''Hg2(NO3)2 mercury(I) nitrate \n''Hg2SO4 mercury(I) sulfate \n''Hg2WO4 mercury(I) tungstate \n''Hg3O6S mercury oxide sulfate \n''Hg3O8P2 mercury(II) phosphate \n''CH2HgI2 iodo(iodomethyl)mercury \n''CH3HgBr methylmercury(II)bromide \n''CH3HgCl methylmercuric chloride \n''CH3HgI methylmercury(II)iodide \n''CH4HgO methylmercury hydroxide \n''C2F6HgS2 bis(trifluoromethylthio)mercury \n''C2H2Cl2Hg chloro(2-chlorovinyl)mercury \n''C2H3BrHg vinylmercuric bromide \n''C2H3HgN methylmercury nitrile \n''C2H5ClHg chloroethylmercury \n''C2H6HgS (methanethiolato)methylmercury \n''C2HgN2O2 mercury(II) fulminate \n''Hg(SCN)2 mercuric thiocyanate \n''C2HgN10O4 1H-tetrazole, 5-nitro-, mercury(II) salt \n''Hg(CN)2·HgO mercury(II) oxycyanide \n''C3H6HgN4 methylmercuric dicyanamide \n''C3H7ClHg propylmercuric chloride \n''C4H6HgO2 bis(formylmethyl)mercury \n''(CH3COO)2Hg mercury(II)acetate \n''C4H7ClHg cis-2-butenylmercuric chloride \n''C4H8HgN4 ethylmercuric dicyandiamide \n''C4H8HgO2 mercury, (acetato)ethyl \n''C4H9BrHg sec-butylmercuric bromide \n''C4H9ClHg N-butylmercuric chloride \n''C4HgK2N4 mercuric potassium cyanide \n''C6Cl2HgO4 mercury, (2,5-dichloro-3,6-dihydroxy-p-benzoquinolato) \n''C6H5BrHg phenylmercuric bromide \n''C6H5HgCl phenylmercuric chloride \n''C6H6HgO2 bis(3-hydroxy-1-propynyl)mercury \n''C6H10HgO6 mercury(II) lactate \n''C6H11HgO7 mercury gluconate \n''C6H12HgO3 mercury, (acetato-o)(2-ethoxyethyl) \n''C6H13BrHg bromohexylmercury \n''C7H5Br3Hg phenyl(tribromomethyl)mercury \n''C7H5Cl3Hg phenyl(trichloromethyl)mercury \n''C7H5HgO2 mercuribenzoic acid \n''C7H6HgO3 4-(hydroxymercury)benzoic acid \n''C7H6HgO3 p-hydroxymercuribenzoate \n''C7H7HgI iodo(p-tolyl)mercury \n''C6H5HgOCOCH3 phenylmercuric acetate \n''[(CH3)3SiCH2]2Hg bis(trimethylsilylmethyl)mercury \n''C10H8HgN2 di-3-pyridylmercury \n''C11H12HgO2 mercury, (2,4-pentanedionato-o,O')phenyl \n''C12H10HgO2 germisan \n''C18H30HgS (dodecylthio)phenylmercury \n''C36H58Hg2S phenylmercurilauryl thioether \n''C36H66HgO4 mercury oleate \n''C36H70HgO4 mercury distearate \n''HgNH2Cl ammoniated mercuric chloride \n''HgClO4·4H2O mercury(I)perchlorate tetrahydrate \n''Hg(ClO4)2·xH2O mercury(II)perchlorate hydrate \n''Hg2(NO3)2·2H2O mercury(I)nitrate dihydrate \n''Hg(NO3)2·H2O mercury(II) nitrate monohydrate \n''HgHAsO4 mercury(II) hydrogen arsenate \n''Hg2(C2H3O2)2 mercury(I) acetate \n''Hg2(SCN)2 mercury(I) thiocyanate \n''CHHgNO hydroxymercury nitrile \n''(CF3SO3)2Hg mercury(II)trifluoromethanesulfonate \n''Hg(CF3COO)2 mercury(II) trifluoroacetate \n''C2H3BrHgO2 mercury, bromo(methoxycarbonyl) \n''C2H5BrHgO bromo(2-hydroxyethyl)mercury \n''C2H5ClHgO chloro(2-hydroxyethyl)mercury \n''C2H5ClHgS mercury, chloro(ethanethiolato)- \n''C3H7BrHgO bromo(2-hydroxypropyl)mercury \n''C3H7ClHgO agallol \n''C3H7HgNS methyl(thioacetamido)mercury \n''HgCo(SCN)4 mercury(II) tetrakis(thiocyanato-n)cobaltate(2-) \n''C4H3ClHgO chloro(2-furyl)mercury \n''C4H5HgNO4 mercury(II), iminodiacetato \n''C4H6BrHgO2 crotonylmercuric bromide \n''C4H10HgO2S mercury, ((dihydroxypropyl)thio)methyl \n''C4H11HgI3S ethyldimethyl sulfonium iodide mercuric iodide addition compound \n''C4HgK2N4S4 mercury dipotassium tetrathiocyanate \n''C5H4ClHgN pyridine, 3-(chloromercuri) \n''C5H13HgI3S diethylmethylsulfonium iodide mercuric iodide addition compound \n''C6H5ClHgO chloro(hydroxyphenyl)mercury \n''C6H5ClHgO chloro(o-hydroxyphenyl)mercury \n''C6H5ClHgO mercury, chloro(p-hydroxyphenyl) \n''C6H5HgO3S para-mercury-benzenesulfonic acid \n''C6H10Hg2N2S2 ethyl(5-ethylmercuri-3-(1,2,4-thiadiazolyl)thio)mercury(II) \n''C6H15HgI3S triethylsulfonium triiodomercurate(1-) \n''C7H5ClHgO2 p-chloromercuribenzoic acid \n''HOHgC6H4CO2Na p-chloromercuriobenzoate \n''C7H8HgN2O mercury, phenylureido \n''CH3CO2HgC6H4NH2 4-aminophenylmercuric acetate \n''C8H13ClHgO mercury, chloro(3-methoxybicyclo(2.2.1)hept-2-yl) \n''C9H10HgO2S thimerosal \n''C9H17ClHgO chloro(trans-2-methoxycyclooctyl)mercury \n''C10H9HgNO lM seed protectant \n''C10H12HgI6N4 diiodobis(5-iodopyridin-2-amine)mercury dihydroiodide \n''C10H14HgN2O8 mercury(II) EDTA complex \n''C12H8HgN2O6 bis(4-hydroxy-3-nitrophenyl)mercury \n''C12H10HgN4O4 bis(2-amino-5-nitrophenyl)mercury \n''C6H5HgNO3·C6H5HgOH basic phenylmercury(II) nitrate \n''C12H15HgNO6 mercury, (3-(alpha-carboxy-o-anisamido)-2-hydroxypropyl)hydroxy \n''C15H21HgN2O5 N-(3-acetoxymercuri-2-methoxypropyl)-hippuramide \n''C16H19HgI3S dibenzylethylsulfonium iodide mercuric iodide \n''C18H23HgI3S dibenzylbutylsulfonium iodide mercuric iodide \n''C19H16HgN4S phenylmercuric dithiazonate \n''C21H21HgI3S sulfonium, tribenzyl-, iodide, compound with mercury iodide (1:1) \n''C26H26HgN8S2 mercury dithizonate \n''Hg(NO3)2·2H2O mercury(II) nitrate dihydrate \n''C2H8BrHgNO bromo(2-hydroxyethyl)mercury ammonia salt \n''C4H9HgNO2S s-(methylmercury)-l-cysteine \n''C5H11ClHgN2O2 chlormerodrin \n''C5H11HgNO2S ethylmercuric cysteine \n''C6H3ClHgN2O5 mercury, chloro(2-hydroxy-3,5-dinitrophenyl) \n''C6H4ClHgNO3 2-chloromercuri-4-nitrophenol \n''C6H5ClHgO3S p-chloromercuriphenylsulfonate \n''C6H7HgN2O2S 3-mercuri-4-aminobenzenesulfonamide \n''C6H12HgN2O4S2 bis(l-cysteinato)mercury \n''C7H6ClHgNO chloro(N-phenylformamido)mercury \n''C7H11ClHgN2O3 1-(3-chloromercuri-2-methoxy)propylhydantoin \n''C7H11ClHgN2O3 3-(3-chloromercuri-2-methoxy-1-propyl)hydantoin \n''C7H11ClHgN2O3 chloro((3-(2,4-dioxo-5-imidazolidinyl)-2-methoxy)propyl)mercury \n''C8H9HgNaO3S2 sodium timerfonate \n''C8H13ClHgN2O3 1-(3-chloromercuri-2-methoxy-1-propyl)-3-methylhydantoin \n''C8H13ClHgN2O3 3-(3-chloromercuri-2-methoxy-1-propyl)-1-methylhydantoin \n''C8H13ClHgN2O3 5-(3-chloromercuri-2-methoxy-1-propyl)-3-methylhydantoin \n''C9H15ClHgN2O3 3-(3-chloromercuri-2-methoxy-1-propyl)-5,5-dimethylhydantoin \n''C10H5Cl6HgNO2 methylmercurichlorendimide; \n''C10H16HgN2O2S4 bis(4-morpholinecarbodithioato)mercury \n''C10H18ClHgNO2 chloro(2-(3-methoxypropionamido)cyclohexyl)mercury \n''C11H7Cl6HgNO2 ethylmercurichlorendimide \n''C12H8ClHgN3O4 mercury, chloro[4-[(2,4-dinitrophenyl)amino]phenyl] \n''C12H8HgNa2O8S2 hermophenyl \n''C12H22ClHgNO (E)-chloro(2-hexanamidocyclohexyl)-mercury \n''C15H7Cl6HgNO2 PHIMM \n''C15H17HgNO2S Granosan MDB \n''C15H17HgNO4S2 mercury, methyl-, N-bis(p-tolylsulfonyl)amido- \n''C16H11ClHgN2O mercury orange \n''C16H27HgNO6S mercaptomerin \n''C16H36HgO4P2S4 bis(O,O-dibutylphosphorodithioato-S)-mercury \n''C18H23HgNO2S methyl(5-isopropyl-N-(p-tolyl)-o-toluenesulfonamido)mercury \n''C20H25HgN5NaO8 salyrgan theophylline \n''C21H32HgN5NaO7 mercurophylline \n''C24H51Br2HgO3P mercury(II) bromide complex with tris(2-ethylhexyl) phosphite \n''C24H51Cl2HgO3P mercury(II) chloride complex with tris(2-ethylhexyl) phosphite \n''C34H34HgN4Na2O6 hematoporphyrinmercury disodium salt \n''Hg(C7H5O2)2·H2O mercury(II) benzoate monohydrate \n''(NH4)2HgCl4·2H2O ammonium mercuric chloride dihydrate \n'""", '80', '200.59')
        self.colorHg=colorHg="CadetBlue3"
        self.Hg = tk.Button(self, text=Hg[0], width=5, height=2, bg=colorHg, font=10, borderwidth=3,
                           command=lambda text=Hg: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorHg, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Hg()])
        self.Hg.grid(row=8, column=13)

        Cn = ('Cn', 'Copernicium', """'Cn copernicium copernicium metal\n'""", '112', '285')
        self.colorCn=colorCn="CadetBlue4"
        self.Cn = tk.Button(self, text=Cn[0], width=5, height=2, bg=colorCn, font=10, borderwidth=3,
                           command=lambda text=Cn: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCn, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cn()])
        self.Cn.grid(row=9, column=13)

        B = ('B', 'Boron', """'B boron\n''AlB2 aluminum diboride\n''AlB12 aluminum dodecaboride\n''BAs boron arsenide\n''BBr3 boron tribromide\n''BCl3 boron trichloride\n''CrB chromium boride\n''BF3 boron trifluoride\n''BI3 boron triiodide\n''BN boron nitride\n''NaBH4 sodium borohydride\n''NbB niobium boride\n''Ni2B nickel boride\n''10B2O3 boron oxide-10 B\n''11B2O3 boron-11 boxide\n''BP boron phosphide\n''TaB tantalum boride\n''BV vanadium boride\n''WB tungsten boride\n''B2Be beryllium boride\n''B2Br4 tetrabromodiborane\n''B2Cl4 tetrachloradiborane\n''CrB2 chromium diboride\n''B2D6 diborane-d 610%in D2,electronic grade\n''B2F4 tetrafluorodiborane\n''B2H6 diborane\n''B2O3 boron oxide\n''B2S3 boron sulfide\n''B2U uranium boride\n''B4H10 tetraborane(10)\n''SiB4 silicon tetraboride\n''B5H9 pentaborane(9)\n''B5H11 pentaborane(11)\n''BaB6 barium hexaboride\n''B6Be beryllium hexaboride\n''CaB6 calcium hexaboride\n''B6H10 hexaborane(10)\n''B6H12 hexaborane(12)\n''SiB6 silicon hexaboride\n''SrB6 strontium hexaboride\n''B9H15 nonaborane(15)\n''B10H14 decaborane(14)\n''B10H16 decaborane(16)\n''B12H16 dodecaborane(16)\n''B13H19 tridecaborane(19)\n''B14H18 tetradecaborane(18)\n''B16H20 hexadecaborane(20)\n''B18H22 octadecaborane(22)\n''CB4 boron carbide\n''CeB6 cerium boride\n''DyB4 dysprosium boride\n''ErB4 erbium boride\n''EuB6 europium boride\n''GdB6 gadolinium boride\n''HfB2 hafnium boride\n''LaB6 lanthanum hexaboride\n''LuB4 lutetium boride\n''MgB2 magnesium diboride\n''MgB6 magnesium hexaboride\n''MgB12 magnesium dodecaboride\n''NbB2 niobium diboride\n''NdB6 neodymium boride\n''PrB6 praseodymium boride\n''ScB2 scandium boride\n''SmB6 samarium boride\n''TaB2 tantalum diboride\n''ThB6 thorium boride\n''TiB2 titanium boride\n''VB2 vanadium diboride\n''YB6 yttrium boride\n''ZrB2 zirconium diboride\n''AgBF4 silver tetrafluoroborate\n''BCsO2 cesium metaborate\n''D3BO3 boric acid-d 3\n''NaBD4 sodium borodeuteride\n''HBF4 fluoboric acid\n''KBF4 potassium fluoroborate\n''LiBF4 lithium tetrafluoroborate\n''NaBF4 sodium borofluoride\n''BF4Rb rubidium fluoroborate\n''HBO2 metaboric acid\n''H3N·BH3 borane-ammonia complex\n''B(OH)3 boric acid\n''H310BO3 boric acid-10 B\n''H311BO3 boric acid-11 B\n''KBH4 potassium borohydride\n''LiBH4 lithium borohydride\n''KBO2 potassium metaborate\n''LiBO2 lithium metaborate\n''BNaO2 sodium metaborate\n''BNaO3 sodium peroxoborate\n''Ba(BF4)2 barium fluoborate\n''Ba(BO2)2 barium borate\n''B2CaO4 calcium metaborate\n''B2Cd3O6 cadmium borate\n''B2CuF8 borate(1-), tetrafluoro-, copper(2+) (2:1)\n''Ni(BF4)2 nickel(II) fluoborate\n''Pb(BF4)2 lead(II)tetrafluoroborate\n''Sn(BF4)2 tin bis(tetrafluoroborate)\n''Zn(BH4)2 zinc borohydride\n''B3H6N3 borazine\n''Li2B4O7 lithium tetraborate\n''Na2B4O7 sodium tetraborate\n''C2H12B10 m-carborane\n''C2H12B10 o-carborane\n''B(CD3)3 deuterated trimethylboron\n''B(CH3)3 trimethylborane\n''(C2H5)3B triethylborane\n''C8H15B 9-borabicyclo[3.3.1]nonane\n''[(CH3)2CHCH(CH3)]2BH disiamylborane\n''[C2H5CH(CH3)]3B tri(butan-2-yl)borane\n''[CH3(CH2)3]3B tributylborane\n''C15H21B B-benzyl-9-BBN\n''C8H15B 9-borabicyclo[3.3.1]nonane\n''(C6F5)3B tris(pentafluorophenyl)borane\n''(C6H5)3B triphenylborane\n''C18H31B S-alpine-borane\n''C18H31B R-alpine-borane\n''(C10H17)2BCH2CH=CH2 (-)-ipc 2B(allyl)\n''(C10H17)2BCH2CH=CH2 (+)-ipc 2B(allyl)\n''[(CH3)3C6H2]3B trimesitylborane\n''CsBF4 cesium fluoroborate\n''Cu(BO2)2 copper(II) barate\n''2Al2O3·B2O3 aluminum barate\n''BF3·2H2O boron trifluoride dihydrate\n''NH4BF4 ammonium tetrafluoroborate\n''NOBF4 nitrosyl tetrafluoroborate\n''NaBO2·xH2O sodium metaborate hydrate\n''BNaO3·H2O sodium perborate monohydrate\n''BPO4·xH2O boron phosphate hydrate\n''BH3CO borane carbonyl\n''LiBO2·2H2O lithium metaborate dihydrate\n''K2B4O7·4H2O potassium tetraborate tetrahydrate\n''NaBO3·4H2O sodium perborate tetrahydrate\n''Na2B4O7·10H2O sodium borate decahydrate\n''CH3B(OH)2 methylboronic acid\n''C2H5BO3 1,3,2-dioxaborolan-2-ol\n''(CH3)2BBr bromodimethylborane\n''(CH3)2S·BH3 borane-methyl sulfide complex\n''(CH3)2NH·BH3 borane dimethylamine complex\n''CH3CH2OB(OH)2 ethyl borate\n''H3CCH=CHB(OH)2 cis-1-propene-1-boronic acid\n''C3H7BO2 cyclopropylboronic acid\n''CH3CH=CHB(OH)2 trans-1-propen-1-ylboronic acid\n''C3H9BO2 isopropylboronic acid\n''B(OCH3)3 trimethyl borate\n''(CH3O)311B trimethyl borate-11 B\n''C3H9B3O3 trimethylboroxine\n''C3H9B3O6 trimethoxyboroxine\n''(CH3)3N·BH3 trimethylamine borane\n''C4H5BO3 2-furanboronic acid\n''C4H5BO3 3-furanboronic acid\n''BH3OC4H8 borane-tetrahydrofuran\n''CH3(CH2)3BCl2 butyldichloroborane\n''C4H9BO2 cyclobutylboronic acid\n''(CH3)3CNH2·BH3 tert-butylamine borane\n''C4H11BO2 1-butane boronic acid\n''(CH3)2CHCH2B(OH)2 2-methylpropylboronic acid\n''CH3(CH2)3B(OH)2 N-butylboronic acid\n''(CH3)4N(BH4) tetramethylammonium borohydride\n''C5H5BO4 5-formyl-2-furanboronic acid\n''C5H7BO3 5-methyl-2-furanboronic acid\n''C5H8BN borane pyridine\n''C5H11B O2 1-penten-1-ylboronic acid\n''(CH2)2C=CCH3BO2 3-methyl-2-buten-2-ylboronic acid\n''C5H11BO2 cyclopentylboronic acid\n''(C2H5)2BOCH3 diethylmethoxyborane\n''C5H13BO2 3-methyl-1-butylboronic acid\n''C5H13BO2 neopentylboronic acid\n''(CF3CO2)3B boron tris(trifluoroacetate)\n''C6H5BO2 catecholborane\n''C6H5BCl2 dichlorophenylborane\n''C6H10B2N4 pyrazabole\n''C6H5B(OH)2 benzeneboronic acid\n''HOC6H4B(OH)2 3-hydroxyphenylboronic acid\n''HOC6H4B(OH)2 4-hydroxyphenylboronic acid\n''C6H4[B(OH)2]2 benzene-1,4-diboronic acid\n''C6H13BO2 4,4,5,5-tetramethyl-1,3,2-dioxaborolane\n''C6H13BO2 cyclohexyl boronic acid\n''CH3(CH2)3CH=CHB(OH)2 trans-1-hexen-1-ylboronic acid\n''C6H13BO2 trans-3,3-dimethyl-1-butenylboronic acid\n''(C2H5)3N·BH3 triethylamine borane\n''C6H15BO2 1-hexaneboronic acid\n''(C2H5O)3B triethyl borate\n''KB(C2H5)3H potassium triethylborohydride\n''Li(C2H5)3BH super-hydride\n''(C2H5)3NaBH sodium triethylborohydride\n''B(N(CH3)2)3 tris(dimethylamido)borane\n''C7H7BF4 tropylium tetrafluoroborate\n''C7H7BO2 2-(hydroxymethyl)phenylboronic acid cyclic monoester\n''HCOC6H4B(OH)2 2-formylphenylboronic acid\n''HCOC6H4B(OH)2 3-formylphenylboronic acid\n''HCOC6H4B(OH)2 4-formylphenylboronic acid\n''C7H7BO4 3,4-(methylenedioxy)phenylboronic acid\n''HO2CC6H4B(OH)2 3-carboxyphenylboronic acid\n''HO2CC6H4B(OH)2 4-boronobenzoic acid\n''CH3C6H4B(OH)2 m-tolylboronic acid\n''CH3C6H4B(OH)2 o-tolylboronic acid\n''CH3C6H4B(OH)2 4-methylphenylboronic acid\n''CH3OC6H4B(OH)2 2-methoxyphenylboronic acid\n''HOCH2C6H4B(OH)2 3-(hydroxymethyl)phenylboronic acid\n''CH3OC6H4B(OH)2 3-methoxyphenylboronic acid\n''HOCH2C6H4B(OH)2 4-(hydroxymethyl)phenylboronic acid\n''CH3OC6H4B(OH)2 p-anisylboronic acid\n''C7H15BO3 2-methoxy-4,4,5,5-tetramethyl-1,3,2-dioxaborolane\n''[(CH3)2CHO]2BCH3 diisopropoxymethylborane\n''(C2D5)4BNa sodium tetraethylborate-d 20\n''C8H7BO3 2-benzofuranboronic acid\n''C6H3(CHO)2B(OH)2 3,5-diformylphenylboronic acid\n''C6H5C=CH2B(OH)2 1-phenylvinylboronic acid\n''C8H9BO2 3-vinylphenylboronic acid\n''H2C=CHC6H4B(OH)2 4-vinylphenylboronic acid\n''C6H5CH=CHB(OH)2 trans-2-phenylvinylboronic acid\n''CH3COC6H4B(OH)2 2-acetylphenylboronic acid\n''CH3COC6H4B(OH)2 3-acetylphenylboronic acid\n''C8H9BO3 3-formyl-5-methylphenylboronic acid\n''CH3COC6H4B(OH)2 4-acetylphenylboronic acid\n''C8H9BO4 1,4-benzodioxane-6-boronic acid\n''CH3O2C(C6H4)B(OH)2 2-methoxycarbonylphenylboronic acid\n''HCOC6H3(OCH3)B(OH)2 3-formyl-4-methoxyphenylboronic acid\n''CH3O2CC6H4B(OH)2 3-methoxycarbonylphenylboronic acid\n''C8H9BO4 4-methoxycarbonylphenylboronic acid\n''HCOC6H3(OCH3)B(OH)2 5-formyl-2-methoxyphenylboronic acid\n''(CH3)2C6H3B(OH)2 2,3-dimethylphenylboronic acid\n''(CH3)2C6H3B(OH)2 2,5-dimethylphenylboronic acid\n''(CH3)2C6H3B(OH)2 2,6-dimethylphenylboronic acid\n''C2H5C6H4B(OH)2 2-ethylphenylboronic acid\n''(CH3)2C6H3B(OH)2 3,5-dimethylphenylboronic acid\n''C2H5C6H4B(OH)2 4-ethylphenylboronic acid\n''C6H5CH2CH2B(OH)2 phenethylboronic acid\n''C2H5OC6H4B(OH)2 2-ethoxyphenylboronic acid\n''C6H3CH3OCH3B(OH)2 2-methoxy-5-methylphenylboronic acid\n''C2H5OC6H4B(OH)2 3-ethoxyphenylboronic acid\n''C2H5OC6H4B(OH)2 4-ethoxyphenylboronic acid\n''CH3OC6H3(CH3)B(OH)2 4-methoxy-2-methylphenylboronic acid\n''CH3OC6H3(CH3)B(OH)2 4-methoxy-3-methylphenylboronic acid\n''C6H3(OCH3)2B(OH)2 2,3-dimethoxyphenylboronic acid\n''(CH3O)2C6H3B(OH)2 2,4-dimethoxyphenylboronic acid\n''(CH3O)2C6H3B(OH)2 2,5-dimethoxyphenylboronic acid\n''(CH3O)2C6H3B(OH)2 2,6-dimethoxyphenylboronic acid\n''(CH3O)2C6H3B(OH)2 3,4-dimethoxyphenylboronic acid\n''C8H14BBr B-bromo-9-BBN\n''C8H14BI B-iodo-9-BBN\n''C8H16BLi lithium 9-BBN hydride\n''C8H15BO2 trans-(2-cyclohexylvinyl)boronic acid\n''C8H15BO2 4,4,6-trimethyl-2-vinyl-1,3,2-dioxaborinane\n''C8H15BO2 vinylboronic acid pinacol ester\n''CH3(CH2)5CH=CHB(OH)2 trans-1-octen-1-ylboronic acid\n''[(CH3)2CH]2NC2H5·BH3 borane N,N-diisopropylethylamine complex\n''(C2H5)4BNa sodium tetraethylborate\n''((CH3)2N)2BB(N(CH3)2)2 tetrakis(dimethylamido)diborane\n''C9H9BO4 4-(carboxyvin-2-yl)phenylboronic acid\n''C9H11BO2 1-propylboronic acid catechol ester\n''C9H11BO2 phenylboronic acid 1,3-propanediol ester\n''C6H4CH3CH=CHB(OH)2 trans-2-(4-methylphenyl)vinylboronic acid\n''C9H11BO2 trans-3-phenyl-1-propen-1-ylboronic acid\n''CH3OC6H4CH=CHB(OH)2 trans-2-(4-methoxyphenyl)vinylboronic acid\n''CH3CH2O2C(C6H4)B(OH)2 2-ethoxycarbonylphenylboronic acid\n''C2H5OCOC6H4B(OH)2 3-ethoxycarbonylphenylboronic acid\n''C6H2CHO(CH3)(OCH3)B(OH)2 3-formyl-2-methoxy-5-methylphenylboronic acid\n''C6H3OCH2CH3CHOB(OH)2 4-ethoxy-3-formylphenylboronic acid\n''C2H5OCOC6H4B(OH)2 4-ethoxycarbonylphenylboronic acid\n''C6H2(CH3)3B(OH)2 2,4,5-trimethylphenylboronic acid\n''C6H2(CH3)3B(OH)2 2,4,6-trimethylphenylboronic acid\n''CH3CH2CH2C6H4B(OH)2 4-propylphenylboronic acid\n''C6H3CH3OCH2CH3B(OH)2 2-ethoxy-5-methylphenylboronic acid\n''C6H4OCH(CH3)2B(OH)2 2-isopropoxyphenylboronic acid\n''C6H4(OCH2CH2CH3)B(OH)2 2-propoxyphenylboronic acid\n''(CH3)2C6H2OCH3B(OH)2 3,5-dimethyl-4-methoxyphenylboronic acid\n''(CH3)2CHOC6H4B(OH)2 3-isopropoxyphenylboronic acid\n''C6H4(OCH2CH2CH3)B(OH)2 3-propoxyphenylboronic acid\n''C2H5OC6H3(CH3)B(OH)2 4-ethoxy-2-methylphenylboronic acid\n''C6H4OCH(CH3)2B(OH)2 4-isopropoxyphenylboronic acid\n''C6H4(OCH2CH2CH3)B(OH)2 4-propoxyphenylboronic acid\n''(CH3O)3C6H2B(OH)2 2,3,4-trimethoxyphenylboronic acid\n''C9H13BO5 3,4,5-trimethoxyphenylboronic acid\n''C9H14BN diethyl(3-pyridyl)borane\n''C9H15BO3 allyl borate\n''C9H17BO B-methoxy-9-BBN\n''((CH3)4C2O2)BCH2CH=CH2 allylboronic acid pinacol ester\n''C9H17BO2 cyclopropylboronic acid pinacol ester\n''C9H17BO2 isopropenylboronic acid pinacol ester\n''C9H18B2O6 trimethylene borate\n''C9H19BO2 trans-1-nonenylboronic acid\n''(CH3)3CCO2B(C2H5)2 trimethylacetic acid,anhydride with diethylborinic acid\n''C9H19BO3 2-isopropoxy-4,4,5,5-tetramethyl-1,3,2-dioxaborolane\n''[(CH3)2CHO]3B triisopropyl borate\n''(CH3CH2CH2O)3B tripropyl borate\n''C10H7B(OH)2 2-naphthylboronic acid\n''C10H7B(OH)2 naphthalene-1-boronic acid\n''C6H2CHOCH3OCH2CH3B(OH)2 2-ethoxy-3-formyl-5-methylphenylboronic acid\n''C10H13BO4 3-formyl-5-isopropoxyphenylboronic acid\n''C10H13BO4 3-formyl-5-propoxyphenylboronic acid\n''C6H(CH3)4B(OH)2 2,3,5,6-tetramethylphenylboronic acid\n''CH3(CH2)3C6H4B(OH)2 4-butylphenylboronic acid\n''(CH3)3CC6H4B(OH)2 4-tert-butylphenylboronic acid\n''C6H4OCH2CH2CH2CH3B(OH)2 2-butoxyphenylboronic acid\n''C10H15BO3 2-isobutoxyphenylboronic acid\n''H3CC6H3[OCH(CH3)2]B(OH)2 2-isopropoxy-5-methylphenylboronic acid\n''C6H4OCH2CH2CH2CH3B(OH)2 3-butoxyphenylboronic acid\n''C10H15BO3 3-furanboronic acid pinacol ester\n''C10H15BO3 3-isobutoxyphenylboronic acid\n''C6H4OCH2CH2CH2CH3B(OH)2 4-butoxyphenylboronic acid\n''(CH3)2C6H2OCH2CH3B(OH)2 4-ethoxy-3,5-dimethylphenylboronic acid\n''C10H15BO3 4-isobutoxyphenylboronic acid\n''C10H15BO3 4-isopropoxy-2-methylphenylboronic acid\n''C10H15BO3 5-isopropyl-2-methoxyphenylboronic acid\n''H3CC6H3(OCH2CH2CH3)B(OH)2 5-methyl-2-propoxyphenylboronic acid\n''C10H15BO4 2-isopropoxy-6-methoxyphenylboronic acid\n''C6H5N(C2H5)2·BH3 borane-N,N-diethylaniline\n''C10H19BO3 trans-3-methoxy-1-propenylboronic acid pinacol ester\n''C10H20B2O4 bis(neopentyl glycolato)diboron\n''C10H21BO2 n-butylboronic acid pinacol ester\n''H2C=CHB(OCH2CH2CH2CH3)2 vinylboronic acid dibutyl ester\n''[(CH3)2CH2CH2]S·BH3 borane isoamylsulfide complex\n''CH3(CH2)3B[OCH(CH3)2]2 butyldiisopropoxyborane\n''CH3C10H6B(OH)2 4-methyl-1-naphthaleneboronic acid\n''C10H6OCH3B(OH)2 6-methoxy-2-naphthaleneboronic acid\n''C11H15BO2 phenylboronic acid neopentylglycol ester\n''C6H2COHOCH(CH3)2CH3B(OH)2 3-formyl-2-isopropoxy-5-methylphenylboronic acid\n''C6H2CHOCH3OCH2CH2CH3B(OH)2 3-formyl-5-methyl-2-propoxyphenylboronic acid\n''C6H5N(C2H5)CH(CH3)2·BH3 boron-n-ethyl-n-isopropyl aniline\n''CH3C6H3O(CH2)3CH3B(OH)2 2-butoxy-5-methylphenylboronic acid\n''C11H17BO3 2-isobutoxy-5-methylphenylboronic acid\n''C11H17BO3 3,5-dimethyl-4-isopropoxyphenylboronic acid\n''C11H17BO3 3,5-dimethyl-4-propoxyphenylboronic acid\n''C11H19BO2 (trans)-2-cyclopropylvinylboronic acid pinacol ester\n''C11H21BO2 trans-1-penten-1-ylboronic acid pinacol ester\n''K[CH(CH3)CH2CH3]3BH K-selectride\n''Li[CH(CH3)CH2CH3]3BH L-selectride\n''BF3·CH3CH2CH2OH boron trifluoride propanol complex\n''(CH3)3O(BF4) trimethyloxonium tetrafluoroborate(1-)\n''C3H9BF4S trimethylsulphonium tetrafluoroborate\n''CH3SS(CH3)2BF4 dimethyl(methylthio)sulfonium tetrafluoroborate\n''NaB(OCH3)3H sodium trimethoxyborohydride\n''C4H5BO2S 2-thienylboronic acid\n''C4H5BO2S 3-thienylboronic acid\n''C4H6B2O4S 2,5-thiophenediboronic acid\n''C4H8O2·BHCl2 dichloroborane dioxane complex\n''BF3·THF boron trifluoride tetrahydrofuran complex\n''BF3·2CH3COOH dihydrogen bis(acetato-o)difluoroborate(1-)\n''CH3CH2CH2CH2BF3K potassium butyltrifluoroborate\n''C4H12BNO morpholineborane\n''C4H10BClO2 mono-chloroborane dioxane complex\n''(C2H5)2O·(10B)F3 boron-10 trifluoride diethyl etherate\n''HBF4·O(CH2CH3)2 tetrafluoroboric acid diethyl ether complex\n''C4H11BLiN lithium pyrrolidinoborohydride\n''[(CH3)2N]2BBr bromobis(dimethylamino)borane\n''(CH3)4N(BF4) tetramethylammonium tetrafluoroborate\n''C5H5BF5N 1-fluoropyridinium tetrafluoroborate\n''C5H5BO3S 2-formyl-3-thiopheneboronic acid\n''C5H5BO3S 3-formyl-2-thiopheneboronic acid\n''C5H5BO3S 5-formyl-2-thiopheneboronic acid\n''C5H6BNO2 3-pyridineboronic acid\n''C5H6BNO2 4-pyridineboronic acid\n''C5H7BO2S 4-methyl-3-thiopheneboronic acid\n''C5H7BO2S 5-methyl-2-thiopheneboronic acid\n''BrC6H4N2BF4 4-bromobenzenediazonium tetrafluoroborate\n''C6H4BBr2FO2 2,4-dibromo-6-fluorophenylboronic acid\n''C6H4BBr2FO2 3,6-dibromo-2-fluorophenylboronic acid\n''C6H4BClF3K potassium 4-chlorophenyltrifluoroborate\n''C6H4N3O2·BF4 p-nitrophenyldiazonium fluoborate\n''C6H5BBrFO2 3-bromo-2-fluorophenylboronic acid\n''C6H5BBrFO2 3-bromo-5-fluorophenylboronic acid\n''BrC6H3(F)B(OH)2 5-bromo-2-fluorophenylboronic acid\n''C6H3ClFB(OH)2 2-chloro-6-fluorophenylboronic acid\n''ClC6H3(F)B(OH)2 3-chloro-4-fluorophenylboronic acid\n''ClC6H3(F)B(OH)2 5-chloro-2-fluorophenylboronic acid\n''C6H5BFIO2 2-fluoro-6-iodophenylboronic acid\n''C6H5BF3KO potassium 3-hydroxyphenyltrifluoroborate\n''H2NC6H4B(OH)2·HCl 3-aminophenylboronic acid hydrochloride\n''C7H5BF3KO potassium 3-formylphenyltrifluoroborate\n''CHOC6H4BF3K potassium 4-formylphenyltrifluoroborate\n''C7H5BF3KO2 potassium 3,4-(methylenedioxy)phenyltrifluoroborate\n''C7H5BF3KO2 potassium 3-carboxyphenyltrifluoroborate\n''HO2CC6H4BF3K potassium 4-carboxyphenyltrifluoroborate\n''C7H7BBrFO3 3-bromo-5-fluoro-2-methoxyphenylboronic acid\n''C6H2ClF(CH3)B(OH)2 2-chloro-6-fluoro-3-methylphenylboronic acid\n''ClC6H2(F)(CH3)B(OH)2 2-chloro-6-fluoro-5-methylphenylboronic acid\n''C7H7BClFO2 5-chloro-2-fluoro-3-methylphenylboronic acid\n''CH3OC6H4BF3K potassium 2-methoxyphenyltrifluoroborate\n''H3COC6H4BF3·K potassium 3-methoxyphenyltrifluoroborate\n''calcium hexaborate pentahydrate\n''Cd5(BW12O40)·18H2O cadmium borotungstate octadecahydrate\n''(NH4)2B4O7·4H2O ammonium tetraborate tetrahydrate\n''NH4B5O8·4H2O ammonium pentaborate tetrahydrate\n''2ZnO·3B2O3·5H2O zinc barate pentahydrate\n''2ZnO·3B2O3·3.5H2O zinc borate hemiheptahydrate\n''NO2C6H4BF3K potassium 3-nitrophenyltrifluoroborate\n''C9H9BClF4NO 2-chloro-3-ethylbenzoxazolium tetrafluoroborate\n'""", '5', '10.81')
        self.colorB=colorB="CadetBlue1"
        self.B = tk.Button(self, text=B[0], width=5, height=2, bg=colorB, font=10, borderwidth=3,
                           command=lambda text=B: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorB, text[0], text[3], text[4]), self.voice(text[1]), self.compound_B()])
        self.B.grid(row=4, column=14)
        
        Al = ('Al', 'Aluminum', """'Al aluminum\n''AlAs aluminum arsenide\n''AlB2 aluminum diboride\n''AlB12 aluminum dodecaboride\n''AlBr3 aluminum tribromide\n''AlCl3 aluminum chloride\n''AlCl3 polyaluminum chloride\n''AlF3 aluminum fluoride\n''AlI3 aluminum iodide\n''LiAl lithium-aluminum alloy\n''AlN aluminum nitride\n''AlNi aluminum-nickel catalyst\n''AlP aluminum phosphide\n''AlSb aluminum antimonide\n''Al2O3 aluminum oxide\n''Al2S3 aluminum sulfide\n''Al2Se3 aluminum selenide\n''Al2Zr aluminum zirconium\n''Al3Ta tantalum aluminide\n''ThAl3 thorium aluminum alloy\n''BaAl4 aluminium, compound with barium (4:1)\n''C3Al4 aluminum carbide\n''AlCl3O9 aluminum chlorate nonahydrate\n''AlCl3O12aluminum perchlorate\n''KAlCl4  potassium tetrachloroaluminate\n''AlCl4Li lithium tetrachloroaluminate\n''NaAlCl4 sodium tetrachloroaluminate\n''(TiCl3)3·AlCl3 titanium(III)chloride-aluminum chloride\n''Cs2AlF5 cesium fluoroaluminate\n''AlCuZn devarda’s alloy\n''LiAlD4 lithium aluminum deuteride\n''K3AlF6 potassium hexafluoroaluminate\n''Na3AlF6 sodium hexafluoroaluminate\n''Al(OH)3 aluminum hydroxide\n''LiAlH4 lithium aluminum hydride\n''NaAlH4 sodium aluminum hydride\n''LaAlO3 lanthanum aluminum oxide\n''LiAlO2 lithium aluminate\n''Al(NO3)3 aluminum nitrate\n''AlNaO2 sodium aluminate\n''AlO4P aluminum phosphate\n''Al2CaO4 calcium aluminate\n''CoAl2O4 cobalt aluminum oxide\n''CuAl2O4 copper aluminum oxide\n''MgO·Al2O3 magnesium aluminate\n''Al2O3·TiO2 aluminum titanate\n''Al2(SO4)3 aluminum sulfate\n''Y3Al5O12 yttrium aluminum oxide\n''3Al2O3·2SiO2 aluminum silicate\n''(CH3)3Al trimethylaluminum\n''Al(C2H5)3 triethylaluminum\n''[(CH3)2CHCH2]2AlH diisobutylaluminum hydride\n''(CH3CH2CH2)3Al tripropyl aluminum\n''C12H27Al tri-N-butylaluminum\n''[(CH3)2CHCH2]3Al triisobutylaluminum\n''C18H39Al trihexylaluminium\n''[CH3(CH2)7]3Al trioctylaluminium\n''C30H63Al tridecylaluminium\n''C36H75Al tris(dodecyl)aluminum\n''C42H87Al tritetradecylaluminium\n''C48H99Al trihexadecylaluminum\n''C60H123Al trieicosylaluminum\n''Ca(AlH4)2 calcium tetrahydroaluminate\n''CsAlCl4 cesium tetrachloroaluminate\n''Fe(AlO2)2 iron(II) aluminate\n''AlBr3·6H2O aluminum bromide hexahydrate\n''AlCeO3 aluminum cerium oxide\n''AlCl3·xH2O aluminum chloride hydrate\n''AlCl3H12O6 aluminum chloride hexahydrate\n''Al(ClO4)3·9H2O aluminum perchlorate nonahydrate\n''AlF3·3H2O aluminum fluoride trihydrate\n''AlF6H12N3 ammonium hexafluoroaluminate\n''Al(H2PO2)3 aluminum hypophosphite\n''Al(PO3)3 aluminum metaphosphate\n''Al(NO3)3·9H2O aluminum nitrate nonahydrate\n''AlI3·6H2O aluminum iodide hexahydrate\n''AlKO8S2 potassium alum\n''AlNaO8S2 aluminum sodium sulfate\n''AlP4·2H2O aluminum phosphate dihydrate\n''Al2Be3O18Si6 beryl\n''Al2H2O6Si bentoquatam\n''Al2O3·(SiO2)4·H20 bentonite\n''Al2(SO4)3·xH2O aluminum sulfate hydrate\n''2Al2O3·B2O3 aluminum barate\n''Bi2(Al2O4)3·xH2O bismuth aluminate hydrate\n''CH3AlCl2 methylaluminum dichloride\n''CH3CH2AlCl2 dichloroethylaluminum\n''(CH3)2AlCl dimethylaluminum chloride\n''Al(OOCCH3)(OH)2 aluminum acetate dihydroxide\n''C3H9Al2Br3 methyl aluminum sesquibromide\n''C3H9Al2Cl3 methyl aluminum sesquichloride\n''AlH3·N(CH3)3 alane trimethylamine complex\n''(CH3)2CHCH2AlCl2 isobutylaluminum dichloride\n''(C2H5)2AlCl chlorodiethylaluminum\n''Al[OC(CH3)3]3 aluminium tri-tert-butanolate\n''C2H5N(CH3)2·AlH3 alane N,N-dimethylethylamine complex\n''(C2H5)2AlCN diethylaluminum cyanide\n''(C2H5)2AlOC2H5 diethylaluminum ethoxide\n''Al(OC2H5)3 aluminum triethoxide\n''(C2H5)2AlCl·Cl2AlC2H5 ethylaluminum sesquichloride\n''[(CH3)2CHCH2]2AlCl diisobutylaluminum chloride\n''[(CH3)2CHCH2]2AlF diisobutylaluminum fluoride\n''(C2H5)2AlOAl(C2H5)2 tetraethyldialuminoxane\n''[CH3CH(OH)COO]3Al aluminum L-lactate\n''Al[OCH(CH3)2]3 aluminum isopropylate\n''Al[OCH(CH3)C2H5]3 aluminium tri-sec-butanolate\n''Al(O(CH2)3CH3)3 aluminum tributoxide\n''Al(N(CH3)2)3 tris(dimethylamido)aluminum(III)\n''Al(C5H7O2)3 aluminum acetylacetonate\n''[(CH3)2CHCH2]2AlOAl[CH2CH(CH3)2]2 tetraisobutyldialuminoxane\n''(C6H5O)3Al aluminum phenoxide\n''Al(OCC(CH3)3CHCOC(CH3)3)3 aluminum tris(2,2,6,6-tetramethyl-3,5-heptanedionate)\n''C48H93AlO6 aluminum palmitate\n''C54H99AlO6 aluminum oleate\n''Al(C18H35O2)3 aluminum stearate\n''NH4AlCl4 ammonium tetrachloroaluminate\n''Al(BrO3)3·9H2O aluminum bromate nonahydrate\n''AlCs(SO4)2·12H2O aluminum cesium sulfate dodecahydrate\n''AlHNa2O5P+ sodium phosphoaluminate\n''SrLaAlO4 strontium lanthanum aluminate\n''AlK(SO4)2·12H2O potassium aluminum sulfate dodecahydrate\n''AlH24NaO20S2 sodium alum\n''AlNH4(SO4)2·12H2O aluminum ammonium sulfate dodecahydrate\n''Al2(C2O4)3·H2O aluminum oxalate monohydrate\n''Al2(OH3)3PO4 aluminum phosphate trihydroxide\n''Al2(SO4)3·18H2O aluminum sulfate octadecahydrate\n''Al2(SiF6)3·9H2O aluminum hexafluorosilicate nonahydrate\n''Al2Si2O5(OH)4 kaolin\n''Mg6Al2(CO3)(OH)16·4H2O hydrotalcite,synthetic\n''C2H8AlNO4 dihydroxyaluminium\n''(CF3SO3)3Al aluminum trifluoromethanesulfonate\n''C4H8AlCl3O aluminum chloride THF complex\n''NaAlH2(OCH2CH2OCH3)2 sodium dihydridobis(2-methoxyethanolato)aluminate(1-)\n''C6H2CH3(NO2)3·Al tritonal\n''C8H20AlLiO2 lithium aluminum hydride bis(tetrahydrofuran)\n''C11H60Al9O55S8 sucralfate\n''LiAlH[OC(CH3)3]3 lithium tri-tert-butoxyaluminum hydride\n''C13H18AlClTi tebbe reagent\n''[C6H5N(NO)O-]3Al tris(N-nitroso-N-phenylhydroxylaminato)aluminum\n''C27H18AlN3O3 tris-(8-hydroxyquinoline)aluminum\n''Alq3 aluminum 8-hydroxyquinolinate\n''C32H16AlClN8 aluminum phthalocyanine chloride\n''C32H17AlN8O aluminum phthalocyanine hydroxide\n''C48H24AlClN8 aluminum 2,3-naphthalocyanine chloride\n''C56H33AlN8O5 aluminum 2,9,16,23-tetraphenoxy-29H,31 H-phthalocyanine hydroxide\n''K2Al2O4·3H2O potassium aluminate trihydrate\n''Al(OH)(C2H3O2)2 aluminum diacetate\n''Al(OH)(C18H35O2)2 aluminum distearate\n''Al(OH)2(C18H35O2) aluminum monostearate\n''LiAl[OC(CH3)3]3D lithium tri-tert-butoxyaluminodeuteride\n''C36H52AlClN2O2 (R,R)-N,N'-bis(3,5-di-tert-butylsalicylidene)-1,2-cyclohexanediaminoaluminum chloride\n''C36H52AlClN2O2 (S,S)-N,N'-bis(3,5-di-tert-butylsalicylidene)-1,2-cyclohexanediaminoaluminum chloride\n''C56H32AlClN8O4 aluminum 2,9,16,23-tetraphenoxy-29H,31 H-phthalocyanine chloride\n''C56H32AlClN8S4 aluminum 1,8,15,22-tetrakis(phenylthio)-29H,31 H-phthalocyanine chloride\n''C56H32AlClN8S4 aluminum 2,9,16,23-tetrakis(phenylthio)-29H,31 H-phthalocyanine chloride\n''C70H95AlN8O9Si aluminum 1,4,8,11,15,18,22,25-octabutoxy-29H,31 H-phthalocyanine triethylsiloxide\n''(Mg,Fe+2,Al)3(Al,Si)4O10(OH)2·4(H2O) vermiculite\n''(Na,Ca)0.33(Al,Mg)2(Si4O10)(OH)2·nH2O montmorillonite\n''RbAl(SO4)2·12H2O rubidium aluminum sulfate dodecahydrate\n''LiAl[OC(C2H5)3]3H lithium tris[(3-ethyl-3-pentyl)oxy]aluminohydride\n'""", '13', '26.98')
        self.colorAl=colorAl="CadetBlue2"
        self.Al = tk.Button(self, text=Al[0], width=5, height=2, bg=colorAl, font=10, borderwidth=3,
                           command=lambda text=Al: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAl, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Al()])
        self.Al.grid(row=5, column=14)

        Ga = ('Ga', 'Gallium', """'Ga gallium\n''GaAs gallium arsenide\n''GaBr3 gallium(III) bromide\n''GaCl3 gallium trichloride\n''Ga2Cl4 gallium(II)chloride\n''GaF3 gallium fluoride\n''GaH3 gallium(III) hydride\n''GaI3 gallium(III) iodide\n''GaN gallium nitride\n''GaP gallium phosphide\n''GaS gallium(II) sulfide\n''GaSb gallium antimonide\n''GaSegallium(II) selenide\n''GaTe  gallium(II) telluride\n''Ga2O gallium suboxide\n''Ga2O3 gallium(III) oxide\n''Ga2S3 gallium(III) sulfide\n''Ga2Se3 gallium selenide\n''Ga2Te3 gallium(III) telluride\n''Ga(CH3)3 trimethylgallium\n''(CH3CH2)3Ga triethylgallium\n''Cl4GaLi lithium tetrachlorogallate\n''Gd3Ga5O12 gadolinium gallium garnet\n''GaHO2 gallium(III) oxide hydroxide\n''Ga(OH)3 gallium(III) hydroxide\n''Ga(NO3)3 gallium(III) nitrate\n''Ga(N(CH3)2)3 tris(dimethylamido)gallium(III)\n''[CH3COCH=C(O)CH3]3Ga gallium(III) acetylacetonate\n''Ga(CIO4)3·xH2o gallium(III)perchlorate hydrate\n''GaF3·3H2O gallium(III) fluoride trihydrate\n''Ga2(SO4)3 gallium(III) sulfate\n''Ga(NO3)3·xH2O gallium(III) nitrate hydrate\n''Ga2(SO4)3·xH2O gallium(III)sulfate hydrate\n''(NH4)3GaF6 ammonium hexafluorogallate\n''C16H36Cl4GaN tetrabutylammonium tetrachlorogallate\n''C27H18GaN3O3 tris(8-hydroxyquinolinato)gallium(III)\n''C28H44GaN9O13 gallichrome\n''C32H17GaN8O gallium(III)phthalocyanine hydroxide\n''C32H16ClGaN8 gallium(III)-phthalocyanine chloride\n''C48H24ClGaN8 gallium(III)2,3-naphthalocyanine chloride\n''Ga(ClO4)3·6H2O gallium(III) perchlorate hexahydrate\n'""", '31', '69.72')
        self.colorGa=colorGa="CadetBlue3"
        self.Ga = tk.Button(self, text=Ga[0], width=5, height=2, bg=colorGa, font=10, borderwidth=3,
                           command=lambda text=Ga: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorGa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ga()])
        self.Ga.grid(row=6, column=14)

        In = ('In', 'Indium', """'In indium\n''AsIn indium arsenide\n''InBr indium(I)bromide\n''InBr3 indium(III) bromide\n''InCl indium(I)chloride\n''InCl2 indium(II)chloride\n''InCl3 indium trichloride\n''InF3 indium(III)fluoride\n''InI indium monoiodide\n''InI3 indium(III) iodide\n''InN indium nitride\n''InP indium phosphide\n''InS indium(II) sulfide\n''InSb indium antimonide\n''In2O3 indium(III) oxide\n''In2S3 indium(III)sulfide red\n''In2Se3 indium(III)selenide\n''In2Te3 indium(III)telluride\n''C3H9In trimethylindium\n''In(OH)3 indium hydroxide\n''InPO4 indium(III) phosphate\n''In2(SO4)3 indium(III) sulfate\n''(In2O3)0.9·(SnO2)0.1 indium-tin oxide\n''In(C2H3O2)3 indium(III)acetate\n''(CH3CO2)3In·xH2O indium(III)acetate hydrate\n''In(OC(CH3)3)3 indium(III)tert-butoxide\n''In(OCCH3CHOCCH3)3 indium(III)acetylacetonate\n''InCl3·4H2O indium(III)chloride tetrahydrate\n''In(ClO4)3·xH2O indium(III)perchlorate hydrate\n''InF3·3H2O indium(III)fluoride trihydrate\n''In(NO3)3·xH2O indium(III)nitrate hydrate\n''In2(SO4)3·xH2O indium(III)sulfate hydrate\n''(CF3SO3)3In indium(III)trifluoromethanesulfonate\n''C32H16ClInN8 indium(III)phthalocyanine chloride\n''In(ClO4)3·8H2O indium(III) perchlorate octahydrate\n''In(NO)3·3H2O indium(III) nitrate trihydrate\n'""", '49', '69.72')
        self.colorIn=colorIn="turquoise2"
        self.In = tk.Button(self, text=In[0], width=5, height=2, bg=colorIn, font=10, borderwidth=3,
                           command=lambda text=In: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorIn, text[0], text[3], text[4]), self.voice(text[1]), self.compound_In()])
        self.In.grid(row=7, column=14)

        Tl = ('Tl', 'Thallium', """'Tl thallium\n''Tl3As thallium(I)arsenide\n''TlBr thallium(I) bromide\n''TlCl thallium chloride\n''Cl3Tl thallium(III) chloride\n''TlF thallium(I) fluoride\n''TlF3 thallium(III)fluoride\n''TlI thallium(I)iodide\n''OTl2 thallium(I) oxide\n''Tl2O3 thallium(III)oxide\n''Tl2S thallium(I)sulfide\n''Tl2S thallium sulfide\n''Tl2Se thallium(I) selenide\n''TlN3 thallium(I) azide\n''TlBrO3 thallium bromate\n''C5H5Tl cyclopentadienylthallium\n''TlClO3 thallium chlorate\n''Tl2CrO4 thallium chromate\n''F6PTl thallium(I) hexafluorophosphate\n''HOTl thallium(I) hydroxide\n''Tl(OH)3 thallium(III) hydroxide\n''IO3Tl thallium(I) iodate\n''TlIO3 thallium iodate\n''TlNO3 thallous nitrate\n''N3O9Tl thallium(III) nitrate\n''TlReO4 thallium(I)perrhenate\n''Tl2SO4 thallium(I)sulfate\n''O4STl2 thallium sulfate\n''O12S3Tl2 thallium(III) sulfate\n''TlCN thallium(I) cyanide\n''TlClO4 thallium(I) perchlorate\n''TlNO2 thallium(I) nitrite\n''Tl2C2O4 thallium(I) oxalate\n''Tl2MoO4 thallium(I) molybdate\n''Tl2SeO4 thallium(I) selenate\n''HCO2Tl thallium(I) formate\n''Tl2CO3 thallium(I)carbonate\n''TlSCN thallium thiocyanate\n''C2H3O2Tl thallium(I) acetate\n''Tl(CH3COO)3 thallium(III) acetate\n''TlOC2H5 thallium(I) ethoxide\n''C3H2O4Tl2 thallous malonate\n''TlC5H7O2 thallium(I)acetylacetonate\n''TlCl3·4H2O thallium(III)chloride tetrahydrate\n''Tl(ClO4)3·xH2O thallium(III)perchlorate hydrate\n''Tl(NO3)3·3H2O thallium(III)nitrate trihydrate\n''TlBr3·4H2O thallium(III) bromide tetrahydrate\n''Tl(CF3COO)3 thallium(III) trifluoroacetate\n''TlC5HF6O2 thallium(I)hexafluoroacetylacetonate\n'""", '81', '204.37')
        self.colorTl=colorTl="turquoise3"
        self.Tl = tk.Button(self, text=Tl[0], width=5, height=2, bg=colorTl, font=10, borderwidth=3,
                           command=lambda text=Tl: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTl, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Tl()])
        self.Tl.grid(row=8, column=14)

        Nh = ('Nh', 'Nihonium', """'Uut ununtrium ununtrium metal\n'""", '113', '286')
        self.colorNh=colorNh="CadetBlue4"
        self.Nh = tk.Button(self, text=Nh[0], width=5, height=2, bg=colorNh, font=10, borderwidth=3,
                           command=lambda text=Nh: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNh, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Nh()])
        self.Nh.grid(row=9, column=14)

        C = ('C', 'Carbon', """ """, '6', '12.01')
        self.colorC=colorC="wheat2"
        self.C = tk.Button(self, text=C[0], width=5, height=2, bg=colorC, font=10, borderwidth=3,
                           command=lambda text=C: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorC, text[0], text[3], text[4]), self.voice(text[1]), self.compound_C()])
        self.C.grid(row=4, column=15)

        Si = ('Si', 'Silicon', """'Si silicon \n''MoSi2 molybdenum disilicide \n''SiB4 silicon tetraboride \n''SiB6 silicon hexaboride \n''BaSi2 barium silicide \n''SiBr4 silicon tetrabromide \n''SiC silicon carbide \n''CaSi calcium silicide \n''CeSi2 cerium silicide \n''Cl2SiH2 dichlorosilane \n''SiHCl3 trichlorosilane \n''SiCl4 silicon tetrachloride \n''(SiCl3)2 hexachlorodisilane \n''Cl8Si3 octachlorotrisilane \n''CoSi2 cobalt silicide \n''CrSi2 chromium silicide \n''Cu5Si copper silicide \n''SiD4 deuterated silane \n''DySi2 dysprosium silicide \n''ErSi2 erbium silicide \n''EuSi2 europium silicide \n''SiF4 silicon tetrafluoride \n''F6Si2 hexafluorodisilane \n''F8Si3 octafluorotrisilane \n''FeSi iron silicide \n''FeSi2 iron disilicide \n''GdSi2 gadolinium silicide \n''SiH4 silane \n''Si2H6 disilane \n''H8Si3 trisilane \n''H10Si4 tetrasilane \n''H12Si5 pentasilane \n''HfSi2 hafnium silicide \n''HoSi2 holmium silicide \n''SiH2I2 diiodosilane \n''SiI4 silicon tetraiodide \n''LaSi2 lanthanum silicide \n''Mg2Si magnesium silicide \n''MnSi2 manganese silicide \n''Si3N4 silicon nitride \n''NbSi2 niobium silicide \n''SiO silicon monoxide \n''SiO2 cristobalite \n''SiO2 quartz \n''SiO2 silicon dioxide \n''SiO2 tridymite \n''PrSi2 praseodymium silicide \n''PtSi platinum silicide \n''ReSi2 rhenium(IV) silicide \n''S2Si silicon disulfide \n''SiS silicon monosulfide \n''SiV3 trivanadium monosilicide \n''Si2Br6 hexabromosilane \n''Si2I6 hexaiododisilane \n''TaSi2 tantalum silicide \n''Si2Th thorium silicide \n''TiSi2 titanium silicide \n''Si2U uranium disilicide \n''VSi2 vanadium silicide \n''WSi2 tungsten silicide \n''ZrSi2 zirconium silicide \n''Si3Br8 octabromotrisilane \n''Si4F10 decafluorotetrasilane \n''Si5H10 cyclopentasilane \n''Si6H12 cyclohexasilane \n''Si7H16 heptasilane \n''SmSi2 samarium silicide \n''SrSi2 strontium silicide \n''TbSi2 terbium silicide \n''YbSi2 ytterbium silicide \n''3Al2O3·2SiO2 aluminum silicate \n''BaSiF6 barium hexafluorosilicate \n''BaSiO3 barium metasilicate \n''Be2O4Si diberyllium monosilicate \n''BrCl3Si bromotrichlorosilane \n''Br2Cl2Si dibromodichlorosilane \n''Br2H2Si dibromosilane \n''Br3ClSi tribromochlorosilane \n''Cl3CSiCl3 trichloro(trichloromethyl)silane \n''CH3SiH3 methylsilane \n''(CH4Si)n poly(carbodihydridosilane) \n''C2Cl8Si dichlorobis(trichloromethyl)silane \n''(C2H6Si)n polycarbomethylsilane \n''(C2H5)2SiH2 diethylsilane \n''CH3SiH2CH2CH2SiH2CH3 1,2-ethanediylbis(methylsilane) \n''CH3CH2SiH(CH3)2 dimethylethylsilane \n''Si(CH3)4 tetramethylsilane \n''(CH3)2SiHSiH(CH3)2 1,1,2,2-tetramethyldisilane \n''(CH3)3SiC≡CH trimethylsilylacetylene \n''(CH3)3SiCHCH2 vinyltrimethylsilane \n''(C2H5)2SiHCH3 diethylmethylsilane \n''(CH3)2CHSiH(CH3)2 dimethylisopropylsilane \n''C5H14Si ethyl-trimethyl-silane \n''(CH3)3SiSi(CH3)2H pentamethyldisilane \n''C6H5SiH3 phenylsilane \n''CH3C≡CSi(CH3)3 1-(trimethylsilyl)-1-propyne \n''(H2C=CH)2Si(CH3)2 divinyldimethylsilane \n''HC≡CCH2Si(CH3)3 trimethyl(propargyl)silane \n''H2C=CHCH2Si(CH3)3 allyltrimethylsilane \n''(CH3)3CSiH(CH3)2 tert-butyldimethylsilane \n''(C2H5)3SiH triethylsilane \n''(Si(CH3)3)2 hexamethyldisilane \n''C6H5SiH2(CH3) methylphenylsilane \n''C7H12Si trivinylmethylsilane \n''H2C=C=C(CH3)Si(CH3)3 1-methyl-1-(trimethylsilyl)allene \n''CH3Si(C2H5)2CH=CH2 diethylmethylvinylsilane \n''H2C=C(CH3)CH2Si(CH3)3 methallyltrimethylsilane \n''(CH3)3SiSi(CH3)2C≡CH (pentamethyldisilyl)acetylene \n''[(CH3)3Si]2CH2 silane, methylenebis[trimethyl- \n''C6H5SiH(CH3)2 dimethylphenylsilane \n''Si(CH=CH2)4 tetravinylsilane \n''C8H14Si cyclopentadienyltrimethylsilane \n''CH3CH2CH2C≡CSi(CH3)3 1-trimethylsilyl-1-pentyne \n''(H2C=CHCH2)2Si(CH3)2 diallyldimethylsilane \n''(C2H5)3SiC≡CH (triethylsilyl)acetylene \n''(CH3)3CSi(CH3)2C≡CH (tert-butyldimethylsilyl)acetylene \n''C6H11SiH(CH3)2 cyclohexyldimethylsilane \n''H2C=CHSi(C2H5)3 triethylvinylsilane \n''(CH3)3SiC≡CSi(CH3)3 silane, 1,2-ethynediylbis[trimethyl- \n''[(CH3)3C]2SiH2 ditert-butylsilane \n''Si(C2H5)4 tetraethylsilane \n''C6H5CH2SiH(CH3)2 benzyldimethylsilane \n''C6H5Si(CH3)3 trimethylphenylsilane \n''CH3(CH2)3C≡CSi(CH3)3 1-trimethylsilyl-1-hexyne \n''[(CH3)2CH]3SiH triisopropylsilane \n''(CH3CH2CH2)3SiH tripropylsilane \n''(CH3)3SiCH2C[Si(CH3)3]=CH2 2,3-bis(trimethylsilyl)-1-propene \n''[(CH3)3Si]3SiH tris(trimethylsilyl)silane \n''C6H5C≡CSiH(CH3)2 1-(dimethylsilyl)-2-phenylacetylene \n''C6H5Si(CH3)2C≡CH (dimethylphenylsilyl)acetylene \n''C6H5Si(CH3)2CH=CH2 dimethylphenylvinylsilane \n''C6H5CH2Si(CH3)3 benzyltrimethylsilane \n''C6H5CH2CH2SiH(CH3)2 dimethylphenethylsilane \n''C6H4[SiH(CH3)2]2 1,4-bis(dimethylsilyl)benzene \n''(CH3)3SiC≡CC≡CSi(CH3)3 1,4-bis(trimethylsilyl)butadiyne \n''[(CH3)3Si]3CH tris(trimethylsilyl)methane \n''C6H5C≡CSi(CH3)3 1-phenyl-2-trimethylsilylacetylene \n''[(CH3)2CH]3SiC≡CH (triisopropylsilyl)acetylene \n''(C6H5)2SiH2 diphenylsilane \n''C12H16Si 1 H-inden-1-yltrimethylsilane \n''(CH3)3SiC≡CC6H4CH3 2-[(trimethylsilyl)ethynyl]toluene \n''(H2C=CHCH2)4Si tetraallylsilane \n''C12H22Si trimethyl(2,3,4,5-tetramethyl-2,4-cyclopentadien-1-yl)silane \n''C6H4[Si(CH3)3]2 1,4-bis(trimethylsilyl)benzene \n''[(CH3)2CH]3SiC≡CCH3 1-(triisopropylsilyl)-1-propyne \n''[(CH3)2CH]3SiCH2CH=CH2 allyltriisopropylsilane \n''[CH3(CH2)3]3SiH tributylsilane \n''[(CH3)2CHCH2]3SiH triisobutylsilane \n''[(CH3)3Si]4Si tetrakis(trimethylsilyl)silane \n''(Si(CH3)2)6 dodecamethylcyclohexasilane \n''(C6H5)2SiHCH3 methyldiphenylsilane \n''C6H4CH2CH3C≡CSi(CH3)3 (4-ethylphenylethynyl)trimethylsilane \n''C13H24Si trimethyl(1,2,3,4,5-pentamethyl-2,4-cyclopentadien-1-yl)silane \n''(C6H5)2Si(CH3)2 dimethyldiphenylsilane \n''(C2H5)3SiC≡CSi(C2H5)3 bis(triethylsilyl)acetylene \n''CH3(CH2)7SiH[CH(CH3)2]2 diisopropyloctylsilane \n''CH3Si(C6H5)2C≡CH (methyldiphenylsilyl)acetylene \n''C10H7C≡CSi(CH3)3 1-(1-naphthyl)-2-(trimethylsilyl)acetylene \n''C6H4[C≡CSi(CH3)3]2 1,4-bis[(trimethylsilyl)ethynyl]benzene \n''C17H38Si4 2,3,5,5-tetrakis(trimethylsilyl)-1,3-cyclopentadiene \n''(C6H5)3SiH triphenylsilane \n''(H2C=CHCH2)2Si(C6H5)2 diallyldiphenylsilane \n''CH3(CH2)17SiH3 octadecylsilane \n''[CH3(CH2)5]3SiH trihexylsilane \n''(C6H5)3SiC≡CH (triphenylsilyl)acetylene \n''(C6H5)3SiCH=CH2 triphenylvinylsilane \n''C20H32Si dimethylbis(2,3,4,5-tetramethyl-2,4-cyclopentadien-1-yl)silane \n''CH3(CH2)17SiH(CH3)2 dimethyloctadecylsilane \n''H2C=CHCH2Si(C6H5)3 allyltriphenylsilane \n''[CH3(CH2)7]3SiH trioctylsilane \n''(SiCH3(C6H5)2)2 1,2-dimethyl-1,1,2,2-tetraphenyldisilane \n''C26H34Si2 1,2-bis[1-(trimethylsilyl)-1 H-inden-3-yl)ethane,mixture of isomers \n''C28H24Si di-9 H-fluoren-9-yldimethylsilane \n''C28H42Si2 1,4-bis[dimethyl[2-(5-norbornen-2-yl)ethyl]silyl]benzene \n''(Si(C6H5)2)4 octaphenylcyclotetrasilane \n''CaSiF6 calcium hexafluorosilicate \n''CaSiO3 calcium silicate \n''Ca3O5Si tricalcium silicate \n''CdF6Si cadmium fluosilicate \n''CdO3Si cadmium metasilicate \n''ClF3Si chlorotrifluorosilane \n''Cl3FSi trichlorofluorosilane \n''Cl3SiOSiCl3 hexachlorodisiloxane \n''Co2SiO4 cobalt(II) orthosilieate \n''F2H2Si difluorosilane \n''F3HSi trifluorosilane \n''H2SiF6 fluorosilicic acid \n''K2SiF6 potassium hexafluorosilicate \n''Na2SiF6 sodium fluorosilicate \n''PbSiF6 lead(II) hexafluorosilicate \n''F6SiZn zinc silicofluoride \n''FeLiSi lithium ferrosilicon \n''Fe2SiO4 iron(II) orthosilieate \n''HI3Si triiodosilane \n''H2O3Si metasilicic acid \n''H4O4Si orthosilicic acid \n''H6OSi2 disiloxane \n''HfSiO4 hafnium(IV) silicate \n''Li2O3Si lithium silicate \n''Li2Si5O11 lithium polysilicate \n'""", '14', '28.09')
        self.colorSi=colorSi="wheat3"
        self.Si = tk.Button(self, text=Si[0], width=5, height=2, bg=colorSi, font=10, borderwidth=3,
                           command=lambda text=Si: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSi, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Si()])
        self.Si.grid(row=5, column=15)

        Ge = ('Ge', 'Germanium', """'Ge germanium \n''GeBr2 germanium(II)bromide \n''GeBr4 germanium tetrabromide \n''Cl2Ge germanium(II) chloride \n''GeCl4 germanium(IV)chloride \n''GeF4 germanium(IV)fluoride \n''GeF2 germanium(II) fluoride \n''GeH4 germane \n''GeH31 iodogermane \n''GeI2 germanium(II)iodide \n''GeI4 germanium(IV) iodide \n''GeO germanium(II) oxide \n''GeO2 germanium dioxide \n''GeS germanium(II)sulfide \n''GeS2 germanium(IV) sulfide \n''GeSe germanium(II)selenide \n''GeSe2 germanium(IV) selenide \n''GeTe germanium telluride \n''Ge2H6 digermane \n''Ge3H8 trigermane \n''Ge3N4 germanium(III)nitride \n''Ge4H10 tetragermane \n''Ge5H12 pentagermane \n''Mg2Ge magnesium germanide \n''BaGeF6 barium hexafluorogermanate \n''BrGeH3 bromogermane \n''Br2GeH2 dibromogermane \n''CH6Ge methylgermane \n''(CH3)4Ge tetramethylgermane \n''(C2H5)3GeH triethylgermanium hydride \n''(CH3)3GeGe(CH3)3 hexamethyldigermanium(IV) \n''Ge(C2H5)4 tetraethylgermanium \n''[CH3(CH2)3]3GeH tributylgermanium hydride \n''(CH3CH2CH2)4Ge tetrapropylgermanium \n''(C2H5)3GeGe(C2H5)3 hexaethyldigermanium(IV) \n''Ge(C4H9)4 tetrabutylgermanium \n''(C6H5)3GeH triphenylgermanium hydride \n''Ge(C6H5)4 tetraphenylgermanium \n''(C6H5)3GeGe(C6H5)3 hexaphenyldigermanium(IV) \n''ClGeH3 chlorogermane \n''Cl2GeH2 dichlorogermane \n''Cs2GeF6 cesium hexafluorogermanate \n''FGeH3 fluorogermane \n''GeF3Cl chlorotrifluorogermane \n''GeHBr3 tribromogermane \n''GeHCl3 trichlorogermane \n''Mg2GeO4 magnesium germanate \n''Na2GeO3 sodium germanate \n''Rb2GeF6 rubidium hexafluorogermanate \n''2Bi2O3·3GeO2 bismuth germanium oxide \n''C2H5GeCl3 ethylgermanium trichloride \n''(CH3)2GeCl2 dichlorodimethylgermane \n''(CH3)3GeBr trimethylgermanium bromide \n''(CH3)3GeCl chlorotrimethylgermane \n''(CH3)3GeI trimethylgermanium iodide \n''(C2H5)2GeCl2 dichlorodiethylgermane \n''Ge(OCH3)4 germanium(IV)methoxide \n''C6H5GeCl3 phenylgermanium trichloride \n''O[Ge(=O)CH2CH2CO2H]2 carboxyethylgermanium sesquioxide \n''(C2H5)3GeCl chlorotriethylgermane \n''[CH3(CH2)3]2GeCl2 dibutylgermanium dichloride \n''Ge(OC2H5)4 germanium(IV)ethoxide \n''[(CH3)3Si]3GeH tris(trimethylsilyl)germanium hydride \n''(C6H5)2GeCl2 diphenylgermanium dichloride \n''[CH3(CH2)3]3GeCl tributylgermanium chloride \n''Ge(OCH(CH3)2)4 germanium(IV)isopropoxide \n''(C6H5)3GeBr triphenylgermanium bromide \n''(C6H5)3GeCl triphenylgermanium chloride \n''[(C6H5)3Ge]2O hexaphenyldigermoxane \n''(NH4)2GeF6 ammonium hexafluorogermanate \n''C4H8Cl2GeO2 germanium(II)chloride dioxane complex(1:1) \n''C6H12GeK2O6 dipotassium tris(1,2-benzenediolato-O,O')germanate \n''C9H15GeN3NaO6-5 naphtha (petroleum), heavy straight run, arom.-contg \n'""", '32', '72.59')
        self.colorGe=colorGe="wheat4"
        self.Ge = tk.Button(self, text=Ge[0], width=5, height=2, bg=colorGe, font=10, borderwidth=3,
                           command=lambda text=Ge: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorGe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ge()])
        self.Ge.grid(row=6, column=15)
        
        Sn = ('Sn', 'Tin', """'Sn gray tin \n''Sn white tin \n''SnBr2 tin(II)bromide \n''SnBr4 tin(IV) bromide \n''SnCl2 stannous chloride \n''SnCl4 stannic chloride \n''CuSn copper-tin alloy \n''F2Sn tin difluoride \n''SnF4 tin(IV) fluoride \n''H4Sn stannane \n''SnI2 tin(II)iodide \n''SnI4 tin(IV)iodide \n''Mg2Sn magnesium stannide \n''SnO stannous oxide \n''SnO2 stannic oxide \n''PSn tin monophosphide \n''SnS tin(II)sulfide \n'SnS2 tin(IV) sulfide \n''SnSe tin(II) selenide \n''SnSe2 tin(IV) selenide \n''SnTe tin(II) telluride \n''Sn4P3 tin triphosphide \n''Sn(BF4)2 tin bis(tetrafluoroborate) \n''BaO3Sn barium stannate \n''Sn(CH3)4 tetramethyltin \n''(CH3)3SnSn(CH3)3 hexamethylditin \n''Sn(CH=CH2)4 tetravinylstannane \n''(CH3)3SnC≡CSn(CH3)3 bis(trimethylstannyl)acetylene \n''Sn(C2H5)4 tetraethyltin \n''C6H5Sn(CH3)3 trimethyl(phenyl)tin \n''C6H5C≡CSn(CH3)3 trimethyl(phenylethynyl)tin \n''(H2C=CHCH2)4Sn tetraallyltin \n''[CH3(CH2)3]3SnH tributyltin hydride \n''HC≡CSn(CH2CH2CH2CH3)3 ethynyltributylstannane \n''CH2=CHSn[CH3(CH2)3]3 tributylvinylstannane \n''[CH3(CH2)3]3SnCH=C=CH2 allenyltributyltin(IV) \n''[CH3(CH2)3]3SnC≡CCH3 tributyl(1-propynyl)tin \n''CH2=CHCH2Sn(CH2CH2CH2CH3)3 allyltributylstannane \n''(CH3CH2CH2CH2)4Sn tetra-N-butyltin \n''[CH3(CH2)3]3SnCH2CH=C(CH3)2 tributyl(3-methyl-2-butenyl)tin \n''(C6H5)3SnH triphenyltin hydride \n''C6H5Sn[(CH2)3CH3]3 tributylphenylstannane \n''(C6H11)3SnH tricyclohexyltin hydride \n''[CH3(CH3)3]2Sn(C6H5)2 dibutyldiphenyltin \n''C6H5C≡CSn[(CH2)3CH3]3 tributyl(phenylethynyl)tin \n''[CH3(CH2)4]4Sn tetrapentyltin \n''CH2=CHCH2Sn(C6H5)3 allyltriphenylstannane \n''Sn(C6H5)4 tetraphenylstannane \n''(CH3CH2CH2CH2)3SnSn(CH2CH2CH2CH3)3 hexa-N-butylditin \n''[CH3(CH2)3]3SnC≡CSn[(CH2)3CH3]3 bis(tributylstannyl)acetylene \n''[(C6H5)3Sn]2 hexaphenylditin(IV) \n''Co2SnO4 cobalt(II) stannate \n''CuSnO3 copper(II) stannate \n''Sn(OH)2 tin(II) hydroxide \n''(In2O3)0.9·(SnO2)0.1 indium-tin oxide \n''K2O3Sn potassium stannate \n''Li2SnF6 lithium hexafluorostannate \n''Na2SnO3 sodium stannate \n''SnSO4 stannous sulfate \n''Sn2P2O7 tin(II) pyrophosphate \n''Sn(CrO4)2 tin(IV) chromate \n''SnH3eH3 methylstannane \n''Sn(SeO3)2 tin(IV) selenite \n''SnZrF6 tin(II) hexafluorozirconate \n''BiCdPbSn woods metal \n''CH3SnCl3 methyltin trichloride \n''SnC2O4 tin(II) oxalate \n''(CH3)2SnBr2 dimethyltin dibromide \n''(CH3)2SnCl2 dimethyltin dichloride \n''C2H6F2Sn difluorodimethylstannane \n''(CH3)3SnBr trimethyltin bromide \n''(CH3)3SnCl trimethyltin chloride \n''(CH3)3SnN3 azidotrimethyltin(IV) \n''C4H4O6Sn stannous tartrate \n''Sn(CH3CO2)2 stannous acetate \n''CH3(CH2)3SnCl3 butyltrichlorotin \n''CH3(CH2)3Sn(=O)OH·xH2O butyltin hydroxide oxide hydrate \n''(CH3)3SnN(CH3)2 (dimethylamino)trimethyltin(IV) \n''C6H5SnCl3 trichlorophenyltin \n''(CH3CO2)2Sn(CH3)2 dimethyltin diacetate \n''(C2H5)3SnBr bromotriethylstannane \n''Sn(CH3CO2)4 tin(IV)acetate \n''C8H17Cl3Sn mono-N-octyltin trichloride \n''[CH3(CH2)3]2SnBr2 dibutyltin dibromide \n''[(CH3)3C]2SnCl2 di-tert-butyltin dichloride \n''(CH3CH2CH2CH2)2SnCl2 dibutyldichlorotin \n''(CH3CH2CH2CH2)2SnO dibutyltin oxide \n''C9H21ClSn chlorotripropylstannane \n''[CH3(CH2)3]2Sn(OCH3)2 dibutyldimethoxytin \n''(C6H5)2SnCl2 diphenyltin dichloride \n''(C6H5)2Sn(=O) diphenyltin(IV)oxide \n''C12H20O4Sn dibutyltin maleate \n''(CH3CH2CH2CH2)2Sn(OCOCH3)2 dibutyltin diacetate \n''[CH3(CH2)3]3SnBr tributyltin bromide \n''[CH3(CH2)3]3SnCl tri-N-butyltin chloride \n''[(CH3CH2CH2CH2)3SnF]n tributyltin fluoride polymer \n''[CH3(CH2)3]3SnI tributyltin iodide \n''[CH3(CH2)3]3SnN3 azidotributyltin(IV) \n''[CH3(CH2)3]3SnCN tri-N-butyltin cyanide \n''[CH3(CH2)3]3SnOCH3 tributyltin methoxide \n''CH3CO2Sn[(CH2)3CH3]3 tributyltin acetate \n''[CH3(CH2)3]3SnOC2H5 tributyltin ethoxide \n''[CH3(CH2)3]3SnSi(CH3)3 trimethyl(tributylstannyl)silane \n''(C4H3N2)Sn[(CH2)3CH3]3 2-(tributylstannyl)pyrazine \n''C16H30OSn 2-(tributylstannyl)furan \n''[CH3(CH2)3CH(C2H5)CO2]2Sn tin(II)2-ethylhexanoate \n''C16H30SSn 2-(tributylstannyl)thiophene \n''C16H34Cl2Sn di-N-octyltin dichloride \n''C16H34OSn di-N-octyltin oxide \n''[CH3(CH2)3]3SnC(OC2H5)=CH2 tributyl(1-ethoxyvinyl)tin \n''[CH3(CH2)3O]2Sn[(CH2)3CH3]2 dibutoxydibutyltin \n''Sn(OC(CH3)3)4 tin(IV)tert-butoxide \n''[(C2H5)2N]4Sn tetrakis(diethylamido)tin(IV) \n''[H3C(C4H3N)]Sn[(CH2)3CH3]3 1-methyl-2-(tributylstannyl)pyrrole \n''(C6H5)3SnCl triphenyltin chloride \n''(C6H5)3SnF triphenyltin fluoride \n''(C6H5)3SnOH triphenyltin hydroxide \n''[CH3COCH=C(O)CH3]2Sn[(CH2)3CH3]2 dibutyltin bis(acetylacetonate) \n''(C6H11)3SnCl tricyclohexyltin chloride \n''(C6H5)3CSnCl5 trityl pentachlorostannate \n''C6H5CO2Sn[(CH2)3CH3]3 tributyltin benzoate \n''CH3C(O)OSn(C6H5)3 phentin acetate \n''C20H32SSn 2-tributylstannylbenzo[b]thiophene \n''C20H35N3Sn azocyclotin \n''(CH3CO2Sn((CH2)3CH3)2)2O 1,3-diacetoxy-1,1,3,3-tetrabutyldistannoxane \n''C22H32O2Sn (+)-(1r,2r)-1,2-diphenylethane-1,2-diol \n''[CH3(CH2)3CH(C2H5)CO2]2Sn[(CH2)3CH3]2 dibutyltin bis(2-ethylhexanoate) \n''(CH3CH2CH2CH2)3SnOSn(CH2CH2CH2CH3)3 bis(tributyltin)oxide \n''[CH3(CH2)3CH(C2H5)CO2]3Sn(CH2)3CH3 butyltin tris(2-ethylhexanoate) \n''C32H16N8Sn tin(II)phthalocyanine \n''(CH3CH2CH2CH2)2Sn[OCO(CH2)10CH3]2 dibutyltin dilaurate \n''C32H68S2Sn dibutylbis(dodecylthio)stannane \n''[(C6H11)3Sn]2S bis(tricyclohexyltin(IV))sulfide \n''C48H24N8Sn tin(II)2,3-naphthalocyanine \n''SnCl2·2H2O stannous chloride dihydrate \n''SnCl4·5H2O stannic chloride pentahydrate \n''K2SnO3·3H2O potassium stannate trihydrate \n''Na2SnO3·3H2O sodium stannate trihydrate \n''(NH4)2SnF6 ammonium hexafluorostannate \n''BaSnO3·3H2O barium stannate trihydrate \n''Bi2(SnO3)3·5H2O bismuth stannate pentahydrate \n''Sn(CH3SO3)2 tin(II)methanesulfonate \n''CH3(CH2)3Sn(OH)2Cl butyltin chloride dihydroxide \n''[CH3COCH=C(O)CH3]2SnBr2 tin(IV)bis(acetylacetonate)dibromide \n''[CH3COCH=C(CH3)O]2SnCl2 tin(IV)bis(acetylacetonate)dichloride \n''C10H18N2S2Sn dibutyltin diisothiocyanate \n''[[(CH3)3Si]2N]2Sn bis[bis(trimethylsilyl)amino]tin(II) \n''[CH3(CH2)3]3SnNCO tributyltin isocyanate \n''C15H29NOSn 2-(tri-n-butylstannyl)oxazole \n''C15H29NSSn 2-tributylstannylthiazole \n''[CH3(CH2)3]3SnN(C2H5)CO2CH3 methyl ethyl(tributylstannyl)carbamate \n''((CH3(CH2)3)2SnCl)2O bis(dibutylchlorotin(IV))oxide \n''C32H16Cl2N8Sn tin(IV)phthalocyanine dichloride \n''C32H16N8OSn tin(IV)phthalocyanine oxide \n''(CH3CH2CH2CH2)4N[(C6H5)3SnF2] tetrabutylammonium difluorotriphenylstannate \n''C34H66O6S3Sn stannane, butyltris(isooctyloxycarbonylmethylthio) \n''C36H72O4S2Sn dioctyltin bis(isooctyl thioglycolate) \n''CaSnO3·3H2O calcium stannate trihydrate \n''NiSnO3·2H2O nickel(II) stannate dihydrate \n''(CF3SO3)2Sn tin(II)trifluoromethanesulfonate \n''CF3SO3Sn[(CH2)3CH3]3 tributylstannyl trifluoromethanesulfonate \n'""", '50', '118.69')
        self.colorSn=colorSn="azure1"
        self.Sn = tk.Button(self, text=Sn[0], width=5, height=2, bg=colorSn, font=10, borderwidth=3,
                           command=lambda text=Sn: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSn, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Sn()])
        self.Sn.grid(row=7, column=15)
        
        Pb = ('Pb', 'Lead', """'Pb lead \n''PbBr2 lead(II) bromide \n''Br4Pb lead(IV) bromide \n''PbCl2 lead(II) chloride \n''Cl4Pb lead tetrachloride \n''PbF2 lead fluoride \n''PbF4 lead(IV)fluoride \n''H4Pb plumbane \n''PbI2 lead iodide \n''Pb(N3)2 lead(II) azide \n''NaPb sodium-lead alloy \n''PbO lead monoxide \n''PbO2 lead dioxide \n''Pb3O4 lead(II,IV) oxide \n''PbS lead sulfide \n''PbSe lead(II) selenide \n''PbTe lead(II)telluride \n''As2O4Pb lead arsenite \n''As2O6Pb lead metaarsenate \n''Pb3(AsO4)2 lead(II) arsenate \n''BaPbO3 barium plumbate \n''PbCO3 cerussete \n''Pb(CN)2 lead(II) cyanide \n''PbC2O4 lead(II) oxalate \n''(CH3)4Pb tetramethyllead \n''C5H14Pb ethyltrimethyllead \n''C6H16Pb diethyldimethyllead \n''C7H18Pb methyltriethyllead \n''(C2H5)4Pb lead tetraethyl \n''Pb(C6H5)4 tetraphenyllead(IV) \n''(C6H5)3PbC≡CC6H5 triphenyl(phenylethynyl)lead(IV) \n''[(C6H5)3Pb]2 hexaphenyldilead(IV) \n''Ca2PbO4 calcium plumbate \n''ClFPb lead(II) chloride fluoride \n''Pb(ClO4)2 lead perchlorate \n''PbCrO4 lead(II) chromate \n''CrO5Pb2 lead chromate oxide \n''PbSiF6 lead(II) hexafluorosilicate \n''Pb(OH)2 lead(II) hydroxide \n''Pb(IO3)2 lead(II)iodate \n''PbMoO4 lead(II) molybdate \n''N2O4Pb lead nitrite \n''Pb(NO3)2 lead(II)nitrate \n''Pb(NbO3)2 lead(II)niobate \n''PbO·PbSO3 basic lead(II) sulfite \n''2PbO·PbSO3 dibasic lead(II) sulfite \n''O3PbS2 lead tetrathionate \n''O3PbS2 lead thiosulfate \n''PbSeO3 lead(II)selenite \n''1.5PbO·SiO2 lead silicate \n''PbTiO3 lead(II) titanate \n''PbZrO3 lead(II)zirconate \n''PbxSO4 anglislite lead(II) sulfate \n''4PbO·PbSO4 tetrabasic lead(II) sulfate \n''O4PbTe lead tellurate \n''PbWO4 lead tungstate \n''Pb(VO3)2 lead(II) metavanadate \n''Pb3(PO4)2 lead(II) phosphate \n''O8Pb3Sb2 lead(II) antimonate \n''Pb(ClO2)2 lead(II) chlorite \n''Pb(ClO3)2 lead(II) chlorate \n''PbSO3 lead(II) sulfite \n''PbSeO4 lead(II) selenate \n''Pb(TaO3)2 lead(II) tantalate \n''Pb2SiO4 lead(II) orthosilicate \n''PbHAsO4 schultenite \n''PbCO3 lead(II) carbonate \n''C2H2O4Pb lead(II) formate formic acid\n''2PbCO3·Pb(OH)2 basic lead(II) carbonate \n''C2H6PbS2 lead(II) methylthiolate \n''(CH3)3PbBr bromotrimethyllead(IV) \n''C4H6O4Pb lead(II) acetate \n''2Pb(OH)2·Pb(CH3CO2)2 basic lead(II) acetate \n''Pb(CH3CO2)2·3H2O lead(II)acetate trihydratez\n''CH3CO2Pb(CH3)3 acetoxytrimethyllead(IV) \n''PbC6H10O6 lead(II) lactate \n''C6H15ClPb triethyl lead chloride \n''Pb(CH3CO2)4 lead tetraacetate \n''C8H14O4Pb lead(II) butanoate \n''CH3CO2Pb(C2H5)3 acetoxytriethyllead(IV) \n''Pb(C5H7O2)2 lead(II)acetylacetonate \n''Pb(OCOC6H4OH)2 lead(II)salicylate \n''C16H30O4Pb lead(II) 2-ethylhexanoate \n''C16H32O4Pb octanoic acid, lead(2+) salt \n''(C6H5)3PbCl chlorotriphenyllead(IV) \n''C20H34O4Pb lead bis(4-cyclohexylbutyrate) \n''C32H16N8Pb lead(II)phthalocyanine \n''C36H66O4Pb lead(II) oleate \n'C36H70O4Pb lead stearate \n''Pb(ClO4)2·xH2O lead(II)perchlorate hydrate \n''HO4PPb lead(II) hydrogen phosphate \n''PbSO4 milk white \n''Pb(H2PO2)2 lead(II) hypophosphite \n''3PbO·H2O lead(II) oxide hydrate \n''Pb(SCN)2 lead(II) thiocyanate \n''Pb(CH3SO3)2 lead(II)methanesulfonate \n''PbC6H3N3O8 lead(II) styphnate \n''C6H12N2PbS4 lead dimethyldithiocarbamate \n''Pb(BO2)2·H2O lead(II) borate monohydrate \n''Pb(BrO3)2·H2O lead(II) bromate monohydrate \n''PbSiF6·2H2O lead(II) hexafluorosilicate dihydrate \n''Pb3(C6H5O7)2·3H2O lead(II) citrate trihydrate \n''Pb(CF3COCHCOCF3)2 lead(II) hexafluoro 2,4-pentanedioate\n'""", '82', '207.20')
        self.colorPb=colorPb="azure2"
        self.Pb = tk.Button(self, text=Pb[0], width=5, height=2, bg=colorPb, font=10, borderwidth=3,
                           command=lambda text=Pb: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPb, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Pb()])
        self.Pb.grid(row=8, column=15)

        Fl = ('Fl', 'Flerovium', """'Fl flerovium flerovium metal\n'""", '114', '289')
        self.colorFl=colorFl="azure3"
        self.Fl = tk.Button(self, text=Fl[0], width=5, height=2, bg=colorFl, font=10, borderwidth=3,
                           command=lambda text=Fl: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorFl, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Fl()])
        self.Fl.grid(row=9, column=15)

        N = ('N', 'Nitrogen', """'N2 liquid nitrogen \n''N2 nitrogen \n''AgN3 silver azide \n''AlN aluminum nitride \n''BN boron nitride \n''C2N2 cyanogen \n''C3N12 cyanuric triazide \n''(NC)2C=C(CN)2 tetracyanoethylene \n''Ca3N2 calcium nitride \n''CeN cerium nitride \n''ClN3 chlorine azide \n''Cl3N nitrogen trichloride \n''CsN3 cesium azide \n''CuN3 copper(I) azide \n''CuN6 copper(II) azide \n''Cu3N copper nitride \n''ND3 ammonia-d 3 \n''15ND3 ammonia-15 N,d 3 \n''D2NND2·2DCl hydrazine-d 4dideuteriochloride \n''DyN dysprosium nitride \n''ErN erbium nitride \n''EuN europium nitride \n''F2N2 cis-difluorodiazine \n''F2N2 trans-difluorodiazine \n''F3N nitrogen trifluoride \n''F4N2 tetrafluorohydrazine \n''GaN gallium nitride \n''GdN gadolinium nitride \n''Ge3N4 germanium(III)nitride \n''HNN≡N hydrazoic acid \n''H2NR acceptor-nh2 \n''H2NR an amine \n''H2NR substituted-amine \n''NH3 ammonia \n''15NH3 ammonia-15 N \n''NH2NH2 diazane \n''H4N4 ammonium azide \n''HfN hafnium nitride \n''Hg2N6 mercury azide \n''HoN holmium nitride \n''IN3 iodine azide \n''I3N nitrogen triiodide \n''InN indium nitride \n''LaN lanthanum nitride \n''LiN3 lithium azide \n''LuN lutetium nitride \n''Mg3N2 magnesium nitride \n''MoN molybdenum nitride (MaN) \n''MoN molybdenum nitride (1:1) \n''NbN niobium nitride \n''NNd neodymium nitride \n''NO nitric oxide \n''15NO nitric-15 noxide \n''15N18O nitric-15 noxide-18 O \n''15N2O nitrous oxide-15 N2 \n''NO2 nitrogen dioxide \n''NPr praseodymium nitride \n''TaN tantalum nitride \n''NTb terbium nitride \n''TiN titanium nitride \n''NU uranium nitride \n''VN vanadium nitride \n''ZrN zirconium nitride \n''N2O nitrous oxide \n''N2O3 nitrogen trioxide \n''N2O4 nitrogen tetroxide \n''N2O5 nitrogen pentoxide \n''NaN3 sodium azide \n''N4S4 tetrasulfur tetranitride \n''Si3N4 silicon nitride \n''Pb(N3)2 lead(II) azide \n''PuN plutonium nitride \n''ThN thorium nitride \n''TlN3 thallium(I) azide \n''AgNO2 silver nitrite \n''AgNO3 silver nitrate \n''Al(NO3)3 aluminum nitrate \n''H3N·BH3 borane-ammonia complex \n''B3H6N3 borazine \n''BaN2O4 barium nitrite \n''Ba(NO3)2 barium nitrate \n''Be(NO3)2 beryllium nitrate \n''BiNO4 bismuth oxynitrate \n''ND4Br ammonium-d 4bromide \n''15NH4Br ammonium-15 nbromide \n''NH4Br ammonium bromide \n''H2NNH2·HBr hydrazine monohydrobromide \n''BrNO nitrosyl bromide \n''Br2H6N2 hydrazine dihydrobromide dihydrate \n''AgCN silver cyanide \n''Ag13C15N silver cyanide-13 C,15 N \n''AuCN gold cyanide \n''BrCN cyanogen bromide \n''CaNCN calcium cyanamide \n''CClN cyanogen chloride \n''13C3N3Cl3 cyanuric chloride-13 C3 \n''CuCN cuprous cyanide \n''Cu13CN copper(I)cyanide-13 C \n''CuC15N copper(I)cyanide-13 C,15 N \n''CuC15N copper(I)cyanide-15 N \n''CD3ND2 methylamine-d 5 \n''D2NC(=ND)ND2 guanidine-d 5deuterochloride \n''CFN cyanogen fluoride \n''HCN hydrogen cyanide \n''NCNH2 cyanamide \n''CH2N2 diazomethane \n''(N=C=N)n polycarbodiimide \n''CH2N4 1H-tetrazole \n''13CH313CN acetonitrile-13 C2 \n''13CH313C15N acetonitrile-13 C2,15 N \n''CH3N5 5-aminotetrazole \n''CH4NR a methylated amine \n''CH4N2 ammonium cyanide \n''CH3NH2 methylamine \n''CH3NHNH2 monomethylhydrazine \n''H2NC(=NH)NHNH2 aminoguanidine \n''13C6H5NH2 aniline-13 C6 \n''CIN cyanogen iodide \n''KCN potassium cyanide \n''K13CN potassium cyanide-13 C \n''K13C15N potassium cyanide-13 C,15 N \n''KC15N potassium cyanide-15 N \n''NaCN sodium cyanide \n''C(NO2)4 tetranitromethane \n''Ba(CN)2 barium cyanide \n''C2CaN2 calcium cyanide \n''C2CdN2 cadmium cyanide \n''Cl3CCN trichloroacetonitrile \n''C2CoN2 cobalt(II) cyanide \n''C2CuN2 copper dicyanide \n''C2CuN2 cupric cyanide \n''CD3CN deuterated acetonitrile (D3) \n''CF3CN trifluoroacetonitrile \n''C2HN3 dicyanamide \n''CH3CN acetonitrile \n''CH3C15N acetonitrile-15 N \n''C2H3N methyl isocyanide \n''C2H3N3 1,2,4-triazole \n''C2H3N3 1H-1,2,3-triazole \n''C2H4N2 aminoacetonitrile \n''C2H4N4 amitrole \n''C2H4N4 4-amino-4 H-1,2,4-triazole \n''C2H4N4 5-methyl-1 H-tetrazole \n''NH2C(=NH)NHCN cyanoguanidine \n''C2H5N aziridine \n''(CH2CH2NH)n everamine \n''C2H5N vinylamine \n''C2H5N5 guanazole \n''C2H6N2 2-aminoethanimidic acid \n''(CH3)2NH dimethylamine \n''C2H5NH2 ethylamine \n''C2H7N3 methylguanidine \n''C2H8N2 1,2-dimethylhydrazine \n''NH2CH2CH2NH2 ethylenediamine \n''(CH3)2NNH2 1,1-dimethylhydrazine \n''Hg(CN)2 mercuric cyanide \n''Ni(CN)2 nickel cyanide \n''Pb(CN)2 lead(II) cyanide \n''Pd(CN)2 palladium(II)cyanide \n''Pt(CN)2 platinum(II)cyanide \n''Zn(CN)2 zinc cyanide \n''NaN(CN)2 sodium dicyanamide \n''C2N4O6 trinitroacetonitrile \n''C2N6O12 hexanitroethane \n''NCCCl2CN dichloromalononitrile \n''C3Cl3N3 cyanuric chloride \n''D2C=CDCN acrylonitrile-d 3 \n''C3D4N2 imidazole-d 4 \n''C2D5CN propionitrile-d 5 \n''(CD3)2NCN dimethyl-d 6-cyanamide \n''C3F3N3 cyanuric fluoride \n''C3F5N pentafluoropropionitrile \n''CH2(CN)2 malononitrile \n''CH2=CHCN acrylonitrile \n''(C3H3N)n polyacrylonitrile \n''C3H3N3 s-triazine \n''C3H3N3 triazine \n''C3H415N2 imidazole-15 N2 \n''C3H4N2 imidazole \n''C3H4N2 alpha-hydroformamine cyanide \n''C3H4N2 1H-pyrazole \n''C3H4N4 1,3,5-triazin-2-amine\n''C3H4N4 3-amino-1,2,4-triazine \n''HC≡CCH2NH2 2-propyn-1-amine \n''CH3CH2CN propionitrile \n''C3H5N3 3-aminopyrazole \n''C3H5N3 4-aminoimidazole \n''C3H5N3 amino-imidazole \n''C3H6N ethyl isocyanide \n''C3H6N2 3-aminopropionitrile \n''(CH3)2NCN dimethylcyanamide \n''C3H6N5 1,2,4-triazole-carboxamidine \n''C3H6N6 melamine \n''C3H7N propyleneimine \n''CH2=CHCH2NH2 allylamine \n''C3H7N azetidine \n''C3H5NH2 cyclopropylamine \n''[CH2CH(CH2NH2)]n poly(allylamine) \n''C3H7N2 2-pyrazoline \n''NCCH2CH2NHNH2 beta-cyanoethylhydrazine \n''C3H8N2 pyrazolidine \n''(CH3)2CHNH2 2-aminopropane \n''C2H5NHCH3 methylethylamine \n''CH3CH2CH2NH2 N-propylamine \n''(CH3)3N trimethylamine \n''(CH3)315N trimethylamine-15 N \n''CH3CH(NH2)CH2NH2 1,2-diaminopropane \n''NH2(CH2)3NH2 1,3-diaminopropane \n''NH2CH2CH2NHCH3 N-methylethylenediamine \n''C4Cl4N2 2,4,5,6-tetrachloropyrimidine \n''C4D4N2 pyrazine-d 4 \n''NCCD2CD2CN succinonitrile-d 4 \n''C4D5N pyrrole-d 5 \n''NCCH=CHCN fumaronitrile \n''C4H4N2 pyrazine \n''C4H4N2 pyridazine \n''C4H4N2 pyrimidine \n''NCCH2CH2CN succinonitrile \n''C4H4N4 5-aminopyrazole-4-carbonitrile \n''NCC(NH2)=C(NH2)CN diaminomaleonitrile \n''C4H4N6 8-azaadenine \n''CH2=CHCH2CN allyl cyanide \n''CH3CH=CHCN 2-butenenitrile \n''C3H5CN cyclopropanecarbonitrile \n''C4H5N isocrotonic nitrile \n''CH2=C(CH3)CN methacrylonitrile \n''C4H5N polypyrrole \n''C4H5N pyrrole \n''C4H5N3 2-aminopyrimidine \n''C4H5N3 4-aminopyrimidine \n''C4H5N3 2-aminopyrazine \n''HN(CH2CN)2 iminodiacetonitrile \n''C4H6N2 1-methylimidazole \n''C4H6N2 1-methylpyrazole \n''C4H6N2 2-methylimidazole \n''H2N(CH3)C=CHCN 3-aminocrotononitrile \n''C4H6N2 3-methylpyrazole \n''C4H6N2 4-methylimidazole \n''C4H6N2 fomepizole \n''C4H6N4 2,4-diaminopyrimidine \n''C4H6N4 4,5-diaminopyrimidine \n''C4H6N8 3,5,7-triamino-s-triazolo[4,3-a]-s-triazine \n''C4H7N 1-pyrroline \n''C4H7N 3-pyrroline \n''CH3CH2CH2CN N-butyronitrile \n''(CH3)2CHCN isobutyronitrile \n''(CH3)2CHNC isopropyl isocyanide \n''HC≡CCH2NHCH3 N-methylpropargylamine \n''C4H7N n-propyl isocyanide \n''C4H7N3 3-amino-5-methylpyrazole \n''C4H7N5 pyrimidine-2,4,6-triyltriamine \n''C4H7N5 6-methyl-1,3,5-triazine-2,4-diamine \n''C4H8N2 1,4,5,6-tetrahydropyrimidine \n''C4H8N2 2-methyl-2-imidazoline \n''CH3NHCH2CH2CN (2-cyanoethyl)methylamine \n''(CH3)2NCH2CN 2-dimethylaminoacetonitrile \n''C4H8N4 2,4-dimethyl-3-methylenepentane \n''C3H5CH2NH2 cyclopropanemethylamine \n''C4H7NH2 cyclobutylamine \n''CH2=CHCH2NHCH3 N-allylmethylamine \n''C4H9N pyrrolidine \n''C4H10N2 piperazine \n''C4H10N2 piperazine hydrochloride hydrate \n''C4H10N2 (R)-(+)-3-aminopyrrolidine \n''C4H10N2 (S)-(-)-3-aminopyrrolidine \n''CH3(CH2)3NH2 butylamine \n''C4H11N amines, c13-15-alkyldimethyl \n''(C2H5)2NH diethylamine \n''(CH3)2CHCH2NH2 isobutylamine \n''(CH3)2NC2H5 N,N-dimethylethylamine \n''(CH3)2CHNHCH3 N-methyl-2-propanamine \n''CH3CH2CH2NHCH3 N-methylpropylamine \n''C2H5CH(NH2)CH3 (R)-2-butanamine \n''C2H5CH(NH2)CH3 (S)-(+)-sec-butylamine \n''CH3CH2CH(NH2)CH3 sec-butylamine \n''(CH3)3CNH2 tert-butylamine \n''C4H12N2 1,2-diamino-2-methylpropane \n''C4H12N2 1,2-diethylhydrazine \n''C4H12N2 1,3-butanediamine \n''NH2(CH2)4NH2 putrescine \n''CH3NHCH2CH2NHCH3 N,N'-dimethylethylenediamine \n''(CH3)2NCH2CH2NH2 N,N-dimethylethylenediamine \n''C2H5NHCH2CH2NH2 N-ethylethylenediamine \n''CH3NH(CH2)3NH2 N-methyl-1,3-propanediamine \n''C4H12N2 putrescine \n''C4H13N3 diethylenetriamine \n''C5Cl5N pentachloropyridine \n''C5D5N deuterated pyridine (D5) \n''C5D11N piperidine-d 11 \n''C5F5N pentafluoropyridine \n''C5H2N4 4,5-dicyanoimidazole \n''C5H3N3 2-pyrimidinecarbonitrile \n''C5H3N3 cyanopyrazine \n''C5H3N5 2-amino-4,5-imidazoledicarbonitrile \n''C5H4N2 pyrrole-2-carbonitrile \n''C5H4N4 1,2,4-triazolo[1,5-a]pyrimidine \n''C5H4N4 1 H-1,2,3-triazolo[4,5-b]pyridine \n''C5H4N4 4-amino-5-pyrimidinecarbonitrile \n''C5H4N4 1H-purine \n''C5H4N5 adenine-ring \n''C5H5N pyridine \n''C5H515N pyridine-15 N \n''C5H5N5 1H-pyrazolo[3,4-d]pyrimidin-4-amine \n''C5H5N5 2-aminopurine \n''C5H5N5 4-aminopyrazolo[3,4-d]pyrimidine \n''C5H5N5 adenine \n''C5H6N2 1-vinylimidazole \n''C5H6N2 2-aminopyridine \n''C5H6N2 2-methylpyrazine \n''C5H6N2 2-methylpyrimidine \n''C5H6N2 3-pyridinamine \n''C5H6N2 3-methylpyridazine \n''C5H6N2 4-aminopyridine \n''C5H6N2 4-methylpyridazine \n''C5H6N2 4-methylpyrimidine \n''C5H6N2 5-methylpyrimidine \n''(CH3)2C(CN)2 2,2-dicyanopropane \n''NC(CH2)3CN glutaronitrile \n''C5H6N2 pyridinamine \n''C5H6N6 2,6-diaminopurine \n''C5H7N 2-methyl-2-butenenitrile \n''C5H7N 2-methyl-3-butenenitrile \n''C5H7N 2-pentenenitrile \n''C5H7N 3-methylpyrrole \n''C5H7N 3-pentenenitrile \n''CH3CH=CHCH2CN 3-pentenenitrile,predominately trans 95% \n''CH2=CHCH2CH2CN 4-pentenenitrile \n''C2H5CH=CHCN cis-2-pentenenztrile \n''C5H7N cyclobutanecarbonitrile \n''C3H5CH2CN cyclopropylacetonitrile \n''C5H7N N-methylpyrrole \n''C5H7N trans-2-methyl-2-butenenitrile \n''C5H7N (Z)-2-methyl-2-butenenitrile \n''C5H7N3 2,3-diaminopyridine \n''C5H7N3 2,5-diaminopyridine \n''C5H7N3 2,6-diaminopyridine \n''C5H7N3 4-methyl-2-pyrimidinamine \n''C5H7N3 2-hydrazinopyridine \n''C5H7N3 3,4-diaminopyridine \n''C5H8N2 1,2-dimethylimidazole \n''C5H8N2 1-cyanopyrrolidine \n''C5H8N2 2,4-dimethylimidazole \n''C5H8N2 2-ethylimidazole \n''C5H8N2 3,5-dimethylpyrazole \n''C5H8N2 2-propenenitrile, 3-(dimethylamino) \n''(CH3)2NCH=CHCN trans-3-(dimethylamino)acrylonitrile \n''C5H8N4 3-amino-5,6-dimethyl-1,2,4-triazine \n''C5H9N 1,2,3,6-tetrahydropyridine \n''C5H9N 3,4-dihydro-5-methyl-2H-pyrrole \n''C5H9N 1,1-dimethylpropargylamine \n''(CH3)2NCH2C≡CH N,N-dimethyl-2-propyn-1-amine \n''CH3(CH2)3NC butyl isocyanide \n''C5H9N amines, c5-6-alkylenedi \n''(CH3)2CHCH2CN isovaleronitrile \n''C2H5CH(CH3)CN (S)-(+)-2-methylbutyronitrile \n''(CH3)3CNC tert-butyl isocyanide \n''(CH3)3CCN pivalonitrile \n''CH3(CH2)3CN valeronitrile \n''C5H9N3 5-amino-1,3-dimethylpyrazole \n''C5H9N3 5-amino-1-ethylpyrazole \n''C5H9N3 betazole \n''C5H9N3 histamine \n''C5H10N2 2-amino-2-methylbutanenitrile \n''(CH3)2NCH2CH2CN dimethylaminopropionitrile \n''C2H5NHCH2CH2CN 3-ethylaminopropanenitrile \n''C5H10N2 (3s)-2,3,4,5-tetrahydropyridin-3-amine \n''C5H10N2 4,4-dimethyl-2-imidazoline \n''(C2H5)2NCN diethylcyanamide \n''C5H10N4 2-methyl-4-octene \n''C5H11N 2-methylpyrrolidine \n''C5H9NH2 cyclopentylamine \n''C5H11N N,N-dimethylallylamine \n''C5H11N 1-methylpyrrolidine \n''C5H11N piperidine \n''C5H11N (R)-(-)-2-methylpyrrolidine \n''C5H12N2 1-aminopiperidine \n''C5H12N2 1-methylpiperazine \n''C5H12N2 2-methylpiperazine \n''C5H10NNH2 4-aminopiperidine \n''C5H12N2 homopiperazine \n''C5H12N2 (R)-(-)-2-methylpiperazine \n''C5H12N2 (S)-(+)-2-(aminomethyl)pyrrolidine \n''C5H12N2 (S)-(+)-2-methylpiperazine \n''(CH3)2CHCH(CH3)NH2 1,2-dimethylpropylamine \n''(C2H5)2CHNH2 3-pentylamine \n''CH3CH(NH2)CH2CH2CH3 2-pentylamine \n''CH3CH2CH(CH3)CH2NH2 2-methylbutylamine \n''CH3(CH2)4NH2 amylamine \n''(CH3)2CHCH2CH2NH2 isoamylamine \n''CH3N(C2H5)2 diethylmethylamine \n''(CH3)2CHN(CH3)2 N,N-dimethylisopropylamine \n''C5H13N N,N-dimethylpropylamine \n''CH3NH(CH2)3CH3 N-methylbutylamine \n''(CH3)2CHNHC2H5 N-ethylisopropylamine \n''C2H5CH(CH3)CH2NH2 (S)-(-)-2-methylbutylamine \n''C2H5C(CH3)2NH2 tert-pentylamine \n''(CH3)2NC(=NH)N(CH3)2 1,1,3,3-tetramethylguanidine \n''C5H13N3 4-methylpiperazin-1-amine \n''CH3CH(NH2)CH2N(CH3)2 1-dimethylamino-2-propylamine \n''H2NCH2C(CH3)2CH2NH2 2,2-dimethyl-1,3-propanediamine \n''(CH3)2N(CH2)3NH2 3-dimethylaminopropylamine \n''AlF3·xH2O fluellite \n''NH2(CH2)5NH2 cadaverine \n''CH3CH2CH(NH2)CH2CH2NH2 dytek®EP diamine \n''CH3NHCH2CH2CH2NHCH3 N-dimethyl-1,3-propanediamine \n''C5H14N2 N-ethyl-n'-methylethylenediamine \n''(CH3)2CHNHCH2CH2NH2 N-isopropylethylenediamine \n''C5H14N2 n-methylputrescine \n''CH3CH2CH2NHCH2CH2NH2 N-propylethylenediamine \n''(CH3)2CHCH2CH(OH)CH3 (S)-(+)-4-methyl-2-pentanol \n''C5H14N4 agmatine \n''H2N(CH2)3NHCH2CH2NH2 N-(2-aminoethyl)-1,3-propanediamine \n''C6Br4N3 tetrabromo-2-benzotriazole \n''C6D7N 2-picoline-d 7 \n''C6D5ND2 aniline-d 7 \n''C6D4(ND2)2 1,4-phenylenediamine-d 8 \n''NC(CD2)4CN adiponitrile-d 8 \n''(C2D5)3N triethyl-d 15-amine \n''(CF3)2C=NN=C(CF3)2 hexafluoroacetone azine \n''N(CF2CF3)3 perfluorotriethylamine \n''Fe4[Fe(CN)6]3 iron(III) ferrocyanide \n''C6H2N4 2,3-pyrazinedicarbonitrile \n''C6H3N5 6-cyanopurine \n''C6H4N2 pyridine-2-carbonitrile \n''C6H4N2 3-cyanopyridine \n''C6H4N2 4-cyanopyridine \n''C6H4N4 pteridine-ring \n''C6H4N6 p-diazidobenzene \n''C6H5N2+ benzenediazonium ion \n''C6H5N3 1H-imidazo(4,5-b)pyridine \n''C6H5N3 5-amino-2-pyridinecarbonitrile \n''C6H5N3 5-azabenzimidazole \n''C5H3NNH2CN 6-amino-3-pyridinecarbonitrile \n''C6H5N3 benzotriazole \n''C6H5N4 9-deazaadenine \n''C6H6N2 vinylpyrazine \n''C6H6N4 1-aminobenzotriazole \n''C6H6N4 3-deazaadenine \n''C6H6N4 5-aminobenzotriazole \n''C6H6N4 6,7-dihydropteridine \n''C6H6N4 6-methylpurine \n''C6H7N 2-picoline \n''C6H7N 3-methylpyridine \n''C6H7N 4-methylpyridine \n''HC≡C(CH2)3CN 5-hexynenitrile \n''C6H515NH2 aniline-15 N \n''(C6H5NH2)2·H2SO4 aniline \n''C6H5NH2 aniline \n''C6H7N3 4-imino-5-methidyl-2-methylpyrimidine \n''(CH3)2NCH=C(CN)2 2-(dimethylaminomethylene)malononitrile \n''C6H7N5 1-methyladenine \n''C6H7N5 3-methyladenine \n''C6H7N5 7-methyladenine \n''C6H7N5 9-methyladenine \n''C6H4(15NH2)2 1,4-phenylenediamine-15 N2 \n''C6H8N n-methylpyridinium \n''C6H4(NH2)2 1,2-diaminobenzene \n''C6H4(NH2)2 m-phenylenediamine \n''C6H8N2 1-allyl-1H-imidazole \n''C6H8N2 2,3-dimethylpyrazine \n''C6H8N2 2,5-dimethylpyrazine \n''C6H8N2 2,6-dimethylpyrazine \n''C6H8N2 3-methyl-2-pyridinamine \n''C6H8N2 2-amino-4-picoline \n''C6H8N2 6-methyl-2-pyridinamine \n''C6H8N2 2-methylaminopyridine \n''NCCH(CH3)CH2CH2CN methylglutaronitrile \n''C6H8N2 2-pyridinemethanamine \n''C6H8N2 3-amino-2-methylpyridine \n''C6H8N2 3-(aminomethyl)pyridine \n''C6H8N2 4,6-dimethylpyrimidine \n''C6H8N2 4-amino-2-methylpyridine \n''C6H8N2 4-(aminomethyl)pyridine \n''C6H8N2 4-(methylamino)pyridine \n''C6H8N2 5-amino-2-methylpyridine \n''C6H8N2 6-amino-3-picoline \n''NC(CH2)4CN adiponitrile \n''C6H8N2 2-ethylpyrazine \n''C6H4(NH2)2 p-phenylenediamine \n''C6H5NHNH2 phenylhydrazine \n''C6H8N4 5,6,7,8-tetrahydropteridine \n''C6H8N5 n1-methyladenine \n''C6H9N 2,4-dimethylpyrrole \n''C6H9N 2,5-dimethylpyrrole \n'""", '7', '14.01')
        self.colorN=colorN="forest green"
        self.N = tk.Button(self, text=N[0], width=5, height=2, bg=colorN, font=10, borderwidth=3,
                           command=lambda text=N: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorN, text[0], text[3], text[4]), self.voice(text[1]), self.compound_N()])
        self.N.grid(row=4, column=16)

        P = ('P', 'Phosphorus', """'P black phosphorus \n''P red phosphorus \n''P2 diphosphorus \n''P4 white phosphorus \n''AlP aluminum phosphide \n''BP boron phosphide \n''PBr3 phosphorus tribromide \n''PBr5 phosphorus pentabromide \n''Ca3P2 calcium phosphide \n''Cd3P2 cadmium phosphide \n''PCl3 phosphorus trichloride \n''Cl4P2 diphosphorus tetrachloride \n''PCl5 phosphorus pentachloride \n''Co2P cobalt phosphide \n''CrP chromium phosphide \n''CuP2 copper phosphide \n''PD3 deuterated phosphine \n''F3P phosphorus trifluoride \n''F4P2 diphosphorus tetrafluoride \n''PF5 phosphorus pentafluoride \n''FeP iron phosphide (1:1) \n''Fe3P iron phosphide (3:1) \n''GaP gallium phosphide \n''PH3 phosphine \n''H4P2 diphosphine \n''HfP hafnium phosphide \n''PI3 phosphorus(III) iodide \n''P2I4 diphosphorous tetraiodide \n''InP indium phosphide \n''Mg3P2 magnesium phosphide \n''MoP molybdenum phosphide \n''Na3P sodium phosphide \n''NbP niobium phosphide \n''Ni2P nickel phosphide \n''P2O3 phosphorus trioxide \n''O6P4 tetraphosphorus(III) hexoxide \n''P2O5 phosphorus pentoxide \n''PSn tin monophosphide \n''PTi titanium phosphide \n''PV vanadium phosphide \n''PY yttrium phosphide \n''P2S3 phosphorus trisulfide \n''P2Se5 phosphorus(V) selenide \n''Sr3P2 strontium phosphide \n''P4S3 phosphorus sesquisulfide \n''P4S7 phosphorus heptasulfide \n''P2S5 phosphorus pentasulfide \n''P4Se3 tetraphosphorus triselenide \n''Sn4P3 tin triphosphide \n''ZrP2 zirconium phosphide \n''AgPF6 silver hexafluorophosphate \n''AgO3P silver(I) metaphosphate \n''Ag3PO4 silver phosphate \n''AlO4P aluminum phosphate \n''Ba(PO3)2 barium dimetaphosphate \n''Ba2P2O7 barium pyrophosphate \n''Be3(PO4)2 beryllium phosphate \n''BiO4P bismuth(III) phosphate \n''BrF2P phosphorus(III) bromide difluoride \n''POBr3 phosphorus oxybromide \n''Br3PS phosphorothioc tribromide \n''P(CD3)3 trimethyl-d 9-phosphine \n''(CH3)3P trimethylphosphine \n''(CH3)2PCH2P(CH3)2 bis(dimethylphosphino)methane \n''C6H5PH2 phenylphosphine \n''C6H4(PH2)2 1,2-phenylenebisphosphine \n''(C2H5)3P triethylphosphine \n''(CH3)2PCH2CH2P(CH3)2 1,2-bis(dimethylphosphino)ethane \n''(CH3)2PC6H5 dimethylphenylphosphine \n''(CH3)3CPHC(CH3)3 di-tert-butylphosphine \n''(CH2=CHCH2)3P triallylphosphine \n''[(CH3)3C]2PCH3 di-tert-butylmethylphosphine \n''[(CH3)2CH]3P triisopropylphosphine \n''(CH3CH2CH2)3P tripropylphosphine \n''C6H5P(CH=CH2)2 divinylphenylphosphine \n''(C2H5)2PC6H5 diethylphenylphosphine \n''C6H5PHC(CH3)3 tert-butylphenylphosphine \n''C10H19P dicyclopentylphosphine \n''C10H23P tert-butyldiisopropylphosphine \n''(C6H5)2PH diphenylphosphine \n''C6H5P(CH2CH=CH2)2 diallylphenylphosphine \n''(C6H11)2PH dicyclohexylphosphine \n''[(CH3)3C]3P tri-tert-butylphosphine \n''[CH3(CH2)3]3P tri-N-butylphosphine \n''[(CH3)2CHCH2]3P triisobutylphosphine \n''(C6H5)2PCH3 methyldiphenylphosphine \n''(C6H5)2PCH=CH2 diphenylvinylphosphine \n''(C6H5)2PCH2CH3 ethyldiphenylphosphine \n''C14H28P2 (-)-1,2-bis((2S,5 S)-2,5-dimethylphospholano)ethane \n''C14H28P2 (+)-1,2-bis((2R,5 R)-2,5-dimethylphospholano)ethane \n''(C6H5)2PCH2CH=CH2 allyldiphenylphosphine \n''(C6H5)2PCH2CH2CH3 diphenylpropylphosphine \n''(C6H5)2PCH(CH3)2 isopropyldiphenylphosphine \n''C15H27P tricyclopentylphosphine \n''(C6H5)2PC(CH3)3 tert-butyldiphenylphosphine \n''C16H31P tert-butyldicyclohexylphosphine \n''C16H32P2 (S,S',R,R')-tangphos \n''(C6D5)3P triphenylphosphine-d 15 \n''(C6F5)3P tris(pentafluorophenyl)phosphine \n''[(C6H5)3P]2Pd(CH2C6H5)Cl trans-benzyl(chloro)bis(triphenylphosphine)palladium(II) \n''C18H15P triphenylphosphine \n''C6H11P(C6H5)2 cyclohexyldiphenylphosphine \n''(C6H11)2PC6H5 dicyclohexylphenylphosphine \n''C18H28P2 (-)-1,2-bis[(2R,5 R)-2,5-dimethylphospholano]benzene \n''C18H28P2 (+)-1,2-bis[(2S,5 S)-2,5-dimethylphospholano]benzene \n''(C6H11)3P tricyclohexylphosphine \n''C18H36P2 (-)-1,2-bis((2S,5 S)-2,5-diethylphospholano)ethane \n''C18H36P2 (+)-1,2-bis((2R,5 R)-2,5-diethylphospholano)ethane \n''C6H5CH2P(C6H5)2 benzyldiphenylphosphine \n''(C6H5)2PC6H4CH3 diphenyl(o-tolyl)phosphine \n''(C6H5)2PC6H4CH3 diphenyl p-tolylphosphine \n''C19H29P dicyclohexyl-(2-methylphenyl)phosphine \n''C6H5C6H4P[C(CH3)3]2 (2-biphenyl)di-tert-butylphosphine \n''(CH3C6H4)3P tri(m-tolyl)phosphine \n''(CH3C6H4)3P tris(2-methylphenyl)phosphine \n''(CH3C6H4)3P tris(4-methylphenyl)phosphine \n''(C6H5CH2)3P tribenzylphosphine \n''CH3CH2CH2P(C6H5)3Br triphenylpropylphosphonium \n''C21H33P dicyclohexyl-(2,4,6-trimethylphenyl)phosphine \n''C22H36P2 (-)-1,2-bis[(2R,5 R)-2,5-diethylphospholano]benzene \n''C22H36P2 (+)-1,2-bis[(2S,5 S)-2,5-diethylphospholano]benzene \n''C23H19P triphenylphosphonium cyclopentadienide \n''C24H20P tetraphenylphosphonium \n''(C6H5)2PP(C6H5)2 tetraphenylbiphosphine \n''C24H31P (2-biphenyl)dicyclohexylphosphine \n''C24H32P2 (1R,1'R,2S,2'S)-duanphos \n''C6H4[CH2P[C(CH3)2]2] 1,2-bis(di-tert-butylphosphinomethyl)benzene \n''[CH3(CH2)7]3P tri-N-octylphosphine \n''[C6H5CH2P(C6H5)3]+1 benzyltriphenylphosphonium ion \n''(C6H5)2PCH2P(C6H5)2 methylenebis[diphenylphosphine] \n''(C6H11)2PCH2P(C6H11)2 bis(dicyclohexylphosphino)methane \n''(C6H5)2PC≡CP(C6H5)2 bis(diphenylphosphino)acetylene \n''[(C6H5)2P]2C=CH2 1,1-bis(diphenylphosphino)ethylene \n''(C6H5)2PCH=CHP(C6H5)2 cis-vinylenebis[diphenylphosphine] \n''(C6H5)2PCH=CHP(C6H5)2 trans-vinylenebis[diphenylphosphine] \n''(C6H5)2PCH2CH2P(C6H5)2 1,2-bis(diphenylphosphino)ethane \n''C26H44P2 (-)-1,2-bis((2S,5 S)-2,5-diisopropylphospholano)benzene \n''C26H44P2 (+)-1,2-bis[(2R,5 R)-2,5-diisopropylphospholano]benzene \n''(C6H11)2PCH2CH2P(C6H11)2 1,2-bis(dicyclohexylphosphino)ethane \n''(C6H5)2PCH2CH2CH2P(C6H5)2 1,3-bis(diphenylphosphino)propane \n''(C6H5)2PCH(CH3)CH2P(C6H5)2 (R)-(+)-1,2-bis(diphenylphosphino)propane \n''[(CH3)3C6H2]3P tris(2,4,6-trimethylphenyl)phosphine \n''(C6H11)2P(CH2)3P(C6H11)2 1,3-bis(dicyclohexylphosphino)propane \n''(C6H5)2P(CH2)4P(C6H5)2 1,4-bis(diphenylphosphino)butane \n''[-CH(CH3)P(C6H5)2]2 (2S,3S)-(-)-bis(diphenylphosphino)butane \n''(C6H11)2P(CH2)4P(C6H11)2 1,4-bis(dicyclohexylphosphino)butane \n''(C6H5)2P(CH2)5P(C6H5)2 1,5-bis(diphenylphosphino)pentane \n''C29H45P 2-di-tert-butylphosphino-2',4',6'-triisopropylbiphenyl \n''(C10H7)3P tri-1-naphthylphosphine \n''C6H4[P(C6H5)2]2 1,2-bis(diphenylphosphino)benzene \n''(C6H5)2P(CH2)6P(C6H5)2 1,6-bis(diphenylphosphino)hexane \n''C33H49P 2-dicyclohexylphosphino-2',4',6'-triisopropylbiphenyl \n''C33H53P 2-di-tert-butylphosphino-3,4,5,6-tetramethyl-2',4',6'-triisopropyl-1,1'-biphenyl \n''C6H5P[CH2CH2P(C6H5)2]2 bis[2-(diphenylphosphino)ethyl]phenylphosphine \n''C34H36P2 (-)-1,2-bis((2R,5 R)-2,5-diphenylphospholano)ethane \n''C34H36P2 (+)-1,2-bis((2S,5 S)-2,5-diphenylphospholano)ethane \n''C40H34P2 (R)-(–)-4,12-bis(diphenylphosphino)-[2.2]-paracyclophane \n''C40H34P2 (S)-(+)-4,12-bis(diphenylphosphino)-[2.2]-paracyclophane \n''CH3C[CH2P(C6H5)2]3 1,1,1-tris(diphenylphosphino-methyl)ethane \n''[(C6H5)2PCH2CH2]3P tris[2-(diphenylphosphino)ethyl]phosphine \n''[-C10H6P(C6H5)2]2 2,2'-bis(diphenylphosphino)-1,1'-binaphthalene \n''[-C10H6P(C6H5)2]2 (R)-(+)-2,2'-bis(diphenylphosphino)-1,1'-binaphthalene \n''[-C10H6P(C6H5)2]2 (S)-(-)-2,2'-bis(diphenylphosphino)-1,1'-binaphthalene \n''C48H40P2 2,2'-bis(di-p-tolylphosphino)-1,1'-binaphthyl \n''C48H40P2 (R)-(+)-2,2'-bis(di-p-tolylphosphino)-1,1'-binaphthyl \n''C48H40P2 (S)-(-)-2,2'-bis(di-p-tolylphosphino)-1,1'-binaphthyl \n''C48H50P2 (R)-(–)-4,12-bis[di(3,5-xylyl)phosphino]-[2.2]-paracyclophane \n''C50H36P2 (R)-binaphane \n''C52H48P2 (S)-binapine Ca3(PO4)2 \n''Cd3(PO4)2 cadmium phosphate \n''ClF2P phosphorus(III) chloride difluoride \n''Cl2FP phosphorus(III) dichloride fluoride \n''POCl3 phosphoryl chloride \n''PSCl3 thiophosphoryl chloride \n''Cl2P(O)OP(O)Cl2 diphosphoryl chloride \n''(NPCl2)3 hexachlorocyclotriphosphazene \n''Co3(PO4)2 cobalt phosphate \n''CrO4P chromium(III) phosphate \n''Cu3(PO4)2 copper phosphate \n''Cu3(PO4)2 copper(II) phosphate \n''D3PO2 (-{2}-h2)phosphinic (-{2}-h)acid \n''D3PO4 deuterated phosphoric acid \n''F3OP phosphoryl fluoride \n''F3PS phosphorothioc trifluoride \n''HPF6 hexafluorophosphoric acid \n''KPF6 potassium hexafluorophosphate \n''LiPF6 lithium hexafluorophosphate \n''F6N3P3 phosphonitrilic fluoride trimer \n''NaPF6 sodium hexafluorophosphate \n''F6PTl thallium(I) hexafluorophosphate \n''FePO4 iron(III) phosphate \n''FePO4 iron phosphate \n''Fe4(P2O7)3·9H2O iron(III) pyrophosphate nonahydrate \n''HPO3 metaphosphoric acid \n''HP(O)(OH)2 phosphorous acid \n''H2O4P(R1) [acetyl-coa carboxylase] phosphate \n''H3P17O4 phosphoric acid-17 O4 \n''HP(O)(OH)2 phosphorous acid \n''H3PO4 phosphoric acid \n''(HO)2P(O)OP(O)(OH)2 pyrophosphoric acid \n''H4P2O6 hypophosphoric acid \n''H5P3O10 triphospate \n''Hg3O8P2 mercury(II) phosphate \n''HoO4P holmium(III)phosphate \n''InPO4 indium(III) phosphate \n''O2[P(O)(OK)2]2 potassium peroxydiphosphate \n''LiO3P lithium metaphosphate \n''Li3PO4 lithium phosphate \n''Mg2P2O7 magnesium pyrophosphate \n''Mg3(PO4)2·5H2O Trimagnesium diphosphate pentahydrate \n''MnP2O7 manganese(IV) pyrophosphate \n''Mo(PO3)6 molybdenum(VI) metaphosphate \n''NaPO3 calgon pT \n''Na3PO4 trisodium phosphate \n''Na3O9P3 sodium trimetaphosphate \n''Na4O7P2 sodium pyrophosphate \n''Na4O12P4 metaphosphoric acid, tetrasodium salt \n''Na5O10P3 polygon \n''Ni3(PO4)2 nickel phosphate \n''O4PPr praseodymium(III)phosphate \n''YPO4 yttrium(III)phosphate \n''Sn2P2O7 tin(II) pyrophosphate \n''Pb3(PO4)2 lead(II) phosphate \n''Zn3(PO4)2 zinc phosphate \n''PBr2F phosphorus(III) dibromide fluoride \n''PBr2F3 phosphorus(V) dibromide trifluoride \n''PBr4F phosphorus(V) tetrabromide fluoride \n''PClF4 phosphorus(V) chloride tetrafluoride \n''PCl2F3 phosphorus(V) dichloride trifluoride \n''PCl3F2 phosphorus(V) trichloride difluoride \n''PCl4F phosphorus(V) tetrachloride fluoride \n''PH4Cl phosphonium chloride \n''PH4I phosphonium iodide \n''POI3 phosphoryl iodide \n''PSI3 phosphorothioc triiodide \n''SbPO4 antimony(III) phosphate \n''ZrP2O7 zirconium(IV) pyrophosphate \n''C6H11O9P 2-dehydro-3-deoxy-D-gluconate-6-phosphate \n''C6H11O9P 5-dehydro-2-deoxy-d-gluconate 6-phosphate \n''C6H11K2O9P·2H2O α-D-glucose-1-phosphate dipotassium salt dihydrate  \n''C6H11O9P l-myo-inositol-1-phosphate \n''C6H11O9P methanofuran biosynththesis intermediate mf2 \n''C6H11O10P 2-keto-6-phosphate-d-gluconic acid, alpha-furanose form \n''C6H11O10P 3-keto-l-gulonate 6-phosphate \n''C6H11O10P 6-phospho-2-dehydro-d-gluconate \n''C6H11O10P alpha-d-galacturonate 1-phosphate \n''C6H11O10P alpha-d-glucuronate 1-phosphate \n''C6H11O11P 3-phosphoglucarate \n''C6H12O9P d-myo-inositol (1)-monophosphate \n''C6H12O9P d-myo-inositol (2) monophosphate \n''C6H12O9P d-myo-inositol (3)-monophosphate \n''C6H12O9P d-myo-inositol (5)-phosphate \n''C6H12O9P d-myo-inositol (6)-monophosphate \n''C6H12O12P2 d-myo-inositol (1,2) bisphosphate \n''C6H12O12P2 d-myo-inositol (1,3)-bisphosphate \n''C6H12O12P2 d-myo-inositol (2,4) bisphosphate \n''C6H12O12P2 d-myo-inositol (3,4)-bisphosphate \n''C6H12O12P2 d-myo-inositol (4,5)-bisphosphate \n''C6H12O13P2 2-carboxy-3-keto-d-arabinitol-1,5-bisphosphate \n''C6H12O15P3 d-myo-inositol (1,2,3) trisphosphate \n''C6H12O15P3 d-myo-inositol (1,2,6) trisphosphate \n''C6H12O15P3 d-myo-inositol (1,3,4)-trisphosphate \n''C6H12O15P3 d-myo-inositol (1,4,5)-trisphosphate \n''C6H12O15P3 d-myo-inositol (2,3,4) trisphosphate \n''C6H12O15P3 d-myo-inositol (3,4,6)-trisphosphate \n''C6H12O15P3 d-myo-inositol (3,5,6)-trisphosphate \n''C6H12O18P4 d--inositol (1,2,3,4) tetra<i>kisphosphate \n''C6H12O18P4 d--inositol (1,2,3,6) tetra<i>kisphosphate \n''C6H12O18P4 d--inositol (1,2,5,6) tetra<i>kisphosphate \n''C6H12O18P4 d--inositol (1,3,4,5)-tetra<i>kisphosphate \n''C6H12O18P4 d--inositol (1,3,4,6)-tetra<i>kisphosphate \n''C6H12O18P4 d--inositol (1,4,5,6)-tetra<i>kisphosphate \n''C6H12O21P5 d--inositol (1,2,3,4,5)-penta<i>kisphosphate \n''C6H12O21P5 d--inositol (1,2,3,4,6)-penta<i>kisphosphate \n''C6H12O21P5 d--inositol (1,2,3,5,6) penta<i>kisphosphate \n''C6H13O9P glucose-1-phosphate \n''C6H13O9P glucose-6-phosphate \n''C6H13O9P hexulose 6-phosphate \n''C6H13O9P l-galactose-1-phosphate \n''C6H13O9P l-sorbose 1-phosphate \n''C6H13O9P l-tagatose-6-phosphate \n''C6H13O9P tagatose-6-phosphate \n'""", '15', '30.97')
        self.colorP=colorP="lawn green"
        self.P = tk.Button(self, text=P[0], width=5, height=2, bg=colorP, font=10, borderwidth=3,
                           command=lambda text=P: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorP, text[0], text[3], text[4]), self.voice(text[1]), self.compound_P()])
        self.P.grid(row=5, column=16)

        As = ('As', 'Arsenic', """'As black arsenic \n''As gray arsenic \n''As4 yellow arsenic \n''AlAs aluminum arsenide \n''AsBr3 arsenic tribromide \n''AsCl3 arsenic trichloride \n''AsF3 arsenic trifluoride \n''AsF5 arsenic pentafluoride \n''AsFe iron arsenide \n''GaAs gallium arsenide \n''AsH3 arsine \n''AsI3 arsenic iodide \n''AsIn indium arsenide \n''AsNi nickel arsenide \n''(AsS4)-3 orthothioarsenate ion \n''Tl3As thallium(I)arsenide \n''AsY yttrium arsenide \n''As2H4 diarsine \n''As2I4 arsenic diiodide \n''As2Mg3 magnesium arsenide \n''As2O3 arsenic trioxide \n''As2O5 arsenic pentoxide \n''As2S2 arsenic(II)sulfide \n''As2S3 arsenic(III)sulfide \n''As2S3 arsenic trisulfide \n''As2S5 arsenic(V)sulfide \n''As2Se arsenic hemiselenide \n''As2Se3 arsenic(III) selenide \n''As2Se5 arsenic(V) selenide \n''As2Te3 arsenic(III) telluride \n''As4S4 tetraarsenic tetrasulfide \n''BAs boron arsenide \n''Cr2As chromium arsenide \n''Cu3As copper arsenide \n''SbAs antimony arsenide \n''AgAsF6 silver hexafluoroarsenate(V) \n''Ag3AsO4 silver arsenate \n''AsCs3O4 cesium arsenate \n''KAsF6 potassium hexafluoroarsenate(V) \n''LiAsF6 lithium hexafluoroarsenate \n''NaAsF6 sodium hexafluoroarsenate(V) \n''FeAsO4 ferric arsenate \n''As(OH)3 arsenious acid \n''BF3·O(C2H5)2 boron trifluoride etherate \n''H3AsO4 arsenic acid, solid \n''AsHgI4 donovan's solution \n''AsKO2 potassium arsenite \n''NaAsO2 sodium arsenite \n''Na3AsO4 sodium arsenate \n''AsNa3O4 arsenic acid, trisodium salt \n''As2Ca3O8 pencal \n''As2Ca3O8 tricalcium orthoarsenate \n''Cd3(AsO4)2 cadmium arsenate \n''Co3(AsO4)2 cobalt arsenate \n''Cu3(AsO4)2 copper(II) arsenate \n''Fe3(AsO4)2 iron(II) arsenate \n''As2O5·xH2O arsenic(V)oxide hydrate \n''Mg3(AsO4)2 magnesium arsenate \n''As2Mg6O11 arsenic acid, magnesium salt (1:6) \n''As2O4Pb lead arsenite \n''ZnAs2O4 zinc arsenite \n''As2O6Pb lead metaarsenate \n''Pb3(AsO4)2 lead(II) arsenate \n''Sr3(AsO4)2 strontium arsenate \n''Zn3(AsO4)2 zinc arsenate \n''As(CH3)3 trimethylarsine \n''(C6H5)3As triphenylarsine \n''C24H20As tetraphenyl-arsonium \n''(C6H5)2AsCH2CH2As(C6H5)2 ethylenebis(diphenylarsine) \n''CaAsO3 calcium arsenite \n''KAsO3 potassium metaarsenate \n''BiH3AsO3 bismuth arsenate \n''AsCaHO4 arsenic acid, calcium salt (1:1) \n''AsCuHO3 copper(II) arsenite \n''AsHNa2O4 disodium hydrogen arsenate \n''PbHAsO4 schultenite \n''KH2AsO4 potassium dihydrogen arsenate \n''AsH2NaO4 monosodium arsenate \n''RbH2AsO4 rubidium dihydrogenarsenate \n''AsH3O5Zn arsenic acid, zinc salt (1:1), monohydrate \n''K2HAsO4·2H2O potassium hydrogenarsenate dihydrate \n''AsH6NO4 ammonium dihydrogen arsenate \n''(NH4)2HAsO4 ammonium arsenate \n''Na2HAsO4·7H2O disodium hydrogen arsenate heptahydrate \n''As2H6O6Sb2 antimony oxide mixed with arsenic oxide \n''As2H8O8Sr strontium arsenite tetrahydrate \n''CH3AsCl2 methyldichloroarsine \n''CH5AsO3 methylarsonic acid \n''C2H2AsCl3 lewisite \n''C2H5AsCl2 ethyldichloroarsine \n''C2H5AsO5 arsonoacetate \n''C2H7AsO dimethylarsinous acid \n''C2H7AsO2 cacodylic acid \n''C5H11AsO8 ribose-1-arsenate \n''C6H5AsCl2 phenyldichloroarsine \n''C6H5AsO oxophenylarsine \n''C6H7AsO3 benzenearsonic acid \n''As(C2H5O)3 arsenic(III) ethoxide \n''NaAuCl4·2H2O sodium tetrachloroaurate(III)dihydrate \n''C12H10AsCl diphenylchloroarsine \n''C13H10AsN diphenylcyanoarsine \n''(C6H5)3AsO triphenylarsine oxide \n''C19H18AsI methyltriphenylarsonium iodide \n''C24H16As2O3 phenarsazine oxide \n''C24H20AsO2 (3,4-dihydroxy-phenyl)-triphenyl-arsonium \n''(C6H5)4As(Cl)·xH2O tetraphenylarsonium chloride \n''C24H21AsCl2 tetraphenylarsonium hydrogen dichloride \n''HgHAsO4 mercury(II) hydrogen arsenate \n''XeF5AsF6 xenon pentafluoride hexafluoroarsenate \n''Xe2F3AsF6 xenon fluoride hexafluoroarsenate \n''Mg(NH4)(AsO4) magnesium ammonium arsenate \n''CH3AsNa2O3 disodium methanearsonate \n''CH4AsNaO3 sodium methanearsonate \n''(CH3)2AsO2Na sodium cacodylate \n''C4H6As6Cu4O16 copper(II) acetate metaarsenite \n''O2NC6H4AsO3H2 2-nitrophenylarsonic acid \n''HOC6H3(NO2)AsO3H2 roxarsone \n''C6H8AsNO3 arsanilic acid \n''H2NC6H4AsO3H2 o-arsanilic acid \n''C7H9AsN2O4 carbarsone \n''C12H9AsClN phenarsazine chloride \n''C12H12AsN3O3 4-(4-aminophenylazo)phenylarsonic acid \n''(C6H5)4AsCl·HCl·xH2O tetraphenylarsonium(V)chloride hydrochloride hydrate \n''Co3(AsO4)2·8H2O cobalt(II) arsenate octahydrate \n''Fe3(AsO4)2·6H2O iron(II) arsenate hexahydrate \n''Ni3(AsO4)2·8H2O nickel(II) arsenate octahydrate \n''Zn3(AsO4)2·8H2O zinc arsenate octahydrate \n''C3H8AsNO3S thiarsahydroxy-cysteine \n''C3H8AsNO5S s-arsonocysteine \n''C5H12AsNO2S s-(dimethylarsenic)cysteine \n''C5H12AsNO3S cystein-s-yl cacodylate \n''C6H7AsNNaO3 sodium arsanilate \n''C11H19AsN5O12P2 gamma-arsono-beta, gamma-methyleneadenosine-5'-diphosphate \n''(CH3)2NC6H4N=NC6H4AsO3H2·HCl 4-[4-(dimethylamino)phenylazo]benzenearsonic acid hydrochloride \n''C16H11N2O10S2Na2As thorin \n''C16H13AsN2O11S2 arsenazo\n''C22H18As2N4O14S2 arsenazo III \n''C16H11AsN2Na2O10S2 thorin \n''C22H16As2N4Na2O14S2 arsenazo III disodium salt \n'""", '33', '74.92')
        self.colorAs=colorAs="lime green"
        self.As = tk.Button(self, text=As[0], width=5, height=2, bg=colorAs, font=10, borderwidth=3,
                           command=lambda text=As: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAs, text[0], text[3], text[4]), self.voice(text[1]), self.compound_As()])
        self.As.grid(row=6, column=16)

        Sb = ('Sb', 'Antimony', """'Sb gray antimony \n''AlSb aluminum antimonide \n''Ba3Sb2 barium antimonide \n''BiSb bismuth antimonide \n''SbBr3 antimony tribromide \n''CdSb cadmium antimonide \n''SbCl3 antimony(III) chloride \n''SbCl5 antimony pentachloride \n''CoSb cobalt antimonide \n''CrSb chromium antimonide \n''Cs3Sb cesium antimonide \n''Cu3Sb copper antimonide \n''DySb dysprosium antimonide \n''ErSb erbium antimonide \n''SbF3 antimony trifluoride \n''SbF5 antimony pentafluoride \n''FeSb2 iron diantimonide \n''GaSb gallium antimonide \n''GdSb gadolinium antimonide \n''HoSb holmium antimonide \n''SbI3 antimony(III) iodide \n''InSb indium antimonide \n''LaSb lanthanum antimonide \n''Li3Sb lithium antimonide \n''LuSb lutetium antimonide \n''Mg3Sb2 magnesium antimonide \n''MnSb manganese antimonide (1:1) \n''Mn2Sb manganese antimonide (2:1) \n''Na3Sb sodium antimonide \n''NdSb neodymium antimonide \n''Ni3Sb nickel antimonide \n''Sb2O3 antimony trioxide \n''O3Sb2 antimony oxide \n''Sb2O4 antimony tetroxide \n''Sb2O5 antimony pentoxide \n''Rb3Sb rubidium antimonide \n''Sb2S3 antimony(III)sulfide \n''Sb2S5 antimony(V)sulfide \n''SbAs antimony arsenide \n''SbH3 stibine \n''ScSb scandium antimonide \n''TbSb terbium antimonide \n''TmSb thullium monoantimonide \n''YbSb ytterbium monoantimonide \n''Sb2Se3 antimony(III) selenide \n''Sb2Te3 antimony(III)telluride \n''YSb yttrium antimonide \n''ZnSb zinc antimonide \n''AgSbF6 silver(I) hexafluoroantimonate \n''(CH3)3Sb trimethylantimony \n''C5H15Sb pentamethylstibine \n''(C6H5)3Sb triphenylstibine \n''(C6H5)2SbC6H4CH3 diphenyl(o-tolyl)antimony(III) \n''HSbF6 fluoroantimonic acid \n''KSbF6 potassium hexafluoroantimonate(V) \n''NaSbF6 sodium hexafluoroantimonate \n''LiSbF6 lithium hexafluoroantimonate \n''O3S3Sb4 antimony oxide sulfide \n''O8Pb3Sb2 lead(II) antimonate \n''O12S3Sb2 antimony(III) sulfate \n''[Sb(CH3)2]2 tetramethyldistibine \n''SbCl2F3 antimony(V) dichlorotrifluoride \n''SbOCl antimony(III) oxychloride \n''Sb(OH)3 trihydroxyantimonite(iii) \n''SbPO4 antimony(III) phosphate \n''As2H6O6Sb2 antimony oxide mixed with arsenic oxide \n''Sb(OC2H5)3 antimony(III)ethoxide \n''Sb(CH3)3Br2 trimethylantimony(V)bromide \n''Sb(CH3)3Cl2 trimethylantimony(V)dichloride \n''(CH3CO2)3Sb antimony(III) acetate \n''[(CH3)2N]3Sb tris(dimethylamido)antimony(III) \n''Sb(CH3CH(OH)COO)3 antimony lactate \n''Sb(OCH(CH3)2)3 antimony(III)isopropoxide \n''Sb(OC3H7)3 antimony(III)propoxide \n''Sb(OC4H9)3 antimony(III)butoxide \n''[CH3(CH2)3]4SbBr tetrabutylantimony(V)bromide \n''(C6H5)3SbCl2 triphenylantimony(V)dichloride \n''(CH3CO2)2Sb(C6H5)3 triphenylantimony(V)diacetate \n''(C6H5)4SbBr tetraphenylantimony(V)bromide \n''(C6H5)4SbOCH3 tetraphenylantimony(V)methoxide \n''CH3CO2Sb(C6H5)4 tetraphenylantimony(V)acetate \n''(C6H5)3Sb(O2CC6H5)2 triphenylantimony(V)dibenzoate \n''HSbF6·6H2O fluoroantimonic acid hexahydrate \n''NOSbF6 nitrosonium hexafluoroantimonate \n''KSb(OH)6 potassium hexahydroxyantimonate \n''KrFSb2F11 krypton fluoride hexafluoroantimonate \n''NH4SbF4 ammonium tetrafluoroantimonate \n''NO2SbF6 nitronium hexafluoroantimonate \n''XeFSb2F11 xenon fluoride undecafluoroantimonate \n''XeF3SbF6 xenon fluoride hexafluoroantimonate \n''XeF3Sb2F11 xenon trifluoride undecafluoroantimonate \n''(C2H5)3OSbCl6 triethyloxonium hexachloroantimonate \n''C8H4BaO12Sb2 antimony barium tartrate \n''C8H4K2O12Sb2·xH2O potassium antimony(III)tartrate hydrate \n''C12H35Na3O26Sb2 sodium stibogluconate \n''C20H15OP (triphenylphosphoranylidene)ketene \n''(C24H20S2)(C36H30S3)(SbF6)3 triarylsulfonium hexafluoroantimonate salts \n''HSO3F·SbF5 magic acid \n'""", '51', '121.75')
        self.colorSb=colorSb="olive drab"
        self.Sb = tk.Button(self, text=Sb[0], width=5, height=2, bg=colorSb, font=10, borderwidth=3,
                           command=lambda text=Sb: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSb, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Sb()])
        self.Sb.grid(row=7, column=16)

        Bi = ('Bi', 'Bismuth', """'Bi bismuth \n''BiBr3 bismuth bromide \n''BiCl3 bismuth chloride \n''BiF3 bismuth trifluoride \n''BiF5 bismuth pentafluoride \n''BiI3 bismuth(III) iodide \n''BiI3 bismuth iodide \n''BiSb bismuth antimonide \n''Bi2O3 bismuth trioxide \n''Bi2O4 bismuth tetroxide \n''Bi2S3 bismuth sulfide \n''Bi2Se3 bismuth selenide \n''ThBi2 thorium bismide \n''BaBiO3 barium bismuthate \n''BiNO4 bismuth oxynitrate \n''NaBiO3 sodium bismuthate \n''BiOBr bismuth oxybromide \n''BiO4P bismuth(III) phosphate \n''BiVO4 bismuth orthovanadate \n''Bi2(MoO4)3 bismuth(III)molybdate \n''Bi2O3·2TiO2 bismuth titanate \n''Bi2(SO4)3 bismuth sulfate \n''2Bi2O3·3ZrO2 bismuth(III)zirconate \n''(BiO)2CO3 basic bismuth(III) carbonate \n''C3H9Bi bismuth trimethyl \n''(C6H5)3Bi triphenylbismuth \n''Bi2(Al2O4)3·xH2O bismuth aluminate hydrate \n''BiH3AsO3 bismuth arsenate \n''BiCdPbSn woods metal \n''BiClO bismuth(III)oxychloride \n''BiIO bismuth(III)oxyiodide \n''BiONO3·H2O bismuth(III)subnitrate monohydrate \n''Bi(NO3)3·5H2O bismuth(III) nitrate pentahydrate \n''Bi2O3·2CrO3 bismuth basic dichromate \n''2Bi2O3·3GeO2 bismuth germanium oxide \n''C2H3BiO3 bismuth subacetate \n''(CH3CO2)3Bi bismuth acetate \n''[O2CCH2C(OH)(CO2)CH2CO2]Bi bismuth(III)citrate \n''HOC6H4COOBiO bismuth(III)subsalicylate \n''(C6H5)3BiCl2 triphenylbismuth(V)dichloride \n''(C6H5)3BiCO3 triphenylbismuth(III)carbonate \n''(CH3OC6H4)3Bi tris(2-methoxyphenyl)bismuthine \n''(CH3CO2)2Bi(C6H5)3 bis(acetato-O)triphenylbismuth(V) \n''Bi(OCOC(CH3)2(CH2)5CH3)3 bismuth neodecanoate \n''Bi(OCC(CH3)3CHCOC(CH3)3)3 bismuth(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''C54H99BiO6 bismuth oleate \n''Bi2(SnO3)3·5H2O bismuth stannate pentahydrate \n''Bi(OSO2CF3)3 bismuth(III) trifluoromethanesulfonate \n''Bi5O(OH)9(NO3)4 bismuth subnitrate \n''Bi(CF3COCHCOCF3)3 bismuth hexafluoro 2,4-pentanedioate \n'""", '83', '208.98')
        self.colorBi=colorBi="sea green"
        self.Bi = tk.Button(self, text=Bi[0], width=5, height=2, bg=colorBi, font=10, borderwidth=3,
                           command=lambda text=Bi: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorBi, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Bi()])
        self.Bi.grid(row=8, column=16)

        Mc = ('Mc', 'Moscovium', """'Uup ununpentium ununpentium metal\n'""", '115', '290')
        self.colorMc=colorMc="dark green"
        self.Mc = tk.Button(self, text=Mc[0], width=5, height=2, bg=colorMc, font=10, borderwidth=3,
                           command=lambda text=Mc: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(color7, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Mc()])
        self.Mc.grid(row=9, column=16)
        
        O = ('O', 'Oxygen', """'O2 oxygen \n''O3 ozone \n''AgO silver(II) oxide \n''AgO silver oxide \n''Al2O3 aluminum oxide \n''AmO2 americium(IV) oxide \n''Am2O3 americium(III) oxide \n''As2O3 arsenic trioxide \n''As2O5 arsenic pentoxide \n''Au2O3·xH2O gold(III) oxide \n''10B2O3 boron oxide-10 B \n''11B2O3 boron-11 boxide \n''B2O3 boron oxide \n''BaO barium oxide \n''BaO2 barium peroxide \n''BeO beryllium oxide \n''Bi2O3 bismuth trioxide \n''Bi2O4 bismuth tetroxide \n''BrO2 bromine dioxide \n''Br2O3 dibromine trioxide \n''Br2O5 dibromine pentoxide \n''CO carbon monoxide \n''13CO carbon-13C monoxide \n''CO2 carbon dioxide \n''13CO2 carbon-13 cdioxide \n''CO2 dry ice \n''CO2 liquid carbon dioxide \n''C3O2 carbon suboxide \n''C6O6·8H2O cyclohexanehexaone\n''CaO lime \n''CaO2 calcium peroxide \n''CdO cadmium oxide \n''CeO2 ceric oxide \n''Ce2O3 cerium(III) oxide \n''ClO2 chlorine dioxide \n''Cl2O chlorine monoxide \n''Cl2O3 dichlorine trioxide \n''Cl2O4 chlorine perchlorate \n''Cl2O6 dichlorine hexoxide \n''Cl2O7 dichlorine heptoxide \n''CoO cobalt monoxide \n''Co2O3 cobalt(III) oxide \n''Co3O4 cobalt(II,III)oxide \n''CrO2 magtrieve™ \n''CrO3 chromium trioxide \n''Cr2O3 chromium(III) oxide \n''Cr2O5 chromium(V) oxide \n''Cr3O4 chromium(II,III) oxide \n''Cr5O12 chromic chromate \n''CsO2 cesium superoxide \n''Cs2O3 cesium trioxide \n''CuO cupric oxide \n''D2O heavy water \n''Dy2O3 dysprosium(III) oxide \n''Er2O3 erbium oxide \n''Eu2O3 europium(III) oxide \n''F2O oxygen difluoride \n''F2O2 difluorine dioxide \n''F2O4 fluorine tetroxide \n''FeO iron(II) oxide \n''Fe2O3 iron(III) oxide \n''FeO·Fe2O3 iron(II,III) oxide \n''Ga2O gallium suboxide \n''Ga2O3 gallium(III) oxide \n''Gd2O3 gadolinium(III) oxide \n''GeO germanium(II) oxide \n''GeO2 germanium dioxide \n''HO2R a lipid hydroperoxide \n''H2O ice \n''H2O steam \n''H2O water \n''H218O water-18 O \n''3H2O water-t2 \n''H2O2 hydrogen peroxide \n''HfO2 hafnium oxide \n''HgO mercuric oxide \n''Hg2O mercury(I) oxide \n''Ho2O3 holmium(III) oxide \n''I2O4 iodine tetroxide \n''I2O5 iodopentoxide \n''iodic anhydride \n''I2O6 iodine hexoxide \n''I4O9 iodine nonaoxide \n''In2O3 indium(III) oxide \n''IrO2 iridium(IV) oxide \n''Ir2O3 iridium(III) oxide \n''KO2 potassium superoxide \n''K2O2 potassium peroxide \n''La2O3 lanthanum oxide \n''Li2O lithium oxide \n''Li2O2 lithium peroxide \n''Lu2O3 lutetium(III) oxide \n''MgO magnesium oxide \n''MgO2·xMgO magnesium peroxide \n''MnO manganese monoxide \n''MnO2 manganese dioxide \n''Mn2O3 manganese(III) oxide \n''Mn2O7 manganese(VII) oxide \n''MoO2 molybdenum dioxide \n''MoO3 molybdenum trioxide \n''Mo2O3 molybdenum(III) oxide \n''NO nitric oxide \n''15NO nitric-15 noxide \n''15N18O nitric-15 noxide-18 O \n''15N2O nitrous oxide-15 N2 \n''NO2 nitrogen dioxide \n''N2O nitrous oxide \n''N2O3 nitrogen trioxide \n''N2O4 nitrogen tetroxide \n''N2O5 nitrogen pentoxide \n''NaO2 sodium superoxide \n''Na2O sodium oxide \n''Na2O2 sodium peroxide \n''NbO niobium(II) oxide \n''NbO2 niobium(IV) oxide \n''Nb2O5 niobium pentoxide \n''Nd2O3 neodymium(III) oxide \n''NiO nickel monoxide \n''NpO2 neptunium(IV) oxide \n''PbO lead monoxide \n''OPd palladium oxide \n''OPt platinum(II) oxide \n''SiO silicon monoxide \n''SnO stannous oxide \n''SrO strontium oxide \n''TiO titanium monoxide \n''OTl2 thallium(I) oxide \n''OV vanadium(II) oxide \n''ZnO zinc oxide \n''PbO2 lead dioxide \n''PtO2 platinum(IV) oxide \n''ReO2 rhenium oxide \n''RhO2 rhodium dioxide \n''RuO2 ruthenium dioxide \n''SO2 sulfur dioxide \n''SeO2 selenium dioxide \n''O2Se selenium oxide \n''SiO2 cristobalite \n''SiO2 quartz \n''SiO2 silicon dioxide \n''SiO2 tridymite \n''SnO2 stannic oxide \n''SrO2 strontium peroxide \n''O2Ta tantalum(IV) oxide \n''TeO2 tellurium dioxide \n''ThO2 thorium(IV) oxide \n''TiO2 titanium(IV) oxide (anatase) \n''TiO2 titanium(IV) oxide (rutile) \n''TiO2 titanium dioxide \n''O2U uranium dioxide \n''V2O4 vanadium(IV)oxide \n''WO2 tungsten dioxide \n''ZnO2 zinc peroxide \n''ZrO2 zirconium(IV) oxide \n''P2O3 phosphorus trioxide \n''ReO3 rhenium(vI) oxide rhenium oxide \n''Rh2O3 rhodium(III) oxide \n''SO3 sulfur trioxide \n''Sb2O3 antimony trioxide \n''O3Sb2 antimony oxide \n''Sc2O3 scandium(III) oxide \n''SeO3 selenium trioxide \n''Sm2O3 samarium(III) oxide \n''Tb2O3 terbium(III)oxide \n''O3Te tellurium trioxide \n''Ti2O3 titanium(III) oxide \n''Tl2O3 thallium(III)oxide \n''Tm2O3 thulium(III) oxide \n''O3U uranium(vI) oxide \n''V2O3 vanadium(III)oxide \n''WO3 tungsten trioxide \n''Y2O3 yttrium oxide \n''Yb2O3 ytterbium(III) oxide \n''OsO4 osmium tetroxide \n''Pb3O4 lead(II,IV) oxide \n''O4Ru ruthenium(VIII) oxide \n''Sb2O4 antimony tetroxide \n''Sb2O5 antimony pentoxide \n''Ta2O5 tantalum(V)oxide \n''V2O5 vanadium pentoxide \n''O6P4 tetraphosphorus(III) hexoxide \n''Re2O7 rhenium(VII) oxide \n''Tb4O7 terbium(III,IV)oxide \n''P2O5 phosphorus pentoxide \n''Pr2O3 prasedymium(III)oxide \n''Pr6O11 praseodymium oxide \n''OsO2 osmium(IV) oxide \n''PoO2 polonium(IV) oxide \n''PuO plutonium(II) oxide \n''PuO2 plutonium(IV) oxide \n''Pu2O3 plutonium(III) oxide \n''RbO2 rubidium superoxide \n''Ti3O5 titanium(III,IV) oxide \n''U3O8 uranium(V,VI) oxide \n''U4O9 uranium(IV,V) oxide \n''XeO3 xenon trioxide \n''XeO4 xenon tetroxide \n''AgClO2 silver(I) chlorite \n''AgClO3 silver chlorate \n''AgClO4 silver perchlorate \n''AgIO3 silver iodate \n''AgNO2 silver nitrite \n''AgNO3 silver nitrate \n''AgO3P silver(I) metaphosphate \n''AgReO4 silver(I)perrhenate \n''Ag2CrO4 silver(I) chromate \n''Ag2Cr2O7 silver(I) dichromate \n''Ag2O silver(I)oxide \n''Ag2MoO4 silver molybdate \n''Ag2SO3 silver(I)sulfite \n''Ag2SO3 silver sulfite \n''Ag2O3Se silver(I) selenite \n''Ag2SO4 silver sulfate \n''Ag2WO4 silver tungstate \n''Ag2S2O3 silver(I) thiosulfate \n''Ag2SeO4 silver(I) selenate \n''Ag3AsO4 silver arsenate \n''Ag3PO4 silver phosphate \n''AlCl3O9 aluminum chlorate nonahydrate \n''AlCl3O12 aluminum perchlorate \n''Al(OH)3 aluminum hydroxide \n''LaAlO3 lanthanum aluminum oxide \n''LiAlO2 lithium aluminate \n''Al(NO3)3 aluminum nitrate \n''AlNaO2 sodium aluminate \n''AlO4P aluminum phosphate \n''Al2CaO4 calcium aluminate \n''CoAl2O4 cobalt aluminum oxide \n''CuAl2O4 copper aluminum oxide \n''MgO·Al2O3 magnesium aluminate \n''Al2O3·TiO2 aluminum titanate \n''Al2(SO4)3 aluminum sulfate \n''Y3Al5O12 yttrium aluminum oxide \n''3Al2O3·2SiO2 aluminum silicate \n''AsCs3O4 cesium arsenate \n''FeAsO4 ferric arsenate \n''As(OH)3 arsenious acid \n''BF3·O(C2H5)2 boron trifluoride etherate \n''H3AsO4 arsenic acid, solid \n''AsKO2 potassium arsenite \n''NaAsO2 sodium arsenite \n''Na3AsO4 sodium arsenate \n''AsNa3O4 arsenic acid, trisodium salt \n''As2Ca3O8 pencal \n''As2Ca3O8 tricalcium orthoarsenate \n''Cd3(AsO4)2 cadmium arsenate \n''Co3(AsO4)2 cobalt arsenate \n''Cu3(AsO4)2 copper(II) arsenate \n''Fe3(AsO4)2 iron(II) arsenate \n''As2O5·xH2O arsenic(V)oxide hydrate \n'""", '8', '15.99')
        self.colorO=colorO="DeepSkyBlue2"
        self.O = tk.Button(self, text=O[0], width=5, height=2, bg=colorO, font=10, borderwidth=3,
                           command=lambda text=O: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorO, text[0], text[3], text[4]), self.voice(text[1]), self.compound_O()])
        self.O.grid(row=4, column=17)

        S = ('S', 'Sulfur', """'S mixed sulfur \n''32S sulfur 32 \n''34S sulfur 34 \n''S2 disulfur \n''S3 trisulfur \n''S6 cyclo-hexasulfur \n''S8 monoclinic sulfur \n''S8 rhombic sulfur \n''Al2S3 aluminum sulfide \n''(AsS4)-3 orthothioarsenate ion \n''As2S2 arsenic(II)sulfide \n'As2S3 arsenic(III)sulfide \n''As2S3 arsenic trisulfide \n''As2S5 arsenic(V)sulfide \n''As4S4 tetraarsenic tetrasulfide \n''Au2S3 gold(III) sulfide \n''B2S3 boron sulfide \n''BaS barium sulfide \n''BeS beryllium sulfide \n''Bi2S3 bismuth sulfide \n''Br2S2 sulfur bromide (SSBr2) \n''CS2 carbon disulfide \n''13CS2 carbon-13 cdisulfide \n''C3S2 carbon subsulfide \n''CaS calcium sulfide \n''CdS cadmium sulfide \n''CeS cerium(II) sulfide \n''Ce2S3 cerium(III) sulfide \n''SCl2 sulfur dichloride \n''S2Cl2 sulfur monochloride \n''CoS cobaltous sulfide \n''CoS2 cobalt disulfide \n''Cr2S3 chromium(III) sulfide \n''CuS cupric sulfide \n''D2S deuterium sulfide \n''Dy2S3 dysprosium(III) sulfide \n''Er2S3 erbium sulfide \n''EuS europium(II) sulfide \n''F4S sulfur tetrafluoride \n''SF6 sulfur hexafluoride \n''FeS ferrous sulfide \n''FeS2 pyrite \n''Fe3S3 fe3 iron-sulfur center \n''Fe3S4 fe4 iron-sulfur cluster \n''Fe4S4 fe4 iron-sulfur center \n''Ga2S3 gallium(III) sulfide \n''Gd2S3 gadolinium(III) sulfide \n''GeS germanium(II)sulfide \n''GeS2 germanium(IV) sulfide \n''H2S hydrogen sulfide \n''HfS2 hafnium(IV) sulfide \n''HgS mercury(II) sulfide \n''HgS mercury(II) sulfide \n''Hg2S mercury(I) sulfide \n''Ho2S3 holmium sulfide \n''InS indium(II) sulfide \n''In2S3 indium(III)sulfide red \n''IrS2 iridium(IV) sulfide \n''Ir2S3 iridium(III) sulfide \n''LaS lanthanum monosulfide \n''La2S3 lanthanum sulfide \n''Li2S lithium sulfide \n''Lu2S3 lutetium sulfide \n''MgS magnesium sulfide \n''MnS manganese sulfide \n''MoS2 molybdenum disulfide \n''MoS3 molybdenum(VI) sulfide \n''N4S4 tetrasulfur tetranitride \n''NbS2 niobium(IV) sulfide \n''Nd2S3 neodymium(III) sulfide \n''NiS nickel(II) sulfide \n''Ni3S2 nickel sulfide \n''Ni3S4 nickel(II,III) sulfide \n''SO2 sulfur dioxide \n''SO3 sulfur trioxide \n''P2S3 phosphorus trisulfide \n''P4S3 phosphorus sesquisulfide \n''P4S7 phosphorus heptasulfide \n''P2S5 phosphorus pentasulfide \n''PbS lead sulfide \n''PdS palladium(II) sulfide \n''Pr2S3 praseodymium(III) sulfide \n''PtS platinum(II) sulfide \n''PtS2 platinum(IV)sulfide \n''ReS2 rhenium(IV) sulfide \n''SSe selenium monosulfide \n''SnS tin(II)sulfide \n''SrS strontium sulfide \n''Tl2S thallium(I)sulfide \n''Tl2S thallium sulfide \n''SV vanadium sulfide \n''ZnS zinc sulfide \n''SeS2 selenium disulfide \n''S2Si silicon disulfide \n''SnS2 tin(IV) sulfide \n''S2Ta tantalum(IV) sulfide \n''S2Th thorium(IV) sulfide \n''TiS2 titanium disulfide \n''S2U uranium sulfide \n''WS2 tungsten(IV) sulfide \n''S2Zr zirconium(IV) sulfide \n''Sb2S3 antimony(III)sulfide \n''Sb2S5 antimony(V)sulfide \n''SiS silicon monosulfide \n''Sm2S3 samarium(III) sulfide \n''Tb2S3 terbium(III) sulfide \n''TiS titanium(II) sulfide \n''Ti2S3 titanium(III) sulfide \n''V2S3 vanadium(III) sulfide \n''V2S5 vanadium(V) sulfide \n''WS3 tungsten(VI) sulfide \n''Y2S3 yttrium sulfide \n''Ag2S silver(I) sulfide \n''Ag2SO3 silver(I)sulfite \n''Ag2SO3 silver sulfite \n''Ag2SO4 silver sulfate \n''Ag2S2O3 silver(I) thiosulfate \n''Al2(SO4)3 aluminum sulfate \n''Au2S gold(I)sulfide \n''BaH2S polybarit \n''BaSO3 barium sulfite \n''BaSO4 barium sulfate \n''BeSO4 beryllium sulfate \n''Bi2(SO4)3 bismuth sulfate \n''SOBr2 thionyl bromide \n''Br3PS phosphorothioc tribromide \n''CSCl2 thiophosgene \n''CCl3SCl perchloromethyl mercaptan \n''CH3SH methanethiol \n''CH3SNa sodium methanethiolate \n''CNa2S3 sodium trithiocarbonate \n''COS carbonyl sulfide \n''13COS carbonyl-13 csulfide \n''CSSe carbon sulfide selenide \n''CSTe carbon sulfide telluride \n''CD3SCD3 dimethyl sulfide-d 6 \n''(CD3)2S2 dimethyl-d 6disulfide \n''C2F4S2 2,2,4,4-tetrafluoro-1,3-dithietane \n''C2H4S ethylene sulfide \n''(CH3)2S dimethyl sulfide \n''C2H5SH ethanethiol \n''HSCH2CH2SH 1,2-ethanedithiol \n''CH3SSCH3 dimethyl disulfide \n''CH3SSSCH3 dimethyl trisulfide \n''C3H2S3 vinylene trithiocarbonate \n''C3H4S thioacrolein \n''C3H4S3 ethylene trithiocarbonate \n''CH2=CHCH2SH 2-propene-1-thiol \n''C3H6S propylene sulfide \n''C3H6S trimethylene sulfide \n''C3H6S2 1,3-dithiolane \n''C3H6S3 1,3,5-trithiane \n''(CH3S)2CS dimethyl trithiocarbonate \n''CH3CH2CH2SH 1-propanethiol \n''(CH3)2CHSH 2-propanethiol \n''CH3CH2SCH3 (methylthio)ethane \n''HS(CH2)3SH 1,3-propanedithiol \n''CH3SCH2SCH3 bis(methylthio)methane \n''C3H8S2 yeast lytic enzyme \n''C4Br4S tetrabromothiophene \n''C4Cl4S tetrachlorothiophene \n''C4H4S thiophene \n''C4H4S2 thiophene-2-thiol \n''H2C=CHCH2SCH3 allyl methyl sulfide \n''C2H5SCH=CH2 ethyl vinyl sulfide \n''C4H8S tetrahydrothiophene \n''C4H8S2 1,3-dithiane \n''C4H8S2 1,4-dithiane \n''CH3CSSCH2CH3 ethyl dithioacetate \n''C4H8S3 allyl methyl trisulfide \n''CH3(CH2)3SH 1-butanethiol \n''C4H10S 1-(methylthio)propane \n''CH3CH2CH(SH)CH3 2-butanethiol \n''(CH3)2CHCH2SH 2-methyl-1-propanethiol \n''(CH3)3CSH 2-methyl-2-propanethiol \n''(C2H5)2S diethyl sulfide \n''CH3CH(SH)CH2CH2SH 1,3-butanedithiol \n''HS(CH2)4SH 1,4-butanedithiol \n''CH3CH(SH)CH(SH)CH3 2,3-butanedithiol \n''(C2H5)2S2 diethyl disulfide \n''CH3CH2CH2SSCH3 methyl propyl disulfide \n''(HSCH2CH2)2S 2,2'-thiodiethanethiol \n''(CH3S)3CH tris(methylthio)methane \n''C4O2S4 1,3,4,6-tetrathiapentalene-2,5-dione \n''C5H4S5 4,5-ethylenedithio-1,3-dithiol-2-thione \n''C5H6S 2-methylthiophene \n''C5H6S 3-methylthiophene \n''C5H6S2 2-(methylthio)thiophene \n''C5H6S2 2-thiophenemethanethiol \n''C5H6S5 4,5-bis(methylthio)-1,3-dithiol-2-thione \n''C5H10S allyl ethyl sulfide \n''C5H9SH cyclopentanethiol \n''C5H10S pentamethylene sulfide \n''C5H10S2 2-methyl-1,3-dithiane \n''CH3(CH2)4SH 1-pentanethiol \n''C2H5CH(CH3)CH2SH 2-methyl-1-butanethiol \n''C5H12S 2-methyl-2-butanethiol \n''CH3CH2CH2CH(SH)CH3 2-pentanethiol \n''(CH3)2CHCH2CH2SH 3-methyl-1-butanethiol \n''(CH3)2CHCH(SH)CH3 3-methyl-2-butanethiol \n''C5H12S butyl methyl sulfide \n''C5H12S ethyl n-propyl sulfide \n''C5H12S sec-butyl methyl sulfide \n''(CH3)3CSCH3 tert-butyl methyl sulfide \n''C5H12S2 1,3-bis(methylthio)propane \n''HS(CH2)5SH 1,5-pentanedithiol \n''C6H4S 3-ethynylthiophene \n''C6H4S4 tetrathiafulvalene \n''C6H5SH phenyl mercaptan \n''C6H4(SH)2 benzene-1,2-dithiol \n''C6H4(SH)2 1,3-benzenedithiol \n''(-C6H4S-)n poly(1,4-phenylene sulfide) \n''C6H8S 2,3-dimethylthiophene \n''C6H8S 2,5-dimethylthiophene \n''C6H8S 2-ethylthiophene \n''C6H8S2 2-vinyl-[4h]-1,3-dithin \n''C6H8S2 3-vinyl-[4h]-1,2-dithin \n''C6H8S2 alpha-methylthiophene-2-methanethiol \n''C6H10S 7-thiabicyclo[4.1.0]heptane \n''(CH2=CHCH2)2S diallyl sulfide \n''CH2=CHCH2SSCH2CH=CH2 diallyl disulfide \n''[C(SC2H5)=C(SC2H5)]n poly[1,2-bis(ethylthio)acetylene] \n''C6H12S allyl propyl sulfide \n''C6H11SH cyclohexanethiol \n''C6H12S2 allyl propyl disulfide \n''C6H12S3 1,4,7-trithiacyclononane \n''C6H14S 1-(ethylthio)butane \n''CH3(CH2)5SH 1-hexanethiol \n''(CH3CH2CH2)2S dipropyl sulfide \n''C6H14S isopropyl n-propyl sulfide \n''[(CH3)2CH]2S diisopropyl sulfide \n''C6H14S tert-butyl ethyl sulfide \n''HS(CH2)6SH 1,6-hexanedithiol \n''CH3CH2CH2SSCH2CH2CH3 dipropyl disulfide \n''[(CH3)2CH]2S2 diisopropyl disulfide \n''CH3C6H4SH o-thiocresol \n''CH3C6H4SH m-toluenethiol \n''CH3C6H4SH p-thiocresol \n''C6H5CH2SH benzyl mercaptan \n''C6H5SCH3 thioanisole \n''C7H8S2 4-methylsulfanylbenzenethiol \n''C7H8S2 methyl phenyl disulfide \n''CH3C6H3(SH)2 toluene-3,4-dithiol \n''C7H10S 2-N-propylthiophene \n''C7H14S cyclohexyl methyl sulfide \n''CH3(CH2)6SH 1-heptanethiol \n''C7H16S butyl propyl sulfide \n''C7H16S3 tris(ethylthio)methane \n''C8H6S benzo[b]thiophene \n''C8H6S2 2,2'-bithiophene \n''C8H6S2 2,3'-bithiophene \n''C8H6S2 3,3'-bithiophene \n''C8H6S4 2-thienyl disulfide \n''C6H5SCH=CH2 (ethenylthio)benzene \n''C8H8S2 2-(2,4-cyclopentadien-1-ylidene)-1,3-dithiolane \n''(CH3)2C6H3SH 2,4-dimethylbenzenethiol \n''(CH3)2C6H3SH 2,5-dimethylbenzenethiol \n''(CH3)2C6H3SH 2,6-dimethylbenzenethiol \n''C2H5C6H4SH o-ethylbenzenethiol \n''C8H10S 2-methylbenzyl mercaptan \n''C6H5CH2CH2SH 2-phenylethanethiol \n''(CH3)2C6H3SH 3,4-dimethylbenzenethiol \n''(CH3)2C6H3SH 3,5-dimethylbenzenethiol \n''C8H10S 4-methylbenzyl mercaptan \n''C6H5CH2SCH3 benzyl methyl sulfide \n''C6H5SC2H5 (1-thiapropyl)benzene \n''CH3C6H4SCH3 methyl p-tolyl sulfide \n''C6H4(CH2SH)2 1,2-benzenedimethanethiol \n''C6H4(CH2SH)21,3-benzenedimethanethiol \n''C6H4(CH2SH)2 1,4-benzenedimethanethiol \n''C8H12S 2-N-butylthiophene \n''C8H12S 3-butylthiophene \n''C8H16S (S)-(-)-1,2-epithiooctane \n''C8H16S4 1,4,7,10-tetrathiacyclododecane \n''CH3(CH2)7SH 1-octanethiol \n''C8H18S 2-ethylhexanethiol \n''C8H18S di-tert-butyl sulfide \n''CH3(CH2)3S(CH2)3CH3 dibutyl sulfide \n''[C2H5CH(CH3)]2S di-sec-butyl sulfide \n''C8H18S tert-octyl mercaptan \n''C8H18S tert-octylthiol \n''C8H18S2 2,9-dithiadecane \n''(CH3)3CSSC(CH3)3 tert-butyl disulfide \n''CH3(CH2)3SS(CH2)3CH3 dibutyl disulfide \n''C8H18S2 1,8-octanedithiol \n''[C2H5CH(CH3)]2S2 sec-butyl disulfide \n''C9H8S 2-methylthianaphthene \n''C9H8S 3-methylbenzo[b]thiophene \n''C9H8S 5-methylbenzo[b]thiophene \n'""", '16', '32.06')
        self.colorS=colorS="DeepSkyBlue3"
        self.S = tk.Button(self, text=S[0], width=5, height=2, bg=colorS, font=10, borderwidth=3,
                           command=lambda text=S: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorS, text[0], text[3], text[4]), self.voice(text[1]), self.compound_S()])
        self.S.grid(row=5, column=17)

        Se = ('Se', 'Selenium', """'Se black selenium \n''Se gray selenium \n''Se8 red selenium \n''Ag2Se silver selenide \n''Al2Se3 aluminum selenide \n''As2Se arsenic hemiselenide \n''As2Se3 arsenic(III) selenide \n''As2Se5 arsenic(V) selenide \n''Au2Se3 gold(III) selenide \n''Bi2Se3 bismuth selenide \n''Br2Se2 selenium bromide \n''SeBr4 selenium tetrabromide \n''CSe2 carbon diselenide \n''CaSe calcium selenide \n''CdSe cadmium selenide \n''Se2Cl2 diselenium dichloride \n''SeCl4 selenium tetrachloride \n''CoSe cobalt(II) selenide \n''CrSe chromium selenide \n''CuSe cupric selenide \n''Cu2Se copper(I) selenide \n''EuSe europium(II) selenide \n''F4Se selenium tetrafluoride \n''F6Se selenium hexafluoride \n''FeSe iron(II) selenide \n''GaSe gallium(II) selenide \n''Ga2Se3 gallium selenide \n''GdSe gadolinium(II) selenide \n''GeSe germanium(II)selenide \n''GeSe2 germanium(IV) selenide \n''SeH2 hydrogen selenide \n''HfSe2 hafnium selenide \n''HgSe mercury(II) selenide \n''In2Se3 indium(III)selenide \n''K2Se potassium selenide \n''Li2Se lithium selenide \n''MgSe magnesium selenide \n''MnSe manganese(II) selenide \n''MoSe2 molybdenum(IV) selenide \n''Na2Se sodium selenide \n''NbSe2 niobium selenide \n''NiSe nickel(II) selenide \n''SeO2 selenium dioxide \n''O2Se selenium oxide \n''SeO3 selenium trioxide \n''P2Se5 phosphorus(V) selenide \n''P4Se3 tetraphosphorus triselenide \n''PbSe lead(II) selenide \n''Rb2Se rubidium selenide \n''ReSe2 rhenium(IV) selenide \n''SSe selenium monosulfide \n''SeS2 selenium disulfide \n''Sb2Se3 antimony(III) selenide \n''SrSe strontium selenide \n''Tl2Se thallium(I) selenide \n''ZnSe zinc selenide \n''TaSe2 tantalum(IV) selenide \n''Se2Th thorium(IV) selenide \n''Se2U uranium diselenide \n''Se2V vanadium diselenide \n''WSe2 tungsten(IV) selenide \n''SnSe tin(II) selenide \n''SnSe2 tin(IV) selenide \n''Ag2O3Se silver(I) selenite \n''Ag2SeO4 silver(I) selenate \n''Au2(SeO4)3 gold(III) selenate \n''BaSeO3 barium selenite \n''BaSeO4 barium selenate \n''BaSeO4 barium selenate(VI) \n''Br2OSe selenium oxybromide \n''CH2Se selenoformaldehyde \n''CSSe carbon sulfide selenide \n''C2H6Se dimethyl selenide \n''(CH3)2Se2 dimethyl diselenide \n''(CH3)3Se+ trimethylselenonium ion \n''C4H4Se selenophene \n''Se(C2H5)2 diethyl selenide \n''C6H5SeH benzeneselenol \n''C7H8Se methyl phenyl selenide \n''C8H6Se benzo[b]selenophene \n''Se(C(CH3)3)2 di-tert-butyl selenide \n''C10H12Se4 tetramethyltetraselenafulvalene \n''C12H8Se2 selenanthrene \n''(C6H5)2Se diphenyl selenide \n''C6H5SeSeC6H5 diphenyl diselenide \n''C14H14Se dibenzyl selenide \n''(C6H5CH2)2Se2 dibenzyl diselenide \n''CdSeO4 cadmium selenate \n''Ce2(SeO4)3 cerium(III) selenate \n''SeOCl2 selenium oxychloride \n''CuSeO4 copper(II) selenate \n''H2SeO3 selenious acid \n''H2SeO4 selenic acid \n''K2SeO3 selenious acid, dipotassium salt \n''K2SeO4 potassium selenate \n''Na2SeO3 sodium selenite \n''PbSeO3 lead(II)selenite \n''SrSeO4 strontium selenate \n''PbSeO4 lead(II) selenate \n''SeF5Cl selenium chloride pentafluoride \n''SeOF2 selenium oxyfluoride \n''SeOF4 selenium oxytetrafluoride \n''SeO2F2 selenium dioxydifluoride \n''Sn(SeO3)2 tin(IV) selenite \n''Tl2SeO4 thallium(I) selenate \n''NH2CSeNH2 selenourea \n''CH3SeO2H methaneseleninic acid \n''KSeCN potassium selenocyanate \n''C3H5O2Se [methylseleno]acetate \n''(CH3)2NC(Se)NH2 1,1-dimethyl-2-selenourea \n''C3H8N2Se se-ethyl-isoselenourea \n''C3H8O2Se N-propylseleninic acid \n''C6H4N2Se 2,1,3-benzoselenadiazole \n''C6H5SeBr bromoselenobenzene \n''C6H5SeCl phenylselenyl chloride \n''C6H5SeO2H benzeneseleninic acid \n''C6H12SSe ((2-(ethylthio)ethyl)seleno)ethene \n''C6H5SeCN phenyl selenocyanate \n''C8H7NSe 2-methylbenzoselenazole \n''C8H7NSe benzyl selenocyanate \n''C8H15O2Se 6-seleno-octanoate \n''C8H15O2Se 8-seleno-octanoate \n''C9H9NSe 2,5-dimethylbenzoselenazole \n''C10H8N2Se2 selenocyanic acid, 1,4-phenylenebis(methylene) ester \n''C10H11NSe 2,5,6-trimethylbenzoselenazole \n''C6H5SeCH2Si(CH3)3 trimethyl(phenylselenomethyl)silane \n''C10H18N2Se 2-amino-4-butyl-5-propylselenazole \n''(ClC6H4)2Se2 bis(p-chlorophenyl) diselenide \n''C6H5SeOOSeOC6H5 benzeneseleninic anhydride \n''C12H10P2Se4 woollins'reagent \n''C12H12N2Se2 bis(2-aminophenyl)diselenide \n''C12H20Cl4Se dichlorobis(2-chlorocyclohexyl)selenium \n''C18H15ClSe triphenylselenonium chloride \n''C18H15PSe triphenylphosphine selenide \n''C19H22N2Se 1-(10,11-dihydrodibenzo(B,F)selenepin-10-yl)-4-methyl-piperazine \n''CuSeO3·2H2O copper(II) selenite dihydrate \n''CuH10O9Se copper(II) selenate pentahydrate \n''KHSeO3 potassium selenite \n''HOSeF5 pentafluoroorthoselenic acid \n''Na2SeO4 sodium selenate \n''ZnSeO3 zinc selenite \n''H6N2O4Se hydrazine selenate \n''H8N2O3Se ammonium selenite \n''H8N2O4Se ammonium selenate \n''H10Na2O8Se sodium selenite pentahydrate \n''H12NiO10Se nickel(II) selenate hexahydrate \n''Na2SeO4·10H2O sodium selenate decahydrate \n''BeSeO4·4H2O beryllium selenate tetrahydrate \n''C3H6NO4Se dioxyselenocysteine \n''C3H7NO2Se l-selenocysteine \n''C3H7NO2Se selenocysteine \n''C4H8NO2Se selenohomocysteine \n''C4H9NO2Se methylselenocysteine \n''C4H12Cl2PtSe2 cis-dichlorobis(dimethylselenide)platinum(II) \n''SeC5H11NO2 DL-selenomethionine \n''CH3SeCH2CH2CH(NH2)CO2H L-selenomethionine \n''C5H11NO2Se selenomethionine \n''C5H11NO3Se selenomethionine selenoxide \n''C5H12N2O2Se thialysine \n''C5H14N2O2Se selenalysine \n''C6H3N3O2Se 4-nitro-2,1,3-benzoselenadiazole \n''ClC6H4Se(O)OH 4-chlorobenzeneseleninic acid \n''CO2HCH(NH2)CH2(Se)2CH2CH(NH2)CO2H L-selenocystine \n''C7H4N2O2Se selenocyanic acid, p-nitrophenyl ester \n''O2NC6H4SeCN 2-nitrophenyl selenocyanate \n''C7H11NO2Se butyl selenocyanoacetate \n''C8H5NO3Se 5-(2-furanylmethylene)selenazolidine-2,4-dione \n''C8H6N2O3Se 4-methoxy-2-nitrophenyl selenocyanate \n''C8H7NSSe 3-methylbenzothiazole-2(3H)-selone \n''C9H8N2OSe selenocyanic acid, 2-oxo-2-(phenylamino)ethyl ester \n''C9H9NOSe 5-methoxy-2-methylbenzselenazole \n''C9H9N2O2Se (s)-2-amino-3-(4h-selenolo[3,2-b]-pyrrol-6-yl)-propionic acid \n''C9H9N2O2Se (s)-2-amino-3-(6h-selenolo[2,3-b]-pyrrol-4-yl)-propionic acid \n''C10H6N2O4Se 5-((2-nitrophenyl)methylene)selenazolidine-2,4-dione \n''C10H6N2O4Se 5-((4-nitrophenyl)methylene)selenazolidine-2,4-dione \n''C10H7NO3Se 2,4-selenazolidinedione, 5-salicylidene \n''C10H12N4O4Se selenoinosine \n''C11H9NO3Se 5-((4-methoxyphenyl)methylene)selenazolidine-2,4-dione \n''C11H9NO4Se 5-((3-hydroxy-4-methoxyphenyl)methylene)selenazolidine-2,4-dione \n''C11H9NO4Se 5-((4-hydroxy-3-methoxyphenyl)methylene)selenazolidine-2,4-dione \n''C11H17N3O5Se 5-methylaminomethyl-2-selenouridine \n''C12H8N2O4Se 5-(3-(2-nitrophenyl)-2-propenylidene)selenazolidine-2,4-dione \n''C12H8N2O4Se2 bis(2-nitrophenyl)diselenide \n''C12H9NO2Se 5-(3-phenyl-2-propenylidene)selenazolidine-2,4-dione \n''C12H11NO4Se 5-((2,4-dimethoxyphenyl)methylene)selenazolidine-2,4-dione \n''C12H11NO4Se 5-((3,4-dimethoxyphenyl)methylene)selenazolidine-2,4-dione \n''C12H12N2O2Se 5-((4-dimethylaminophenyl)methylene)selenazolidine-2,4-dione \n''C12H24N4S8Se selenium dimethyldithiocarbamate \n''C13H9NOSe ebselen \n''C14H9NO2Se N-(phenylseleno)phthalimide \n'""", '34', '78.96')
        self.colorSe=colorSe="DeepSkyBlue4"
        self.Se = tk.Button(self, text=Se[0], width=5, height=2, bg=colorSe, font=10, borderwidth=3,
                           command=lambda text=Se: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Se()])
        self.Se.grid(row=6, column=17)

        Te = ('Te', 'Tellurium', """'Te tellurium \n''Ag2Te silver telluride \n''As2Te3 arsenic(III) telluride \n''BaTe barium telluride \n''BeTe beryllium telluride \n''TeBr2 tellurium dibromide \n''TeBr4 tellurium tetrabromide \n''CaTe calcium telluride \n''CdTe cadmium telluride \n''TeCl4 tellurium tetrachloride \n''CoTe cobalt(II) telluride \n''Cr2Te3 chromium(III)telluride \n''CuTe copper(II) telluride \n''Cu2Te copper(I) telluride \n''Dy2Te3 dysprosium(III) telluride \n''Er2Te3 erbium telluride \n''EuTe europium(II) telluride \n''F4Te tellurium tetrafluoride \n''TeF6 tellurium hexafluoride \n''FeTe iron(II) telluride \n''GaTe gallium(II) telluride \n''Ga2Te3 gallium(III) telluride \n''Gd2Te3 gadolinium(III) telluride \n''GeTe germanium telluride \n''H2Te hydrogen telluride \n''HgTe mercury telluride \n''TeI4 tellurium tetraiodide \n''In2Te3 indium(III)telluride \n''Lu2Te3 lutetium telluride \n''MnTe manganese(II) telluride \n''MoTe2 molybdenum(IV) telluride \n''NbTe2 niobium(IV) telluride \n''Nd2Te3 neodymium(III) telluride \n''TeO2 tellurium dioxide \n''O3Te tellurium trioxide \n''PbTe lead(II)telluride \n''Pr2Te3 praseodymium(III) telluride \n''ReTe2 rhenium ditelluride \n''Sb2Te3 antimony(III)telluride \n''Sc2Te3 scandium telluride \n''Sm2Te3 samarium(III) telluride \n''SnTe tin(II) telluride \n''TaTe2 tantalum(IV) telluride \n''TeCl2 tellurium dichloride \n''ZnTe zinc telluride \n''Te2Th thorium telluride \n''Te2U uranium ditelluride \n''Te2V vanadium telluride \n''Te2W tungsten(IV) telluride \n''K2TeBr6 potassium hexabromotellurate(IV) \n''CSTe carbon sulfide telluride \n''C2H6Te dimethyltelluride \n''Te(CH2CH3)2 diethyltellurium \n''(C6H5)2Te2 diphenyl ditelluride \n''(C10H7)2Te2 1-naphthyl ditelluride \n''CdO3Te cadmium tellurite \n''CdTeO4 cadmium tellurate \n''CuO3Te copper(II) tellurite \n''CuTeO4 copper(II) tellurate \n''H2O3Te tellurous acid \n''H6TeO6 telluric(vI) acid \n''K2TeO3 potassium tellurite \n''K2TeCl6 potassium hexachlorotellurate \n''N4O12Te tellurium tetranitrate \n''O4PbTe lead tellurate \n''C3H5O2Te [methyltelluro]acetate \n''C14H14Br2Te dibromodi-p-tolyltellurane \n''C14H14F2Te bis(p-tolyl)difluorotellurium \n''C14H18Cl2Ti bis(ethylcyclopentadienyl)titanium(IV)dichloride \n''C18H18O4Te 1,3-dioxolane, 2,2'-(tellurodi-2,1-phenylene)bis \n''C28H24O10Te di(p-anisyl)tellurium diresorcylate \n''K2TeO4·xH2O potassium tellurate hydrate \n''Na2TeO3 sodium tellurite \n''Na2TeO4·2H2O sodium tellurate dihydrate \n''H8N2O4Te ammonium tellurate \n''(NH4)2TeBr6 ammonium hexabromotellurate(IV) \n''(NH4)2TeCl6 ammonium hexachlorotellurate(IV) \n''C14H14Cl2O2Te dichloro(3,4-dimethoxyphenyl)phenyltellurium \n''C14H14I2O2Te bis(p-methoxyphenyl)diiodotellurium \n''C15H17Br2NTe tellurium, dibromo(p-(dimethylamino)phenyl)-p-tolyl \n''C15H17Cl2NTe tellurium, dichloro(p-(dimethylamino)phenyl)-m-tolyl \n''C15H17Cl2NTe tellurium, dichloro(p-(dimethylamino)phenyl)(p-tolyl) \n''C18H18Cl2O4Te bis(o-(1,3-dioxolan-2-yl)phenyl)dichlorotellurium \n''C20H40N4S8Te ethyl tellurac \n''K2TeO4·3H2O potassium tellurate(VI) trihydrate \n''C5H6F5NOTe pyridinium teflate \n''C14H14Cl2N2O2Te dichloro(p-(dimethylamino)phenyl)(m-nitrophenyl)tellurium \n''C14H14FNOTe 4-((4-fluorophenyl)tellurinyl)-N,N-dimethylbenzamine \n'""", '52', '127.60')
        self.colorTe=colorTe="SkyBlue2"
        self.Te = tk.Button(self, text=Te[0], width=5, height=2, bg=colorTe, font=10, borderwidth=3,
                           command=lambda text=Te: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Te()])
        self.Te.grid(row=7, column=17)

        Po = ('Po', 'Polonium', """'Po polonium\n''Cl4Po polonium(IV) chloride\n''PoO2 polonium(IV) oxide\n'""", '84', '209.00')
        self.colorPo=colorPo="SkyBlue3"
        self.Po = tk.Button(self, text=Po[0], width=5, height=2, bg=colorPo, font=10, borderwidth=3,
                           command=lambda text=Po: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPo, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Po()])
        self.Po.grid(row=8, column=17)

        Lv = ('Lv', 'Livermorium', """'Lv livermorium livermorium metal\n'""", '116', '293.00')
        self.colorLv=colorLv="SkyBlue4"
        self.Lv = tk.Button(self, text=Lv[0], width=5, height=2, bg=colorLv, font=10, borderwidth=3,
                           command=lambda text=Lv: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorLv, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Lv()])
        self.Lv.grid(row=9, column=17)

        F = ('F', 'Fluorine', """ """, '9', '18.99')
        self.colorF=colorF="light steel blue"
        self.F = tk.Button(self, text=F[0], width=5, height=2, bg=colorF, font=10, borderwidth=3,
                           command=lambda text=F: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorF, text[0], text[3], text[4]), self.voice(text[1]), self.compound_F()])
        self.F.grid(row=4, column=18)

        Cl = ('Cl', 'Chlorine', """'AgCl silver chloride \n''AlCl3 aluminum chloride \n''AlCl3 polyaluminum chloride \n''AmCl3 americium(III) chloride \n''AsCl3 arsenic trichloride \n''AuCl gold(I)chloride \n''AuCl3 gold(III)chloride \n''BCl3 boron trichloride \n''B2Cl4 tetrachloradiborane \n''BaCl2 barium chloride \n''BeCl2 beryllium chloride \n''BiCl3 bismuth chloride \n''BrCl bromine chloride \n''CCl2 dichlorocarbene \n''CCl4 carbon tetrachloride \n''13CCl4 carbon-13C tetrachloride \n''C2Cl2 dichloroacetylene \n''CCl2=CCl2 tetrachloroethylene \n''Cl3CCCl3 hexachloroethane \n''C3Cl4 tetrachlorocyclopropene \n''CCl3CCl=CCl2 hexachloropropene \n''CCl2=CClCCl=CCl2 hexachlorobutadiene \n''C5Cl6 hexachlorocyclopentadiene \n''C6Cl6 hexachlorobenzene \n''C10Cl10 pentac \n''C10Cl12 mirex \n''CaCl2 calcium chloride \n''CdCl2 cadmium chloride \n''CdCl2 cadmium chloride monohydrate \n''CeCl3 cerous chloride \n''CsCl cesium chloride \n''CuCl cuprous chloride \n''ClF3 chlorine trifluoride \n''ClF5 chlorine pentafluoride \n''DCl deuterium chloride \n''HCl hydrogen chloride \n''ICl iodine monochloride \n''InCl indium(I)chloride \n''KCl potassium chloride \n''LiCl lithium chloride \n''ClN3 chlorine azide \n''NaCl sodium chloride \n''Na35Cl sodium chloride-35 \n''ClO2 chlorine dioxide \n''RbCl rubidium chloride \n''TlCl thallium chloride \n''CoCl2 cobalt dichloride \n''CrCl2 chromous chloride \n''CuCl2 copper(II)chloride \n''Cl2Eu europium(II)chloride \n''FeCl2 iron(II)chloride \n''Cl2Ge germanium(II) chloride \n''HgCl2 mercuric chloride \n''Hg2Cl2 mercury(I) chloride \n''MgCl2 magnesium chloride \n''MnCl2 manganese(II)chloride \n''Cl2Mo molybdenum(II) chloride \n''NiCl2 nickel(II) chloride \n''Cl2O chlorine monoxide \n''Cl2O3 dichlorine trioxide \n''Cl2O4 chlorine perchlorate \n''Cl2O6 dichlorine hexoxide \n''Cl2O7 dichlorine heptoxide \n''PbCl2 lead(II) chloride \n''Cl2Pd palladium(II)chloride \n''PtCl2 platinum(II)chloride \n''SCl2 sulfur dichloride \n''S2Cl2 sulfur monochloride \n''Se2Cl2 diselenium dichloride \n''Cl2SiH2 dichlorosilane \n''SnCl2 stannous chloride \n''SrCl2 strontium chloride \n''TiCl2 titanium(II)chloride \n''Cl2Tm thulium(II) chloride \n''VCl2 vanadium(II) chloride \n''ZnCl2 zinc chloride \n''CrCl3 chromic chloride \n''DyCl3 dysprosium(III) chloride \n''ErCl3 erbium chloride \n''Cl3Eu europium(III) chloride \n''FeCl3 iron(III)chloride \n''GaCl3 gallium trichloride \n''GdCl3 gadolinium(III) chloride \n''HoCl3 holmium chloride \n''ICl3 iodine trichloride \n''InCl2 indium(II)chloride \n''InCl3 indium trichloride \n''IrCl3 iridium(III) chloride \n''LaCl3 lanthanum(III)chloride \n''LuCl3 lutetium chloride \n''MoCl3 molybdenum(III) chloride \n''Cl3N nitrogen trichloride \n''Cl3Nb niobium(III) chloride \n''NdCl3 neodymium chloride \n''OsCl3 osmium(III) chloride \n''PCl3 phosphorus trichloride \n''PrCl3 praseodymium(III) chloride \n''ReCl3 rhenium(III) chloride \n''RhCl3 rhodium(III) chloride \n''RuCl3 ruthenium(III) chloride \n''SbCl3 antimony(III) chloride \n''ScCl3 scandium chloride \n''SiHCl3 trichlorosilane \n''SmCl3 samarium(III)chloride \n''Cl3Ta tantalum(III) chloride \n''TbCl3 terbium(III)chloride \n''TiCl3 titanium trichloride \n''Cl3Tl thallium(III) chloride \n''TmCl3 thulium chloride \n''Cl3U uranium(III) chloride \n''VCl3 vanadium trichloride \n''YCl3 yttrium chloride \n''YbCl3 ytterbium(III) chloride \n''Cl4Cr chromium(IV) chloride \n''Ga2Cl4 gallium(II)chloride \n''GeCl4 germanium(IV)chloride \n''HfCl4 hafnium tetrachloride \n''Cl4Ir iridium(IV) chloride \n''Cl4Mo molybdenum(IV) chloride \n''Cl4Nb niobium(IV) chloride \n''Cl4Os osmium(IV) chloride \n''Cl4P2 diphosphorus tetrachloride \n''Cl4Pb lead tetrachloride \n''Cl4Po polonium(IV) chloride \n''PtCl4 platinum(IV) chloride \n''Cl4Re rhenium(IV) chloride \n''SeCl4 selenium tetrachloride \n''SiCl4 silicon tetrachloride \n''SnCl4 stannic chloride \n''Cl4Ta tantalum(IV) chloride \n''TeCl4 tellurium tetrachloride \n''Cl4Th thorium(IV)chloride \n''TiCl4 titanium tetrachloride \n''Cl4U uranium(IV) chloride \n''VCl4 vanadium tetrachloride \n''WCl4 tungsten(IV)chloride \n''ZrCl4 zirconium tetrachloride \n''MoCl5 molybdenum pentachloride \n''NbCl5 niobium(V) chloride \n''PCl5 phosphorus pentachloride \n''ReCl5 rhenium(V)chloride \n''SbCl5 antimony pentachloride \n''TaCl5 tantalum(V) chloride \n''Cl5W tungsten(V) chloride \n''(SiCl3)2 hexachlorodisilane \n''WCl6 tungsten hexachloride \n''Cl8Si3 octachlorotrisilane \n''DyCl2 dysprosium(II) chloride \n''HCl hydrochloric acid \n''HfCl2 hafnium(II) chloride \n''HfCl3 hafnium(III) chloride \n''NdCl2 neodymium(II) chloride \n''OsCl2 osmium(II) chloride \n''PaCl5 protactinium(V) chloride \n''PmCl3 promethium(III) chloride \n''PtCl3 platinum(III) chloride \n''PuCl3 plutonium(III) chloride \n''ReCl6 rhenium(VI) chloride \n''SmCl2 samarium(II) chloride \n''TeCl2 tellurium dichloride \n''UCl5 uranium(V) chloride \n''UCl6 uranium(VI) chloride \n''WCl2 tungsten(II) chloride \n''WCl3 tungsten(III) chloride \n''YbCl2 ytterbium(II) chloride \n''ZrCl2 zirconium(II) chloride \n''ZrCl3 zirconium(III) chloride \n''AgClO2 silver(I) chlorite \n''AgClO3 silver chlorate \n''AgClO4 silver perchlorate \n''AlCl3O9 aluminum chlorate nonahydrate \n''AlCl3O12 aluminum perchlorate \n''KAlCl4 potassium tetrachloroaluminate \n''AlCl4Li lithium tetrachloroaluminate \n''NaAlCl4 sodium tetrachloroaluminate \n''(TiCl3)3·AlCl3 titanium(III)chloride-aluminum chloride \n''HAuCl4·xH2O gold(III) chloride hydrate \n''HAuCl4·3H2O gold(III) chloride trihydrate \n''AuCl4Li lithium tetrachloroaurate(III) \n''AuCl4Na sodium gold chloride \n''BaClF barium chloride fluoride \n''BaCl2O6 barium chlorate \n''Ba(ClO4)2 barium perchlorate \n''BrCl3Si bromotrichlorosilane \n''Br2ClRb rubidium chlorobromo bromide \n''Br2Cl2Si dibromodichlorosilane \n''CBr3Cl tribromochloromethane \n''Br3ClSi tribromochlorosilane \n''BrCCl3 bromotrichloromethane \n''CBr2Cl2 dibromodichloromethane \n''Cl2C=13CCl2 tetrachloroethylene-13 C1 \n''CClF3 chlorotrifluoromethane \n''CClN cyanogen chloride \n''CCl2F2 dichlorodifluoromethane \n''COCl2 phosgene \n''CSCl2 thiophosgene \n''Cl3CF trichlorofluoromethane \n''13C3N3Cl3 cyanuric chloride-13 C3 \n''CCl3SCl perchloromethyl mercaptan \n''Cl3CSiCl3 trichloro(trichloromethyl)silane \n''CDCl3 trichloromethane-d \n''CD2Cl2 deuterated dichloromethane (D2) \n''CD3Cl chloromethane-d 399.5 atom%D \n''CHCl3 chloroform \n''13CHCl3 chloroform-13 C \n''CH2Cl2 methylene chloride \n''13CH2Cl2 dichloromethane-13 C \n''CH3Cl methyl chloride \n''13CH3Cl chloromethane-13 C \n''13C6H5Cl chlorobenzene-13 C6 \n''BrCCl2CCl2Br 1,2-dibromotetrachloroethane \n''ClCF=CF2 chlorotrifluoroethylene \n''[CF2CF(Cl)]n ethene, chlorotrifluoro-, homopolymer \n''C2ClF5 chloropentafluoroethane \n''C2Cl2F2 1,2-dichloro-1,2-difluoroethylene \n''C2Cl2F4 1,1-dichloro-1,2,2,2-tetrafluoroethane \n''ClCF2CF2Cl 1,2-dichlorotetrafluoroethane \n''C2Cl2F4 tetrafluorodichloroethane \n''ClCOCOCl oxalyl chloride \n''C2Cl3F trichlorofluoroethene \n''Cl3CCF3 1,1,1-trichloro-2,2,2-trifluoroethane \n''ClCF2CCl2F 1,1,2-trichlorotrifluoroethane \n''CFC-113 Freon 113 \n''Cl3CCN trichloroacetonitrile \n''C2Cl4F2 1,1,1,2-tetrachloro-2,2-difluoroethane \n''C2Cl4F2 1,1,2,2-tetrachloro-1,2-difluoroethane \n''Cl3CCOCl trichloroacetyl chloride \n''C2Cl4O2 trichloromethyl chloroformate \n''C2Cl6Hg bis(trichloromethyl)mercury \n''C2Cl8Si dichlorobis(trichloromethyl)silane \n''Cl2CDCDCl2 1,1,2,2-tetrachloroethane-D2 \n''D2C=CDCl vinyl chloride-d 3 \n''ClCD2CD2Cl 1,2-dichloroethane-d 4 \n''ClCH=CCl2 trichloroethylene \n''CCl3CHCl2 pentachloroethane \n''C2H2Cl2 1,1-dce \n''CH2=CCl2 1,1-dichloroethylene \n''ClCH=CHCl 1,2-dichloroethylene \n''ClCH=CHCl cis-1,2-dichloroethylene \n''ClCH=CHCl trans-1,2-dichloroethylene \n''ClCH2CCl3 1,1,1,2-tetrachloroethane \n''CHCl2CHCl2 sym-tetrachloroethane \n''(CH2CHCl)n poly(vinyl chloride) \n''(C3H4O2·C2H3Cl)x poly(vinyl chloride)carboxylated \n''H2C=CHCl vinyl chloride \n''Cl3CCH3 1,1,1-trichloroethane \n''ClCH2CHCl2 1,1,2-trichloroethane \n''CH3CHCl2 1,1-dichloroethane \n''ClCH2CH2Cl ethylene dichloride \n''C2H5Cl chloroethane \n''NCCCl2CN dichloromalononitrile \n''C3Cl3F3 1,1,2-trichloro-3,3,3-trifluoro-1-propene \n''C3Cl3N3 cyanuric chloride \n''C3Cl4O3 1,3-dioxolan-2-one, 4,4,5,5-tetrachloro- \n''CCl3COCCl3 hexachloroacetone \n''Cl3COCOOCCl3 bis(trichloromethyl)carbonate \n''(CD3)2CDCl 2-chloropropane-d 7 \n''C3HCl5 pentachlorocyclopropane \n''C2Cl5CHCl2 1,1,1,2,2,3,3-heptachloropropane \n''HC≡CCH2Cl propargyl chloride \n''C3H3Cl3 1,2,3-trichloro-1-propene \n''C3H4Cl2 1,1-dichloropropene \n''C3H4Cl2 1,2-dichloropropene \n''ClCH2CH=CHCl 1,3-dichloro-1-propene \n''ClCH2CCl=CH2 2,3-dichloro-1-propene \n''C3H4Cl2 3,3-dichloro-1-propene \n''C3H4Cl2 cis-1,2-dichloropropene \n''ClCH2CH=CHCl cis-1,3-dichloropropylene \n''C3H4Cl2 (E)- 1,2-dichloro-1-propene \n''C3H4Cl2 trans-1,3-dichloropropene \n''C3H4Cl4 1,1,1,3-tetrachloropropane \n''C3H5Cl 1-chloro-1-propene \n''CH3CCl=CH2 2-chloro-1-propene \n''CH2=CHCH2Cl 3-chloro-1-propene \n''CH2ClCHClCH2Cl 1,2,3-trichloropropane \n''C2H5CHCl2 1,1-dichloropropane \n''CH3CHClCH2Cl 1,2-dichloropropane \n''Cl(CH2)3Cl 1,3-dichloropropane \n''CH3CCl2CH3 2,2-dichloropropane \n''CH3CH2CH2Cl 1-chloropropane \n''(CH3)2CHCl isopropyl chloride \n''CF3C(Cl)=C(Cl)CF3 2,3-dichloro-1,1,1,4,4,4-hexafluoro-2-butene \n''C4Cl2O3 2,3-dichloromaleic anhydride \n''C4Cl4N2 2,4,5,6-tetrachloropyrimidine \n''C4Cl4S tetrachlorothiophene \n''(Cl3CCO)2O trichloroacetic anhydride \n''ClCD2(CD2)2CD2Cl 1,4-dichlorobutane-d 8 \n''(CD3)3CCl 2-chloro-2-methylpropane-d 9 \n''C4H2Cl4 1,1,2,3-tetrachloro-1,3-butadiene \n''ClCH2C≡CCH2Cl 1,4-dichloro-2-butyne \n''C4H5Cl chloroprene \n''C4H5Cl3 2,3,4-trichlorobut-1-ene \n''(CH2CCl2)x(CH2CHCl)y poly(vinylidene chloride-co-vinyl chloride) \n''C4H5Cl3 trichlorobutene \n''Lu(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]lutetium(III) \n''C4H6Cl2 1,2-dichloro-2-butene \n''C4H6Cl2 1,3-dichloro-2-butene \n'""", '17', '35.45')
        self.colorCl=colorCl="light blue"
        self.Cl = tk.Button(self, text=Cl[0], width=5, height=2, bg=colorCl, font=10, borderwidth=3,
                           command=lambda text=Cl: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCl, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cl()])
        self.Cl.grid(row=5, column=18)

        Br = ('Br', 'Bromine', """'Br2 bromine \n''AgBr silver bromide \n''AlBr3 aluminum tribromide \n''AmBr3 americium(III) bromide \n''AsBr3 arsenic tribromide \n''AuBr3·xH2O gold(III) bromide \n''BBr3 boron tribromide \n''B2Br4 tetrabromodiborane \n''BaBr2 barium bromide \n''BeBr2 beryllium bromide \n''BiBr3 bismuth bromide \n''BrCl bromine chloride \n''CsBr cesium bromide \n''CuBr copper(I) bromide \n''DBr·D2O deuterium bromide \n''BrF3 bromine trifluoride \n''BrF5 bromine pentafluoride \n''HBr hydrogen bromide \n''IBr iodine bromide \n''KBr potassium bromide \n''LiBr lithium bromide \n''BrN3 bromine azide \n''NaBr sodium bromide \n''BrO2 bromine dioxide \n''RbBr rubidium bromide \n''TlBr thallium(I) bromide \n''CaBr2 calcium bromide \n''CdBr2 cadmium bromide \n''CoBr2 cobalt dibromide \n''CuBr2 cupric bromide \n''Br2Eu europium(II)bromide \n''FeBr2 iron(II)bromide \n''GeBr2 germanium(II)bromide \n''HgBr2 mercuric bromide \n''Hg2Br2 mercury(I) bromide \n''MgBr2 magnesium bromide \n''MnBr2 manganese(II) bromide \n''NiBr2 nickel bromide \n''NiBr2·xH2O nickel(II)bromide hydrate \n''Br2O3 dibromine trioxide \n''Br2O5 dibromine pentoxide \n''PbBr2 lead(II) bromide \n''PdBr2 palladium(II)bromide \n''PtBr2 platinum(II) bromide \n''Br2S2 sulfur bromide (SSBr2) \n''Br2Se2 selenium bromide \n''SnBr2 tin(II)bromide \n''SrBr2 strontium bromide \n''TeBr2 tellurium dibromide \n''Br2Yb ytterbium(II) bromide \n''ZnBr2 zinc bromide \n''CeBr3 cerium(III) bromide \n''Br3Cr chromium tribromide \n''CsBr3 cesium tribromide \n''DyBr3 dysprosium(III)bromide \n''ErBr3 erbium(III)bromide \n''Br3Eu europium(III) bromide \n''FeBr3 iron(III) bromide \n''GaBr3 gallium(III) bromide \n''GdBr3 gadolinium(III)bromide \n''HoBr3 holmium(III)bromide \n''InBr indium(I)bromide \n''InBr3 indium(III) bromide \n''Br3Ir iridium(III) bromide \n''Br3La lanthanum bromide \n''LuBr3 lutetium(III)bromide \n''MoBr3 molybdenum bromide \n''Br3N nitrogen tribromide \n''NdBr3 neodymium bromide \n''PBr3 phosphorus tribromide \n''PrBr3 praseodymium(III)bromide \n''Br3Re rhenium(III) bromide \n''SbBr3 antimony tribromide \n''SmBr3 samarium(III)bromide \n''TbBr3 terbium(III)bromide \n''TmBr3 thulium(III)bromide \n''Br3U uranium tribromide \n''VBr3 vanadium tribromide \n''YBr3 yttrium(III)bromide \n''YbBr3 ytterbium(III)bromide \n''GeBr4 germanium tetrabromide \n''HfBr4 hafnium(IV)bromide \n''Br4Pb lead(IV) bromide \n''SeBr4 selenium tetrabromide \n''SiBr4 silicon tetrabromide \n''SnBr4 tin(IV) bromide \n''TeBr4 tellurium tetrabromide \n''Br4Th thorium(IV) bromide \n''TiBr4 titanium(IV) bromide \n''Br4U uranium tetrabromide \n''Br4W tungsten(IV) bromide \n''ZrBr4 zirconium tetrabromide \n''NbBr5 niobium(V) bromide \n''PBr5 phosphorus pentabromide \n''TaBr5 tantalum(V)bromide \n''Br5U uranium pentabromide \n''WBr5 tungsten(V)bromide \n''13CBr4 carbon-13C tetrabromide \n''CBr4 carbon tetrabromide \n''C2Br2 dibromoacetylene \n''C6Br6 hexabromobenzene \n''CrBr2 chromium(II) bromide \n''DyBr2 dysprosium(II) bromide \n''HBr hydrobromic acid \n''HfBr2 hafnium(II) bromide \n''HfBr3 hafnium(III) bromide \n''MoBr2 molybdenum(II) bromide \n''MoBr4 molybdenum(IV) bromide \n''NbBr3 niobium(III) bromide \n''NbBr4 niobium(IV) bromide \n''OsBr3 osmium(III) bromide \n''PmBr3 promethium(III) bromide \n''PtBr3 platinum(III) bromide \n''PtBr4 platinum(IV) bromide \n''PuBr3 plutonium(III) bromide \n''ReBr5 rhenium(V) bromide \n''RhBr3 rhodium(III) bromide \n''Si2Br6 hexabromosilane \n''Si3Br8 octabromotrisilane \n''SmBr2 samarium(II) bromide \n''TaBr3 tantalum(III) bromide \n''TaBr4 tantalum(IV) bromide \n''TiBr2 titanium(II) bromide \n''TiBr3 titanium(III) bromide \n''TmBr2 thulium(II) bromide \n''VBr2 vanadium(II) bromide \n''VBr4 vanadium(IV) bromide \n''WBr2 tungsten(II) bromide \n''WBr3 tungsten(III) bromide \n''WBr6 tungsten(VI) bromide \n''ZrBr2 zirconium(II) bromide \n''ZrBr3 zirconium(III) bromide \n''AuBr4H gold tetrabromide, acid \n''KAuBr4 potassium tetrabromoaurate(III) \n''BiOBr bismuth oxybromide \n''BrCl3Si bromotrichlorosilane \n''ND4Br ammonium-d 4bromide \n''BrF2P phosphorus(III) bromide difluoride \n''BrGeH3 bromogermane \n''HOBr hypobromous acid \n''BrHO3 bromic acid \n''15NH4Br ammonium-15 nbromide \n''NH4Br ammonium bromide \n''H2NNH2·HBr hydrazine monohydrobromide \n''KBrO3 potassium bromate \n''BrNO nitrosyl bromide \n''NaBrO3 sodium bromate \n''BrOF3 bromasyl trifluoride \n''BrO2F bromyl fluoride \n''BrO3F perbromyl fluoride \n''TlBrO3 thallium bromate \n''Br2CaO6 calcium bromate \n''Br2ClRb rubidium chlorobromo bromide \n''Br2Cl2Si dibromodichlorosilane \n''Br2CsI cesium dibromoiodate \n''Br2GeH2 dibromogermane \n''Br2H2Si dibromosilane \n''Br2H6N2 hydrazine dihydrobromide dihydrate \n''SOBr2 thionyl bromide \n''Br2OSe selenium oxybromide \n''Br2O6Zn zinc bromate \n''CBr3Cl tribromochloromethane \n''Br3ClSi tribromochlorosilane \n''POBr3 phosphorus oxybromide \n''Br3O9Pr praseodymium(III) bromate \n''Br3PS phosphorothioc tribromide \n''Li2CuBr4 dilithium tetrabromocuprate(II) \n''K2PdBr4 potassium tetrabromopalladate(II) \n''K2PtBr4 potassium tetrabromoplatinate(II) \n''Li2NiBr4 dilithium tetrabromonickelate(II) \n''Na2PdBr4 sodium tetrabromopalladate(II) \n''H2PtBr6·xH2O hydrogen hexabromoplatinate(IV)hydrate \n''K2PtBr6 potassium hexabromoplatinate(IV) \n''K2ReBr6 potassium hexabromorhenate(IV) \n''K2TeBr6 potassium hexabromotellurate(IV) \n''BrCCl3 bromotrichloromethane \n''CBrF3 bromotrifluoromethane \n''BrCN cyanogen bromide \n''CBr2Cl2 dibromodichloromethane \n''CBr2F2 dibromodifluoromethane \n''CFBr3 tribromofluoromethane \n''CDBr3 bromoform-d \n''CD2Br2 dibromomethane-d 2 \n''CD3Br bromomethane-d 3 \n''CHBr3 bromoform \n''13CHBr3 bromoform-13 C \n''CH2Br2 methylene bromide \n''CH3Br methyl bromide \n''13CH3Br bromomethane-13 C \n''Br13CH213CH2Br 1,2-dibromoethane-13 C2 \n''13C6H5Br bromobenzene-13 C6 \n''13CH313CH2Br bromoethane-13 C2 \n''COBr2 carbonyl bromide \n''C2BrF3 bromotrifluoroethylene \n''BrCCl2CCl2Br 1,2-dibromotetrachloroethane \n''C2Br2F4 1,2-dibromotetrafluoroethane \n''BrCOCOBr oxalyl bromide \n''D2C=CDBr vinyl-d 3bromide \n''BrCD2CD2Br 1,2-dibromoethane-d 4 \n''CD3CD2Br bromoethane-[-{2}-h5] \n''BrCH=CHBr 1,2-dibromoethylene \n''Br2CHCHBr2 1,1,2,2-tetrabromoethane acetylene tetrabromide \n''CH2=CHBr vinyl bromide \n''BrCH2CHBr2 1,1,2-tribromoethane \n''C2H4Br2 1,1-dibromoethane \n''BrCH2CH2Br ethylene dibromide \n''CH3CH2Br bromoethane \n''(CD3)2CDBr 2-bromopropane-d 7 \n''HC≡CCH2Br 3-bromo-1-propyne  \n''C3H4Br2 1,1-dibromo-1-propene \n''BrCH2CH=CHBr 1,3-dibromo-1-propene,mixture of cis and trans 98% \n''CH2BrCBr=CH2 2,3-dibromo-1-propene \n''CH3CH=CHBr 1-bromopropene \n''CH3C(Br)=CH2 2-bromopropene \n''CH2=CHCH2Br allyl bromide \n''C3H5Br bromocyclopropane \n''CH3CH=CHBr cis-1-bromo-1-propene \n''CH3CH=CHBr trans-1-bromo-1-propene \n''BrCH2CH(Br)CH2Br 1,2,3-tribromopropane \n''CH3CHBrCH2Br 1,2-dibromopropane \n''C3H6Br2 1,3-dibromopropane \n''CH3CBr2CH3 2,2-dibromopropane \n''CH3CH2CH2Br 1-bromopropane \n''(CH3)2CHBr 2-bromopropane \n''C4Br4S tetrabromothiophene \n''BrCD2(CD2)2CD2Br 1,4-dibromobutane-d 8 \n''CH3C≡CCH2Br 1-bromo-2-butyne \n''BrCH2CH=CHCH2Br trans-1,4-dibromo-2-butene \n''(CH3)2C=CHBr 1-bromo-2-methyl-1-propene \n''C4H7Br 2-bromo-1-butene \n''CH3CH=C(Br)CH3 2-bromo-2-butene \n''H2C=C(CH3)CH2Br 3-bromo-2-methylpropene \n''BrCH2CH2CH=CH2 4-bromo-1-butene \n''C4H7Br bromocyclobutane \n''C3H5CH2Br bromomethylcyclopropane \n''CH3CH=CHCH2Br 2-butene, 1-bromo-, (2E)- \n''CH3CH=C(Br)CH3 (E)-2-bromo-2-butene \n''CH3CH=C(Br)CH3 (Z)-2-bromo-2-butene \n''(CH3)2C(Br)CH2Br 1,2-dibromo-2-methylpropane \n''C2H5CH(Br)CH2Br 1,2-dibromobutane \n''CH3CHBrCH2CH2Br 1,3-dibromobutane \n''Br(CH2)4Br 1,4-dibromobutane \n''CH3CH(Br)CH(Br)CH3 2,3-dibromobutane \n''CH3CH(Br)CH(Br)CH3 meso-2,3-dibromobutane \n''CH3CH(Br)CH(Br)CH3 (±)-2,3-dibromobutane \n''(CH3)2CHCH2Br isobutyl bromide \n''(CH3)3CBr 2-bromo-2-methylpropane \n''CH3CH2CHBrCH3 2-bromobutane \n''C4H9Br butyl bromide \n''C5D9Br bromocyclopentane-d 9 \n''C5H6Br2 1,2-dibromocyclopentene \n''C2H5C≡CCH2Br 1-bromo-2-pentyne \n''C5H8Br2 trans-1,2-dibromocyclopentane \n''C(CH2Br)4 1,3-dibromo-2,2-bis(bromomethyl)propane \n''C2H5CH=CHCH2Br 1-bromo-2-pentene,predominantly trans 95% \n''(CH3)2C=C(Br)CH3 2-bromo-3-methyl-2-butene \n''(CH3)2C=CHCH2Br 1-bromo-3-methyl-2-butene \n''Br(CH2)3CH=CH2 5-bromo-1-pentene \n''C5H9Br bromocyclopentane \n''C4H7CH2Br bromomethylcyclobutane \n''Br(CH2)3CHBrCH3 1,4-dibromopentane \n''Br(CH2)5Br 1,5-dibromopentane \n''C2H5CH(Br)CH(Br)CH3 2,3-dibromopentane,mixture of diastereomers \n''(CH3)3CCH2Br neopentyl bromide \n''(CH3)2CHCH2CH2Br 1-bromo-3-methylbutane \n''CH3(CH2)4Br amyl bromide \n''CH3CH2CBr(CH3)2 2-bromo-2-methylbutane \n''CH3CH2CH2CHBrCH3 2-bromopentane \n''(C2H5)2CHBr 3-bromopentane \n''C2H5CH(CH3)CH2Br D-amyl bromide \n''BrC6F5 bromopentafluorobenzene \n''CF3(CF2)5Br perfluorohexyl bromide \n''Br2C6F4 1,2-dibromotetrafluorobenzene \n''Br2C6F4 1,3-dibromotetrafluorobenzene \n''Br2C6F4 1,4-dibromotetrafluorobenzene \n''C6Br4N3 tetrabromo-2-benzotriazole \n''C6Br4(=O)2 tetrabromo-o-benzoquinone \n''C6Br4(=O)2 tetrabromo-1,4-benzoquinone \n''C6D4Br2 1,4-dibromobenzene-d 4 \n''C6D5Br bromo(-{2}-h5)benzene \n''C6D11Br bromocyclohexane-d 11 \n''CD3C(CD2)4CD2Br 1-bromohexane-d 13 \n''C6H2Br4 1,2,4,5-tetrabromobenzene \n''C6H3Br3 1,2,4-tribromobenzene \n''C6H3Br3 1,3,5-tribromobenzene \n''C6H4Br2 1,2-dibromobenzene \n''C6H4Br2 1,3-dibromobenzene \n''C6H4Br2 1,4-dibromobenzene \n''C6H4Br2 dibromobenzene \n''C6H5Br bromobenzene \n''C6H9Br 3-bromocyclohexene \n''C6H10Br2 trans-1,2-dibromocyclohexane \n''BrCH2CH2CH=C(CH3)2 5-Bromo-2-methyl-2-pentene \n''Br(CH2)4CH=CH2 6-bromo-1-hexene \n''C6H11Br bromocyclohexane \n''(CH3)3CCH(Br)CH2Br 1,2-dibromo-3,3-dimethylbutane \n''CH3(CH2)3CH(Br)CH2Br 1,2-dibromohexane \n''Br(CH2)6Br 1,6-dibromohexane \n''CH3CH2CH2CH(Br)CH(Br)CH3 2,3-dibromohexane,mixture of diastereomers \n''C2H5CH(Br)CH(Br)C2H5 3,4-dibromohexane \n''(C2H5)2CHCH2Br 3-(bromomethyl)pentane \n''(CH3)2CH(CH2)3Br 1-bromo-4-methylpentane \n''CH3(CH2)5Br 1-bromohexane \n''C6H13Br 2-bromohexane \n''C6H13Br 3-bromohexane \n''BrC6F4CF3 1-bromo-2,3,5,6-tetrafluoro-4-(trifluoromethyl)benzene \n''CF3(CF2)6Br perfluoroheptyl bromide \n''C6D5CD2Br benzyl bromide-d 7 \n''C6Br5CH3 pentabromotoluene \n''Br3C6H2CH3 2,4,6-tribromotoluene \n''C7H5Br3 3,5-dibromobenzyl bromide \n''CH3C6H3Br2 2,5-dibromotoluene \n'""", '35', '79.90')
        self.colorBr=colorBr="powder blue"
        self.Br = tk.Button(self, text=Br[0], width=5, height=2, bg=colorBr, font=10, borderwidth=3,
                           command=lambda text=Br: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorBr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Br()])
        self.Br.grid(row=6, column=18)

        I = ('I', 'Iodine', """'I2 iodine  \n''AgI silver(I) iodide  \n''AlI3 aluminum iodide  \n''AmI3 americium(III) iodide  \n''AsI3 arsenic iodide  \n''As2I4 arsenic diiodide  \n''AuI gold(I) iodide  \n''AuI3 gold(III)iodide  \n''BI3 boron triiodide  \n''BaI2 barium iodide  \n''BeI2 beryllium iodide  \n''BiI3 bismuth(III) iodide  \n''BiI3 bismuth iodide  \n''IBr iodine bromide  \n''CI4 carbon tetraiodide  \n''C2I2 diiodoacetylene  \n''I2C=CI2 tetraiodoethylene  \n''CaI2 calcium iodide  \n''CdI2 cadmium iodide  \n''CeI3 cerium(III) iodide  \n''ICl iodine monochloride  \n''ICl3 iodine trichloride  \n''CoI2 cobalt(II)iodide  \n''CrI3 chromium(III) iodide  \n''CsI cesium iodide  \n''CsI3 cesium triiodide  \n''CuI cuprous iodide  \n''DyI2 dysprosium(II)iodide  \n''DyI3 dysprosium(III)iodide  \n''ErI3 erbium iodide  \n''EuI2 europium(II)iodide  \n''FI iodine fluoride  \n''F5I iodine pentafluoride  \n''F7I iodine heptafluoride  \n''FeI2 ferrous iodide  \n''GaI3 gallium(III) iodide  \n''GdI2 gadolinium(II) iodide  \n''GdI3 gadolinium(III)iodide  \n''GeI2 germanium(II)iodide  \n''GeI4 germanium(IV) iodide  \n''DI deuterium iodide  \n''HI hydrogen iodide  \n''HI hydroiodic acid  \n''HfI3 hafnium(III) iodide  \n''HfI4 hafnium iodide  \n''Hg(IO3)2 mercury(II)iodate  \n''HgI2 mercury(II) iodide  \n''HgI2 mercuric iodide  \n''Hg2I2 mercury(I) iodide  \n''HoI3 holmium(III)iodide  \n''IF3 iodine trifluoride  \n''InI indium monoiodide  \n''KI potassium iodide  \n''LiI lithium iodide  \n''IN3 iodine azide  \n''NaI sodium iodide  \n''RbI rubidium iodide  \n''TlI thallium(I)iodide  \n''MgI2 magnesium iodide  \n''MnI2 manganese(II) iodide  \n''NiI2 nickel iodide  \n''I2O4 iodine tetroxide  \n''I2O5 iodopentoxide  \n''I2O6 iodine hexoxide  \n''PbI2 lead iodide  \n''I2Pd palladium(II) iodide  \n''PtI2 platinum(II) iodide  \n''SiH2I2 diiodosilane  \n''SmI2 samarium(II)iodide  \n''SnI2 tin(II)iodide  \n''SrI2 strontium iodide  \n''TmI2 thulium(II)iodide  \n''VI2 vanadium(II) iodide  \n''YbI2 ytterbium(II)iodide  \n''ZnI2 zinc iodide  \n''InI3 indium(III) iodide  \n''I3La lanthanum iodide  \n''I3Lu lutetium(III)iodide  \n''I3N nitrogen triiodide  \n''I3Nd neodymium iodide  \n''PI3 phosphorus(III) iodide  \n''PrI3 praseodymium(III)iodide  \n''ReI3 rhenium(III)iodide  \n''I3Rh rhodium(III) iodide  \n''RuI3 ruthenium(III) iodide  \n''SbI3 antimony(III) iodide  \n''ScI3 scandium(III)iodide  \n''SmI3 samarium(III)iodide  \n''TbI3 terbium(III)iodide  \n''TmI3 thulium(III)iodide  \n''I3U uranium(III) iodide  \n''VI3 vanadium(III) iodide  \n''YI3 yttrium(III)iodide  \n''I4O9 iodine nonaoxide  \n''P2I4 diphosphorous tetraiodide  \n''I4Pt platinum(IV) iodide  \n''SiI4 silicon tetraiodide  \n''SnI4 tin(IV)iodide  \n''TeI4 tellurium tetraiodide  \n''I4Th thorium(IV) iodide  \n''TiI4 titanium(IV) iodide  \n''I4U uranium(IV) iodide  \n''ZrI4 zirconium tetraiodide  \n''NbI5 niobium(V)iodide  \n''TaI5 tantalum(V)iodide  \n''IrI3 iridium(III) iodide  \n''MoI2 molybdenum(II) iodide  \n''MoI3 molybdenum(III) iodide  \n''MoI4 molybdenum(IV) iodide  \n''NbI3 niobium(III) iodide  \n''NbI4 niobium(IV) iodide  \n''PmI3 promethium(III) iodide  \n''PrI2 praseodymium(II) iodide  \n''PuI3 plutonium(III) iodide  \n''Si2I6 hexaiododisilane  \n''TaI4 tantalum(IV) iodide  \n''TiI2 titanium(II) iodide  \n''TiI3 titanium(III) iodide  \n''WI2 tungsten(II) iodide  \n''WI3 tungsten(III) iodide  \n''WI4 tungsten(IV) iodide  \n''ZrI2 zirconium(II) iodide  \n''ZrI3 zirconium(III) iodide  \n''AgIO3 silver iodate  \n''Ag2HgI4 silver(I) tetraiodomercurate(II)  \n''AsHgI4 donovan's solution  \n''BaHgI4 barium tetraiodomercurate(II)  \n''BaI2O6 barium iodate  \n''Ba(IO4)2 barium periodate  \n''Br2CsI cesium dibromoiodate  \n''CDI3 iodoform-d  \n''CD2I2 diiodomethane-d 2  \n''CD3I deuterated iodomethane (D3)  \n''13CD3I iodomethane-13C,d3  \n''CF3I trifluoroiodomethane  \n''CHI3 iodoform  \n''13CH2I2 diiodomethane-13 C  \n''CH2I2 methylene iodide  \n''13CH3I iodomethane-13 C  \n''CH3I methyl iodide  \n''13CH313CH2I iodoethane-13 C2  \n''CIN cyanogen iodide  \n''CD3CD2I iodoethane-d 599.5 atom%D  \n''C2F4I2 1,2-diiodotetrafluoroethane  \n''CF3CF2I perfluoroethyl iodide  \n''C2H3I vinyl iodide  \n''ICH2CH2I 1,2-diiodoethane  \n''C2H5I iodoethane  \n''(CD3)2CDI 2-iodopropane-d 7  \n''(CF3)2CFI 1,1,1,2,3,3,3-heptafluoro-2-iodopropane  \n''CF3CF2CF2I 1-iodoheptafluoropropane  \n''CH2=CHCH2I allyl iodide  \n''I(CH2)3I 1,3-diiodopropane  \n''CH3CH2CH2I propyl iodide  \n''(CH3)2CHI isopropyl iodide  \n''I(CF2)4I 1,4-diiodooctafluorobutane  \n''CF3(CF2)3I n-nonafluorobutyl iodide  \n''I(CH2)4I 1,4-diiodobutane  \n''(CH3)2CHCH2I 1-iodo-2-methylpropane  \n''CH3(CH2)3I 1-iodobutane  \n''(CH3)3Cl 2-iodo-2-methylpropane  \n''CH3CH2CHICH3 2-iodobutane  \n''C5H9I iodocyclopentane  \n''(CH3)3CCHI2 1,1-diiodo-2,2-dimethylpropane  \n''I(CH2)5I 1,5-diiodopentane  \n''(CH3)3CCH2I neopentyl iodide  \n''(CH3)2CHCH2CH2I 1-iodo-3-methylbutane  \n''CH3(CH2)4I 1-iodopentane  \n''C2H5CH(CH3)CH2I (S)-(+)-1-iodo-2-methylbutane  \n''C6D5I iodobenzene-d 5  \n''C6F4I2 1,2-diiodotetrafluorobenzene  \n''C6F4I2 1,4-diiodotetrafluorobenzene  \n''C6F5I pentafluoroiodobenzene  \n''I(CF2)6I 1,6-diiodoperfluorohexane  \n''CF3(CF2)5I perfluorohexyl iodide  \n''C6H4I2 o-diiodobenzene  \n''C6H4I2 m-diiodobenzene  \n''C6H4I2 p-diiodobenzene  \n''C6H5I iodobenzene  \n''C6H11I iodocyclohexane  \n'I(CH2)6I 1,6-diiodohexane  \n''CH3(CH2)5I 1-iodohexane  \n''C7F7I heptafluorobenzyl iodide  \n''CH3C6H4I 1-iodo-2-methylbenzene  \n''CH3C6H4I 3-iodotoluene  \n''CH3C6H4I p-iodotoluene  \n''C7H7I benzyl iodide  \n''CH3(CH2)6I 1-iodoheptane  \n''I(CF2)8I hexadecafluoro-1,8-diiodooctane  \n''CF3(CF2)7I perfluorooctyl iodide  \n''C2H5C6H4I 1-ethyl-2-iodobenzene  \n''(CH3)2C6H3I 1-iodo-2,3-dimethylbenzene  \n''(CH3)2C6H3I 1-iodo-2,4-dimethylbenzene  \n''(CH3)2C6H3I 4-iodo-1,2-dimethylbenzene  \n''(CH3)2C6H3I 1-iodo-3,5-dimethylbenzene  \n''IC6H3(CH3)2 2-iodo-1,3-dimethylbenzene  \n''C6H5CH2CH2I 2-iodoethylbenzene  \n''C2H5C6H4I 4-ethyliodobenzene  \n''I(CH2)8I 1,8-diiodooctane  \n''CH3(CH2)7I 1-iodooctane  \n''CH3(CH2)3CH(C2H5)CH2I 2-ethylhexyl iodide  \n''C6H5(CH2)3I 1-iodo-3-phenylpropane  \n''CH3(CH2)8I 1-iodononane  \n''CF3(CF2)9I perfluorodecyl iodide  \n''C10H7I 1-iodonaphthalene  \n''(CH3)3CC6H4I 1-tert-butyl-4-iodobenzene  \n''C10H15I 1-iodoadamantane  \n''I(CH2)10I 1,10-diiododecane  \n''CH3(CH2)9I 1-iododecane  \n''CH3(CH2)10I 1-iodoundecane  \n''CF3(CF2)11I pentacosafluoro-1-iodododecane  \n''IC6H4C6H4I 4,4'-diiodobiphenyl  \n''C6H5C6H4l 2-iodobiphenyl  \n''C6H5C6H4I 4-iodobiphenyl  \n''CH3(CH2)11I 1-iodododecane  \n''C13H8I2 2,7-diiodofluorene  \n''C13H9I 2-iodofluorene  \n''C14H9I 9-iodophenanthrene  \n''CH3(CH2)15I 1-iodohexadecane  \n''C18H24I2 1,4-dicyclohexyl-2,5-diiodobenzene  \n''CH3(CH2)17I 1-iodooctadecane  \n''C22H36I2 1,4-bis(2-ethylhexyl)-2,5-diiodobenzene  \n''C22H36I2 1,4-diiodo-2,5-dioctylbenzene  \n''C24H15I3 1,3,5-tris(4-iodophenyl)benzene  \n''C26H44I2 1,4-bis(3,7-dimethyloctyl)-2,5-diiodobenzene  \n''C29H40I2 2,7-diiodo-9,9-dioctyl-9 H-fluorene  \n''C29H40I2 9,9-bis(2-ethylhexyl)-2,7-diiodo-9 H-fluorene  \n''C30H52I2 1,4-didodecyl-2,5-diiodobenzene  \n''C(CH2CH2CH(CH3)CH2CH2CH2CH(CH3)CH3)2(C6H3I)2 2,7-diiodo-9,9-di-(3',7'-dimethyloctyl)-9 H-fluorene  \n''C((CH2)11CH3)2(C6H3I)2 2,7-diiodo-9,9-di(iododecyl)-9 H-fluorene  \n''Cd(IO3)2 cadmium iodate  \n''Cl2CsI cesium dichloroiodide  \n''Co(IO3)2 cobalt(II) iodate  \n''CsIO3 cesium iodate  \n''CuIO3 copper iodate  \n''CuI2O6 copper(II) iodate  \n''Cu2HgI4 copper(I) mercury iodide  \n''HOI hypoiodous acid  \n''HIO3 iodic acid  \n''HI3Si triiodosilane  \n''NH4I ammonium iodide  \n''H5IN2 hydrazine hydroiodide  \n''H5IO6 periodic acid  \n''K2HgI4 mercury potassium iodide  \n''Hg2(IO3)2 mercury(I) iodate  \n''KIO3 potassium iodate  \n''KIO4 potassium periodate  \n''LaIO3 lanthanum iodate  \n''LiIO3 lithium iodate  \n''MnIO3 manganese iodate  \n''NaIO3 sodium iodate  \n''NaIO4 sodium periodate  \n''NiIO3 nickel(II) iodate  \n''IOF3 iodosyl trifluoride  \n''IOF5 iodasyl pentafluoride  \n''IO2F3 iodyl trifluoride  \n''IO3F periodyl fluoride  \n''SrIO3 strontium iodate  \n''IO3Tl thallium(I) iodate  \n''TlIO3 thallium iodate  \n''ZnIO3 zinc iodate  \n''Pb(IO3)2 lead(II)iodate  \n''Y(IO3)3 yttrium iodate  \n''K2PtI6 potassium hexaiodoplatinate(IV)  \n''K2ReI6 potassium hexaiodorhenate(IV)  \n''PH4I phosphonium iodide  \n''POI3 phosphoryl iodide  \n''PSI3 phosphorothioc triiodide  \n''SiCl3I trichloroiodosilane  \n''WO2I2 tungsten(VI) dioxydiiodide  \n''AlI3·6H2O aluminum iodide hexahydrate  \n''Ba(IO3)2·H2O barium iodate monohydrate  \n''Bal2·2H2O barium iodide dihydrate  \n''BiIO bismuth(III)oxyiodide  \n''13CH3CH2I iodoethane-2-13 C  \n''CH313CH2I iodoethane-1-13 C  \n''CD3MgI methyl-d 3-magnesium iodide solution  \n''HCD2I iodomethane-d 2  \n''BrCH2I bromoiodomethane  \n''ClCH2I chloroiodomethane  \n''DCH2I iodomethane-d 1  \n''CH2HgI2 iodo(iodomethyl)mercury  \n''CH3HgI methylmercury(II)iodide  \n''CH3MgI methylmagnesium iodide  \n''C2BrF4I 1-bromo-2-iodotetrafluoroethane  \n''C2ClF4I 1-chloro-2-iodotetrafluoroethane  \n'""", '53', '126.90')
        self.colorI=colorI="salmon3"
        self.I = tk.Button(self, text=I[0], width=5, height=2, bg=colorI, font=10, borderwidth=3,
                           command=lambda text=I: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorI, text[0], text[3], text[4]), self.voice(text[1]), self.compound_I()])
        self.I.grid(row=7, column=18)

        At = ('At', 'Astatine', """'At astatine\n'""", '85', '210.00')
        self.colorAt=colorAt="ivory3"
        self.At = tk.Button(self, text=At[0], width=5, height=2, bg=colorAt, font=10, borderwidth=3,
                           command=lambda text=At: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAt, text[0], text[3], text[4]), self.voice(text[1]), self.compound_At()])
        self.At.grid(row=8, column=18)

        Ts = ('Ts', 'Tennessine', """'Uus ununseptium\n'""", '117', '294.00')
        self.colorTs=colorTs="seashell3"
        self.Ts = tk.Button(self, text=Ts[0], width=5, height=2, bg=colorTs, font=10, borderwidth=3,
                           command=lambda text=Ts: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTs, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ts()])
        self.Ts.grid(row=9, column=18)
        
        He = ('He', 'Helium', """'He helium\n''He liquid helium\n'""", '2', '4.00')
        self.colorHe=colorHe="yellow2"
        self.He = tk.Button(self, text=He[0], width=5, height=2, bg=colorHe, font=10, borderwidth=3,
                           command=lambda text=He: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorHe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_He()])
        self.He.grid(row=3, column=19)

        Ne = ('Ne', 'Neon', """'Ne liquid neon \n''Ne neon \n'""", '10', '20.18')
        self.colorNe=colorNe="yellow3"
        self.Ne = tk.Button(self, text=Ne[0], width=5, height=2, bg=colorNe, font=10, borderwidth=3,
                           command=lambda text=Ne: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ne()])
        self.Ne.grid(row=4, column=19)

        Ar = ('Ar', 'Argon', """'Ar argon \n''Ar liquid argon \n'""", '18', '39.95')
        self.colorAr=colorAr="brown2"
        self.Ar = tk.Button(self, text=Ar[0], width=5, height=2, bg=colorAr, font=10, borderwidth=3,
                           command=lambda text=Ar: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ar()])
        self.Ar.grid(row=5, column=19)

        Kr = ('Kr', 'Krypton', """'Kr krypton \n''Kr liquid krypton \n''F2Kr krypton difluoride \n''KrFSb2F11 krypton fluoride hexafluoroantimonate \n'""", '36', '83.80')
        self.colorKr=colorKr="brown3"
        self.Kr = tk.Button(self, text=Kr[0], width=5, height=2, bg=colorKr, font=10, borderwidth=3,
                           command=lambda text=Kr: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorKr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Kr()])
        self.Kr.grid(row=6, column=19)

        Xe = ('Xe', 'Xenon', """'Xe liquid xenon \n''Xe xenon \n''XeF2 xenon difluoride \n''F4Xe xenon tetrafluoride \n''F6Xe xenon hexafluoride \n''XeO3 xenon trioxide \n''XeO4 xenon tetroxide \n''XeOF4 xenon oxytetrafluoride \n''XeO2F2 xenon dioxydifluoride \n''XeO3F2 xenon difluoride trioxide \n''XeFRuF6 xenon fluoride hexafluororuthenate \n''XeFSb2F11 xenon fluoride undecafluoroantimonate \n''XeF3SbF6 xenon fluoride hexafluoroantimonate \n''XeF3Sb2F11 xenon trifluoride undecafluoroantimonate \n''XeF5AsF6 xenon pentafluoride hexafluoroarsenate \n''XeF5RuF6 xenon pentafluoride hexafluororuthenate \n''Xe2F3AsF6 xenon fluoride hexafluoroarsenate \n'""", '54', '131.30')
        self.colorXe=colorXe="RoyalBlue3"
        self.Xe = tk.Button(self, text=Xe[0], width=5, height=2, bg=colorXe, font=10, borderwidth=3,
                           command=lambda text=Xe: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorXe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Xe()])
        self.Xe.grid(row=7, column=19)

        Rn = ('Rn', 'Radon', """'Rn radon radon gas \n'""", '86', '222.00')
        self.colorRn=colorRn="RoyalBlue4"
        self.Rn = tk.Button(self, text=Rn[0], width=5, height=2, bg=colorRn, font=10, borderwidth=3,
                           command=lambda text=Rn: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorRn, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Rn()])
        self.Rn.grid(row=8, column=19)

        Og = ('Og', 'Oganesson', """'Uuo ununoctium \n'""", '118', '294.00')
        self.colorOg=colorOg="DodgerBlue4"
        self.Og = tk.Button(self, text=Og[0], width=5, height=2, bg=colorOg, font=10, borderwidth=3,
                           command=lambda text=Og: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorOg, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Og()])
        self.Og.grid(row=9, column=19)


        self.fillerLine = tk.Label(self, text="")
        self.fillerLine.grid(row=12, column=0)

        Ce = ('Ce', 'Cerium', """'Ce cerium \n''CeBr3 cerium(III) bromide \n''CeC2Ce cerium carbide \n''CeB6 cerium boride \n''CeCl3 cerous chloride \n''CeF3 cerium fluoride \n''CeF4 cerium(IV)fluoride \n''CeH3 cerium(III) hydride \n''CeI3 cerium(III) iodide \n''CeN cerium nitride \n''CeO2 ceric oxide \n''CeS cerium(II) sulfide \n''CeSi2 cerium silicide \n''Ce2O3 cerium(III) oxide \n''Ce2S3 cerium(III) sulfide \n''C3Ce2O9 cerium(III) carbonate \n''Ce(C5H5)3 tris(cyclopentadienyl)cerium(III) \n''C27H39Ce tris(tetramethylcyclopentadienyl)cerium(III) \n''Ce(ClO4)4 perchloric acid, cerium(4+) salt \n''CeH3O3 cerium(III) hydroxide \n''Ce(OH)4 cerium(IV)hydroxide \n''CeN3O9 cerium nitrate \n''CeVO4 cerium(III) orthovanadate \n''(CeO2)·(ZrO2) cerium(IV)-zirconium(IV)oxide \n''Ce(SO4)2 ceric sulfate \n''Ce2(SO4)3 cerium(III)sulfate \n''Ce2(WO4)3 cerium(III)tungstate \n''Ce2(SeO4)3 cerium(III) selenate \n''AlCeO3 aluminum cerium oxide \n''Ce2(CO3)3·xH2O cerium(III)carbonate hydrate \n''Ce2(C2O4)3·xH2O cerium(III)oxalate hydrate \n''(CH3CO2)3Ce·xH2O cerium(III)acetate hydrate \n''Ce(C5H7O2)3·xH2O cerium(III)acetylacetonate hydrate \n''[CH3(CH2)3CH(C2H5)CO2]3Ce cerium(III)2-ethylhexanoate \n''CeBr3·7H2O cerium(III) bromide heptahydrate \n''Ce(ClO4)3 perchloric acid, cerium(3+) salt \n''CeCl3·7H2O cerium(III)chloride heptahydrate \n''Ce(SO4)2·xH2O·yH2SO4 cerium(IV)sulfate hydrate,complex with sulfuric acid \n''Ce(NH4)2(NO3)6 ammonium cerium(IV) nitrate \n''CeH9O12S2 cerium(IV) sulfate tetrahydrate \n''Ce(NO3)3·6H2O cerium(III)nitrate hexahydrate \n''CeI3·9H2O cerium(III) iodide nonahydrate \n''Ce2(SO4)3·8H2O cerium(III)sulfate octahydrate \n''Ce2(SO4)3·xH2O cerium(III)sulfate hydrate \n''Ce(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]cerium(III) \n''Ce(C2O4)3·9H2O cerium(III) oxalate nonahydrate \n''Ce(ClO4)3·6H2O cerium(III) perchlorate hexahydrate \n''Ce(NH4)4(SO4)4·xH2O ammonium cerium(IV)sulfate hydrate \n''Ce(NH4)4(SO4)4·2H2O ammonium cerium(IV)sulfate dihydrate ceric ammonium sulfate \n''Ce2(CO3)3·5H2O cerium(III) carbonate pentahydrate \n'""", '58', '140.12')
        self.colorCe=colorCe="snow3"
        self.Ce = tk.Button(self, text=Ce[0], width=5, height=2, bg=colorCe, font=10, borderwidth=3,
                           command=lambda text=Ce: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCe, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ce()])
        self.Ce.grid(row=13, column=5)

        Pr = ('Pr', 'Praseodymium', """'Pr praseodymium \n''PrBr3 praseodymium(III)bromide \n''PrCl3 praseodymium(III) chloride \n''PrF3 praseodymium fluoride \n''PrI3 praseodymium(III)iodide \n''NPr praseodymium nitride \n''Pr2O3 prasedymium(III)oxide \n''Pr6O11 praseodymium oxide \n''PrB6 praseodymium boride \n''PrF4 praseodymium(IV) fluoride \n''PrI2 praseodymium(II) iodide \n''PrSi2 praseodymium silicide \n''Pr2S3 praseodymium(III) sulfide \n''Pr2Te3 praseodymium(III) telluride \n''Br3O9Pr praseodymium(III) bromate \n''Pr(C5H5)3 tris(cyclopentadienyl)praseodymium(III) \n''C27H39Pr tris(tetramethylcyclopentadienyl)praseodymium(III) \n''Pr(C5H4CH(CH3)2)3 tris(isopropylcyclopentadienyl)praseodymium(III) \n''Pr(OH)3 praseodymium(III) hydroxide \n''N3O9Pr praseodymium(III) nitrate (1:3) \n''O4PPr praseodymium(III)phosphate \n''Pr2(SO4)3 praseodymium(III)sulfate \n''PrBr3·xH2O praseodymium(III)bromide hydrate \n''Pr2(C2O4)3·xH2O praseodymium(III)oxalate hydrate \n''Pr2(CO3)3·xH2O praseodymium(III)carbonate hydrate \n''Pr(OCH(CH3)2)3 praseodymium(III)isopropoxide \n''C3H16O17Pr2 praseodymium(III) carbonate actahydrate \n''Pr(C5H7O2)3·xH2O praseodymium(III)acetylacetonate hydrate \n''Pr(OCC(CH3)3CHCOC(CH3)3)3 tris(2,2,6,6-tetramethyl-3,5-heptanedionato)praseodymium(III) \n''PrCl3·xH2O praseodymium(III)chloride hydrate \n''Pr(ClO4)3 praseodymium(III)perchlorate \n''Pr(NO3)3·6H2O praseodymium(III) nitrate, hexahydrate \n''Pr(NO3)3·5H2O praseodymium(III) nitrate pentahydrate \n''H16O20Pr2S3 praseodymium(III) sulfate actahydrate \n''PrCl3·7H2O praseodymium(III) chloride heptahydrate \n''Pr(C5HF6O2)3·xH2O praseodymium(III)hexafluoroacetylacetonate hydrate \n''Pr(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]praseodymium(III) \n''Pr(OCC(CH3)3CHCOCF2CF2CF3)3 tris(6,6,7,7,8,8,8-heptafluoro-2,2-dimethyl-3,5-octanedionato)praseodymium(III) \n''C36H42F9O6Pr Pr(tfmc)3 \n''C42H42F21O6Pr praseodymium(hfc)3 \n'""", '59', '140.91')
        self.colorPr=colorPr="SlateBlue3"
        self.Pr = tk.Button(self, text=Pr[0], width=5, height=2, bg=colorPr, font=10, borderwidth=3,
                           command=lambda text=Pr: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Pr()])
        self.Pr.grid(row=13, column=6)

        Nd = ('Nd', 'Neodymium', """'Nd neodymium \n''NdBr3 neodymium bromide \n''NdCl3 neodymium chloride \n''F3Nd neodymium fluoride \n''I3Nd neodymium iodide \n''NNd neodymium nitride \n''NdB6 neodymium boride \n''NdCl2 neodymium(II) chloride \n''NdSb neodymium antimonide \n''Nd2O3 neodymium(III) oxide \n''Nd2S3 neodymium(III) sulfide \n''Nd2Te3 neodymium(III) telluride \n''Nd2(CO3)3 neodymium carbonate \n''Nd(C5H5)3 tris(cyclopentadienyl)neodymium(III) \n''Nd(C5H4CH(CH3)2)3 tris(isopropylcyclopentadienyl)neodymium(III) \n''C27H39Nd tris(tetramethylcyclopentadienyl)neodymium(III) \n''Nd(OH)3 neodymium(III)hydroxide hydrate \n''Nd(NO3)3 neodymium(III) nitrate \n''Nd2(SO4)3 neodymium(III)sulfate \n''NdBr3·xH20 neodymium(III)bromide hydrate \n''Nd2(CO3)3·xH2O neodymium(III)carbonate hydrate \n''Nd(OCH(CH3)2)3 neodymium(III)isopropoxide \n''Nd2(C2O4)3·xH2O neodymium(III)oxalate hydrate \n''(CH3CO2)3Nd·xH2O neodymium(III)acetate hydrate \n''Nd(C5H7O2)3·xH2O neodymium(III)acetylacetonate hydrate \n''Nd(OCC(CH3)3CHCOC(CH3)3)3 neodymium(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''NdCl3·6H2O neodymium(III)chloride hexahydrate \n''Nd(ClO4)3 neodymium(III)perchlorate \n''NdO4P·xH2O neodymium(III)phosphate hydrate \n''Nd(NO3)3·6H2O neodymium(III) nitrate, hexahydrate \n''Nd(NO3)3·xH2O neodymium(III)nitrate hydrate \n''Nd2(SO4)3·xH2O neodymium(III)sulfate hydrate \n''H16Nd2O20S3 neodymium(III) sulfate actahydrate \n''Nd(C2H3O2)2 neodymium(II) acetate \n'""", '60', '144.24')
        self.colorNd=colorNd="PaleTurquoise3"
        self.Nd = tk.Button(self, text=Nd[0], width=5, height=2, bg=colorNd, font=10, borderwidth=3,
                           command=lambda text=Nd: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNd, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Nd()])
        self.Nd.grid(row=13, column=7)    

        Pm = ('Pm', 'Promethium', """'Pm promethium \n''PmBr3 promethium(III) bromide \n''PmCl3 promethium(III) chloride \n''PmF3 promethium(III) fluoride \n''PmI3 promethium(III) iodide \n'""", '61', '145.00')
        self.colorPm=colorPm="IndianRed3"
        self.Pm = tk.Button(self, text=Pm[0], width=5, height=2, bg=colorPm, font=10, borderwidth=3,
                           command=lambda text=Pm: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPm, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Pm()])
        self.Pm.grid(row=13, column=8)

        Sm = ('Sm', 'Samarium', """'Sm samarium \n''SmBr3 samarium(III)bromide \n''SmCl3 samarium(III)chloride \n''Sm2Co7 disamarium heptacobalt \n''SmCo5 samarium pentacobalt \n''SmF3 samarium(III) fluoride \n''SmI2 samarium(II)iodide \n''SmI3 samarium(III)iodide \n''Sm2O3 samarium(III) oxide \n''SmB6 samarium boride \n''SmBr2 samarium(II) bromide \n''SmCl2 samarium(II) chloride \n''SmF2 samarium(II) fluoride \n''SmSi2 samarium silicide \n''Sm2S3 samarium(III) sulfide \n''Sm2Te3 samarium(III) telluride \n''C3O9Sm2 samarium(III) carbonate \n''(C5H5)3Sm tris(cyclopentadienyl)samarium(III) \n''C27H39Sm tris(tetramethylcyclopentadienyl)samarium(III) \n''Sm(OH)3·xH2O samarium(III)hydroxide hydrate \n''N3O9Sm samarium(III) nitrate \n''Sm2(SO4)3 samarium(III)sulfate \n''(CH3CO2)3Sm·xH2O samarium(III)acetate hydrate \n''Sm2(CO3)3·xH2O samarium(III)carbonate hydrate \n''Sm[OCH(CH3)2]3 samarium(III)isopropoxide \n''[CH3COCH=C(O)CH3]3Sm·xH2O samarium(III)acetylacetonate hydrate \n''Sm(ClO4)3 samarium(III)perchlorate \n''SmCl3·6H2O samarium(III)chloride hexahydrate \n''O4PSm·xH2O samarium(III)phosphate hydrate \n''Sm2(SO4)3·8H2O samarium(III)sulfate octahydrate \n''Sm(NO3)3·6H2O samarium(III)nitrate hexahydrate \n''Sm(N(Si(CH3)3)2)3 tris(N,N-bis(trimethylsilyl)amide]samarium(III) \n''Sm(BrO3)3·9H2O samarium(III) bromate nonahydrate \n''Sm(SO3CF3)3 samarium(III)trifluoromethanesulfonate \n''Sm(C2H3O2)3·3H2O samarium(III) acetate trihydrate \n''Sm(OCC(CH3)3CHCOC(CH3)3)3 samarium(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate \n'""", '62', '150.40')
        self.colorSm=colorSm="bisque3"
        self.Sm = tk.Button(self, text=Sm[0], width=5, height=2, bg=colorSm, font=10, borderwidth=3,
                           command=lambda text=Sm: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorSm, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Sm()])
        self.Sm.grid(row=13, column=9)

        Eu = ('Eu', 'Europium', """'Eu europium \n''Eul3 europium(III) iodide \n''Br2Eu europium(II)bromide \n''Br3Eu europium(III) bromide \n''Cl2Eu europium(II)chloride \n''Cl3Eu europium(III) chloride \n''EuB6 europium boride \n''EuF2 europium(II) fluoride \n''EuF3 europium(III)fluoride \n''EuI2 europium(II)iodide \n''EuN europium nitride \n''EuS europium(II) sulfide \n''EuSe europium(II) selenide \n''EuSi2 europium silicide \n''EuTe europium(II) telluride \n''Eu2O3 europium(III) oxide \n''C6Eu2O12 europium(III) oxalate \n''C27H39Eu tris(tetramethylcyclopentadienyl)europium(III) \n''Eu(OH)3 europium(III) hydroxide \n''Eu2(SO4)3 europium(III)sulfate \n''EuBr3·xH2O europium(III)bromide hydrate \n''(NH4)2MoS4 ammonium tetrathiomolybdate \n''(CH3CO2)3Eu·xH2O europium(III)acetate hydrate \n''Eu(C5H7O2)3·xH2O europium(III)acetylacetonate hydrate \n''Cl3Eu·6H2O europium(III)chloride hexahydrate \n''Eu(ClO4)3 europium(III)perchlorate \n''EuO4P·xH2O europium(III)phosphate hydrate \n''Eu(NO3)3·xH2O europium(III)nitrate hydrate \n''Eu(NO3)3·5H2O europium(III)nitrate pentahydrate \n''Eu(NO3)3·6H2O europium(III) nitrate hexahydrate \n''Eu2(SO4)3·xH2O europium(III)sulfate hydrate \n''(CF3CO2)3Eu·3H2O europium(III)trifluoroacetate trihydrate \n''Eu(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]europium(III) \n''Eu(OCC(CH3)3CHCOCF2CF2CF3)3 tris(6,6,7,7,8,8,8-heptafluoro-2,2-dimethyl-3,5-octanedionato)europium(III) \n''C42H35EuN2O6 tris(benzoylacetonato)mono(phenanthroline)europium(III) \n''C42H42EuF21O6 tris[3-(heptafluoropropylhydroxymethylene)-(+)-camphorate]europium(III) \n''C57H41EuN2O6 tris(dibenzoylmethane)mono(1,10-phenanthroline)europium(lll) \n''C57H45EuN3O6 tris(dibenzoylmethane)mono(5-amino-1,10-phenanthroline)europium(lll) \n''Eu(ClO4)3·6H2O europium(III) perchlorate hexahydrate \n''Eu2(C2O4)3·xH2O europium(III)oxalate hydrate \n'""", '63', '151.96')
        self.colorEu=colorEu="cyan3"
        self.Eu = tk.Button(self, text=Eu[0], width=5, height=2, bg=colorEu, font=10, borderwidth=3,
                           command=lambda text=Eu: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorEu, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Eu()])
        self.Eu.grid(row=13, column=10)

        Gd = ('Gd', 'Gadolinium', """'Gd gadolinium \n''GdBr3 gadolinium(III)bromide \n''GdCl3 gadolinium(III) chloride \n''GdF3 gadolinium(III)fluoride \n''GdB6 gadolinium boride \n''GdI2 gadolinium(II) iodide \n''GdI3 gadolinium(III)iodide \n''GdN gadolinium nitride \n''GdSb gadolinium antimonide \n''GdSe gadolinium(II) selenide \n''GdSi2 gadolinium silicide \n''Gd2O3 gadolinium(III) oxide \n''Gd2S3 gadolinium(III) sulfide \n''Gd2Te3 gadolinium(III) telluride \n''Gd(C5H5)3 tris(cyclopentadienyl)gadolinium(III) \n''C21H27Gd tris(ethylcyclopentadienyl)gadolinium(III) \n''C27H39Gd tris(tetramethylcyclopentadienyl)gadolinium(III) \n''Gd3Ga5O12 gadolinium gallium garnet \n''Gd(OH)3·xH2O gadolinium(III)hydroxide hydrate \n''Gd(NO3)3 gadolinium(III) nitrate \n''GdBr3·xH2O gadolinium(III)bromide hydrate \n''(CH3CO2)3Gd·xH2O gadolinium(III)acetate hydrate \n''Gd2(CO3)3·xH2O gadolinium(III)carbonate hydrate \n''Gd2(C2O4)3·xH2O gadolinium(III)oxalate hydrate \n''C6H17GdO10 gadolinium(III) acetate tetrahydrate \n''[CH3(CH2)6CO2]3Gd gadolinium(III)octanoate \n''[CH3COCH=C(O)CH3]3Gd·xH2O gadolinium(III)acetylacetonate hydrate \n''Gd(OCC(CH3)3CHCOC(CH3)3)3 Resolve-Al™Gd \n''GdCl3·6H2O gadolinium(III)chloride hexahydrate \n''GdCl3·xH2O gadolinium(III)chloride hydrate \n''Gd(ClO4)3 gadolinium(III)perchlorate \n''Gd(NO3)3·6H2O gadolinium(III) nitrate hexahydrate \n''Gd2(SO4)3 gadolinium(III)sulfate \n''Gd2(SO4)3·8H2O gadolinium(III)sulfate octahydrate \n''C16H28GdN5O9 gadodiamide \n''C17H29GdN4O7 gadoteridol \n''Gd(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]gadolinium(III) \n''C20H34GdN5O10 gadoversetamide \n''C28H54GdN5O20 gadopentetate dimeglumine \n''C30H30O6F21Gd Resolve-Al™GdFOD \n''C36H62GdN5O21 gadobenate dimeglumine \n''Gd(NO3)3·5H2O gadolinium(III) nitrate pentahydrate \n'""", '64', '157.25')
        self.colorGd=colorGd="tan4"
        self.Gd = tk.Button(self, text=Gd[0], width=5, height=2, bg=colorGd, font=10, borderwidth=3,
                           command=lambda text=Gd: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorGd, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Gd()])
        self.Gd.grid(row=13, column=11)

        Tb = ('Tb', 'Terbium', """'TbF4 terbium(IV) fluoride \n''TbSi2 terbium silicide \n''Tb2S3 terbium(III) sulfide \n''(C5H5)3Tb tris(cyclopentadienyl)terbium(III) \n''Tb(C5H4CH(CH3)2)3 tris(isopropylcyclopentadienyl)terbium(III) \n''C27H39Tb tris(tetramethylcyclopentadienyl)terbium(III) \n''N3O9Tb terbium(III) nitrate \n''Tb2(SO4)3 terbium(III)sulfate \n''(CH3CO2)3Tb·xH2O terbium(III)acetate hydrate \n''Tb(OCC(CH3)3CHCOC(CH3)3)3 terbium(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''TbCl3·6H2O terbium(III)chloride hexahydrate \n''TbCl3·xH2O terbium(III)chloride hydrate \n''Tb(ClO4)3 terbium(III)perchlorate \n''Tb(NO3)3·6H2O terbium(III) nitrate, hexahydrate \n''Tb(NO3)3·5H2O terbium(III)nitrate pentahydrate \n''Tb2(SO4)3·8H2O terbium(III)sulfate octahydrate \n''Tb(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]terbium(III) \n''Tb(CF3SO3)3 terbium(III)trifluoromethanesulfonate \n'""", '65', '158.93')
        self.colorTb=colorTb="DeepPink3"
        self.Tb = tk.Button(self, text=Tb[0], width=5, height=2, bg=colorTb, font=10, borderwidth=3,
                           command=lambda text=Tb: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTb, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Tb()])
        self.Tb.grid(row=13, column=12)

        Dy = ('Dy', 'Dyprosium', """'Dy dysprosium \n''DyBr3 dysprosium(III)bromide \n''DyCl3 dysprosium(III) chloride \n''DyB4 dysprosium boride \n''DyBr2 dysprosium(II) bromide \n''DyCl2 dysprosium(II) chloride \n''DyF3 dysprosium(III) fluoride \n''DyH3 dysprosium hydride \n''DyI2 dysprosium(II)iodide \n''DyI3 dysprosium(III)iodide \n''DyN dysprosium nitride \n''DySb dysprosium antimonide \n''DySi2 dysprosium silicide \n''Dy2O3 dysprosium(III) oxide \n''Dy2S3 dysprosium(III) sulfide \n''Dy2Te3 dysprosium(III) telluride \n''DyH3O3 dysprosium(III) hydroxide \n''DyBr3·xH2O dysprosium(III)bromide hydrate \n''Dy2(CO3)3·xH2O dysprosium(III)carbonate hydrate \n''Dy2(C2O4)3·xH2O dysprosium(III)oxalate hydrate \n''(CH3CO2)3Dy·xH2O dysprosium(III)acetate hydrate \n''C6H17DyO10 dysprosium(III) acetate tetrahydrate \n''Dy(OCC(CH3)3CHCOC(CH3)3)3 tris(2,2,6,6-tetramethyl-3,5-heptanedionato)dysprosium(III) \n''DyCl3·6(H2O) dysprosium(III)chloride hexahydrate \n''Dy(ClO4)3 dysprosium(III)perchlorate \n''Dy(NO3)3·xH2O dysprosium(III) nitrate hydrate \n''Dy2(SO4)3 dysprosium(III)sulfate \n''Dy2(SO4)3·8H2O dysprosium(III)sulfate octahydrate \n''Dy(OCC(CH3)3CHCOCF2CF2CF3)3 Resolve-Al™DyFOD \n'""", '66', '162.50')
        self.colorDy=colorDy="DarkOrchid3"
        self.Dy = tk.Button(self, text=Dy[0], width=5, height=2, bg=colorDy, font=10, borderwidth=3,
                           command=lambda text=Dy: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorDy, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Dy()])
        self.Dy.grid(row=13, column=13)

        Ho = ('Ho', 'Holmium', """'Ho holmium \n''HoBr3 holmium(III)bromide \n''HoCl3 holmium chloride \n''HoF3 holmium(III)fluoride \n''HoI3 holmium(III)iodide \n''HoN holmium nitride \n''HoSb holmium antimonide \n''HoSi2 holmium silicide \n''Ho2O3 holmium(III) oxide \n''Ho2S3 holmium sulfide \n''(C5H5)3Ho tris(cyclopentadienyl)holmium(III) \n''HoO4P holmium(III)phosphate \n''Ho2(SO4)3 holmium(III)sulfate \n''HoBr3·xH2O holmium(III)bromide hydrate \n''Ho2(CO3)3·xH2O holmium(III)carbonate hydrate \n''C6H9HoO6 holmium acetate \n''(CH3CO2)3Ho·xH2O holmium(III)acetate hydrate \n''C6H20Ho2O22 holmium oxalate decahydrate \n''Ho(OCC(CH3)3CHCOC(CH3)3)3 tris(2,2,6,6-tetramethyl-3,5-heptanedionato)holmium(III) \n''Ho(ClO4)3 holmium(III)perchlorate \n''HoCl3·6H2O holmium(III)chloride hexahydrate \n''Ho(NO3)3·5H2O holmium(III) nitrate pentahydrate \n'""", '67', '164.93')
        self.colorHo=colorHo="orange3"
        self.Ho = tk.Button(self, text=Ho[0], width=5, height=2, bg=colorHo, font=10, borderwidth=3,
                           command=lambda text=Ho: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorHo, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Ho()])
        self.Ho.grid(row=13, column=14)
    
        Er = ('Er', 'Erbium', """'Er erbium \n''ErBr3 erbium(III)bromide \n''ErCl3 erbium chloride \n''ErB4 erbium boride \n''ErF3 erbium fluoride \n''ErH3 erbium hydride \n''ErI3 erbium iodide \n''ErN erbium nitride \n''ErSb erbium antimonide \n''ErSi2 erbium silicide \n''Er2O3 erbium oxide \n''Er2S3 erbium sulfide \n''Er2Te3 erbium telluride \n''Er(C5H5)3 tris(cyclopentadienyl)erbium(III) \n''Er(C5H4CH(CH3)2)3 tris(isopropylcyclopentadienyl)erbium(III) \n''Er(C5H4C4H9)3 tris(butylcyclopentadienyl)erbium(III) \n''ErH3O3 erbium hydroxide \n''Er2(SO4)3 erbium(III)sulfate \n''ErBr3·xH2O erbium(III)bromide hydrate \n''Er2(C2O4)3·xH2O erbium(III)oxalate hydrate \n''(CH3CO2)3Er·xH2O erbium(III)acetate hydrate \n''Er(C5H7O2)3·xH2O erbium(III)acetylacetonate hydrate \n''Er(OCC(CH3)3CHCOC(CH3)3)3 erbium(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''ErCl3·6H2O erbium(III)chloride hexahydrate \n''Er(ClO4)3 erbium(III)perchlorate \n''ErBr3·6H2O erbium bromide hexahydrate \n''ErPO4·xH2O erbium(III)phosphate hydrate \n''Er(NO3)3·5H2O erbium(III)nitrate pentahydrate \n''Er2(SO4)3·xH2O erbium(III)sulfate hydrate \n''Er2H16O20S3 erbium sulfate actahydrate \n''C27H18ErN3O3 tris(8-hydroxyquinolinato)erbium(III) \n''C30H30ErF21O6 Resolve-Al™ErFOD \n''C36H42ErF9O6 erbium(III)tris[3-(trifluoromethylhydroxymethylene)-(+)-camphorate] \n''C42H42ErF21O6 erbium tris[3-(heptafluoropropylhydroxymethylene)-(-)-camphorate] \n''Er2(SO4)3·8H2O erbium sulfate octahydrate \n'""", '68', '167.26')
        self.colorEr=colorEr="maroon3"
        self.Er = tk.Button(self, text=Er[0], width=5, height=2, bg=colorEr, font=10, borderwidth=3,
                           command=lambda text=Er: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorEr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Er()])
        self.Er.grid(row=13, column=15)

        Tm = ('Tm', 'Thulium', """'Tm thulium \n''TmBr3 thulium(III)bromide \n''Cl2Tm thulium(II) chloride \n''TmCl3 thulium chloride \n''TmF3 thulium(III)fluoride \n''TmI2 thulium(II)iodide \n''TmI3 thulium(III)iodide \n''Tm2O3 thulium(III) oxide \n''TmSb thullium monoantimonide \n''TmBr2 thulium(II) bromide \n''C6O12Tm2 thulium(III)oxalate \n''(C5H5)3Tm tris(cyclopentadienyl)thulium(III) \n''H3O3Tm thulium(III) hydroxide \n''Tm2(SO4)3 thulium(III)sulfate \n''Tm(NO3)3 thulium(III) nitrate \n''TmBr3·xH2O thulium(III)bromide hydrate \n''Tm2(CO3)3·xH2O thulium(III)carbonate hydrate \n''Tm2(C2O4)3·xH2O thulium(III)oxalate hydrate \n''(CH3CO2)3Tm·xH2O thulium(III)acetate hydrate \n''Tm(OCC(CH3)3CHCOC(CH3)3)3 thulium(III)tris(2,2,6,6-tetramethyl-3,5-heptanedionate) \n''TmCl3·6H2O thulium(III)chloride hexahydrate \n''Cl3H14O7Tm thulium(III) chloride heptahydrate \n''Tm2(SO4)3·8H2O thulium(III)sulfate octahydrate \n''Tm(NO3)3·5H2O thulium(III)nitrate pentahydrate \n''Tm(N(Si(CH3)3)2)3 tris[N,N-bis(trimethylsilyl)amide]thulium(III) \n''Tm2(C2O4)3·6H2O thulium(III) oxalate hexahydrate \n''Tm(CF3SO3)3 thulium(III)trifluoromethanesulfonate \n'""", '69', '168.93')
        self.colorTm=colorTm="SeaGreen3"
        self.Tm = tk.Button(self, text=Tm[0], width=5, height=2, bg=colorTm, font=10, borderwidth=3,
                           command=lambda text=Tm: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTm, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Tm()])
        self.Tm.grid(row=13, column=16)

        Yb = ('Yb', 'Ytterbium', """'Yb ytterbium \n''Br2Yb ytterbium(II) bromide \n''YbBr3 ytterbium(III)bromide \n''YbCl3 ytterbium(III) chloride \n''YbF3 ytterbium fluoride \n''YbI2 ytterbium(II)iodide \n''Yb2O3 ytterbium(III) oxide \n''YbSb ytterbium monoantimonide \n''YbCl2 ytterbium(II) chloride \n''YbF2 ytterbium(II) fluoride \n''YbSi2 ytterbium silicide \n''Yb(C5H5)3 tris(cyclopentadienyl)ytterbium(III) \n''N3O9Yb ytterbium(III) nitrate \n''Yb2(SO4)3 ytterbium(III)sulfate \n''YbBr3·xH2O ytterbium(III)bromide hydrate \n''Yb(C2H3O2)3·4H2O ytterbium(III)acetate tetrahydrate \n''[(CH3)2CHO]3Yb ytterbium(III)isopropoxide \n''La(OCC(CH3)3CHCOC(CH3)3)3 Resolve-Al™La \n''Yb(OCC(CH3)3CHCOC(CH3)3)3 tris(2,2,6,6-tetramethyl-3,5-heptanedionato)ytterbium(III) \n''Yb(ClO4)3 ytterbium(III)perchlorate \n''YbCl3·6H2O ytterbium(III)chloride hexahydrate \n''Yb(NO3)3·5H2O ytterbium(III)nitrate pentahydrate \n''H16O20S3Yb2 ytterbium(III) sulfate actahydrate \n''Yb(OCC(CH3)3CHCOCF2CF2CF3)3 ytterbium(FOD)3 \n''Yb(C12H14F3O2)3 ytterbium(tfc)3 \n''Yb2(SO4)3·8H2O ytterbium(III) sulfate octahydrate \n''Yb(CF3SO3)3 ytterbium(III)trifluoromethanesulfonate \n''Yb(CF3SO3)3·xH2O ytterbium(III)trifluoromethanesulfonate hydrate \n''[(CF3SO2)2N]3Yb ytterbium(III)trifluoromethanesulfonimide \n'""", '70', '173.04')
        self.colorYb=colorYb="DarkGoldenrod3"
        self.Yb = tk.Button(self, text=Yb[0], width=5, height=2, bg=colorYb, font=10, borderwidth=3,
                           command=lambda text=Yb: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorYb, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Yb()])
        self.Yb.grid(row=13, column=17)

        Lu = ('Lu', 'Lutetium', """'Lu lutetium \n''LuBr3 lutetium(III)bromide \n''LuCl3 lutetium chloride \n''F3Lu lutetium fluoride \n''I3Lu lutetium(III)iodide \n''LuB4 lutetium boride \n''LuN lutetium nitride \n''LuSb lutetium antimonide \n''Lu2O3 lutetium(III) oxide \n''Lu2S3 lutetium sulfide \n''Lu2Te3 lutetium telluride \n''LuN3O9 lutetium(III) nitrate (1:3) \n''Lu2O12S4 lutetium(III)sulfate \n''LuBr3·xH2O lutetium(III)bromide hydrate \n''Lu2(CO3)3·xH2O lutetium(III)carbonate hydrate \n''Lu2(C2O4)3·xH2O lutetium(III)oxalate hydrate \n''(CH3CO2)3Lu·xH2O lutetium(III)acetate hydrate \n''[CH3COCHC(O)CH3]3Lu·xH2O lutetium(III)acetylacetonate hydrate \n''LuCl3·6H2O lutetium(III)chloride hexahydrate \n''Lu(ClO4)3 lutetium(III)perchlorate \n''Lu(NO3)3·xH2O lutetium(III)nitrate hydrate \n''Lu2(SO4)3·xH2O lutetium(III)sulfate hydrate \n''H12LuN3O15 lutetium(III) nitrate, hexahydrate (1:3:6) \n''Lu2(SO4)3·8H2O lutetium sulfate octahydrate \n'""", '71', '174.97')
        self.colorLu=colorLu="cornSilk3"
        self.Lu = tk.Button(self, text=Lu[0], width=5, height=2, bg=colorLu, font=10, borderwidth=3,
                           command=lambda text=Lu: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorLu, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Lu()])
        self.Lu.grid(row=13, column=18)


        Th = ('Th', 'Thorium', """'Th thorium \n''ThAl3 thorium aluminum alloy \n''ThBi2 thorium bismide \n''Br4Th thorium(IV) bromide \n''ThC2 thorium dicarbide \n''Cl4Th thorium(IV)chloride \n''F4Th thorium(IV)fluoride \n''I4Th thorium(IV) iodide \n''ThO2 thorium(IV) oxide \n''S2Th thorium(IV) sulfide \n''Se2Th thorium(IV) selenide \n''Si2Th thorium silicide \n''Te2Th thorium telluride \n''ThB6 thorium boride \n''ThH2 thorium hydride \n''ThN thorium nitride \n''Th(CO3)2 thorium(IV) carbonate \n''ThOF2 thorium oxyfluoride \n''Th(OH)4 thorium(IV) hydroxide \n''Th(NO3)4 thorium nitrate \n''Th(SO4)2·9H2O thorium(IV) sulfate nonahydrate \n''C20H28O8Th thorium acetylacetonate \n''Cl4H14O7Th thorium(IV) chloride heptahydrate \n''ThSiO4 thorium orthosilicate \n''H8N4O16Th thorium(IV) nitrate tetrahydrate \n'""", '90', '232.04')
        self.colorTh=colorTh="snow4"
        self.Th = tk.Button(self, text=Th[0], width=5, height=2, bg=colorTh, font=10, borderwidth=3,
                           command=lambda text=Th: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorTh, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Th()])
        self.Th.grid(row=14, column=5)

        Pa = ('Pa', 'Protactinium', """'Pa protactinium \n''PaCl5 protactinium(V) chloride \n'""", '91', '231.04')
        self.colorPa=colorPa="SlateBlue4"
        self.Pa = tk.Button(self, text=Pa[0], width=5, height=2, bg=colorPa, font=10, borderwidth=3,
                           command=lambda text=Pa: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPa, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Pa()])
        self.Pa.grid(row=14, column=6)

        U = ('U', 'Uranium', """'U uranium \n''B2U uranium boride \n''Br3U uranium tribromide \n''Br4U uranium tetrabromide \n''Br5U uranium pentabromide \n''Cl3U uranium(III) chloride \n''Cl4U uranium(IV) chloride \n''F3U uranium(III) fluoride \n''F4U uranium tetrafluoride \n''UF5 uranium pentafluoride \n''F6U uranium hexafluoride \n''I3U uranium(III) iodide \n''I4U uranium(IV) iodide \n''NU uranium nitride \n''O2U uranium dioxide \n''O3U uranium(vI) oxide \n''S2U uranium sulfide \n''Se2U uranium diselenide \n''Si2U uranium disilicide \n''Te2U uranium ditelluride \n''UC uranium carbide (1:1) \n''UCl5 uranium(V) chloride \n''UCl6 uranium(VI) chloride \n''UH3 uranium(III) hydride \n''U3O8 uranium(V,VI) oxide \n''U4O9 uranium(IV,V) oxide \n''K2U2O7 potassium uranate \n''UO2SO4 uranyl sulfate \n''UO2Cl2 uranyl chloride \n''UO2F2 uranyl fluoride \n''U2(NO3)2 uranyl nitrate \n''C10H14O6U dioxobis(2,4-pentanedionato-o,O')-uranium \n''(NH4)2U2O7 ammonium uranate(VI) \n''UO3·H2O uranium(VI) oxide monohydrate \n''UO4·2H2O uranium peroxide dihydrate \n''K(UO2)(NO3)3 potassium uranyl nitrate \n''Na2U2O7·H2O sodium uranate(VI) monohydrate \n''UO2(NH4)3F5 ammonium uranium fluoride \n''UO2(NO3)2·6H2O uranyl nitrate hexahydrate \n''UO2SO4·3H2O uranyl sulfate trihydrate \n''K2(UO2)(SO4)2·2H2O potassium uranyl sulfate dihydrate \n''UO2(C2H3O2)2·2H2O uranyl acetate dihydrate \n''UO2HPO4·4H2O uranyl hydrogen phosphate tetrahydrate \n'""", '92', '238.03')
        self.colorU=colorU="PaleTurquoise4"
        self.U = tk.Button(self, text=U[0], width=5, height=2, bg=colorU, font=10, borderwidth=3,
                           command=lambda text=U: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorU, text[0], text[3], text[4]), self.voice(text[1]), self.compound_U()])
        self.U.grid(row=14, column=7)

        Np = ('Np', 'Neptunium', """Np neptunium \n''NpO2 neptunium(IV) oxide \n'""", '93', '237.05')
        self.colorNp=colorNp="IndianRed4"
        self.Np = tk.Button(self, text=Np[0], width=5, height=2, bg=colorNp, font=10, borderwidth=3,
                           command=lambda text=Np: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNp, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Np()])
        self.Np.grid(row=14, column=8)

        Pu = ('Pu', 'Plutonium', """'Pu plutonium \n''F3Pu plutonium(III) fluoride \n''F4Pu plutonium(IV) fluoride \n''PuBr3 plutonium(III) bromide \n''PuCl3 plutonium(III) chloride \n''PuF6 plutonium(VI) fluoride \n''PuI3 plutonium(III) iodide \n''PuN plutonium nitride \n''PuO plutonium(II) oxide \n''PuO2 plutonium(IV) oxide \n''Pu2O3 plutonium(III) oxide \n'""", '94', '244.00')
        self.colorPu=colorPu="bisque4"
        self.Pu = tk.Button(self, text=Pu[0], width=5, height=2, bg=colorPu, font=10, borderwidth=3,
                           command=lambda text=Pu: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorPu, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Pu()])
        self.Pu.grid(row=14, column=9)

        Am = ('Am', 'Americium', """'Am americium \n''AmBr3 americium(III) bromide \n''AmCl3 americium(III) chloride \n''AmF3 americium(III) fluoride \n''AmF4 americium(IV) fluoride \n''AmI3 americium(III) iodide \n''AmO2 americium(IV) oxide \n''Am2O3 americium(III) oxide \n'""", '95', '243.00')
        self.colorAm=colorAm="cyan4"
        self.Am = tk.Button(self, text=Am[0], width=5, height=2, bg=colorAm, font=10, borderwidth=3,
                           command=lambda text=Am: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorAm, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Am()])
        self.Am.grid(row=14, column=10)

        Cm = ('Cm', 'Curium', """'Cm curium curium metal\n'""", '96', '247.00')
        self.colorCm=colorCm="coral4"
        self.Cm = tk.Button(self, text=Cm[0], width=5, height=2, bg=colorCm, font=10, borderwidth=3,
                           command=lambda text=Cm: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCm, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cm()])
        self.Cm.grid(row=14, column=11)

        Bk = ('Bk', 'Berkelium', """'Bk α-berkelium\n''Bk β-berkelium\n'""", '97', '247.00')
        self.colorBk=colorBk="DeepPink4"
        self.Bk = tk.Button(self, text=Bk[0], width=5, height=2, bg=colorBk, font=10, borderwidth=3,
                           command=lambda text=Bk: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorBk, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Bk()])
        self.Bk.grid(row=14, column=12)

        Cf = ('Cf', 'Californium', """'Cf californium californium metal\n'""", '98', '247.00')
        self.colorCf=colorCf="DarkOrchid4"
        self.Cf = tk.Button(self, text=Cf[0], width=5, height=2, bg=colorCf, font=10, borderwidth=3,
                           command=lambda text=Cf: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorCf, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Cf()])
        self.Cf.grid(row=14, column=13)

        Es = ('Es', 'Einsteinium', """'Es einsteinium einsteinium metal\n'""", '99', '252.00')
        self.colorEs=colorEs="orange4"
        self.Es = tk.Button(self, text=Es[0], width=5, height=2, bg=colorEs, font=10, borderwidth=3,
                           command=lambda text=Es: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorEs, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Es()])
        self.Es.grid(row=14, column=14)

        Fm = ('Fm', 'Fermium', """'Fm fermium fermium metal\n'""", '100', '257.00')
        self.colorFm=colorFm="maroon4"
        self.Fm = tk.Button(self, text=Fm[0], width=5, height=2, bg=colorFm, font=10, borderwidth=3,
                           command=lambda text=Fm: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorFm, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Fm()])
        self.Fm.grid(row=14, column=15)

        Md = ('Md', 'Mendelevium', """'Md mendelevium mendelevium metal\n'""", '101', '260.00')
        self.colorMd=colorMd="SeaGreen4"
        self.Md = tk.Button(self, text=Md[0], width=5, height=2, bg=colorMd, font=10, borderwidth=3,
                           command=lambda text=Md: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorMd, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Md()])
        self.Md.grid(row=14, column=16)

        No = ('No', 'Nobelium', """'No nobelium nobelium metal\n'""", '102', '259.00')
        self.colorNo=colorNo="DarkGoldenrod4"
        self.No = tk.Button(self, text=No[0], width=5, height=2, bg=colorNo, font=10, borderwidth=3,
                           command=lambda text=No: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorNO, text[0], text[3], text[4]), self.voice(text[1]), self.compound_No()])
        self.No.grid(row=14, column=17)

        Lr = ('Lr', 'Lawrencium', """'Lr lawrencium lawrencium metal\n'""", '103', '262.00')
        self.colorLr=colorLr="cornSilk4"
        self.Lr = tk.Button(self, text=Lr[0], width=5, height=2, bg=colorLr, font=10, borderwidth=3,
                           command=lambda text=Lr: [self.arduino(text[0]), self.name(text[1]), self.info(text[2], text[0]), self.canva(colorLr, text[0], text[3], text[4]), self.voice(text[1]), self.compound_Lr()])
        self.Lr.grid(row=14, column=18)

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
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[1]), self.clearText(), self.reset()]).grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1

        close = [
            ('close', 'SERIAL COMMUNICATION', 'Now the ARDUINO SERIAL communication is CLOSED and trying to run THE PROGRAM after these is ERROR PRONE so please EXIT the program if it doesn\'t or RESTART it', 'PORT IS CLOSED')]
        r = 14
        c = 3
        for b in close: 
            tk.Button(self,
                      text=b[0],
                      width=5,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="black",
                      fg="white",
                      command=lambda text=b: [self.arduino(text[0]), self.name(text[0]), self.qmsg(text[2])]).grid(row=r, column=c)
            r += 1
            if r > 9: 
                r = 1
                c += 1


        #setting up the canvas big elements image
        self.canvas = Canvas(self, height=100, width=100, bg=self.colorH, relief=GROOVE, borderwidth=0.5)
        #canvas.pack()
        self.canvas.create_rectangle(100, 100, 0, 0)
        self.canvas.grid(row=1, column=0, rowspan=2)
        self.sy = self.canvas.create_text(50, 50, text="H", fill="black", font=('Helvetica 15 bold', 35))
        self.an = self.canvas.create_text(10, 12, text="1", fill="black", font=('Helvetica 15 bold', 10))
        self.am = self.canvas.create_text(17, 90, text="1.001", fill="black", font=('Helvetica 15 bold', 8))

        #self.turtle_B = Canvas(self, height=290, width=300, bg="bisque2", borderwidth=0.5)
        #self.turtle_B.grid(row=0, column=7, rowspan=6, columnspan=6)
        #this is for text
        #self.infoLine = tk.Label(self, text="", justify='left', font=10, bg=bacG)
        #self.infoLine.grid()
        #self.infoLine.grid(row=3, column=0, rowspan=7, columnspan=2)

        #**
        # on this code I changed from using Lable to Text
        # the reason is since the text is being long I should make it scrollable
        # and to do that, and Label fade out
        from tkinter import VERTICAL, Scrollbar, NS
        self.infoText = tk.Text(self, height=20, width=42)
        self.infoText.grid(row=3, column=0, rowspan=10, columnspan=1)
        self.scrolbar = Scrollbar(self, orient=VERTICAL)
        self.grid()
        self.infoText.config(yscrollcommand=self.scrolbar.set)
        self.scrolbar.config(command=self.infoText.yview)
        self.scrotext=""
        self.infoText.insert(END, self.scrotext)
        #**

        
        #This for the compounds to be form
        #And I'm thinking to make individual canvas for each elements that makes compounds
        #So I have to handle if the first canvas or the first elements is used using some conditional
        #Plus after one or elemets are selected I have to make some other compounds deactivate(that doesn't react)
        #Also when the second element is touched I have to make it light up like additional not just as elements individually(without the clear function())
        self.element_101 = Canvas(self, height=50, width=50, bg="white", relief=RIDGE, borderwidth=0)
        self.element_101.create_rectangle(50, 50, 0, 0)
        self.element_101.grid(row=3, column=5)
        self.sy_1 = self.element_101.create_text(25, 25, text="", fill="black", font=('Helvetica 15 bold', 20))
        self.an = self.element_101.create_text(5, 6, text="", fill="black", font=('Helvetica 15 bold', 6))
        self.am = self.element_101.create_text(8, 45, text="", fill="black", font=('Helvetica 15 bold', 5))
        self.touched_1 = False
        self.touch_count = 0
        
        self.element_102 = Canvas(self, height=50, width=50, bg="white", relief=RIDGE, borderwidth=0)
        self.element_102.create_rectangle(50, 50, 0, 0)
        self.element_102.grid(row=3, column=6)
        self.sy_1 = self.element_102.create_text(25, 25, text="", fill="black", font=('Helvetica 15 bold', 20))
        self.an = self.element_102.create_text(5, 6, text="", fill="black", font=('Helvetica 15 bold', 6))
        self.am = self.element_102.create_text(8, 45, text="", fill="black", font=('Helvetica 15 bold', 5))
        self.touched_2 = False

    def name(self, text): 
        self.topLabel.config(text=text)
        return(text)

    def white_f(self, xcept):
        # to make everything white
        coloId="white"
        coloFg="black"
        colod = [self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Fr, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Ra, self.Sc, self.Y, self.La, self.Ac, self.Ti, self.Zr, self.Hf, self.Rf, self.V, self.Nb, self.Ta, self.Db, self.Cr, self.Mo, self.W, self.Sg, self.Mn, self.Tc, self.Re, self.Bh, self.Fe, self.Ru, self.Os, self.Hs, self.Co, self.Rh, self.Ir, self.Mt, self.Ni, self.Pd, self.Pt, self.Ds, self.Cu, self.Ag, self.Au, self.Rg, self.Zn, self.Cd, self.Hg, self.Cn, self.B, self.Al, self.Ga, self.In, self.Tl, self.Nh, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.Fl, self.N, self.P, self.As, self.Sb, self.Bi, self.Mc, self.O, self.S, self.Se, self.Te, self.Po, self.Lv, self.F, self.Cl, self.Br, self.I, self.At, self.Ts, self.He, self.Ne, self.Ar, self.Xe, self.Rn, self.Og, self.Ce, self.Pr, self.Nd, self.Pm, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.Pa, self.U, self.Np, self.Pu, self.Am, self.Cm, self.Bk, self.Cf, self.Es, self.Kr, self.Fm, self.Md, self.No, self.Lr]
        for x in colod:
            if x not in xcept:
                x.config(bg=coloId)

    def compound_H(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U])

    def compound_Li(self):
        self.white_f([self.H, self.Li, self.K, self.Mg, self.Ti, self.Zr, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Fe, self.Co, self.Ni, self.Pd, self.Cu, self.Au, self.B, self.Al, self.Ga, self.C, self.Si, self.Sn, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Na(self):
        self.white_f([self.H, self.Na, self.K, self.Cs, self.Be, self.Mg, self.Ca, self.Ba, self.Ti, self.Zr, self.V, self.Nb, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Au, self.Hg, self.B, self.Al, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.U])

    def compound_K(self):
        self.white_f([self.K, self.Li, self.Na, self.H, self.Be, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.C, self.Si, self.Ge, self.Sn, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.U])

    def compound_Rb(self):
        self.white_f([self.H, self.Rb, self.V, self.Cr, self.B, self.Al, self.C, self.Ge, self.N, self.As, self.Sb, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Cs(self):
        self.white_f([self.H, self.Na, self.Cs, self.V, self.Cr, self.W, self.Mn, self.B, self.Al, self.C, self.Ge, self.N, self.As, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I])

    def compound_Fr(self):
        self.white_f([self.Fr])

    def compound_Be(self):
        self.white_f([self.H, self.Na, self.K, self.Be, self.Ti, self.V, self.Nb, self.B, self.Al, self.C, self.Si, self.N, self.P, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Mg(self):
        self.white_f([self.H, self.Li, self.Na, self.Mg, self.Ca, self.Ba, self.Ti, self.Zr, self.V, self.Cr, self.Mo, self.W, self.Mn, self.Fe, self.B, self.Al, self.C, self.Si, self.Ge, self.Sn, self.N, self.P, self.As, self.Sb, self.O, self.S, self.self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Ca(self):
        self.white_f([self.H, self.Na, self.Mg, self.Ca, self.Ba, self.Ti, self.Zr, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.B, self.Al, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.As, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Sr(self):
        self.white_f([self.H, self.Sr, self.Ba, self.Ti, self.Zr, self.Nb, self.Cr, self.Mo, self.W, self.Mn, self.Fe, self.B, self.Al, self.C, self.Si, self.N, self.P, self.As, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Ba(self):
        self.white_f([self.H, self.Na, self.Mg, self.Ca, self.Sr, self.Ba, self.Y, self.Ti, self.Zr, self.Nb, self.Cr, self.Mo, self.W, self.Mn, self.Fe, self.Pt, self.Cu, self.Hg, self.B, self.Al, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Ra(self):
        self.white_f([self.Ra, self.O, self.S])

    def compound_Sc(self):
        self.white_f([self.H, self.Sc, self.B, self.C, self.Si, self.N, self.Sb, self.O, self.S, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Y(self):
        self.white_f([self.H, self.Ba, self.Y, self.Zr, self.V, self.W, self.Fe, self.Cu, self.B, self.Al, self.C, self.Si, self.N, self.P, self.As, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I])

    def compound_La(self):
        self.white_f([self.H, self.Sr, self.La, self.B, self.Al, self.C, self.Si, self.N, self.P, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I])

    def compound_Ac(self):
        self.white_f([self.Ac])

    def compound_Ti(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Ti, self.Zr, self.Hf, self.Mn, self.Fe, self.Co, self.Ni, self.Cu, self.Zn, self.Cd, self.B, self.Al, self.C, self.Si, self.Pb, self.N, self.P, self.Bi, self.O, self.S, self.F, self.Cl, self.Br, self.I])

    def compound_Zr(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Mg, self.Ca, self.Sr, self.Ba, self.Y, self.Ti, self.Zr, self.W, self.Ni, self.Cd, self.B, self.Al, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.Bi, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.Ce])

    def compound_Hf(self):
        self.white_f([self.H, self.K, self.Ti, self.Hf, self.B, self.C, self.Si, self.N, self.P, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Rf(self):
        self.white_f([self.Rf])

    def compound_V(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Y, self.V, self.Mn, self.Fe, self.Cu, self.Ag, self.Hg, self.B, self.C, self.Si, self.Pb, self.N, self.P, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Ce])

    def compound_Nb(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Be, self.Sr, self.Ba, self.Nb, self.Cu, self.Zn, self.Cd, self.B, self.C, self.Si, self.Pb, self.N, self.P, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Ta(self):
        self.white_f([self.H, self.Li, self.K, self.Ta, self.Fe, self.B, self.Al, self.C, self.Si, self.Pb, self.N, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Db(self):
        self.white_f([self.Db])

    def compound_Cr(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Mg, self.Ca, self.Sr, self.Ba, self.Cr, self.Fe, self.Co, self.Ni, self.Cu, self.Ag, self.Zn, self.Cd, self.Hg, self.B, self.Tl, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Mo(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Mg, self.Ca, self.Sr, self.Ba, self.Mo, self.Mn, self.Fe, self.Co, self.Ni, self.Cu, self.Ag, self.Zn, self.Cd, self.B, self.Tl, self.C, self.Si, self.Pb, self.N, self.P, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    # no comma after this:(
    def compound_W(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Cs, self.Mg, self.Ca, self.Sr, self.Ba, self.Y, self.Zr, self.W, self.Mn, self.Fe, self.Co, self.Cu, self.Ag, self.Cd, self.Hg, self.B, self.C, self.Si, self.Pb, self.N, self.P, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Ce])

    def compound_Sg(Self):
        self.white_f([self.Sg])

    def compound_Mn(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Cs, self.Mg, self.Ca, self.Sr, self.Ba, self.Ti, self.V, self.Mo, self.W, self.Mn, self.Ag, self.Zn, self.B, self.C, self.Si, self.N, self.P, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Tc(self):
        self.white_f([self.H, self.Tc, self.C, self.N, self.O, self.S, self.F])

    def compound_Re(self):
        self.white_f([self.H, self.Na, self.K, self.Ca, self.Re, self.Ag, self.Tl, self.C, self.Si, self.N, self.P, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Bh(self):
        self.white_f([self.Bh])

    def compound_Fe(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Mg, self.Ca, self.Sr, self.Ba, self.Y, self.Ti, self.V, self.Ta, self.Cr, self.Mo, self.W, self.Fe, self.Ru, self.Co, self.Rh, self.Ni, self.Pd, self.Cu, self.Zn, self.B, self.Al, self.C, self.Si, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Ru(self):
        self.white_f([self.H, self.K, self.Fe, self.Ru, self.C, self.N, self.P, self.O, self.F, self.Cl, self.Br, self.I, self.Xe])

    def compound_Os(self):
        self.white_f([self.H, self.Na, self.K, self.Os, self.C, self.N, self.O, self.S, self.F, self.Cl, self.Br])

    def compound_Hs(self):
        self.white_f([self.Hs])

    def compound_Co(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Ti, self.Cr, self.Mo, self.W, self.Fe, self.Co, self.Ni, self.Pd, self.B, self.Al, self.C, self.Si, self.Sn, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Sm])

    def compound_Rh(self):
        self.white_f([self.H, self.Na, self.K, self.Fe, self.Rh, self.Pt, self.B, self.C, self.N, self.P, self.O, self.S, self.F, self.Cl, self.Br, self.I])

    def compound_Ir(self):
        self.white_f([self.H, self.Na, self.K, self.Ir, self.C, self.N, self.P, self.O, self.S, self.F, self.Cl, self.Br, self.I])

    def compound_Mt(self):
        self.white_f([self.Mt])

    def compound_Ni(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Ti, self.Zr, self.Cr, self.Mo, self.Fe, self.Co, self.Ni, self.Cu, self.B, self.Al, self.C, self.Sn, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Pd(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Fe, self.Co, self.Pd, self.B, self.C, self.N, self.P, self.O, self.S, self.F, self.Cl, self.Br, self.I])

    def compound_Pt(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Ba, self.Rh, self.Pt, self.C, self.Si, self.N, self.P, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Ds(self):
        self.white_f([self.Ds])

    def compound_Cu(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Ba, self.Y, self.Ti, self.V, self.Nb, self.Cr, self.Mo, self.W, self.Fe, self.Ni, self.Cu, self.Zn, self.Hg, self.B, self.Al, self.C, self.Si, self.Sn, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Ag(self):
        self.white_f([self.H, self.K, self.V, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Ag, self.Hg, self.B, self.C, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Au(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Au, self.Cd, self.B, self.C, self.N, self.P, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Rg(self):
        self.white_f([self.Rg])

    def compound_Zn(self):
        self.white_f([self.H, self.K, self.Ti, self.Nb, self.Cr, self.Mo, self.Mn, self.Fe, self.Cu, self.Zn, self.Cd, self.B, self.Al, self.C, self.Si, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_cd(self):
        self.white_f([self.H, self.K, self.Ti, self.Zr, self.Nb, self.Cr, self.Mo, self.W, self.Au, self.Zn, self.Cd, self.B, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Hg(self):
        self.white_f([self.H, self.Na, self.K, self.Ba, self.V, self.Cr, self.W, self.Co, self.Cu, self.Ag, self.Hg, self.C, self.Si, self.N, self.P, self.As, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Cn(self):
        self.white_f([self.Cn])

    def compound_B(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Fe, self.Co, self.Rh, self.Ni, self.Pd, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.B, self.Al, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.As, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Dy, self.Er, self.Lu, self.Th, self.U])

    def compound_Al(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Y, self.Ti, self.Zr, self.Ta, self.Fe, self.Co, self.Ni, self.Cu, self.Zn, self.B, self.Al, self.C, self.Si, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Th])

    def compound_Ga(self):
        self.white_f([self.H, self.Li, self.Ga, self.C, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Gd])

    def compound_In(self):
        self.white_f([self.H, self.In, self.C, self.Sn, self.N, self.P, self.As, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Tl(self):
        self.white_f([self.Cr, self.Mo, self.Re, self.Tl, self.C, self.N, self.P, self.As, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I])

    def compound_Nh(self):
        self.white_f([self.Nh])

    def compound_C(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U])

    def compound_Si(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.Co, self.Pt, self.Cu, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Th, self.U])

    def compound_Ge(self):
        self.white_f([self.H, self.Na, self.K, self.Rb, self.Cs, self.Mg, self.Ba, self.C, self.Si, self.Ge, self.N, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Sn(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Mg, self.Ca, self.Ba, self.Zr, self.Cr, self.Co, self.Ni, selfCu, self.Cd, self.B, self.In, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Pb(self):
        self.white_f([self.H, self.Na, self.Ca, self.Ba, self.Ti, self.Zr, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Cd, self.B, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Fl(self):
        self.white_f([self.Fl])

    def compound_N(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U, self.Pu])

    def compound_P(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.Ru, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I, self.La, self.Pr, self.Nd, self.Sm, self.Eu, self.Ho, self.Er, self.U])

    def compound_As(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Mg, self.Ca, self.Sr, self.Y, self.Cr, self.Fe, self.Co, self.Ni, self.Cu, self.Ag, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Xe])

    def compound_Sb(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Mg, self.Ba, self.Y, self.Cr, self.Mn, self.Fe, self.Co, self.Ni, self.Cu, self.Ag, self.Zn, self.Cd, self.Al, self.Ga, self.In, self.C, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Kr, self.Xe, self.La, self.Nd, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu])

    def compound_Bi(self):
        self.white_f([self.H, self.Na, self.Ba, self.Ti, self.Zr, self.V, self.Cr, self.Mo, self.Cd, self.Al, self.C, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I, self.Th])

    def compound_Mc(self):
        self.white_f([self.Mc])

    def compound_O(self):
        self.white_f([self.H, self.Li, self.Ra, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U, self.Pu, self.Po, self.Np, self.Am])

    #comman after this
    def compound_S(self):
        self.white_f([self.H, self.Li, self.Ra, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.s, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U])

    def compound_Se(self):
        self.white_f([self.H, self.Li, self.Ra, self.Na, self.K, self.Rb, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.Co, self.Ni, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I, self.Ce, self.Eu, self.Gd, self.Th, self.U])

    def compound_Te(self):
        self.white_f([self.H, self.Na, self.K, self.Be, self.Ca, self.Ba, self.Sc, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.Co, self.Cu, self.Ag, self.Zn, self.Cd, self.Hg, self.Ga, self.In, self.C, self.Ge, self.Sn, self.Pb, self.N, self.As, self.Sb, self.O, self.S, self.Te, self.F, self.Cl, self.Br, self.I, self.Pr, self.Nd, self.Sm, self.Eu, self.Gd, self.Dy, self.Er, self.Lu, self.Th, self.U])

    def compound_Po(self):
        self.white_f([self.O, self.Po, self.Cl])

    def compound_Lv(self):
        self.white_f([self.Lv])

    def compound_F(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Kr, self.Xe, self.La, self.Ce, self.Pr, self.Nd, self.Pm, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U, self.Pu, self.Am])

    def compound_Cl(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Kr, self.Xe, self.La, self.Ce, self.Pr, self.Nd, self.Pm, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U, self.Pu, self.Am, self.Pa])

    def compound_Br(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.Ru, self.Os, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Pm, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U, self.Pu, self.Am])

    def compound_I(self):
        self.white_f([self.H, self.Li, self.Na, self.K, self.Rb, self.Cs, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Sc, self.Y, self.Ti, self.Zr, self.Hf, self.V, self.Nb, self.Ta, self.Cr, self.Mo, self.W, self.Mn, self.Tc, self.Re, self.Fe, self.Ru, self.Co, self.Rh, self.Ir, self.Ni, self.Pd, self.Pt, self.Cu, self.Ag, self.Au, self.Zn, self.Cd, self.Hg, self.B, self.Al, self.Ga, self.In, self.Tl, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.N, self.P, self.As, self.Sb, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.La, self.Ce, self.Pr, self.Nd, self.Pm, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.U, self.Pu, self.Am])

    def compound_He(self):
        self.white_f([self.He])

    def compound_Ne(self):
        self.white_f([self.Ne])

    def compound_Ar(self):
        self.white_f([self.Ar])

    def compound_Kr(self):
        self.white_f([self.Sb, self.F, self.Kr])

    def compound_Xe(self):
        self.white_f([self.Ru, self.As, self.Sb, self.O, self.F, self.Xe])

    def compound_Rn(self):
        self.white_f([self.Rn])

    def compound_Og(self):
        self.white_f([self.Og])

    def compound_Ce(self):
        self.white_f([self.H, self.Zr, self.V, self.W, self.B, self.Al, self.C, self.Si, self.N, self.O, self.S, self.Se, self.F, self.Cl, self.Br, self.I, self.Ce])

    def compound_Pr(self):
        self.white_f([self.H, self.B, self.C, self.Si, self.N, self.P, self.O, self.S, self.Te, self.F, self.Cl, self.Br, self.I, self.Pr])

    def compound_Nd(self):
        self.white_f([self.H, self.B, self.C, self.Si, self.N, self.P, self.Sb, self.O, self.S, self.Te, self.F, self.Cl, self.Br, self.I])

    def compound_Pm(self):
        self.white_f([self.Pm, self.F, self.Cl, self.Br, self.I])

    def compound_Sm(self):
        self.white_f([self.H, self.Co, self.B, self.C, self.Si, self.N, self.P, self.O, self.S, self.Te, self.F, self.Cl, self.Br, self.I, self.Sm])

    def compound_Eu(self):
        self.white_f([self.H, self.B, self.C, self.Si, self.N, self.P, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Eu])

    def compound_Gd(self):
        self.white_f([self.H, self.B, self.Ga, self.C, self.Si, self.N, self.Sb, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Gd])

    def compound_Tb(self):
        self.white_f([self.H, self.C, self.Si, self.N, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.Tb])

    def compound_Dy(self):
        self.white_f([self.H, self.C, self.B, self.Si, self.N, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.Sb, self.Te, self.Dy])

    def compound_Ho(self):
        self.white_f([self.H, self.C, self.Si, self.N, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.P, self.Ho])

    def compound_Er(self):
        self.white_f([self.H, self.C, self.B, self.Si, self.N, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.Sb, self.Te, self.P, self.Er])

    def compound_Tm(self):
        self.white_f([self.H, self.C, self.Si, self.N, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.Tb])

    def compound_Yb(self):
        self.white_f([self.H, self.C, self.Si, self.N, self.Sb, self.O, self.S, self.F, self.Cl, self.Br, self.I, self.Yb])

    def compound_Lu(self):
        self.white_f([self.H, self.B, self.C, self.Si, self.N, self.Sb, self.O, self.S, self.Te, self.Lu, self.F, self.Cl, self.Br, self.I])

    def compound_Th(self):
        self.white_f([self.H, self.B, self.Al, self.C, self.Si, self.N, self.Bi, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.Th])

    def compound_Pa(self):
        self.white_f([self.Pa, self.Cl])

    def compound_U(self):
        self.white_f([self.Na, self.K, self.B, self.C, self.Si, self.N, self.P, self.O, self.S, self.Se, self.Te, self.F, self.Cl, self.Br, self.I, self.U])

    def compound_Np(self):
        self.white_f([self.O, self.Np])

    def compound_Pu(self):
        self.white_f([self.N, self.O, self.F, self.Cl, self.Br, self.I, self.Pu])

    def compound_Am(self):
        self.white_f([self.O, self.F, self.Cl, self.Br, self.I, self.Am])

    def compound_Cm(self):
        self.white_f([self.Cm])

    def compound_Bk(self):
        self.white_f([self.Bk])

    def compound_Cf(self):
        self.white_f([self.Cf])

    def compound_Es(self):
        self.white_f([self.Es])

    def compound_Fm(self):
        self.white_f([self.Fm])

    def compound_Md(self):
        self.white_f([self.Md])

    def compound_No(self):
        self.white_f([self.No])

    def compound_Lf(self):
        self.white_f([self.Lr])


    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, text, symbol):
        if self.touch_count < 1:
            txt = text.replace('\'', "")
            #self.infoLine.config(text=txt)
            self.infoText.config(state=NORMAL)
            self.scrotext = txt
            self.infoText.insert(END, self.scrotext)
            self.infoText.config(state=DISABLED)
            self.first_element = symbol
            #=================================color_change========================#
            #new = []
            #second = []
            #for n in new:
            #    sep = n.split(' ')
            #    second.append(sep[0].replace(symbol, ""))
            #from string import digits
            #colored = []
            #remove_digits = str.maketrans('', '', digits)
            #for sec in second:
            #    colored.append(sec.translate(remove_digits))
            #for key in colored:
            #    self.white_f()
            #    self.alkaline_c[key].config(bg=coloFu)
            #return(txt)
        if self.touch_count >= 1:
            self.infoText.config(state=NORMAL)
            txt = text.split('\'\'')
            new = []
            for n in txt:
                new.append(n.strip('\''))
            compound_found = []
            compound_str = ""
            for n in new:
                sep = n.split(' ')
                if self.first_element in sep[0]:
                    compound_found.append(n)
            if len(compound_found) == 0:
                self.infoText.delete("1.0", "end")
                self.scrotext = "Not found"
                self.infoText.insert(END, self.scrotext)
                self.infoText.config(state=DISABLED)
            else:
                for x in compound_found:
                    compound_str = compound_str + x
                    compound_str = compound_str + '\n'
                self.scrotext = compound_str[:-2]
                self.infoText.delete("1.0", "end")
                self.infoText.insert(END, self.scrotext)
                self.infoText.config(state=DISABLED)

        
    # sends command to the arduino
    def arduino(self, text):
        if text =="close":
            user_input = "clear"
            byte_msg = user_input.encode('utf-8')
            time.sleep(0.1)
            nano.write(byte_msg)
            nano.close()
        else:
            time.sleep(0.1)
            byte_msg = text.encode('utf-8')
            nano.write(byte_msg)
        time.sleep(2)

    beSound = True
    # voice description
    def voice(self, text):
        if self.beSound:
            engine.say(text)
            engine.runAndWait()

    def canva(self, color, symbol, An, Am):
        self.canvas.config(bg=color)
        self.canvas.itemconfig(self.sy, text=symbol)
        self.canvas.itemconfig(self.an, text=An)
        self.canvas.itemconfig(self.am, text=Am)
        self.touch_count += 1

        if not self.touched_1:
            self.element_101.config(bg=color)
            self.element_101.itemconfig(self.sy, text=symbol)
            self.element_101.itemconfig(self.an, text=An)
            self.element_101.itemconfig(self.am, text=Am)
            self.touched_1 = True
            
        if not self.touched_2 and self.touch_count > 1:
            self.element_102.config(bg=color)
            self.element_102.itemconfig(self.sy, text=symbol)
            self.element_102.itemconfig(self.an, text=An)
            self.element_102.itemconfig(self.am, text=Am)
            self.touched_2 = True

    def reset(self):
        self.touched_1 = False
        self.touch_count = 0
        self.touched_2 = False
        self.element_101.config(bg="White")
        self.element_101.itemconfig(self.sy, text="")
        self.element_101.itemconfig(self.an, text="")
        self.element_101.itemconfig(self.am, text="")
        
        self.element_102.config(bg="White")
        self.element_102.itemconfig(self.sy, text="")
        self.element_102.itemconfig(self.an, text="")
        self.element_102.itemconfig(self.am, text="")

    def clearText(self):
        self.infoText.config(state=NORMAL)
        self.infoText.delete("1.0", "end")
        coloId="white"
        self.infoText.config(state=DISABLED)
        colod = [self.H, self.Li, self.Na, self.K, self.Rb, self.Rh, self.Kr, self.Cs, self.Fr, self.Be, self.Mg, self.Ca, self.Sr, self.Ba, self.Ra, self.Sc, self.Y, self.La, self.Ac, self.Ti, self.Zr, self.Hf, self.Rf, self.V, self.Nb, self.Ta, self.Db, self.Cr, self.Mo, self.W, self.Sg, self.Mn, self.Tc, self.Re, self.Bh, self.Fe, self.Ru, self.Os, self.Hs, self.Co, self.Ir, self.Mt, self.Ni, self.Pd, self.Pt, self.Ds, self.Cu, self.Ag, self.Au, self.Rg, self.Zn, self.Cd, self.Hg, self.Cn, self.B, self.Al, self.Ga, self.In, self.Tl, self.Nh, self.C, self.Si, self.Ge, self.Sn, self.Pb, self.Fl, self.N, self.P, self.As, self.Sb, self.Bi, self.Mc, self.O, self.S, self.Se, self.Te, self.Po, self.Lv, self.F, self.Cl, self.Br, self.I, self.At, self.Ts, self.He, self.Ne, self.Ar, self.Xe, self.Rn, self.Og, self.Ce, self.Pr, self.Nd, self.Pm, self.Sm, self.Eu, self.Gd, self.Tb, self.Dy, self.Ho, self.Er, self.Tm, self.Yb, self.Lu, self.Th, self.Pa, self.U, self.Np, self.Pu, self.Am, self.Cm, self.Bk, self.Cf, self.Es, self.Fm, self.Md, self.No, self.Lr]
        for x in colod:
            x.config(bg=coloId)
        coloc = [self.colorH, self.colorLi, self.colorNa, self.colorK, self.colorRb, self.colorRh, self.colorKr, self.colorCs, self.colorFr, self.colorBe, self.colorMg, self.colorCa, self.colorSr, self.colorBa, self.colorRa, self.colorSc, self.colorY, self.colorLa, self.colorAc, self.colorTi, self.colorZr, self.colorHf, self.colorRf, self.colorV, self.colorNb, self.colorTa, self.colorDb, self.colorCr, self.colorMo, self.colorW, self.colorSg, self.colorMn, self.colorTc, self.colorRe, self.colorBh, self.colorFe, self.colorRu, self.colorOs, self.colorHs, self.colorCo, self.colorIr, self.colorMt, self.colorNi, self.colorPd, self.colorPt, self.colorDs, self.colorCu, self.colorAg, self.colorAu, self.colorRg, self.colorZn, self.colorCd, self.colorHg, self.colorCn, self.colorB, self.colorAl, self.colorGa, self.colorIn, self.colorTl, self.colorNh, self.colorC, self.colorSi, self.colorGe, self.colorSn, self.colorPb, self.colorFl, self.colorN, self.colorP, self.colorAs, self.colorSb, self.colorBi, self.colorMc, self.colorO, self.colorS, self.colorSe, self.colorTe, self.colorPo, self.colorLv, self.colorF, self.colorCl, self.colorBr, self.colorI, self.colorAt, self.colorTs, self.colorHe, self.colorNe, self.colorAr, self.colorXe, self.colorRn, self.colorOg, self.colorCe, self.colorPr, self.colorNd, self.colorPm, self.colorSm, self.colorEu, self.colorGd, self.colorTb, self.colorDy, self.colorHo, self.colorEr, self.colorTm, self.colorYb, self.colorLu, self.colorTh, self.colorPa, self.colorU, self.colorNp, self.colorPu, self.colorAm, self.colorCm, self.colorBk, self.colorCf, self.colorEs, self.colorFm, self.colorMd, self.colorNo, self.colorLr]
        for (x, y) in zip(colod, coloc):
            x.config(bg=y)


# This class is going to be used to define buttons like for basicCompounds, composition, Discovery, Animations and most probaly
#  will not contain periodic taclass Four(tk.Frame):
class Four(tk.Frame):
    """=======================================blocks==================================="""
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.topLabel = tk.Label(self, text="Others", font=('Helvetica 15 bold', 15), justify="center")
        self.topLabel.grid(row=0, column=0, columnspan=10)
        """=======================================Basic comounds======================================="""
        basic_commpounds = [
            ('Glucose', 'Glucose C6H12O6', 'C6H12O6', 'Blood sugar, or glucose, is the main sugar found in your blood.\nIt comes from the food you eat, and is your body\'s main source of energy.\nYour blood carries glucose to all of your body\'s cells to use for energy.'),
            ('Water', 'Water H2O', 'H2O', 'Water is an inorganic, transparent, tasteless, odorless, and nearly \ncolorless chemical substance, which is the main constituent of Earth\'s hydrosphere \nand the fluids of all known living organisms'),
            ('Carbon dioxide', 'Carbon dioxide CO2', 'CO2', 'Carbon dioxide is a colorless and non-flammable gas at normal temperature\nand pressure. Although much less abundant than nitrogen and oxygen in Earth\'s \natmosphere, carbon dioxide is an important constituent of our planet\'s air'),
            ('Baking soda', 'Baking soda NaHCO3', 'NaHCO3', 'Sodium bicarbonate is a white solid that is crystalline,\nbut often appears as a fine powder. It has a slightly salty, alkaline taste resembling \nthat of washing soda (sodium carbonate).'),
            ('Sodium Chloride', 'Sodium Chloride NaCl', 'NaCl', 'Sodium chloride is the chemical name for salt.\nSodium is an electrolyte that regulates the amount of water in your body. \nSodium also plays a part in nerve impulses and muscle contractions.'),
            ('Silicon Dioxide', 'Silicon Dioxide SiO2', 'SiO2', 'Silicon dioxide, also known as silica, is an oxide of silicon with\nthe chemical formula SiO2, most commonly found in nature as \nquartz and in various living organisms.In many parts of the world, \nsilica is the major constituent of sand.'),
            ('Hydrochloric Acid', 'Hydrochloric Acid HCl', 'HCl', 'Hydrochloric acid, solution is a colorless watery liquid \nwith a sharp, irritating odor. Consists of hydrogen chloride, \na gas, dissolved in water. Sinks and mixes with water. \nProduces irritating vapor.'),
            ('Lithium Hydroxide', 'Lithium Hydroxide LiOH', 'LiOH', 'Lithium hydroxide (LiOH), commonly obtained by the reaction of\nlithium carbonate with lime, is used in making lithium \nsalts (soaps) of stearic and other fatty acids; \nthese soaps are widely used as thickeners in lubricating greases'),
            ('Methane', 'Methane CH4', 'CH4', 'Methane is gas that is found in small quantities in the atmosphere. \nMethane is the simplest hydrocarbon, consisting of one carbon atom and\nfour hydrogen atoms. Methane is a powerful greenhouse gas.'),
            ('Ammonia', 'Ammonia NH3', 'NH3', 'ammonia (NH3), colourless, pungent gas composed of nitrogen and hydrogen. \nIt is the simplest stable compound of these elements and serves as a starting \nmaterial for the production of many commercially important nitrogen compounds.'),
            ('Sulfuric Acid', 'Sulfuric Acid H2S04', 'H2SO4', 'sulfuric also spelled sulphuric (H2SO4), also called oil of vitriol, \nor hydrogen sulfate, dense, colourless, oily, corrosive liquid; one of the most \ncommercially important of all chemicals.'),
            ('Citric Acid', 'Citric Acid C6H8O7', 'C6H8O7', 'Citric acid is an organic compound with the chemical formula HOC(CO2H)(CH2CO2H)2.\nIt is a colorless weak organic acid.It occurs naturally in citrus fruits. \nIn biochemistry, it is an intermediate in the citric acid cycle, which occurs in \nthe metabolism of all aerobic organisms.'),
            ('Hydrogen Peroxide', 'Hydrogen Peroxide H2O2', 'H2O2', 'Hydrogen peroxide is a chemical compound with the formula H2O2. \nIn its pure form, it is a very pale blue liquid, slightly more viscous \nthan water. It is used as an oxidizer, bleaching agent, and antiseptic, \nusually as a dilute solution (3–6% by weight) in water for consumer use, \nand in higher concentrations for industrial use'),
            ('Acetic Acid', 'Acetic Acid C2H4O2', 'C2H4O2', 'Acetic acid is also known as ethanoic acid, ethylic acid, vinegar acid, \nand methane carboxylic acid; it has the chemical formula of CH3COOH. \nAcetic acid is a byproduct of fermentation, and gives vinegar its characteristic odor. \nVinegar is about 4-6% acetic acid in water. More concentrated solutions can be found \nin laboratory use, and pure acetic acid containing only \ntraces of water is known as glacial acetic acid'),
            ('Calcium Carbonate', 'Calcium Carbonate CaCO3', 'CaCO3', 'Calcium carbonate is a dietary supplement used when the amount of calcium taken in \nthe diet is not enough. Calcium is needed by the body for healthy bones, \nmuscles, nervous system, and heart. Calcium carbonate also is used as an \nantacid to relieve heartburn, acid indigestion, and upset stomach.'),
            ('Iron Oxide', 'Iron Oxide Fe2O3', 'Fe2O3', 'Iron oxides are chemical compounds composed of iron and oxygen. \nThere are sixteen known iron oxides and oxyhydroxides, the best known of \nwhich is rust, a form of iron(III) oxide.Iron oxides and oxyhydroxides are \nwidespread in nature and play an important role in many geological \nand biological processes.')]
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
                      bg="light cyan",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.voice(text[0]), self.canv_img(text[2]), self.description(text[3])])
            self.basic_commpounds_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2

        """=======================================Compositions======================================="""
        composition = [
            ('Human', 'Elements Composition\n in human body', 'human', 'Elements Composition in human body', 'Almost 99% of the mass of the human body is made up of \nsix elements: oxygen, carbon, hydrogen, nitrogen, calcium, and phosphorus. \nOnly about 0.85% is composed of another five elements: potassium, sulfur, \nsodium, chlorine, and magnesium. All 11 are necessary for life.'),
            ('Plant', 'Elements Composition\n in plants', 'plant', 'Elements Composition in plants', 'Plants are composed of water, carbon-containing organics, and non-carbon-containing \ninorganic substances such as potassium and nitrogen.'),
            ('Solar', 'Elements Composition\n in the solar system', 'solar', 'Elements Composition in the solar system', 'The solar system consists of the sun, the eight planets and \nseveral other miscellaneous objects, such as comets, asteroids and \ndwarf planets. The most abundant elements among these objects are hydrogen \nand helium, primarily because the sun and the four largest planets \nare predominantly made up of these two elements.'),
            ('Atmosphere', 'Elements Composition\n in the Atmosphere', 'atm', 'Elements Composition in the Atmosphere', 'The vast majority of the atmosphere is made up of nitrogen (78%) and oxygen (21%).\n The rest of the gases combined only account for about 1% of the atmosphere. \nAlong with all of these different gases, the atmosphere also holds many tiny, \nfloating particles and droplets of liquid that scientists collectively call aerosols'),
            ('Earth Crust', 'Elements Composition\n in the earth crust', 'crust', 'Elements Composition in the earth crust', '98.4% of the Earth\'s crust consists of oxygen, silicon, aluminum, iron, calcium, \nsodium, potassium, and magnesium. All other elements account for approximately \n1.6% of the volume of the Earth\'s crust.'),
            ('Ocean', 'Elements Composition\n in the Ocean', 'ocean', 'Elements Composition in the Ocean', 'The six most abundant ions of seawater are chloride (Cl−), sodium (Na+), \nsulfate (SO24−), magnesium (Mg2+), calcium (Ca2+), and potassium (K+). By weight \nthese ions make up about 99 percent of all sea salts.'),
            ('Universe', 'Elements Composition\n in the universe', 'universe', 'Elements Composition in the universe', 'The chemical composition of the Universe is dominated by the hydrogen and \nhelium produced in the Big Bang. The remaining 90 or so chemical elements are \nproduced in stars and constitute only a few percent of the overall mass.')]
        r = 1
        c = 9
        self.composition_c={}
        for b in composition: 
            self.composition_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=14,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="green2",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.voice(text[3]), self.canv_img(text[2]), self.description(text[4])])
            self.composition_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2
        """=======================================Discovered======================================="""
        Discovery = [
            ('Early', 'Early discovered elements', 'Early', '', 'white'),
            ('Eighteen', 'Elements discovered in Eighteen century', 'Eighteen', '', 'white'),
            ('Nineteen', 'Elements discovered in Nineteen century', 'Nineteen', '', 'white'),
            ('Twenty', 'Elements discovered in Twenty century', 'Twenty', '', 'white'),
            ('Twenty one', 'Elements discovered in Twenty one century', 'Twentyone', '', 'white')]
        r = 1
        c = 12
        self.Discovery_c={}
        for b in Discovery: 
            self.Discovery_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=14,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="LightBlue2",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.voice(text[1]), self.description(text[3]), self.canv_img(text[4])])
            self.Discovery_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2

        """=======================================Animation======================================="""
        Animation = [
            ('TimeLine', 'Timeline Animation', 'Timeline', '', 'white'),
            ('Group Animation', 'Group Animation', 'columndance', '', 'white'),
            ('Column Animation', 'Column Animation', 'groupdance', '', 'white')]
        r = 1
        c = 15
        self.Animation_c={}
        for b in Animation: 
            self.Animation_c[b[0]]=tk.Button(self,
                      text=b[0],
                      width=14,
                      height=2,
                      font=10,
                      borderwidth = 3,
                      bg="gold3",
                      command=lambda text=b: [self.arduino(text[2]), self.name(text[0]) + self.info(text[1]), self.description(text[3]), self.canv_img(text[4])])
            self.Animation_c[b[0]].grid(row=r, column=c, columnspan=2)
            r += 1
            if r > 8: 
                r = 1
                c += 2

        self.cmpund = tk.Label(self, text=" ")
        self.cmpund.grid(row=1, column=8)
        self.compo = tk.Label(self, text=" ")
        self.compo.grid(row=1, column=11)
        self.disco = tk.Label(self, text=" ")
        self.disco.grid(row=1, column=14)
        self.filine = tk.Label(self, text="               ")
        self.filine.grid(row=1, column=0, columnspan=2)
        self.infoLine = tk.Label(self, text="Basic commpounds", justify='left', font=10)
        self.infoLine.grid(row=1, column=17, rowspan=2, columnspan=2)
        self.descr = tk.Label(self, text=" ", font=10)
        self.descr.grid(row=3, column=17, rowspan=3)
        #setting up voice


    def name(self, text): 
        self.topLabel.config(text=text)
        return(text)

    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, text): 
        self.infoLine.config(text=text)
        return(text)

    # description
    def description(self, text):
        self.descr.config(text=text)
        return(text)
        
    # Canva image
    def canv_img(self, text):
        self.canvv = Canvas(self, width=200, height=200)
        self.img = (Image.open("IMG/{}.png".format(text)))
        self.resized = self.img.resize((195, 195), Image.ANTIALIAS)
        self.neww_img = ImageTk.PhotoImage(self.resized)
        self.canvv.create_image(10, 10, anchor=NW, image=self.neww_img)
        self.canvv.grid(row=7, column=17, rowspan=8, columnspan=7)

    # sends command to the arduino
    def arduino(self, text):
        if text =="close":
            user_input = "clear"
            byte_msg = user_input.encode('utf-8')
            time.sleep(0.1)
            nano.write(byte_msg)
            nano.close()
        else:
            time.sleep(0.1)
            byte_msg = text.encode('utf-8')
            nano.write(byte_msg)
        time.sleep(2)
        
    beSound = True
    # voice description
    def voice(self, text):
        if self.beSound:
            engine.say(text)
            engine.runAndWait()


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
    a = App(root, bg=bacG)
    tabControl.add(a, text="Properties")

    b = Second(root, bg=bacG_2)
    tabControl.add(b, text="Electrons")

    c = Third(root, bg=bacG_3)
    tabControl.add(c, text="Compounds")

    d = Four(root, bg=bacG_4)
    tabControl.add(d, text="Others")

    tabControl.pack(expand=1, fill="both")

    #root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='Prime.jpg'))

    root.mainloop()


def hellp():
    # function to give help
    hell = tk.Tk()
    hell.title("Help")
    #hell.geometry("250x150")
    hell.resizable(False, False)
    l = ttk.Label(hell, text="Help", font=("Courier", 14))
    x = ttk.Label(hell, text="""This GUI is developed to control interactie periodic table\n To control the interactive periodic table using this software first connect \nyour arduino usng the USB then initiate the software \nwhich will configure the port and baud rate automatically\nThen you can begun the teaching and learning process\n\nIf the software stacks or the LEDs start to lights up\nrandomly restart the software and also don't forget \nto restart the periodic table by unplugging and plugging \nagain before restarting the Software\n   For more help you can contact us using this email\n\teyasuhailegbr@gmail.com""")
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
    aboo.maxsize(400, 200)
    aboo.resizable(False, False)
    l = ttk.Label(aboo, text="About", font=("Courier", 14))
    from tkhtmlview import HTMLLabel
    x = HTMLLabel(aboo, html='This product is desigend, built and deliverd by team of<br><a href="https://t.me/BetMesfin">Betlehem Mesfin</a><br><a href="https://t.me/Eyasuha">Eyasu Hailegbriel</a><br><a href="https://t.me/Samuuel">Samuel Gashaw')
    x.config(font=('Helvetica 15 bold', 13))
    b = tk.Button(aboo, text="Exit",
               command = aboo.destroy)
    l.pack()
    x.pack()
    b.pack()
    pass

def settup(baud, port, voice):
    if voice == "Male":
        voicce = 1
        engine.setProperty("voice", voices[voicce].id)
        App.beSound = True
        Second.beSound = True
        Third.beSound = True
        Four.beSound = True
        
    elif voice == "Female":
        voicce = 0
        engine.setProperty("voice", voices[voicce].id)
        App.beSound = True
        Second.beSound = True
        Third.beSound = True
        Four.beSound = True
        
    elif voice == "Mute":
        App.beSound = False
        Second.beSound = False
        Third.beSound = False
        Four.beSound = False
        
    BBaud = int(re.search(r'\d+', baud).group())
    PPort = port
    rot = tk.Tk()
    rot.overrideredirect(1)
    rot.withdraw()
    msg.showinfo(title="Setup Done", message="The baud rate is configured to {}, And the port is configured to {}, And the voice is configured to {}".format(baud, port, voice))
    #print("The baud rate is {}, And the port {}, And the voice is {}".format(baud, port, voice))
    

def settting():
    # description on setting
    settt = tk.Tk()
    settt.title("Setting")
    settt.resizable(False, False)
    
    mig = ttk.LabelFrame(settt, text="Setting")
    mig.grid(column=0, row=0, padx=9, pady=9, sticky='W')
    baud_text = ttk.Label(mig, text="Select Baud rate")
    baud_text.grid(column=0, row=0)
    port_text = ttk.Label(mig, text="Select Port")
    port_text.grid(column=1, row=0)
    voice_text = ttk.Label(mig, text="Select Voice")
    voice_text.grid(column=2, row=0)

    baud = tk.StringVar()
    nm = ttk.Combobox(mig, width=19, textvariable=baud, state='disabled')
    nm["values"] = ("9600 baud", "19200 baud", "38400 baud", "57600 baud")
    nm.grid(column=0, row=1)
    nm.current(0)
    
    port = tk.StringVar()
    num = ttk.Combobox(mig, width=19, textvariable=port, state='disabled')
    num["values"] = ("COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10", "COM11", "COM12", "COM13")
    num.grid(column=1, row=1)
    num.current(0)

    voice = tk.StringVar()
    vo = ttk.Combobox(mig, width=19, textvariable=voice, state='readonly')
    vo["values"] = ("Male", "Female", "Mute")
    vo.grid(column=2, row=1)
    vo.current(voicce)
   
    act = ttk.Button(mig, text="Settup", command=lambda :[settup(nm.get(), num.get(), vo.get()), settt.destroy()])
    act.grid(column=1, row=3, sticky=tk.W, columnspan=3)


# runs main function
if __name__ == "__main__":
    main()
