word = input("Enter the words you want to check: ")

letters = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
}

for i in word:
    if i in letters:
        letters[i] += 1

panagram = True

for i in letters.values():
    if i == 0:
        panagram = False

if panagram:
    print("It's a panagram, yay")
else:
    print("It's not a pangram, shad")