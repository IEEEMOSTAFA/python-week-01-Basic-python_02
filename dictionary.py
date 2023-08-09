numbers = [12,56,98,78,56,12,6,98]
person = ['kala chan','kali pur',23,'student']
#key value pair
#dictionary
#object
#hash table
#set
#overlap with set
# {key:value,key:value,key:value,key:value,key:vale}
person ={'name':'kala paki','address':'kalipur','age':23,'job':'facebokar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())
person['language'] = 'python'
person['name'] = 'sada pakhi'
del person['age']
print(person)
#special dictionary looking that show only key!!
for item in person:
    print(item)
#if we want to key and value
for key,value in person.items():
    print(key,value)    
