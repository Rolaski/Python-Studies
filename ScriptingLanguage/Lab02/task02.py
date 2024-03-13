import random

def lotto():
    liczby = []

    while len(liczby) < 6:
        cyfra = random.randint(1, 49)

        if cyfra not in liczby:
            liczby.append(cyfra)

    return liczby


result = lotto()
print(result)
