frutta = ["mela", "pera", "mango"]

for fr in frutta:
    print(fr)
    print("---")

for i in range(15):
    print("Gigi " + str(i))

for i in range(3, 10):
    print(i)

print("-----")

start = 3
for i in range(start, 10, 2):
    print(i)

# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for f in fruits:
    if "a" in f:
        newlist.append(f.upper())

print(newlist)

# alternativo al ciclo sopra
# sintassi
# newlist = [expression for item in iterable if condition == True]
newlist = [f.upper() for f in fruits if "a" in f]
print(newlist)

# while
i = 1
while i <= 6:
    print(i)
    i += 1

# break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break

    i += 1

# continue
i = 1
while i < 6:
    i += 1

    if i == 3:
        continue

    print(i)


# print("CTRL+C per uscire...")
# while True:
#     i += 1
