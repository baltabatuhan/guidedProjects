animals = ['duck', 'jackal', 'hippo', 'aardvack', 'cat',
           'flamingo', 'iguana', 'giraffe', 'elephant', 'bear', 'cat', 'hippo']
# Linear Time
# if we double it twice as long,if we triple three times long


def print_animals():
    for a in animals:  # O(n) over the number of elephants
        print(a)


def print_animal(i):
    print(animals[i])  # O(1) over the number of elephants

# o(1) over the number of animals
# o(n) over the length of the string


def print_animal_2(i):
    for c in animals[i]:
        print(c)


def find_dups():  # O(n^2)
    for i0 in range(len(animals)):  # n (over the number of animals)
        for i1 in range(len(animals)):  # n (over the number of animals)
            if i0 == i1:  # O(1)
                continue
            if animals[i0] == animals[i1]:
                print(f"Duplicates: {animals[i0]}")


find_dups()

for i in range(1000000000000000): #O(1000000000000000) so its O(1)
    print(animals[0])
