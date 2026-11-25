### Zip Function
# (Zip returns kye:value pair within 2 collections)
# Let suppose we have 2 collections one is name and other is roll no
# We use the list function and it will return key: value pair

## Zip Practice
rollNumbers = [12,13,14,15]
names = ["Ali","Ahmad","Raza","Maaz"]

# print(list(zip(rollNumbers,names)))
# other method
for rollNumbers, names in zip(rollNumbers, names):
    print(rollNumbers, names)

## Membership Operator (in) / (not in)

# ( such a operator that tells can a item exits in a list or not )
# list = [1,2,3,4,5,6,7,8]
# print(3 in list)

# Reverse of membership operator (not in)
# print(3 not in list)

### Enumerate function
# It returns an objects wiht its index
names = {"Ali", "Ahmad", "Raza", "Maaz"}
print(list(enumerate(names)))
