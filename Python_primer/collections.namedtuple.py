from collections import namedtuple
record = namedtuple('record',['name','DOB'])
# record = namedtuple('record','name DOB')
# internally split() is called on field name string. 'name DOB'.split() == ['name','DOB']

p1 = record('Sam','04052001')

print('from index:  ',p1[0])
print('from keyname:  ',p1.name)

print('record:  ',record)
print('All fields of a record:    ',record._fields)

# Dictionary
di = { 'name' : "Nikhil", 'DOB' : '1391997' } 
print('From dict:  ',record(**di))

# list
li = ['saath',452000]
p2 = record._make(li)
print('p2:  ',p2)


