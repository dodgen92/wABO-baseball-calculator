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
    
    #labels
    bb = Label(wobaWindow, text ="Walks")
    singles = Label(wobaWindow, text ="Singles")
    doubles = Label(wobaWindow, text ="Doubles")
    triples = Label(wobaWindow, text ="Triples")
    homeruns = Label(wobaWindow, text ="Home Runs")
    atbats = Label(wobaWindow, text ="At bats")
    sacflies =Label(wobaWindow, text ="Sacrifice flies")
    ibbs = Label(wobaWindow, text ="Intentional Walks")
   
   
    #inputwindows
    bbentry= Entry(wobaWindow, width= 60)
    singlesentry= Entry(wobaWindow, width= 60)
    doublesentry= Entry(wobaWindow, width=60)
    tripleentry= Entry(wobaWindow, width= 60)
    homerunentry= Entry(wobaWindow, width= 60)
    atbatsentry= Entry(wobaWindow, width= 60)
    sacfliesentry= Entry(wobaWindow, width= 60)
    ibbsentry= Entry(wobaWindow, width= 60)
    
   #entry positions
    bbentry.grid(row=0, column=1)
    singlesentry.grid(row=1, column=1)
    doublesentry.grid(row=2, column=1)
    tripleentry.grid(row=3, column=1)
    homerunentry.grid(row=4, column=1)
    atbatsentry.grid(row=5, column=1)
    sacfliesentry.grid(row=6, column=1)
    ibbsentry.grid(row=7, column=1)
    
    #label positions
    bb.grid (row=0, column=0)
    singles.grid (row=1, column=0)
    doubles.grid (row=2, column=0)
    triples.grid (row=3, column=0)
    homeruns.grid (row=4, column=0)
    atbats.grid (row=5, column=0)
    sacflies.grid (row=6, column=0)
    ibbs.grid (row=7, column=0)










def pythagwins():
    pythagWindow = Toplevel(root)
    pythagWindow.title("Please enter stats")
    

    #labels
    runsscored= Label(pythagWindow, text ="Runs scored")
    runsallowed= Label(pythagWindow, text ="Runs Allowed")
    season= Label(pythagWindow, text ="Length of season")

    #inputs
    runsscoredentry= Entry(pythagWindow, width= 60)
    runsallowedentry= Entry(pythagWindow, width= 60)
    seasonentry= Entry(pythagWindow, width= 60)


    #input positions
    runsscoredentry.grid(row=0, column=1)
    runsallowedentry.grid(row=1, column=1)
    seasonentry.grid(row=2, column=1)

    #label positions
    runsscored.grid (row=0, column=0)
    runsallowed.grid (row=1, column=0)
    season.grid (row=2, column=0)


def babip():
    babipWindow = Toplevel(root)
    babipWindow.title("Please enter stats")
    
    #labels
    hits= Label(babipWindow, text = "Hits")
    homers= Label(babipWindow, text = "Home Runs")
    ks= Label(babipWindow, text = "Strikeouts")
    atbatts= Label(babipWindow, text = "At bats")
    sacrificeflies= Label(babipWindow, text = "Sac Flies")

    #inputs
    hitsentry= Entry(babipWindow, width= 60)
    homersentry= Entry(babipWindow, width= 60)
    ksentry= Entry(babipWindow, width= 60)
    atbattssentry= Entry(babipWindow, width= 60)
    sacrificefliesentry = Entry(babipWindow, width= 60)

    #input positions

    hitsentry.grid(row=0, column=1)
    homersentry.grid(row=1, column=1)
    ksentry.grid(row=2, column=1)
    atbattssentry.grid(row=3, column=1)
    sacrificefliesentry.grid(row=4, column=1)

    #label positions
    hits.grid (row=0, column =0)
    homers.grid (row=1, column=0)
    ks.grid(row=2, column=0)
    atbatts.grid(row=3, column=0)
    sacrificeflies.grid(row=4, column=0)



def rangefactor():
    rfWindow = Toplevel(root)
    rfWindow.title("Please enter stats")

    #labels
    assists= Label(rfWindow, text = "Assists")
    putouts= Label(rfWindow, text= "Putouts")
    innings= Label(rfWindow, text= "Innings")

    #inputs
    assistsentry= Entry(rfWindow, width=60)
    putoutsentry= Entry(rfWindow, width=60)
    inningsentry= Entry(rfWindow, width=60)

    #input positions
    assistsentry.grid(row=0, column=1)
    putoutsentry.grid(row=1, column=1)
    inningsentry.grid(row=2, column=1)

    #label positions
    assists.grid (row=0, column =0)
    putouts.grid (row=1, column =0)
    innings.grid (row=2, column =0)


button_wOBA = Button(root, text="wOBA", padx=200, pady=30, command=woba)
button_pythag = Button(root, text="expected wins", padx=200, pady=30, command=pythagwins)
button_babip = Button(root, text="babip", padx=200, pady=30, command=babip)
button_rf9 = Button(root, text="rangefactor", padx=200, pady=30,command=rangefactor)

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



