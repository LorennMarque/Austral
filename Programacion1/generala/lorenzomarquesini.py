import random
def count(tirada):
    repetitions = {}
    for num in tirada:
        if num in repetitions:
            repetitions[num] += 1
        else:
            repetitions[num] = 1
    return repetitions

tirada = sorted([random.randint(1, 6) for _ in range(5)])  # Generate a random roll and sort it
# tirada = [1, 2, 3, 5, 4]
print("Roll:", tirada)

counts = count(tirada)

if len(counts) == 1:
    print("Generala!") 
elif len(counts) == 2 and 4 in counts.values():
    print("Poker!")
elif (3 in counts.values() and 2 in counts.values()) or (3 in counts.values() and 1 in counts.values()):
    print("Full!")
elif sorted(tirada) in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]:
    print("Escalera!")
else:
    print("No hay nada :(")
