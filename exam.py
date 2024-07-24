animals = ["Lion", "Cat", "Tiger", "Dolphin", "Pig", "Dog", "Whale"]
short_animals = []

for animal in animals:
    if len(animal) <= 3:
        short_animals.append(animal)

print(short_animals)