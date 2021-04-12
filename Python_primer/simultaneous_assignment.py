i = 1
j = 3
print(f'Before: i={i}  j={j}')
i,j = j,i
print(f'After: i={i}  j={j}')

# In effect, the right-hand side of this assignment 
# is automatically packed into a tuple,
# and then automatically unpacked with its elements assigned to 
# the two identifierson the left-hand side.

# the unnamed tuple representing the packed values on the right-hand side 
# implicitly serves as the temporary variable when performing such a swap.