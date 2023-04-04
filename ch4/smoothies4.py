smoothies  = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']

has_coconut = [True, False, False, True, False]

i = 0

#while i < len(has_coconut):
#    if has_coconut[i]:
#       print(smoothies[i], 'contains coconut')
#    i = i +1

#we want to print out the smoothies from (smooothies) that have coconut
#we compare smoothies to has_coconut and print only those that match for True

for smoothie in smoothies:
    if has_coconut[i]:
      print(smoothie)
    i = i + 1
