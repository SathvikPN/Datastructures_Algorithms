# Deques are a generalization of stacks and queues 
# (the name is pronounced “deck” and is short for “double-ended queue”)
from collections import deque

d = deque('ghi')
for element in d:
    print(element.upper(), end=' ')
print()

d.append('j')
d.appendleft('f')

print(d)
print(f'd[0] = {d[0]}  and  d[-1] = {d[-1]}')

pop = d.pop()
popleft = d.popleft()
print(f'Popleft: {popleft}  pop: {pop}')

print(d)

print(f" 'i' in d:   {'i' in d}")

d.extend('jkl')
d.extendleft('def') # extendleft reverses i/p order 
# ... f,e,d --- [original deque] --- j,k,l ...
print(d)

d.rotate(1) # right
print(d)
d.rotate(-1) # left
print(d)

d.clear()
print(d)
