dog_name = ['Codie', 'Sparky', 'Jackson', 'Fido']
dog_weight = [40, 9, 12, 65]

dogs = len(dog_name)

print('Get those dogs ready')

def bark(name, weight):
    if weight > 20:
        print(name, 'says WOOF WOOF')
    else:
        print(name, 'says woof woof')

for i in range(dogs):
    bark(dog_name[i], dog_weight[i])

print("Okay, we're all done")
