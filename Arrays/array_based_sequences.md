Python built-in sequence classes: `list() tuple() str()`
***
Low level Arrays:
-  **Arrays**: Contiguous area of memory consisting of elements of same type indexed by contiguous integers.
-  Each byte of memory is associated with a
unique number that serves as its address.
- Each cell of an array must use the same number of bytes. This requirement is
what allows an arbitrary cell of the array to be accessed in constant time based on
its index. [start + cellsize * index]

Array Types:
1. Referential Arrays: `list() tuple()`
   - Array of Object-References.
   - sequential storage of memory addresses of elements.
     - size of each memory addresses is same. [eg:64-bits]
     - size of element object may vary...
1. Compact Arrays: `str()`  `array()`[from array module]
   - Array of actual bits of data. 
   - eg: characters in `str()`


*** 

## **1. Lists vs Compact arrays**

- Referential array store 64-bit address in addition to real object element space stored elsewhere.
  - Compact array are memory efficient.
- List instance maintain greater capacity than actual length.
  - 5 elemented list may have 8 element worth storage for faster append.
- List do not store actual objects consecutively but only their addresses.
  - having primary data nearby in memory offer performance in some computations.


***

## **2. List contatenation `extend()` vs `[+]`**
- `[+]` merge list with lists only.
  - `extend()` can merge list with list,tuple,str,dict
- `[+]` creates new list
  - `extend()` modifies list in-place.

`extend()` takes iterable object (having `_iter_` method)
`append()` adds only one object.

`extend()` better than `append()` each element in loop:
  - often python methods implemented in natively compiled language than interpreted python code
  -  less overhead to a single function call that accomplishes all the work, versus many individual function calls
  -  resulting size of the updated list can be calculated in advance. 
     -  risk of mulitiple resize while repeated calls to `append()`

> Initialising list with `[None]*n` efficient because it removes multiple resize overhead during the elements addition.

***

## **3. Lists vs Tuples**

- Tuples are memory efficient
  - there is no need for an underlying
dynamic array with surplus capacity like lists.

`len(alist)` is O(1) because list instance explicitly maintains such state information at the time of element add itself.

***

## **4. Efficient string composition**


```python
letters=''
for i in doc:
  letters+=i  # Not good

# new string forms at RHS and identifier reassigns identifier letters.
# n characters = 1+2+3...+n   O(n^2)

letters = ''.join([c for c in document])
# temp list better

letters = ''.join(c for c in document)
# generator BEST
```

***

## **5. Shallow Copy vs Deep Copy**

- **shallow copy**: copy of top level objects only

  - Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object. If any of the fields of the object are references to other objects, just the reference addresses are copied i.e., only the memory address is copied.
- **deep copy**: Top level and all it's child level objects also copied recursively.

```python
a = [[1,2,3],[4,5,6]]
b = list(a) # shallow copy
# b = a.copy() also same.

b.append(9) 
# b = [[1,2,3],[4,5,6],9] changed
# a = [[1,2,3],[4,5,6]] same

a[0][0] = 8888 # changes b also
# b = [['8888',2,3],[4,5,6],9]
# a = [['8888',2,3],[4,5,6]]

--------

# FOR DEEP COPY
import copy
b = copy.deepcopy(a)

```
More info: [shallow vs deep copy](https://realpython.com/copying-python-objects/#3-things-to-remember)

***

## **6. Multi-dimensional datasets**

```python
# 2D matrix ---> list of lists
matrix = [
[0,1,2],
[3,4,5],
[6,7,8]
]

element = matrix[row][column] # access


# Initialisation Mistakes

matrix = ([0]*col)*row # Mistake 1
# ([0]*2)*3 ---> [0,0]*3 ---> [0,0,0,0,0,0]

matrix = [[0]*col]*row # Fatal Mistake
# all rows refers to same object. only-1-row
# matrix[0][0] = 8 ---> [all rows][0] = 8

# Correct Initialisation

matrix = [[0]*col for i in range(row)]
# [0]*col evaluated for each pass.
# we get row no. distinct lists as required.
```

## 7. **Some more**
- `A[k:] + A[:k]` rotates A by k to the left.
- `B = A[:]` does a (shallow)copy of A
- Nested loop in List comprehension :
```py
   A = [1, 3, 5] B = ['d', 'b']
   C = [(x, y) for x in A for y in B] 
   >> [(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]
```

- Convert 2D lists to 1D:
```py
   M = [['a', 'b', 'c'], ['d', 'e','f']]
   N = [x for row in M for x in row]
   >> N = ['a', 'b', 'c', 'd', 'e', 'f ']
```
