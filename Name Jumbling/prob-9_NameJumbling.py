# Practical Problem 9 - Funny Names
# User enter the number of names to be received, Enter first name and surname for that number of times,
# Then the names have to print in original order of their entry with swapping their surnames with one another
# and any first names & surnames can't be original

from random import randint

get = []
num = int(input("How many names do you want to take: "))
for i in range(num):
    get.append(input("Enter First name and Last Name separated by space (e.g., John Smith): "))

fname = []
lname = []
for item in get:
    fname.append(item.split(" ")[0])
    lname.append(item.split(" ", maxsplit=1)[1])

fnum = [i for i in range(len(get))]
lnum = []
count = 0
while True:
    if len(lnum) != len(fnum):
        num = randint(0, len(fnum) - 1)
        if count == 0:
            if num != 0:
                lnum.append(num)
                count += 1
            else:
                continue
        else:
            if num not in lnum:
                lnum.append(num)
                count += 1
    else:
        if lnum == fnum:
            continue
        else:
            break

print("\n")
for index, name in enumerate(fname):
    print(f"{index + 1}: {name} {lname[lnum[index]]}")
