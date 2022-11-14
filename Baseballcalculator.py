from tkinter import *

# Mandatory root widget
root = Tk()
root.title("Baseball Metrics Calculator")

#e= Entry(root, width=65, borderwidth= 15)
#e.grid(row=-0, column=0, columnspan=3, padx=10, pady=10)

#define operations
def woba():
    wobaWindow = Toplevel(root)
    wobaWindow.title("Please enter stats")
    e= Entry(wobaWindow, width=65, borderwidth= 15)
    e.grid(row=-0, column=0, columnspan=3, padx=10, pady=10)


def pythagwins():
    pythagWindow = Toplevel(root)
    pythagWindow.title("Please enter stats")
    e= Entry(pythagWindow, width=65, borderwidth= 15)
    e.grid(row=-0, column=0, columnspan=3, padx=10, pady=10)

def babip():
    babipWindow = Toplevel(root)
    babipWindow.title("Please enter stats")
    e= Entry(babipWindow, width=65, borderwidth= 15)
    e.grid(row=-0, column=0, columnspan=3, padx=10, pady=10)


def rangefactor():
    rf9Window = Toplevel(root)
    rf9Window.title("Please enter stats")
    e= Entry(rf9Window, width=65, borderwidth= 15)
    e.grid(row=-0, column=0, columnspan=3, padx=10, pady=10)


button_wOBA = Button(root, text="wOBA", padx=200, pady=30, command=woba)
button_pythag = Button(root, text="expected wins", padx=200, pady=30)
button_babip = Button(root, text="babip", padx=200, pady=30)
button_rf9 = Button(root, text="rangefactor", padx=200, pady=30)

#place buttons on grid
button_wOBA.grid(row=1, column=1)
button_pythag.grid(row=2, column=1)
button_babip.grid(row=3, column=1)
button_rf9.grid(row=4, column=1)


"""def myClick():
    myLabel= Label(root, text="Hello " + e.get(), padx=50, pady=50)#state=disabled)
    myLabel.pack()

myButton = Button(root, text= "Enter your name", padx=120, pady=200, command=myClick) #, fg="blue", bg="red")

#entry/input widget
e = Entry(root, width = 50)
e.pack()
e.get"""

#Creating label and adding it to root widget)
#myLabel2 = Label(root, text="Im bloodshot for sure")

#grid system packing
#myLabel2.grid(row=0, column=1)

#event loop
root.mainloop()






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


