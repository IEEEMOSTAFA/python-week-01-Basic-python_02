name ='Sakib\'s Khan' #excape

name2 = " sakib khan"
name3 = """ sakib khan 
            number one """

print(name)


#string is a sequence of character
for char in name2:
    print(char)
#mutable means changeable 
#immutable means you can not change

print(name2[3])
print(name2[1:6])
print(name2[-2])
print(name2[::-1])
#name2[0] ='R'
print(name2)
if 'khan' in name2:
    print('exist')

print(name2.upper())
