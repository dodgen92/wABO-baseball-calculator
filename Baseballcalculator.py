from tkinter import *
import tkinter.messagebox

def babipentry():
    babipinput = Tk()
    L15 = Label(babipinput, text = "BABIP", fg="red", font = "Times")
    L15.grid(row=1, column=1)
    L16= Label(babipinput, text = "Hits", font = "Times")
    L16.grid(row=2, column=1)
    L17= Label(babipinput, text = "Home Runs", font = "Times")
    L17.grid(row=3, column=1)
    L18= Label(babipinput, text = "At bats", font = "Times")
    L18.grid(row=4, column=1)
    L19= Label(babipinput, text = "Strikeouts", font = "Times")
    L19.grid(row=5, column=1)
    L20= Label(babipinput, text = "Sac flies", font = "Times")
    L20.grid(row=6, column=1)
    E14= Entry(babipinput, width= 60)
    E14.grid(row=2, column=2)
    E15= Entry(babipinput, width= 60)
    E15.grid(row=3, column=2)
    E16= Entry(babipinput, width= 60)
    E16.grid(row=4, column=2)
    E17= Entry(babipinput, width= 60)
    E17.grid(row=5, column=2)
    E18= Entry(babipinput, width= 60)
    E18.grid(row=6, column=2)
    B4 = Button (babipinput, text='Calculate BABIP', command = lambda: BABIP(E14, E15, E16, E17, E18), bg="red" , padx=15,  font= "Times 14 bold"  )
    B4.grid (row=7, column=2)

def BABIP(E14, E15, E16, E17, E18):
    babipoutput = Tk()
    L21 = Label (babipoutput, text = "BABIP", fg="red", font = "times")
    L21.grid (row=1, column = 1)
    E19 = Entry(babipoutput, bd=5)
    E19.grid(row=2, column=1)
    hits = float(E14.get())
    hrs = float(E15.get())
    atbats = float(E16.get())
    ks = float(E17.get())
    sf = float(E18.get())
    babip = (hits - hrs) / (atbats - hrs - ks + sf)
    E19.insert(0, str(babip))
    E12['bg']='grey'

    

def wobaentry():
    wobainput= Tk()
    L4 = Label(wobainput, text = "wOBA", fg = "red", font = "Times").grid(row=1, column=1)
    L5 = Label(wobainput, text ="Walks").grid(row=2, column=1)
    L6 = Label(wobainput, text ="Singles").grid(row=3, column=1)
    L7 = Label(wobainput, text ="Doubles").grid(row=4, column=1)
    L8 = Label(wobainput, text ="Triples").grid(row=5, column=1)
    L9 = Label(wobainput, text ="Home Runs").grid(row=6, column=1)
    L10 = Label(wobainput, text ="At bats").grid(row=7, column=1)
    L11 =Label(wobainput, text ="Sacrifice flies").grid(row=8, column=1)
    L12 = Label(wobainput, text ="Intentional Walks").grid(row=9, column=1)
    L14 = Label(wobainput, text ="Hit By Pitch").grid(row=10, column=1)
    E4= Entry(wobainput, width= 60)
    E4.grid(row=2, column=2)
    E5= Entry(wobainput, width= 60)
    E5.grid(row=3, column=2)
    E6= Entry(wobainput, width= 60)
    E6.grid(row=4, column=2)
    E7= Entry(wobainput, width= 60)
    E7.grid(row=5, column=2)
    E8= Entry(wobainput, width= 60)
    E8.grid(row=6, column=2)
    E9= Entry(wobainput, width= 60)
    E9.grid(row=7, column=2)
    E10= Entry(wobainput, width= 60)
    E10.grid(row=8, column=2)
    E11= Entry(wobainput, width= 60)
    E11.grid(row=9, column=2)
    E13= Entry(wobainput, width= 60)
    E13.grid(row=10, column=2)
    B5= Button(wobainput, text= "Calculate wOBA", command = lambda: wOBA(E4, E5, E6, E7, E8, E9, E10, E11, E13), bg="red" , padx=15,  font= "Times 14 bold"  )
    B5.grid(row=15, column=2)

def wOBA(E4, E5, E6, E7, E8, E9, E10, E11, E13):
    wOBAoutput = Tk()
    L13 = Label (wOBAoutput, text = "wOBA", fg="black", font = "times")
    L13.grid (row=1, column = 1)
    E12 = Entry(wOBAoutput, bd=5)
    E12.grid(row=2, column=1)
    bb = float(E4.get())
    hbp = float(E13.get())
    singles = float(E5.get())
    doubles = float(E6.get())
    triple = float(E7.get())
    hr = float(E8.get())
    ab = float(E9.get())
    sf = float(E10.get())
    ibb = float(E11.get())
    ubb = bb - ibb
    woba = float(((ubb * .69) + (.720 * hbp) + (.884 * singles) + (1.261 * doubles) + (1.601 * triple) + (2.072 * hr)) / (ab + bb - ibb + sf + hbp))
    E12.insert(0, str(woba))
    E12['bg']='grey'
    


def pythagentry():
    pythaginput = Tk()
    L0 = Label(pythaginput, text= "Expected Wins", fg="black", font = "Times")
    L0.grid(row=1, column=1)
    L1 = Label(pythaginput, text= "Runs Scored", fg="black", font= "Times")
    L1.grid(row=2, column=1)
    L2 = Label(pythaginput, text= "Runs Allowed", fg="black", font= "Times")
    L2.grid(row=3, column=1)
    L3 = Label(pythaginput, text= "Season Length", fg="black", font= "Times")
    L3.grid(row=4, column=1)
    E1 = Entry(pythaginput,bd=5)
    E1.grid (row=2, column=2)
    E2 = Entry(pythaginput,bd=5)
    E2.grid (row=3, column=2)
    E3 = Entry(pythaginput,bd=5)
    E3.grid (row=4, column=2)
    B4 = Button (pythaginput,text='Calculate Pythagorean Wins', command = lambda: pythag(E1, E2, E3), bg="red" , padx=15,  font= "Times 14 bold" )
    B4.grid (row=5, column=2, sticky = "ew")

def pythag(E1, E2, E3):
    pythagoutput = Tk()
    L4=Label(pythagoutput,text="Expected Wins:",fg="red")
    L4.grid (row =1, column =1)
    E5=Entry(pythagoutput, bd=5)
    E5.grid(row=4,column=1)
    runsscored= float(E1.get())
    runsallowed= float(E2.get())
    lengthseason= float(E3.get())
    ratio = runsscored / runsallowed
    winpct = pow (ratio, 2) / (pow(ratio, 2) + 1)
    expectedwins = lengthseason * winpct
    E5.insert(0, str(expectedwins))
    E5['bg']='grey'

top = Tk()
B1=Button(top, bd = 10, text='Calculate Pythagorean Wins',command = pythagentry, padx=30 ,bg="grey" , font= "Times 18 bold")
B1.grid(row=1,column=1, sticky="ew")

B2=Button(top, text='Calculate wOBA' , bd= 10, padx = 30, command=wobaentry, bg="grey" , font= "Times 18 bold")
B2.grid(row=2, column=1, sticky="ew")

B3=Button(top, text='Calculate BABIP', bd=10 ,command=babipentry, bg="grey" , padx=30,  font= "Times 18 bold")
B3.grid(row=3, column=1, sticky="ew")

devlabel = Label(top, text='Developed by Tyler Remington Dodgen' , fg= "Blue", font= "Times 14")
devlabel.grid (row=4, column=1, sticky="ew")
top.mainloop()






""" Saving formulas for GUI
print ("Select which statistic to calculate")
print ("1. wOBA")
print ("2. BABIP")
print ("3. Pythagorean Wins")
print ("4. Range Factor per 9 innings")
operation = input()



if operation == "1":
    bb = float(input('Base on balls: '))
    hbp = float(input('Hit by pitch: '))
    singles = float(input('Singles: '))
    doubles = float(input('Doubles: '))
    tripple = float(input('Tripples: '))
    hr = float(input('Home Runs: '))
    ab = float(input('At bats: '))
    sf = float(input('Sac Flys: '))
    ibb = float(input('Intentional Walks: '))
    ubb = bb - ibb
    woba = float(((ubb * .69) + (.722 * hbp) + (.888 * singles) + (1.271 * doubles) + (1.616 * tripple) + (2.101 * hr)) / (ab + bb - ibb + sf + hbp))
    print(woba)

elif operation == "2":
    hits = float(input('Hits: '))
    hrs = float(input('Home Runs: '))
    ks = float(input('Strikeouts '))
    ab = float(input('At bats: '))
    sf = float(input('Sac Flys: '))
    babip = (hits - hrs) / (ab - hrs - ks + sf)
    print(babip)

elif operation == "3":
    runsScored = float(input('Runs Scored: '))
    runsAllowed = float(input('Runs Allowed: '))
    exp = float(input('Exponent Power- enter 2 for MLB, 2.37 for NFL, and 13.91 for NBA:'))
    games = float(input('Runs Scored: '))
    ratio = runsScored / runsAllowed
    winpct = pow(ratio, exp) / (pow(ratio, exp) + 1)
    expectedWins = games * winpct
    print(expectedWins)

elif operation == "4":
    assists = float(input('Assists: '))
    po = float(input('Put outs: '))
    inn = float(input('Innings played: '))
    rangeFactor = 9 * (po +assists) / inn
    print(rangeFactor)
"""



