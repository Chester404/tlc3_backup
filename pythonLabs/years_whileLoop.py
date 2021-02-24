age = int(input("Please enter your age :  "))

i=0
total =0

while i < age:
    i = i+1
    total +=i
print(total,"years")

totalmonths = total * 12
totaldays = total * 366
totalhours = totaldays * 24

print("There are : ", totalmonths, "months, ", totaldays, "days and ", totalhours, "hours in ", total, "years")
