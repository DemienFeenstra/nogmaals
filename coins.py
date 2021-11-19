# name of student: Demiën Feenstra
# number of student: 99064788
# purpose of program: als je te veel betaald het te veel betaalde aantal word terug gegeven in coins
# function of program: hij geeft het te veel betaalde aantal terug in coins door middel van door al de if's te gaan.
# structure of program: if elif else structuur 

toPay = int(float(input('Amount to pay: '))* 100) # aantal te betalen invoeren en dat doet die x 100.
paid = int(float(input('Paid amount: ')) * 100) # betaald aantal invoeren en dat doet die x 100.
change = paid - toPay # change doet paid aftrekken van toPay.

if change > 0: # als chage groter is dan 0.
  coinValue = 500 # coinValue is 500.
  
  while change > 0 and coinValue > 0: # als change groter dan 0 en coinValue groter dan 0 is.
    nrCoins = change // coinValue # 

    if nrCoins > 0: # als nrCoins groter is dan 0.
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # hij print tekst en nrCoins en coinValue.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # nrCoinsReturned print tekst en str(CoinValue).
      change -= nrCoinsReturned * coinValue # change is change - nrCoinsReturned x coinValue.

# comment on code below: 
    if coinValue == 500:
      coinValue = 300
      coinsReturned500 = nrCoinsReturned
    elif coinValue == 300:
      coinValue = 200
      coinsReturned300 = nrCoinsReturned
    elif coinValue == 200:
      coinValue = 50
      coinsReturned200 = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      coinsReturned50 = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      coinsReturned20 = nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      coinsReturned10 = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      coinsReturned5 = nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      coinsReturned2 = nrCoinsReturned
    else:
      coinValue = 0

if change > 0: # als change groter is dan 0.
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

print(coinsReturned500, "coin(s) of 500")
print(coinsReturned300, "coin(s) of 300")
print(coinsReturned200, "coin(s) of 200")
print(coinsReturned50, "coin(s) of 50")
print(coinsReturned20, "coin(s) of 20")
print(coinsReturned10, "coin(s) of 10")
print(coinsReturned5, "coin(s) of 5")
print(coinsReturned2, "coin(s) of 2")