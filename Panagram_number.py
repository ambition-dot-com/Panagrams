number = input("Enter the number you want to check: ")

digit_count = {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "0":0
}
for i in number:
    if i in digit_count:
        digit_count[i] += 1

panagram = True

for i in digit_count.values():
    if i == 0:
        panagram = False

if panagram:
    print("It's a panagram number!!")
else:
    print("It's not a panagram")


#Ask user to enter a string (line or word) and i have to check for vowels. Same thing but in vowels and show the number of times also.