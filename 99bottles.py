#99 bottles challenge

bottles = 99

def numberOfBottles(bottles):
    return str(bottles if bottles > 0 else "No more")
def singular(bottles):
    return "s" if bottles != 1 else ""

for i in range (150):
    print(numberOfBottles(bottles) + " bottle" + singular(bottles) + " of beer on the wall, " + numberOfBottles(bottles) + " bottle" + singular(bottles) + " of beer.")
    if bottles > 0:
        bottles -= 1
        print("Take one down and pass it around, " + numberOfBottles(bottles) + " bottle" + singular(bottles) + " of beer on the wall.")
    else:
        bottles = 99
        print("Go to the store and buy some more, " + numberOfBottles(bottles) + " bottle" + singular(bottles) + " of beer on the wall.")


