#Við ákvuðum að skipta þessu niður í 4 áttir. North, south, east og west. 
#Við vildum einnig að reitirnir myndu hafa táknið y og x
#Eftir það notuðum við þá að north væri + x og south -
#og þá west væri - y og east væri +
#Síðan gerðum við forritið og allt heppnaðist vel

for_low = ""
x = 1
y = 1
p = True
n = "(N)orth"
s = "(S)outh"
e = "(E)ast"
w = "(W)est"

while True:


    if y == 1:
        change = n + "."
        for_low = "n"
    if x == 1 and y == 2:
        change = n + " or " + e + " or " + s + "."
        for_low = "nes"
    if x == 2 and y == 2:
        change = s + " or " + w + "."
        for_low = "sw"
    if x == 1 and y == 3:
        change = e + " or " + s + "."
        for_low = "es"
    if x == 2 and y == 3:
        change = e + " or " + w + "."
        for_low = "we"
    if x == 3 and y == 3:
        change = s + " or " + w + "."
        for_low = "sw"
    if x == 3 and y == 2:
        change = n + " or " + s + "."
        for_low = "sn"
    
    
    if p == True:
        print("You can travel: " + change)
    p = False
    direct = str(input("Direction: "))
    low = direct.lower()

    for l in for_low:
        if low == l:
            p = True
    
    if p == False:
        print("Not a valid direction!")   

    if p == True:
        if low == "n":
            y += 1

        if low == "s":
            y -= 1

        if low == "e":
            x += 1
    
        if low == "w":
            x -= 1

    if x == 3 and y == 1:
        break