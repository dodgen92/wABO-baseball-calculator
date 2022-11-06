bb = float(input('Base on Balls: '))
hbp = float(input('Hit by Pitch: '))
singles = float(input('Singles: '))
doubles = float(input('Doubles: '))
tripples = float(input('Tripples: '))
hr = float(input('Home Runs: '))
ab = float(input('At bats: '))
sf= float(input('Sac Flys: '))
ibb= float(input('Intentional Base on Balls: '))
ubb = bb - ibb


woba = float (((ubb * .69) + (.722 * hbp) + (.888 * singles) + (1.271 * doubles) + (1.616 * tripples) + (2.101 * hr)) / (ab + bb - ibb + sf + hbp))


print(woba)