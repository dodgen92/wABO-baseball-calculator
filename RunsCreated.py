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
