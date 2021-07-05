# ChainMap groups multiple dicts or other mappings together to create a single, updateable view.
from collections import ChainMap  
     
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
d4 = {'g': 7, 'h': 8}

# Defining the chainmap  
c = ChainMap(d1, d2, d3)  
     
# Accessing Values using key name 
print(c['a']) 
  
# Accesing values using values() 
# method 
print(c.values()) 
  
# Accessing keys using keys() 
# method 
print(c.keys())

# Add new dictionary
c.new_child(d4)
newc = c.new_child(d4)
print('c: ', c)
print('newc: ',newc)
