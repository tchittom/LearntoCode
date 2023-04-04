#Beth and I are trying to make the code on page 180 shorter

dog_name = ['Codie', 'Sparky', 'Jackson', 'Fido']
dog_weight = [40, 9, 12, 65]

length = len(dog_name)

for i in range(length):
    if dog_weight[i] > 20:
        print(dog_name[i], 'says WOOF WOOF')
    else:
        print(dog_name[i], 'say woof woof')
