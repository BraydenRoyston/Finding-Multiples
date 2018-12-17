# Print all multiples of 3 and 5 that are equal to or less than 100.

multiples3 = []
multiples5 = []
multiplesTotal = []

for i in range(1, 101):
    if i % 3 == 0:
        multiples3 = multiples3 + [i]
        multiplesTotal += [i]
    elif i % 5 == 0:
        multiples5 = multiples5 + [i]
        multiplesTotal += [i]



print(multiples3)
print(multiples5)
print(sum(multiplesTotal))
