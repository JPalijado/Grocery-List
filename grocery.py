a = int(input("Number of Apples: "))
o = int(input("Number of Oranges: "))
b = int(input("Number of Banana: "))
t = int(input("Number of Tomato: "))
m = int(input("Number of Melon: "))

aprice = 12.00
oprice = 15.00
bprice = 8.00
tprice = 10.00
mprice = 30.00

print(f"\nApple's Price per piece: P{aprice:.2f}")
print(f"Orange's Price per piece: P{oprice:.2f}")
print(f"Banana's Price per piece: P{bprice:.2f}")
print(f"Tomato's Price per piece: P{tprice:.2f}")
print(f"Melon's Price per piece: P{mprice:.2f}\n")

atotal = a * aprice
ototal = o * oprice
btotal = b * bprice
ttotal = t * tprice
mtotal = m * mprice
gtotal = atotal + ototal + btotal + ttotal + mtotal

print(f"Apple = {a} * {aprice} = {atotal:.2f}")
print(f"Orange = {o} * {oprice} = {ototal:.2f}")
print(f"Banana = {b} * {bprice} = {btotal:.2f}")
print(f"Tomato = {t} * {tprice} = {ttotal:.2f}")
print(f"Melon = {m} * {mprice} = {mtotal:.2f}")
print(f"Grand Total= {atotal} + {ototal} + {btotal} + {ttotal} + {mtotal} = {gtotal:.2f}\n")

print(f"Total Price of Apple: P{atotal:.2f}.")
print(f"Total Price of Orange: P{ototal:.2f}.")
print(f"Total Price of Banana: P{btotal:.2f}.")
print(f"Total Price of Tomato: P{ttotal:.2f}.")
print(f"Total Price of Melon: P{mtotal:.2f}.\n")

print(f"Grand Total: P{gtotal:.2f}.")