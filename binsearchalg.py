animals = ['duck', 'jackal', 'hippo', 'aardvack', 'cat',
           'flamingo', 'iguana', 'giraffe', 'elephant', 'bear', 'cat', 'hippo']

animals.sort()  # O(n log n )

def binary_search(a) # O (log n)
    pass


def find_animal(a):
    for animal in animals:
        if animal == a:
            return True
    return False


print(find_animal('cat'))
print(find_animal('turkey'))
