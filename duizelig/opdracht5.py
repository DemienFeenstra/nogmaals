# Herhaal een input() tot het resultaat daarvan gelijk is aan ‘quit’. 
# Print het aantal iteraties per iteratie. (Het aantal keren dat de vraag is gesteld)

i = input("typ quit als je wilt stoppen")
while i == input():
    print(i)
    if i == "quit":
        break